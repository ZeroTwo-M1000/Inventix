from core.config import settings


class SiteDAO:
    @staticmethod
    def get_all():
        return settings.prisma_connection.prisma.site.find_many(
            include={
                "sitedata": True,
                "reviews": True,
            }
        )

    @staticmethod
    def get_by_name(name: str):
        return settings.prisma_connection.prisma.site.find_first(where={"name": name})

    @staticmethod
    def get_by_name_full(name: str):
        return settings.prisma_connection.prisma.site.find_first(where={"name": name}, include={
            "sitedata": True,
            "reviews": True,
        })
