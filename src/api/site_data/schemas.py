from typing import Optional

from pydantic import BaseModel


class SBaseSiteData(BaseModel):
    rating: Optional[float] = None
    working_conditions: Optional[float] = None
    income_conditions: Optional[float] = None
    management: Optional[float] = None
    team: Optional[float] = None
    growth_opportunities: Optional[float] = None
    recreation_conditions: Optional[float] = None


class SBaseSiteDataParse(SBaseSiteData):
    pass


class SBaseSiteDataCreate(SBaseSiteData):
    siteId: str
    count_review: int
    count_bad_review: int
    count_good_review: int
