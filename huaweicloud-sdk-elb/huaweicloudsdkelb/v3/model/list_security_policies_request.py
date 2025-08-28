# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'protocols': 'list[str]',
        'ciphers': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'protocols': 'protocols',
        'ciphers': 'ciphers'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, protocols=None, ciphers=None):
        r"""ListSecurityPoliciesRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：自定义安全策略的ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：自定义安全策略的名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param description: **参数解释**：自定义安全策略的描述信息。 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param protocols: **参数解释**：空格分隔的自定义安全策略的TLS协议。 支持多值查询，查询条件格式：*protocols&#x3D;xxx&amp;protocols&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type protocols: list[str]
        :param ciphers: **参数解释**：冒号分隔的自定义安全策略的加密套件。 支持多值查询，查询条件格式：*ciphers&#x3D;xxx&amp;ciphers&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ciphers: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._protocols = None
        self._ciphers = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if protocols is not None:
            self.protocols = protocols
        if ciphers is not None:
            self.ciphers = ciphers

    @property
    def marker(self):
        r"""Gets the marker of this ListSecurityPoliciesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListSecurityPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSecurityPoliciesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListSecurityPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityPoliciesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListSecurityPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityPoliciesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListSecurityPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListSecurityPoliciesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListSecurityPoliciesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListSecurityPoliciesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListSecurityPoliciesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListSecurityPoliciesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListSecurityPoliciesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListSecurityPoliciesRequest.

        **参数解释**：自定义安全策略的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListSecurityPoliciesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def protocols(self):
        r"""Gets the protocols of this ListSecurityPoliciesRequest.

        **参数解释**：空格分隔的自定义安全策略的TLS协议。 支持多值查询，查询条件格式：*protocols=xxx&protocols=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The protocols of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        r"""Sets the protocols of this ListSecurityPoliciesRequest.

        **参数解释**：空格分隔的自定义安全策略的TLS协议。 支持多值查询，查询条件格式：*protocols=xxx&protocols=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param protocols: The protocols of this ListSecurityPoliciesRequest.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        r"""Gets the ciphers of this ListSecurityPoliciesRequest.

        **参数解释**：冒号分隔的自定义安全策略的加密套件。 支持多值查询，查询条件格式：*ciphers=xxx&ciphers=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ciphers of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        r"""Sets the ciphers of this ListSecurityPoliciesRequest.

        **参数解释**：冒号分隔的自定义安全策略的加密套件。 支持多值查询，查询条件格式：*ciphers=xxx&ciphers=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ciphers: The ciphers of this ListSecurityPoliciesRequest.
        :type ciphers: list[str]
        """
        self._ciphers = ciphers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSecurityPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
