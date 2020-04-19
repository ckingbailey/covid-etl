# Fetch COVID-19 case data and load it into a Google Sheet
## Extract
Get data on a daily basis from a couple of GitHub repos. For US data we're using [NYT](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv). For world we plan to use [JHU](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv).

## Transform
NYT CSV comes in a shape like
```
<date 1>, <county 1>, <state 1>, <census area>, <cases>, <deaths>
<date 1>, <county 2>, <state 1>, <census area>, <cases>, <deaths>
<date 1>, <county 3>, <state 2>, <census area>, <cases>, <deaths>
<date 2>, <county 1>, <state 1>, <census area>, <cases>, <deaths>
<date 2>, <county 2>, <state 1>, <census area>, <cases>, <deaths>
<date 2>, <county 3>, <state 2>, <census area>, <cases>, <deaths>
```

For the Google Sheets output, I would like it to take the form of

#### County
Date ⬇︎  | <county 1> | <county 2> | <county 3> |
---------|------------|------------|------------|
<date 1> | # cases    | # cases    | # cases    |
<date 2> | # cases    | # cases    | # cases    |
<date 3> | # cases    | # cases    | # cases    |

#### County Deaths
Date ⬇︎  | <county 1> | <county 2> | <county 3> |
---------|------------|------------|------------|
<date 1> | # deaths   | # deaths   | # deaths   |
<date 2> | # deaths   | # deaths   | # deaths   |
<date 3> | # deaths   | # deaths   | # deaths   |

#### State
Date ⬇︎  | <state 1>  | <state 2>  | <state 3>  |
---------|------------|------------|------------|
<date 1> | # cases    | # cases    | # cases    |
<date 2> | # cases    | # cases    | # cases    |
<date 3> | # cases    | # cases    | # cases    |

#### State Deaths
Date ⬇︎  | <state 1>  | <state 2>  | <state 3>  |
---------|------------|------------|------------|
<date 1> | # deaths   | # deaths   | # deaths   |
<date 2> | # deaths   | # deaths   | # deaths   |
<date 3> | # deaths   | # deaths   | # deaths   |

Country and World should follow similar pattern when we get there. JHU CSV comes in a different shape, like
```
State, Country, Lat, Long, <date 1>, <date 2>, <date 3>
<state 1>, <country 1>, <lat>, <long>, <cases>, <cases>, <cases>
<state 2>, <country 2>, <lat>, <long>, <cases>, <cases>, <cases>
<state 3>, <country 2>, <lat>, <long>, <cases>, <cases>, <cases>
```

There's a seperate sheet for deaths, and one for global recovered.

## Load
Write each output CSV to separate sheets in a Google Sheet once a day.

## Develop
It's written in Python 3. Colin is using [Pipenv](https://pipenv.pypa.io/en/latest/). Lee is using [Conda](https://docs.conda.io/en/late). Colin is a carrot; Lee is a pea. You can do what you want. Be a beet if you feel like it.

To access Google Cloud Platform resources you'll need a GCP credentials file, and you'll need to point an env var at the location of that file so that the GCP libraries know where to look for it. Ask someone on the project to get a GCP creds JSON for you.

## Deploy
Project is deployed on Google Cloud Platform.
### Cloud Resources:
- Google Cloud Functions
- Google Cloud Storage buckets
- Google Cloud Pub/Sub
- Google Cloud Scheduler
