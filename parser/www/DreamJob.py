import requests
from bs4 import BeautifulSoup


class DreamJob:
    url = "https://dreamjob.ru/employers/317173"
    site = BeautifulSoup(requests.get(url).text, "lxml")

    def get_reviews(self):
        review_list = self.site.find_all("div", class_="review")

        review_db = []

        for review in review_list:
            rating = review.find("span", class_="dj-rating__value").get_text(strip=True).strip("-")
            text = review.find_all("div", class_="review__text")
            good_text = text[0].get_text(strip=True)
            bad_text = text[1].get_text(strip=True)

            all_rating_item = review.find_all("div", class_="dj-rating")
            items = all_rating_item[0]["data-partly-switch"].replace("rating|", "").split(",")

            working_conditions = float(items[0])
            income_conditions = float(items[1])
            team = float(items[2])
            management = float(items[3])
            recreation_conditions = float(items[4])
            growth_opportunities = float(items[5])

            review_db.append(
                {
                    "rating": float(rating.replace(",", ".")),
                    "text": good_text + " " + bad_text,
                    "good_text": good_text,
                    "bad_text": bad_text,
                    "working_conditions": working_conditions,
                    "income_conditions": income_conditions,
                    "team": team,
                    "management": management,
                    "recreation_conditions": recreation_conditions,
                    "growth_opportunities": growth_opportunities,
                    "Site": "DreamJob",
                }
            )

        return review_db

    def get_site_statistics(self):
        dashboard = self.site.find("div", class_="dashboard")

        rating = dashboard.find("div", class_="dashboard__grade-total").get_text(strip=True).replace(",", ".")

        items = dashboard.find("div", class_="dashboard__ratings").find_all("div", class_="dashboard__rating-val")

        items = [float(item.get_text(strip=True).replace(",", ".")) for item in items]

        working_conditions = items[0]
        team = items[1]
        management = items[2]
        income_conditions = items[3]
        recreation_conditions = items[4]
        growth_opportunities = items[5]

        site_statistics = {
            "rating": float(rating),
            "working_conditions": working_conditions,
            "income_conditions": income_conditions,
            "team": team,
            "management": management,
            "recreation_conditions": recreation_conditions,
            "growth_opportunities": growth_opportunities,
        }

        return site_statistics

    def get_data(self):
        return {"reviews": self.get_reviews(), "site_statistics": self.get_site_statistics(), "name": "DreamJob"}


d = DreamJob()
