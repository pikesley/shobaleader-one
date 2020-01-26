from flask import request
from flask_api import FlaskAPI

from lib.performers.dot import Dot
from lib.performers.simple import SimplePerformer
from lib.shobaleader import Shobaleader

app = FlaskAPI(__name__)

leader = Shobaleader()

performer_lookups = {"simple": SimplePerformer, "dot": Dot}


@app.route("/perform/<performer>", methods=["POST", "PATCH"])
def perform(performer):
    if not request.content_length:
        data = {}
    else:
        data = request.get_json()

    leader.run(performer_lookups[performer], **data)
    return {"status": "OK"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
