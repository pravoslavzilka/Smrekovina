from flask import Blueprint

user_platform = Blueprint("user_platform", __name__, template_folder="templates", static_folder="static")


@user_platform.route("/view")
def platform_view():
    return "platform"

