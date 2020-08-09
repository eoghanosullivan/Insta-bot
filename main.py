from instapy import InstaPy
from details import *

session = InstaPy(username=InstaUsername,
                  password=InstaPassword, headless_browser=True)
session.login()
session.like_by_tags(["100daysofcode", "react.js",
                      "nodejs", "pythn"], amount=5)
session.set_relationship_bounds(enabled=True, max_followers=8500)
session.set_do_comment(True, percentage=75)
session.set_comments(["Love the post! ", "Fantastic", "🔥"])
session.end()
