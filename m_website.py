import fresh_tomatoes
import media

The_Greatest_showman = media.Movie ("The Greatest Showman" , "Celebrates the birth of show business, and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation." ,"https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png" ,"https://www.youtube.com/watch?v=jr9QtXwC9vc" )
Passengers = media.Movie("Passengers" , "A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early." , "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg" , "https://www.youtube.com/watch?v=xb6qmxVrzC4" )
the_beauty = media.Movie("The Beauty And The Beast" , "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love." , "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg","https://www.youtube.com/watch?v=e3Nl_TCQXuw")
Shape_Of_w = media.Movie("The Shape Of Water" , "At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity." , "https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png" , "https://www.youtube.com/watch?v=XFYWazblaUA")
get_out = media.Movie("Get Out ", "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point." , "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png" , "https://www.youtube.com/watch?v=DzfpyUB60YY")
wonder = media.Movie("Wonder" , "Based on the New York Times bestseller, WONDER tells the incredibly inspiring and heartwarming story of August Pullman, a boy with facial differences who enters 5th grade, attending a mainstream elementary school for the first time." , "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_%28film%29.png" , "https://www.youtube.com/watch?v=Ob7fPOzbmzE")
split = media.Movie("Split" , "Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th." ,"https://upload.wikimedia.org/wikipedia/en/3/31/Split_%282017_film%29.jpg", "https://www.youtube.com/watch?v=84TouqfIsiI")

movies = [The_Greatest_showman , Passengers , the_beauty , Shape_Of_w , get_out , wonder , split]
fresh_tomatoes.open_movies_page(movies)
