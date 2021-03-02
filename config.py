import os

COURSES_PATH = os.getenv('COURSES_PATH') or os.path.join(os.path.expanduser('~'), '.scripts', 'unischedule_data', 'courses.yml')

ICON_PATH = os.getenv('ICON_PATH') or os.path.join(os.getcwd(), 'icon.png')
