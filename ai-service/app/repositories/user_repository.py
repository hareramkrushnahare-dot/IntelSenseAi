from sqlalchemy import select
from app.repositories.base_repository import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository):
    async def get_by_username(self, username: str):
        q = select(User).where(User.username == username)
        res = await self.session.execute(q)
        return res.scalar_one_or_none()
