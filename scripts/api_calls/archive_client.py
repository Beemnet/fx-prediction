class ArchiveClient:

    def __init__(self, base_url=None):
        self.base_url = base_url

    def fetch_text(self, url: str) -> str:
        raise NotImplementedError("ArchiveClient not implemented.")