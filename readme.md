# Readme
This is a prototype for the Pillar take home. The frontend is extremely bare bones as I wasn't able to get a Plot.ly dashboard working. Please note that I haven't worked in Python in a while, but I really wanted to give it a shot since I know Pillar works in that environment.

## Installation and Usage
Projects uses Pip and Python 3+. Would recommend install pipenv if you don't have it already.


```bash
pipenv install
pipenv shell
python server.py
```

Go to `localhost:5000` and search for the repo you're looking for

## Roadmap

1. Please see TODOs. 
2. App can be upgraded completely on the front end to use something modern (React) 
3. Backend needs to be unit tested 
4. Dashboard can be responsive and interactive
5. Data caching to speed up dashboard
6. OAuth instead of basic authentication
7. Contributors API call needs to be paginate so that it can capture all contributions