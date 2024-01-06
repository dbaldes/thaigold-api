# Thai Gold Price API

## Overview
The Thai Gold Price API is a simple Flask-based web service that scrapes the current gold price from a designated website and presents the data in JSON format. It's containerized using Docker for easy deployment and management.

## Features
- Scrapes the latest gold prices from a Thai gold price website.
- Presents data in a structured JSON format.
- Runs in a Docker container for portability and ease of deployment.
- Caches responses to minimize redundant scraping and improve performance.

## Installation

### Build the Docker Image
To build the Docker image, run the following command in the project directory:

```
docker build -t thaigoldapi .
```

### Run the Container
To start the container, run:

```
docker run -p 5003:5000 thaigoldapi
```

This command maps port 5003 on your host to port 5000 in the container.

Once the server is running, you can access the API at: http://localhost:5003/thaigold

Example output:

```
{
"bar_buy":"33,550.00",
"bar_sell":"33,650.00",
"date_time":"06/01/2567 09:00",
"jewelry_buy":"32,942.68",
"jewelry_sell":"34,150.00"
}
```
