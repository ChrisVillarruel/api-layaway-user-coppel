from decouple import config

# MongoDb Atlas access database
USERNAME = config("USERNAME_DB")
PASSWORD = config("PASSWORD")
DATABASE = config("DATABASE")
