"""
@author: ToshY
"""

import base64
from dataclasses import dataclass
from wsgiref.simple_server import make_server
import falcon
import cloudscraper
import validators
from src.banner import banner


@dataclass
class ImageResource:
    """
    ImageResource
    """

    def on_get(self, req, resp):
        """
        GET method for requesting image from URL
        :param req:
        :param resp:
        :return:
        """
        image_url = req.get_param("url") or ""

        if not validators.url(image_url):
            # pylint: disable=maybe-no-member
            raise falcon.HTTPBadRequest(
                title="Invalid URL",
                description=(
                    f"The supplied URL `{image_url}` is invalid"
                ),
            )

        result = scraper.get(image_url).content
        b64_image = base64.b64encode(result).decode("utf-8")

        # pylint: disable=maybe-no-member
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = b64_image


app = falcon.App()
image_endpoint = ImageResource()
app.add_route("/image", image_endpoint)

if __name__ == "__main__":
    banner("cloudscraper")
    scraper = cloudscraper.create_scraper()

    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")

        # Serve until process is killed
        httpd.serve_forever()
