from instapy import InstaPy, smart_run
from details import *
import schedule
import time

tags = ["100daysofcode", "react.js", "nodejs", "python",
        "devlife", "webdevelopment", "learnCode", "pythoncode"]
print("Running")

def dailyLikes():
  print("Commenting & Liking")
  session = InstaPy(username=InstaUsername,
                    password=InstaPassword, headless_browser=True)
  with smart_run(session):
    session.set_relationship_bounds(enabled=True, max_followers=8500)
    session.set_do_comment(True, percentage=25)
    session.set_comments(["Love the post! ", "Fantastic", "🔥"])
    session.set_do_follow(True, percentage=25)
    session.like_by_tags(tags, amount=1)
    print("Finished Likes & Comments")


schedule.every().day.at("11:30").do(dailyLikes)

while True:
  schedule.run_pending()
  time.sleep(60)
