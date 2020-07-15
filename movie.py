from bs4 import BeautifulSoup
import urllib.request as req

url = "https://movie.naver.com/movie/running/current.nhn"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

movie_table = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap > ul")
movie_tr = movie_table[0].select("li")
for movie in movie_tr:
    movie_detail = movie.select("dl > dt > a")[0]
    movie_title = movie_detail.string
    movie_link = "http://movie.naver.com" + movie_detail["href"]
    movie_rating = movie.select("dl > dd.star > dl.info_star > dd > div > a > span.num")[0].string
    movie_genre = movie.select("dl > dd > dl > dd > span.link_txt > a")[0].string
    if movie_rating >= '9' and movie_genre == '드라마':
        print(f"제목: {movie_title}")
        print(f"영화 정보: {movie_link}")

