class CD:

    def __init__(self, songwriter, title, songs):
        self.songwriter = songwriter
        self.title = title
        self.songs = songs

    def __str__(self):
        return f'Album: {self.title} by {self.songwriter}'

    def __len__(self):
        return self.songs

my_cd = CD('Pink Floyd', 'The Wall', 24)

print(my_cd)
print(len(my_cd))

