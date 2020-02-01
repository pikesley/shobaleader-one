from flask import request
from flask_api import FlaskAPI

from lib.light_grid import LightGrid
from lib.panel import Panel
from lib.performers.dot import Dot
from lib.performers.marquee import Marquee
from lib.performers.simple import SimplePerformer
from lib.shobaleader import Shobaleader

app = FlaskAPI(__name__)

leader = Shobaleader()

performer_lookups = {"dot": Dot, "marquee": Marquee, "simple": SimplePerformer}


@app.route("/perform/<performer>", methods=["POST", "PATCH"])
def perform(performer):
    if not request.content_length:
        data = {}
    else:
        data = request.get_json()

    leader.run(performer_lookups[performer], **data)
    return {"status": "OK"}


@app.route("/matrix", methods=["POST", "PATCH"])
def matrix():
    if not request.content_length:
        return {"error": "No data"}, 422

    data = request.get_json()
    if not "matrix" in data:
        return {"error": "Bad data"}, 422

    grid = LightGrid(data["matrix"])
    leader.stop()
    leader.panel.display(grid)
    return {"status": "OK"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
