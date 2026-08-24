# Movie Recommendation System

A content-based movie recommendation system built with Python and Flask. It suggests similar movies based on a selected title using cosine similarity on movie metadata.

## Overview

This project analyzes a movie dataset, builds a similarity matrix using content-based filtering, and serves recommendations through a simple Flask web application. Users can search for a movie title and receive a list of similar movies.

## Features

- Content-based recommendation engine using cosine similarity
- Case-insensitive and punctuation-tolerant title search
- Lightweight Flask web interface
- Precomputed model artifacts for fast load times

## Project Structure

```
movie-recommendation-system/
├── data/               # Dataset files
├── static/             # CSS and static assets
├── templates/          # HTML templates
├── main.ipynb          # Data analysis and model building notebook
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md
```

## How It Works

1. Movie metadata is processed and vectorized in `main.ipynb`.
2. A cosine similarity matrix is computed between all movies.
3. The processed data and similarity matrix are saved using `joblib`.
4. The Flask app (`app.py`) loads these artifacts and serves recommendations based on user input.

Search input is normalized before matching: uppercase, lowercase, spacing, and special characters are stripped, so "Avatar", "AVATAR", and "avatar!!" all resolve to the same result. Titles must still match an existing entry; the system does not perform fuzzy matching.

## Installation

Clone the repository:

```bash
git clone https://github.com/RiteshSnippet/movie-recommendation-system.git
cd movie-recommendation-system
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run `main.ipynb` to generate the required `.pkl` files (movie data and similarity matrix), if not already present.
2. Start the Flask application:

```bash
python app.py
```

3. Open your browser and navigate to:

```
http://localhost:5000
```

4. Enter a movie title in the search box to view recommendations.

## Requirements

- Python 3.8+
- Flask
- pandas
- scikit-learn
- joblib

See `requirements.txt` for exact package details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Built as a content-based recommendation system using standard machine learning techniques with scikit-learn and Flask.