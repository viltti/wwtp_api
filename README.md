# Wastewater Treatment Data API

## Overview

This RESTful API is designed for use with a data application, which further processes the fetched data to create actionable insights for professionals in the field. The API fetches data from the database and forwards it to the data application. It provides multiple endpoints for fetching the data, making it flexible and useful for various data analysis, visualization and modeling tasks. It provides the flexibility to fetch data for all variables, or for a specific variable. Fetching data for a specific variable reduces the amount of data transferred, leading to quicker responses.

## Endpoints

The API consists of the following endpoints:

* `/data` : Fetches the latest data point that matches the current datetime.
* `/data/hour` : Fetches the data for the previous hour from the current datetime.
* `/data/day` : Fetches the data for the previous day from the current datetime.
* `/data/all` : Fetches all available historical data before the current datetime

* `/variables`: Fetches the names of all available variables.

* `/data/variable/<variable>`: Fetches the latest data point for a specified variable.
* `/data/variable/<variable>/hour`: Fetches the data for the previous hour for a specified variable.
* `/data/variable/<variable>/day`: Fetches the data for the previous day for a specified variable.
* `/data/variable/<variable>/history`: Fetches all available historical data for a specified variable.

Replace `<variable>` with the name of the variable you want data for.