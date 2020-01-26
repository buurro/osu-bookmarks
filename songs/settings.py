import environ

root = environ.Path(__file__) - 2  # two folder back (/a/b/ - 2 = /)

env = environ.Env(
    OSU_API_KEY=(str,'')
)
env.read_env(root('.env'))

OSU_API_KEY = env('OSU_API_KEY')
