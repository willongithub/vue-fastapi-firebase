from fastapi import Depends, HTTPException, status

from back.app import oauth2_scheme


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


def decode_token(token: str):
    """_summary_

    Args:
        password (str): _description_

    Returns:
        _type_: _description_
    """
    # TODO
    return


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def hash_password(password: str):
    """_summary_

    Args:
        password (str): _description_

    Returns:
        _type_: _description_
    """
    # TODO
    return password


def get_user(username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
