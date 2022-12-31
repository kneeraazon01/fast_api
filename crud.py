# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import CarInfoInfoAlreadyExistError, CarInfoNotFoundError
from models import CarInfo
from schemas import CreateAndUpdateCar


# Function to get list of car info
# def get_all_cars(session: Session, limit: int, offset: int) -> List[CarInfo]:
    # return session.query(CarInfo).offset(offset).limit(limit).all()

# Function to  get info of a particular show
def get_show_info_by_id(session: Session, _id: int) -> ShowInfo:
    show_info = session.query(ShowInfo).get(_id)

    if show_info is None:
        raise ShowInfoNotFoundError

    return show_info