# Football-Data-Pull

Pretty much what the title says! The initial start of grabbing some data to perform some kind of analytics on it 
(version 0.01 so yea not much too it yet). There isn't any testing yet but don't fret it'll come. 
This is more of the data engineering portion of the project, grab some data, 
mold it into something nice, create API to query from it. 
# Notes: 
one repository of what will be many. This is data aggregation, 
to display it in a way that people understand it with the goal to provide this information for everyone. 
I want to make soccer more inviting to the general population. 

## Data Collection and where its coming from
In its current state this is strictly just a `python3` application. It primarly uses `Pandas` to collect 
the data by downloading multiple Excel sheets from [FootballDataUK](https://www.football-data.co.uk/), 
so complete shout out to Joseph Buchdahl who compiles this information for free. 

End goal here is to hopefully get more sources and combine them together. 

## Leagues provided 
| League Name           | Country     |
|-----------------------|-------------|
| Premier League        | England     |
| Championship          | England     |
| Scottish Premiership  | Scotland    |
| Scottish Championship | Scotland    |
| Bundesliga            | Germany     |
| Bundesliga2           | Germany     |
| Seria A               | Italy       |
| Seria B               | Italy       |
| La Liga               | Spain       |
| La Liga 2             | Spain       |
| Ligue 1               | France      |
| Ligue 1               | France      |
| Eredivisie            | Netherlands |
| Belgium Pro League    | Belgium     |
| Liga Portugal         | Portugal    |

## Testing

### `.env` variables
Create your own .env file and make sure to use these variables below for the dockerized
Postgres container to work. These correspond within the `PostgresUtils` class
```
POSTGRES_USER=<insert-here>
POSTGRES_PASSWORD=<insert-here>
POSTGRES_DB=<insert-here>
POSTGRES_PORT=<insert-here>
POSTGRES_HOST=<insert-here>
```

### Docker commands
To run this without anykind of PGAdmin or having to download Postgres simply run 
```
1. docker-compose up [-d] <if you'd like to run in background>

Optional (to check if the docker container has been set up properly): 
2. docker exec -it <docker-container-id> bash 
3. psql -U <POSTGRES_USER> <POSTGRES_DB>
```
if all goes well then you should be able to `exec` into our newly created docker container which 
will hold our Footy Data.

### Running the backfill
Once the docker container is up and running and your `.env` variables are in place simply 
go into your terminal and run the command below. 
```
python3 run_backfill.py
```

## Authors
If you've got any question please don't hesitate to reach out. 
- [@salarchitetto](https://www.github.com/salarchitetto) and hopefully some others soon. 