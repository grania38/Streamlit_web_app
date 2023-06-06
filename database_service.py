import harperdb
from yt_extractor import get_info

url = "https://cloud-1-grania388.harperdbcloud.com"
username = "grania"
password = "Bonjour123456!"

db = harperdb.HarperDB(url=url, username=username, password=password)
# print(db.describe_all())

SCHEMA = "workout_repo"
TABLE = "workouts"
TABLE_TODAY = "workout_today"
def insert_workout(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])

def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])

def get_all_workouts():
    return db.sql(f"Select * from {SCHEMA}.{TABLE}")

def get_workout_today():
    return db.sql(f"Select * from {SCHEMA}.{TABLE_TODAY}")

def update_workout_today(workout_data, insert=False):
    workout_data["id"]=0
    if insert:
        return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
    return db.update(SCHEMA, TABLE_TODAY, [workout_data])

# infos = get_info("youtube video url !!!!!!!!!!")
# print(infos)
# insert_workout(infos)
# workouts = get_all_workouts()
# print(workouts)
