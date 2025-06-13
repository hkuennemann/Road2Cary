import plotly.graph_objects as go
import os

from LibRoad2Cary.utility import constants, functions_calcVals
from LibRoad2Cary.data import datasets

class Road2CaryMap:
    def __init__(self, date):
        self.date = date
        self.team_progress_df = datasets.get_data(date)
        self.ROAD2CARY_MAP = go.Figure()

        # Add route lines
        for i in range(len(constants.ROUTE) - 1):
            start = constants.ROUTE[i][1]
            end = constants.ROUTE[i + 1][1]
            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                          lon=[start[1], end[1]],
                          lat=[start[0], end[0]],
                          mode='lines',
                          line=dict(color="black", dash='dot'),
                          showlegend=False
            ))

        # Add text labels and leader lines
        for city, (lat, lon) in constants.ROUTE:
            dx, dy = constants.CITY_LABEL_OFFSETS.get(city, (0, 0.6))  # Default offset if missing
            label_lon = lon + dx
            label_lat = lat + dy

            # Add markers
            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                          lon=[lon],
                          lat=[lat],
                          mode='markers',
                          marker=dict(size=8, color="black", symbol="diamond"),
                          text=f"{city}",
                          hoverinfo='text',
                          showlegend=False
            ))

            # Add leader line (dashed)
            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                          lon=[lon, lon + dx * constants.LEADER_LINE_SHORTENING_FACTOR],
                          lat=[lat, lat + dy * constants.LEADER_LINE_SHORTENING_FACTOR],
                          mode='lines',
                          line=dict(color="black", width=1.5, dash='dot'),
                          showlegend=False,
                          hoverinfo='skip'
            ))

            # Add text
            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                          lon=[label_lon],
                          lat=[label_lat],
                          mode='text',
                          text=[f"{city}"],
                          textfont=dict(size=14, color='black'),
                          textposition='middle center',
                          showlegend=False,
                          hoverinfo='skip'
            ))

        # Add team markers with tooltips
        for _, row in self.team_progress_df.iterrows():
            lat, lon = functions_calcVals.interpolate_position(row["Duration"])
            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                          lon=[lon],
                          lat=[lat],
                          mode='markers',
                          marker=dict(size=6, color=constants.TEAM_MARKER_COLOR),
                          text=f"{row['Team_Name']}<br>{row['Duration']:.1f} km",
                          hoverinfo='text',
                          showlegend=False
            ))

        self.ROAD2CARY_MAP.update_layout(
            images=[
                dict(
                    source=functions_calcVals.IMAGE_URI,
                    xref="paper", yref="paper",
                    x=constants.IMAGE_POSITION_X, y=constants.IMAGE_POSITION_Y,  # bottom-right-ish
                    sizex=0.2, sizey=0.2,
                    xanchor="center", yanchor="middle",
                    layer="above"
                )
            ],
            annotations=[
                dict(
                    text=functions_calcVals.CURRENT_DATETIME,
                    xref="paper", yref="paper",
                    x=constants.DATETIME_POSITION_X, y=constants.DATETIME_POSITION_Y,
                    showarrow=False,
                    font=dict(size=12, color="gray")
                )
            ],
            showlegend=False,
            title=None,
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
            dragmode=False
        )

        # update geos
        self.ROAD2CARY_MAP.update_geos(
                      showcountries=True,
                      countrycolor=constants.COUNTRY_COLOR,
                      showland=True,
                      landcolor=constants.LAND_COLOR,
                      showocean=True,
                      oceancolor=constants.OCEAN_COLOR,
                      showcoastlines=True,
                      coastlinecolor= constants.COATLINE_COLOR,
                      coastlinewidth=0.3,
                      fitbounds="locations",
                      resolution=50
        )
    
    def show(self):
        self.ROAD2CARY_MAP.show(config=constants.MAP_CONFIGS)
    
    def write_html(self, new_main: bool = False):
        if new_main:
            file_path = "index.html"
        else:
            file_path = os.path.join(
                r"Data",
                self.date,
                "index.html"
            )
        self.ROAD2CARY_MAP.write_html(file_path, include_plotlyjs='cdn')
