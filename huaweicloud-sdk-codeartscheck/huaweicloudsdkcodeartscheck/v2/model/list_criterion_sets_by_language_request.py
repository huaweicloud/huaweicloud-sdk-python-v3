# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCriterionSetsByLanguageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'search': 'str',
        'page_size': 'int',
        'page': 'int',
        'project_id': 'str',
        'is_reliable': 'str'
    }

    attribute_map = {
        'language': 'language',
        'search': 'search',
        'page_size': 'page_size',
        'page': 'page',
        'project_id': 'project_id',
        'is_reliable': 'is_reliable'
    }

    def __init__(self, language=None, search=None, page_size=None, page=None, project_id=None, is_reliable=None):
        r"""ListCriterionSetsByLanguageRequest

        The model defined in huaweicloud sdk

        :param language: **参数解释:** 规则集语言。 **约束限制:** 不涉及。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值：** 不涉及。
        :type language: str
        :param search: **参数解释:** 搜索关键字。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        :param page_size: **参数解释:** 每页规则集数量。 **约束限制:** 不涉及。 **取值范围:** 1~1000 **默认取值:** 1000
        :type page_size: int
        :param page: **参数解释:** 规则集页数。 **约束限制:** 不涉及。 **取值范围:** 0-999 **默认取值:** 1
        :type page: int
        :param project_id: **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。
        :type project_id: str
        :param is_reliable: 是否可信
        :type is_reliable: str
        """
        
        

        self._language = None
        self._search = None
        self._page_size = None
        self._page = None
        self._project_id = None
        self._is_reliable = None
        self.discriminator = None

        self.language = language
        if search is not None:
            self.search = search
        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page
        self.project_id = project_id
        if is_reliable is not None:
            self.is_reliable = is_reliable

    @property
    def language(self):
        r"""Gets the language of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 规则集语言。 **约束限制:** 不涉及。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值：** 不涉及。

        :return: The language of this ListCriterionSetsByLanguageRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 规则集语言。 **约束限制:** 不涉及。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值：** 不涉及。

        :param language: The language of this ListCriterionSetsByLanguageRequest.
        :type language: str
        """
        self._language = language

    @property
    def search(self):
        r"""Gets the search of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 搜索关键字。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListCriterionSetsByLanguageRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 搜索关键字。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListCriterionSetsByLanguageRequest.
        :type search: str
        """
        self._search = search

    @property
    def page_size(self):
        r"""Gets the page_size of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 每页规则集数量。 **约束限制:** 不涉及。 **取值范围:** 1~1000 **默认取值:** 1000

        :return: The page_size of this ListCriterionSetsByLanguageRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 每页规则集数量。 **约束限制:** 不涉及。 **取值范围:** 1~1000 **默认取值:** 1000

        :param page_size: The page_size of this ListCriterionSetsByLanguageRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page(self):
        r"""Gets the page of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 规则集页数。 **约束限制:** 不涉及。 **取值范围:** 0-999 **默认取值:** 1

        :return: The page of this ListCriterionSetsByLanguageRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 规则集页数。 **约束限制:** 不涉及。 **取值范围:** 0-999 **默认取值:** 1

        :param page: The page of this ListCriterionSetsByLanguageRequest.
        :type page: int
        """
        self._page = page

    @property
    def project_id(self):
        r"""Gets the project_id of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :return: The project_id of this ListCriterionSetsByLanguageRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListCriterionSetsByLanguageRequest.

        **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :param project_id: The project_id of this ListCriterionSetsByLanguageRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_reliable(self):
        r"""Gets the is_reliable of this ListCriterionSetsByLanguageRequest.

        是否可信

        :return: The is_reliable of this ListCriterionSetsByLanguageRequest.
        :rtype: str
        """
        return self._is_reliable

    @is_reliable.setter
    def is_reliable(self, is_reliable):
        r"""Sets the is_reliable of this ListCriterionSetsByLanguageRequest.

        是否可信

        :param is_reliable: The is_reliable of this ListCriterionSetsByLanguageRequest.
        :type is_reliable: str
        """
        self._is_reliable = is_reliable

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCriterionSetsByLanguageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
