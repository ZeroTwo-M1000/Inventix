from typing import Optional

from pydantic import BaseModel


class SBaseReview(BaseModel):
    text: str
    bad_text: Optional[str] = None
    good_text: Optional[str] = None
    rating: Optional[float] = None
    working_conditions: Optional[float] = None
    income_conditions: Optional[float] = None
    management: Optional[float] = None
    team: Optional[float] = None
    growth_opportunities: Optional[float] = None
    recreation_conditions: Optional[float] = None


class SReviewParse(SBaseReview):
    Site: str


class SReviewCreate(SBaseReview):
    siteId: str
