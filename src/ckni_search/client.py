import httpx

class CNKIClient:
    BASE_HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120 Safari/537.36"
        ),
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    def __init__(self, timeout: float = 15.0):
        self.client = httpx.Client(
            headers=self.BASE_HEADERS,
            timeout=timeout,
            follow_redirects=True
        )

    def get(self, url: str, **kwargs):
        resp = self.client.get(url, **kwargs)
        resp.raise_for_status()
        return resp
