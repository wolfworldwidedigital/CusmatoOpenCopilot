from typing import List, Type
from shared.models.opencopilot_db import async_engine, PdfDataSource, WebsiteDataSource
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from models.repository.utils import db_session

async_session = async_sessionmaker(
    async_engine, expire_on_commit=False
)  # Use your session factory


@db_session
async def get_all_pdf_datasource_by_bot_id(
    session: AsyncSession, bot_id: str, limit: int = 20, offset: int = 0
):
    datasources = (
        await session.scalars(
            select(PdfDataSource)
            .where(PdfDataSource.chatbot_id == bot_id)
            .order_by(PdfDataSource.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
    ).all()

    return datasources


@db_session
async def get_all_website_datasource_by_bot_id(
    session: AsyncSession, bot_id: str, limit: int = 20, offset: int = 0
):
    datasources = (
        await session.scalars(
            select(WebsiteDataSource)
            .where(WebsiteDataSource.chatbot_id == bot_id)
            .order_by(WebsiteDataSource.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
    ).all()

    return datasources
