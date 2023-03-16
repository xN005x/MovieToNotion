import requests, os
from dotenv import load_dotenv

load_dotenv()

movie_key = os.getenv('TMDB_API_KEY')
notion_key = os.getenv('NOTION_API_KEY')
databaseId = os.getenv('NOTION_DATABASE_ID')
language = os.getenv('LANGUAGE')

# Recuperation des informations sur le film
def get_movie_info(movie_title):
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={movie_key}&query={movie_title}&language={language}")
    movie_data = response.json()
    movie_id = movie_data['results'][0]['id']
    movie_details = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={movie_key}&append_to_response=credits&language={language}")
    movie_details = movie_details.json()
    return movie_details

# Demander à l'utilisateur de saisir le nom d'un film
movie_title = input("Which movie do you want to add ? ")

# Récupérer les informations sur le film
movie_details = get_movie_info(movie_title)

# Stocker les informations sur le film dans des variables
film_titre = movie_details['title']
sortie_date = movie_details['release_date']
realisateur = movie_details['credits']['crew'][0]['name']
duree = movie_details['runtime']
heures = duree // 60
minutes = duree % 60
duree = str(heures)+'h'+str(minutes)
poster = "https://image.tmdb.org/t/p/w1280" + movie_details['poster_path']


acteurs = []
cpt = 0
for actor in movie_details['credits']['cast']:
    if cpt < 10 :
        cpt +=1
        acteurs.append(actor['name'])

genres = []
for genre in movie_details['genres']:
    genres.append(genre['name'])

resume = movie_details['overview']

movie_infos = {'title' : film_titre, 'release' : sortie_date, 'real' : realisateur, 'time' : duree, 'actors' : acteurs, 'genres' : genres, 'resume' : resume, 'poster' : poster}


headers = {
    "Authorization": "Bearer " + notion_key,
    "Notion-Version": "2022-06-28"
}

def createPage(databaseId, headers, movie_infos):
    createUrl = f"https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId },
        "cover": {
            "external": {
                "url": movie_infos['poster']
            }
        },
        "properties": {
            "Nom": {
                "title": [
                    {
                        "text": {
                            "content": movie_infos['title']
                        }
                    }
                ]
            },
            "Genres": {
                "multi_select": [
                    {
                        "name": movie_infos['genres'][0]
                    },
                    {
                        "name": movie_infos['genres'][1]
                    }
                ]
            },
            "Sortie": {
                "date": {
                    "start": movie_infos['release']
                }
            },
            "Durée": {
                "rich_text": [
                    {
                        "text": {
                            "content": movie_infos['time']
                        }
                    }
                ]
            },
            "Acteurs": {
                "multi_select": [
                    {
                        "name": movie_infos['actors'][0]
                    },
                    {
                        "name": movie_infos['actors'][1]
                    },
                    {
                        "name": movie_infos['actors'][2]
                    },
                    {
                        "name": movie_infos['actors'][3]
                    },
                    {
                        "name": movie_infos['actors'][4]
                    },
                    {
                        "name": movie_infos['actors'][5]
                    },
                    {
                        "name": movie_infos['actors'][6]
                    },
                    {
                        "name": movie_infos['actors'][7]
                    },
                    {
                        "name": movie_infos['actors'][8]
                    },
                    {
                        "name": movie_infos['actors'][9]
                    }
                ]
            },
            "Réalisateur": {
                "select": {
                    "name": movie_infos['real']
                }
            }
        },
        "children": [
           {
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": movie_infos['resume']
                            }
                        }
                    ]
                }
            }
        ]
    }
    

    res = requests.request("POST", createUrl, headers=headers, json=newPageData)
    data = res.json()
    print(res.status_code)

createPage(databaseId, headers, movie_infos)
