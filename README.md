# Wastewater Treatment Data API

## Overview

This RESTful API is designed for use with a data application, which processes the data fetched from this API and creates visualizations using Plotly/Dash. It fetches data from the database and forwards it to the data application. The API provides multiple endpoints for fetching the data, making it flexible and useful for various data analysis and visualization tasks.

## Endpoints

The API consists of the following endpoints:

* /data : Fetches the latest data point that matches the current datetime.
* /data/hour : Fetches the data for the previous hour from the current datetime.
* /data/day : Fetches the data for the previous day from the current datetime.
* /data/all : Fetches all available historical data before the current datetime