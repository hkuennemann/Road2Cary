"""
Road2CaryMap: A visualization tool for plotting team progress on the 'Road to Cary' route using Plotly.

This module defines the `Road2CaryMap` class, which builds an interactive map showing:
- The predefined route with city markers and labels.
- Progress of teams based on distance covered.
- Special indication for teams on their second lap.

Features:
- Route rendering
- Team progress interpolation
- Second-lap marker customization
- Image/logo embedding
- Timestamp annotation
- Export to HTML

Dependencies: plotly, pandas, os
"""


import plotly.graph_objects as go
import os

from LibRoad2Cary.utility import constants, functions_calcVals
from LibRoad2Cary.data import datasets

class Road2CaryMap:
    """
    A class for building and displaying a map visualization of team progress 
    along a defined route to Cary using Plotly's geographic plotting features.

    Attributes:
        date (str): The date string used to fetch team progress data.
        team_progress_df (DataFrame): DataFrame of team progress on the given date.
        ROAD2CARY_MAP (go.Figure): The Plotly figure that holds the rendered map.
    """

    def __init__(self, date):
        """
        Initializes the Road2CaryMap instance with team data for the specified date.

        Args:
            date (str): The date string (e.g., '2025-06-22') used to load progress data.
        """
        self.date = date
        self.team_progress_df = datasets.get_data(date)
        self.ROAD2CARY_MAP = go.Figure()

    def build_map(self):
        """
        Constructs the full map figure by adding route lines, city labels,
        team markers, images, annotations, and applying styling.
        """
        self._add_route_lines()
        self._add_city_labels()
        self._add_team_markers()
        self._add_image_and_annotations()
        self._style_map()

    def _add_route_lines(self):
        """
        Adds the dashed route lines connecting cities along the route to Cary.
        """
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

    def _add_city_labels(self):
        """
        Adds city markers, leader lines, and text labels for each stop on the route.
        """
        for city, (lat, lon) in constants.ROUTE:
            dx, dy = constants.CITY_LABEL_OFFSETS.get(city, (0, 0.6))
            label_lon = lon + dx
            label_lat = lat + dy

            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                lon=[lon],
                lat=[lat],
                mode='markers',
                marker=dict(size=8, color="black", symbol="diamond"),
                text=f"{city}",
                hoverinfo='text',
                showlegend=False
            ))

            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                lon=[lon, lon + dx * constants.LEADER_LINE_SHORTENING_FACTOR],
                lat=[lat, lat + dy * constants.LEADER_LINE_SHORTENING_FACTOR],
                mode='lines',
                line=dict(color="black", width=1.5, dash='dot'),
                showlegend=False,
                hoverinfo='skip'
            ))

            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                lon=[label_lon],
                lat=[label_lat],
                mode='text',
                text=[f"{city}"],
                textfont=dict(size=14, color='black'),
                showlegend=False,
                hoverinfo='skip'
            ))

    def _add_team_markers(self):
        """
        Adds markers for each team showing their current position along the route.
        Teams on their second lap are colored green and include a 'SECOND LAP' note.
        """
        second_lap_threshold = 9800
        df = self.team_progress_df.copy()

        # Identify second-lap teams
        second_lap_teams = list(df.loc[df.Total_Capped_Duration > second_lap_threshold, 'Team_Name'])

        # Adjust distance for second-lap teams
        df.loc[df.Total_Capped_Duration > second_lap_threshold, "Total_Capped_Duration"] -= second_lap_threshold

        # Add team markers with tooltips and coloring
        for _, row in df.iterrows():
            lat, lon = functions_calcVals.interpolate_position(row["Total_Capped_Duration"])
            is_second_lap = row["Team_Name"] in second_lap_teams
            marker_color = "green" if is_second_lap else constants.TEAM_MARKER_COLOR

            tooltip = f"{row['Team_Name']}<br>{row['Total_Capped_Duration']:.1f} km"
            if is_second_lap:
                tooltip += "<br>SECOND LAP"

            self.ROAD2CARY_MAP.add_trace(go.Scattergeo(
                lon=[lon],
                lat=[lat],
                mode='markers',
                marker=dict(size=6, color=marker_color),
                text=tooltip,
                hoverinfo='text',
                showlegend=False
            ))


    def _add_image_and_annotations(self):
        """
        Embeds a static image (e.g., a logo) and a timestamp annotation on the map.
        """
        self.ROAD2CARY_MAP.update_layout(
            images=[
                dict(
                    source=functions_calcVals.IMAGE_URI,
                    xref="paper", yref="paper",
                    x=constants.IMAGE_POSITION_X, y=constants.IMAGE_POSITION_Y,
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
            ]
        )

    def _style_map(self):
        """
        Applies layout and geographic styling to the map: colors, margins, bounds, etc.
        """
        self.ROAD2CARY_MAP.update_layout(
            showlegend=False,
            title=None,
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
            dragmode=False
        )
        self.ROAD2CARY_MAP.update_geos(
            showcountries=True,
            countrycolor=constants.COUNTRY_COLOR,
            showland=True,
            landcolor=constants.LAND_COLOR,
            showocean=True,
            oceancolor=constants.OCEAN_COLOR,
            showcoastlines=True,
            coastlinecolor=constants.COASTLINE_COLOR,
            coastlinewidth=0.3,
            fitbounds="locations",
            resolution=50
        )

    def show(self):
        """
        Displays the interactive map in a browser or notebook using Plotly.
        """
        self.ROAD2CARY_MAP.show(config=constants.MAP_CONFIGS)

    def write_html(self, new_main: bool = False):
        """
        Writes the map to an HTML file.

        Args:
            new_main (bool): If True, writes to 'index.html' in the root directory.
                            If False, writes to 'Data/<date>/index.html'.
        """
        if new_main:
            file_path = "index.html"
        else:
            file_path = os.path.join("Data", self.date, "index.html")
        self.ROAD2CARY_MAP.write_html(file_path, include_plotlyjs='cdn')
