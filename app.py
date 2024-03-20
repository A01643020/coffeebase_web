from website import create_app
from website.views import show_from_database

app = create_app()

if __name__ == '__main__':
    show_from_database()