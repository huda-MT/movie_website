import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
         Behavior: Initialize the movie instance.
         Arguments:
         movie_title: title of the movie
         movie_storyline: Shortcut for the movie story
         poster_image: image of the movie poster
         trailer_youtube: YouTube Short Video
          Returns:
          None
         '''

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self): #to show the trailers links
        webbrowser.open(self.trailer_youtube_url)
