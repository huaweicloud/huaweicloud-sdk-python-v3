# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulnRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, x_language=None, enterprise_project_id=None, offset=None, limit=None, _from=None, to=None):
        r"""ListVulnRulesRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释：** 语言类型 **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** zh-cn
        :type x_language: str
        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0
        :type enterprise_project_id: str
        :param offset: **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回 **约束限制：** 不涉及 **取值范围：** [0,2147483645] **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** [1, 1000] **默认取值：** 10
        :type limit: int
        :param _from: **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        """
        
        

        self._x_language = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def x_language(self):
        r"""Gets the x_language of this ListVulnRulesRequest.

        **参数解释：** 语言类型 **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** zh-cn

        :return: The x_language of this ListVulnRulesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListVulnRulesRequest.

        **参数解释：** 语言类型 **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** zh-cn

        :param x_language: The x_language of this ListVulnRulesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulnRulesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :return: The enterprise_project_id of this ListVulnRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulnRulesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListVulnRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVulnRulesRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回 **约束限制：** 不涉及 **取值范围：** [0,2147483645] **默认取值：** 0

        :return: The offset of this ListVulnRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulnRulesRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回 **约束限制：** 不涉及 **取值范围：** [0,2147483645] **默认取值：** 0

        :param offset: The offset of this ListVulnRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVulnRulesRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** [1, 1000] **默认取值：** 10

        :return: The limit of this ListVulnRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulnRulesRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** [1, 1000] **默认取值：** 10

        :param limit: The limit of this ListVulnRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def _from(self):
        r"""Gets the _from of this ListVulnRulesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListVulnRulesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListVulnRulesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListVulnRulesRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListVulnRulesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListVulnRulesRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListVulnRulesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListVulnRulesRequest.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ListVulnRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
