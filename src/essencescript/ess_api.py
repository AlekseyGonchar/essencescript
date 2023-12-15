from time import sleep

import httpx

from essencescript.essence_models import ActivityDto, MethodDto, PatternDto, PracticeDto, WorkProductDto


class EssenceAPI:
    # api_url = "http://localhost:5184"
    api_url = "https://essence-backend.freydin.space"

    def __init__(
        self,
        login: str = "Admin@localhost.local",
        password: str = "Admin123",
    ) -> None:
        self._login = login
        self._auth = ""
        self._password = password
        self.login(login, password)

    def login(self, login: str, password: str) -> None:
        sleep(0)
        response = httpx.post(
            f"{self.api_url}/authentication/login",
            json={"userIdentificationInfo": login, "password": password},
        )
        self._auth = response.json()["entity"]["accessToken"]

    def create_practice(self, practice: PracticeDto) -> PracticeDto:
        sleep(0)
        response = httpx.post(
            f"{self.api_url}/practice/create",
            headers={"Authorization": f"Bearer {self._auth}"},
            params={"versionId": practice.versionId},
            json={
                "name": practice.name,
                "description": practice.description,
                "areaOfConcernId": practice.areaOfConcern.id,
                "methodId": practice.methodId,
                "VersionId": str(practice.versionId),
            },
        )
        entity = response.json()["entity"]
        return PracticeDto(**practice.model_dump(exclude_unset=True), id=entity["id"])

    def create_method(self, method: MethodDto) -> MethodDto:
        sleep(0)
        response = httpx.post(
            f"{self.api_url}/methods/create",
            headers={"Authorization": f"Bearer {self._auth}"},
            json={"name": method.name, "description": method.description, "isPublic": True, "isPracticeMethod": False},
        )
        return MethodDto(
            **method.model_dump(exclude_unset=True),
            id=response.json()["id"],
            versionId=response.json()["versionId"],
        )

    def create_work_product(self, product: WorkProductDto) -> WorkProductDto:
        sleep(0)
        response_elem_create = httpx.post(
            f"{self.api_url}/elements/create",
            params={"versionId": product.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "name": product.name,
                "description": product.description,
                "elementType": product.elementType,
                "areaOfConcern": product.areaOfConcern.model_dump(),
                "order": None,
                "groupId": str(product.groupId),
                "isSaved": False,
                "isActive": False,
            },
        )
        product.id = response_elem_create.json()["entity"]["id"]

        sleep(0)
        describes_response = httpx.post(
            f"{self.api_url}/workProduct/set/describes",
            params={"versionId": product.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(product.id),
                "describes": [
                    {
                        "isParent": item.isParent,
                        "lowerBound": "0",
                        "upperBound": "N",
                        "id": item.relatedElement.id,
                    }
                    for item in product.describes
                ],
                "VersionId": product.versionId,
            },
        )

        sleep(0)
        desc_response = httpx.post(
            f"{self.api_url}/elements/set/description",
            params={"versionId": product.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(product.id),
                "description": product.description,
                "VersionId": str(product.versionId),
            },
        )

        for level_of_detail in product.states:
            sleep(0)
            states_response = httpx.post(
                f"{self.api_url}/workProduct/{product.id!s}/createLevelOfDetail",
                params={"versionId": product.versionId},
                headers={"Authorization": f"Bearer {self._auth}"},
                json={
                    "checkpoints": [],
                    "id": None,
                    "name": level_of_detail.name,
                    "description": level_of_detail.description,
                },
            )
            level_of_detail.id = states_response.json()["entity"]["id"]

        return product

    def create_activity(self, activity: ActivityDto) -> ActivityDto:
        sleep(0)
        response_elem_create = httpx.post(
            f"{self.api_url}/elements/create",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "name": activity.name,
                "description": activity.description,
                "elementType": activity.elementType,
                "areaOfConcern": activity.areaOfConcern.model_dump(),
                "order": None,
                "groupId": str(activity.groupId),
                "isSaved": False,
                "isActive": False,
            },
        )
        activity.id = response_elem_create.json()["entity"]["id"]

        sleep(0)
        desc_response = httpx.post(
            f"{self.api_url}/elements/set/description",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(activity.id),
                "description": activity.description,
                "VersionId": str(activity.versionId),
            },
        )

        sleep(0)
        states_response = httpx.post(
            f"{self.api_url}/activity/set/workProductCriteria",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(activity.id),
                "inOrOut": 1,
                "criteria": [
                    {"levelOfDetailId": str(item.relatedElement.relatedElement.id), "orBeyond": False}
                    for item in activity.outWorkProductCriteria
                ],
                "VersionId": str(activity.versionId),
            },
        )

        sleep(0)
        related_to_response = httpx.post(
            f"{self.api_url}/elements/set/relatedTo",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(activity.id),
                "relatedTo": [{"id": str(item.relatedElement.id), "isOwned": True} for item in activity.relatedTo],
                "VersionId": str(activity.versionId),
            },
        )

        sleep(0)
        competencies_response = httpx.post(
            f"{self.api_url}/activity/set/requiredCompetencyLevels",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(activity.id),
                "requiredLevels": [
                    {"competencyLevelId": str(item.relatedElement.id)} for item in activity.requiredCompetencyLevels
                ],
                "VersionId": str(activity.versionId),
            },
        )

        sleep(0)
        states_in_response = httpx.post(
            f"{self.api_url}/activity/set/alphaCriteria",
            params={"versionId": activity.versionId},
            headers={"Authorization": f"Bearer {self._auth}"},
            json={
                "id": str(activity.id),
                "inOrOut": 0,
                "criteria": [
                    {"stateId": str(item.relatedElement.id), "contributesTo": item.contributesTo, "orBeyond": False}
                    for item in activity.inAlphaCriteria
                ],
                "VersionId": str(activity.versionId),
            },
        )

        sleep(0)
        states_out_response = httpx.post(
            f"{self.api_url}/activity/set/alphaCriteria",
            params={"versionId": activity.versionId},
            headers={
                "Authorization": f"Bearer {self._auth}",
                "Access-Control-Allow-Origin", "https://essence-backend.freydin.space",
            },
            json={
                "id": str(activity.id),
                "inOrOut": 1,
                "criteria": [
                    {"stateId": str(item.relatedElement.id), "contributesTo": item.contributesTo, "orBeyond": False}
                    for item in activity.outAlphaCriteria
                ],
                "VersionId": str(activity.versionId),
            },
        )

        return activity

    def create_pattern(self, pattern: PatternDto) -> PatternDto:
        pass
