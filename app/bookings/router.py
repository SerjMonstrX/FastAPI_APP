from fastapi import APIRouter, Depends

from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]:
    print(user, type(user), user.email)
    # return await BookingDAO.find_by_id()
