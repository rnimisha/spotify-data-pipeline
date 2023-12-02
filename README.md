# Spotify ETL Pipeline

Apache Airflow-driven Spotify Data Pipeline that drives data extraction and transformation, to uncover insights into user behavior and stream trends within the Spotify.

<p align="center">
    <img src="https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white" alt="Spotify">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white" alt="Apache Airflow">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
    <!-- <img src="https://a11ybadges.com/badge?logo=metabase" alt="metabase"> -->
    <img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white" alt="githubactions">
</p>

## Features

- **Spotify API Integration** : Retrieves user's _recently played songs_ data from the Spotify API.
- **Automate Login** : Automates Spotify login and token retrieval with Selenium.
- **Data Cleaning** : Clean and prepare data according to schema.
- **Optimized for Analysis** : Stores refined data into a well-organized star schema for optimized querying.
- **Scheduled Batch Processing** : Utilizes airflow to orchestrate pipeline and schedule for every midnight.

## Analysis Metrics

- **KPI** : The key focus is to analyze user's listening trends, particularly emphasizing hourly activity, and to evaluate artist popularity based on play counts.
- **Granularity** : The grain for this project is user-specific song play durations tracked hourly, emphasizing individual days within weekly cycles of the month.

## Batch Processing Architecture

Orchestrated through Apache Airflow, the data pipeline ensures consistent handling of Spotify data by executing tasks, such as extraction and transformation, at interval of every midnight.

![Architecture Diagram](https://raw.githubusercontent.com/rnimisha/spotify-data-pipeline/main/assets/architecturaldiagram.jpeg)

## OLAP Data Modeling

Star schema model to increase efficiency for Analysis.
![Star Schema](https://raw.githubusercontent.com/rnimisha/spotify-data-pipeline/main/assets/star_schema.png)

## Workflow Overview

Here is a visual representation of the Airflow DAG Tasks:

![Airflow DAG Tasks](https://raw.githubusercontent.com/rnimisha/spotify-data-pipeline/main/assets/runningtask.gif)

## Analytics

The database is connected with metabase to sync analytics.

![Spotify Dashboard](https://raw.githubusercontent.com/rnimisha/spotify-data-pipeline/main/assets/spotifydashboard.jpeg)

Clicking on the aritist will redirect to artist based dashboard.
![Aritist Dashboard](https://raw.githubusercontent.com/rnimisha/spotify-data-pipeline/main/assets/artistdashboard.jpeg)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in root of the project

| Name                     | Description                                         |
| ------------------------ | --------------------------------------------------- |
| SPOTIFY_CLIENT_ID        | Spotify client ID.                                  |
| SPOTIFY_CLIENT_SECRET    | Spotify Client Secret.                              |
| POSTGRES_DB              | Name of the PostgreSQL database.                    |
| POSTGRES_USER            | Username for accessing the PostgreSQL database.     |
| POSTGRES_PASSWORD        | Password for the PostgreSQL database.               |
| POSTGRES_HOST            | Hostname or IP address for the PostgreSQL database. |
| POSTGRES_PORT            | Port number for the PostgreSQL database.            |
| AIRFLOW_UID              | User ID for the Apache Airflow service.             |
| AIRFLOW_DB_NAME          | Name of the database used by Apache Airflow.        |
| AIRFLOW_ADMIN_USER       | Username for the Apache Airflow admin account.      |
| AIRFLOW_ADMIN_PASSWORD   | Password for the Apache Airflow admin account.      |
| AIRFLOW_ADMIN_FIRSTNAME  | First name of the Apache Airflow admin user.        |
| AIRFLOW_ADMIN_LASTNAME   | Last name of the Apache Airflow admin user.         |
| PGADMIN_DEFAULT_EMAIL    | Email for the PGAdmin tool.                         |
| PGADMIN_DEFAULT_PASSWORD | Password for the PGAdmin tool.                      |
| MY_SPOTIFY_PASSWORD      | Password for the Spotify user account.              |
| MY_SPOTIFY_USERNAME      | Username or email for the Spotify user account.     |

## Prerequisites

Before proceeding with this project, ensure you have the following:

- **Git:** Version control. [Download Git](https://git-scm.com/downloads)
- **Docker:** Containerization. [Get Docker](https://www.docker.com/products/docker-desktop)
- **Docker Compose:** Running Multi-container Docker applications. [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the project from the repository.

```bash
  git clone https://github.com/rnimisha/spotify-data-pipeline.git
```

2. Duplicate the `.env.example` file and rename it to `.env`.

```bash
  cp .env.example .env
```

3. Adjust values for environment variables
4. Build images and run the services.

```bash
  docker compose up -d --build
```

5. Access the Airflow webserver in your localhost running at port 8080.

## Future Scope

- **Testing** : Implement unit testing.
- **Storage** : Use storage like mongoDb instead of csv for staging datas.
