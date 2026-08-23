import re
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

df = joblib.load('movies.pkl')
cosine_sim = joblib.load('similarity.pkl')


def get_recommendations(title, cosine_sim=cosine_sim):
    title = re.sub(r'[^a-zA-Z0-9]', '', title).lower()

    matches = df[df['normalized_title'] == title]

    if matches.empty:
        return None

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices].tolist()


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    searched_title = None
    not_found = False

    if request.method == 'POST':
        searched_title = request.form.get('title', '').strip()
        if searched_title:
            recommendations = get_recommendations(searched_title)
            if recommendations is None:
                not_found = True

    return render_template(
        'index.html',
        recommendations=recommendations,
        searched_title=searched_title,
        not_found=not_found
    )


if __name__ == '__main__':
    app.run(debug=True)