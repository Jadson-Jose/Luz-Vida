from fastapi import Response


def apply_pagination(
    response: Response, skip: int = 0, limit: int = 100, total: int = 0
):
    response.headers["X-Total-Count"] = str(total)
    response.headers["X-Skip"] = str(skip)
    response.headers["X-Limit"] = str(limit)
    return response
