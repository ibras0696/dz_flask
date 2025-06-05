import requests



#
def post_add_movie(title: str, genre: str, year: str, rating: str, description: str):
    url_post = 'http://127.0.0.1:5000/movies/add/'
    headers = {
        'title': title,
        'genre': genre,
        'year': year,
        'rating': rating,
        'description': description,
    }
    response = requests.post(url_post, headers=headers)
    print(f'Статус кода: {response}')
    print(response.text)
    return response.status_code

#
# print(post_add_movie(
#     title='Deadpool',
#     genre='REAL',
#     year=str(2015),
#     rating=str(4.2),
#     description='fantastic movie it pull sheet'
# ))