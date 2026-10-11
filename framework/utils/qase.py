import json
from urllib.request import Request, urlopen

from settings import settings

PAGE_SIZE = 100


def fetch_case_titles(case_ids: set[int]) -> dict[int, str]:
    """
    Fetches titles of the given test cases from the Qase TestOps.

    Returns
    -------
    dict[int, str]
        A mapping of a test case ID to its title. Cases not found in Qase are omitted.
    """
    titles: dict[int, str] = {}
    offset = 0

    while True:
        request = Request(  # noqa: S310 - fixed https URL
            f"{settings.qase_api_url}/case/{settings.qase_testops_project}?limit={PAGE_SIZE}&offset={offset}",
            headers={"Token": settings.qase_testops_api_token, "Accept": "application/json"},
        )
        with urlopen(request, timeout=10) as response:  # noqa: S310 - fixed https URL
            result = json.load(response)["result"]

        titles |= {case["id"]: case["title"] for case in result["entities"] if case["id"] in case_ids}

        offset += PAGE_SIZE
        if titles.keys() >= case_ids or offset >= result["total"]:
            return titles
