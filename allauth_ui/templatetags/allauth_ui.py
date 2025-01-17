import re
from pathlib import Path

from django import template

register = template.Library()


socialprovider_colors = {
    "GitHub": "bg-stone-900 hover:bg-black",
    "Facebook": "bg-blue-700 hover:bg-blue-800",
    "Google": "bg-red-700 bg-red-800",
}


input_css_path = Path(__file__).parent / ".." / "static" / "allauth_ui" / "input.css"
social_colors = []

with open(input_css_path, encoding="utf8") as f:
    for line in f.readlines():
        m = re.search(r"\.social-(?P<provider>\w+)\s?", line)
        if m:
            social_colors.append(m.groupdict()["provider"])


@register.filter()
def socialprovider_color(socialprovider):
    name = socialprovider.name.lower()
    if name in social_colors:
        return f"social-{name}"
    return "bg-stone-900 hover:bg-black"
