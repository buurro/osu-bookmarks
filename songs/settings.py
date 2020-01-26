import environ

root = environ.Path(__file__) - 2  # two folder back (/a/b/ - 2 = /)

env = environ.Env()
env.read_env(root('.env'))

OSU_API_KEY = env('OSU_API_KEY')
