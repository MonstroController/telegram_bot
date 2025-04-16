from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from bot.databases.models.base import Base, created_at, updated_at


class ProfilesOrm(Base):
    __tablename__ = "profiles"
    pid: Mapped[int] = mapped_column(primary_key=True)
    data_create: Mapped[created_at]
    party: Mapped[str] = mapped_column(String(40), server_default=None)
    cookies_len: Mapped[int] = mapped_column(server_default=None)
    accounts: Mapped[str] = mapped_column(server_default=None)
    is_google: Mapped[bool] = mapped_column(server_default="f")
    is_yandex: Mapped[bool] = mapped_column(server_default="f")
    is_mail: Mapped[bool] = mapped_column(server_default="f")
    is_youtube: Mapped[bool] = mapped_column(server_default="f")
    ismobiledevice: Mapped[bool] = mapped_column(server_default="f")
    platform: Mapped[str] = mapped_column(String(40), server_default=None)
    platform_version: Mapped[str] = mapped_column(String(40), server_default=None)
    browser: Mapped[str] = mapped_column(String(40), server_default=None)
    browser_version: Mapped[str] = mapped_column(String(40), server_default=None)
    folder: Mapped[str] = mapped_column(String(40), server_default=None)
    fingerprints: Mapped[str] = mapped_column(server_default=None)
    cookies: Mapped[str] = mapped_column(server_default=None)
    localstorage: Mapped[str] = mapped_column(server_default=None)
    proxy: Mapped[str] = mapped_column(server_default=None)
    last_date_work: Mapped[updated_at] = mapped_column(server_default=None)
    date_block: Mapped[updated_at] = mapped_column(server_default=None)
    last_visit_sites: Mapped[str] = mapped_column(String(40), server_default=None)
    last_task: Mapped[str] = mapped_column(String(40), server_default=None)
    geo: Mapped[str] = mapped_column(String(40), server_default=None)
    tel: Mapped[str] = mapped_column(String(40), server_default=None)
    email: Mapped[str] = mapped_column(String(40), server_default=None)
    name: Mapped[str] = mapped_column(String(40), server_default=None)
    mouse_config: Mapped[str] = mapped_column(String(25), server_default=None)
    domaincount: Mapped[int]
    metrikacount: Mapped[int]
    yacount: Mapped[int] = mapped_column(server_default=None)
    warm: Mapped[updated_at] = mapped_column(server_default=None)
