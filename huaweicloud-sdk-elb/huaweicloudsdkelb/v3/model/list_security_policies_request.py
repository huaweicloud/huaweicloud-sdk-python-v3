# coding: utf-8

import re
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
        """ListSecurityPoliciesRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param id: 自定义安全策略的ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param name: 自定义安全策略的名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param description: 自定义安全策略的描述信息。  支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。
        :type description: list[str]
        :param protocols: 空格分隔的自定义安全策略的TLS协议。  支持多值查询，查询条件格式：*protocols&#x3D;xxx&amp;protocols&#x3D;xxx*。
        :type protocols: list[str]
        :param ciphers: 冒号分隔的自定义安全策略的加密套件。  支持多值查询，查询条件格式：*ciphers&#x3D;xxx&amp;ciphers&#x3D;xxx*。
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
        """Gets the marker of this ListSecurityPoliciesRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListSecurityPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecurityPoliciesRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListSecurityPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListSecurityPoliciesRequest.

        每页返回的个数。

        :return: The limit of this ListSecurityPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityPoliciesRequest.

        每页返回的个数。

        :param limit: The limit of this ListSecurityPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListSecurityPoliciesRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListSecurityPoliciesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListSecurityPoliciesRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListSecurityPoliciesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListSecurityPoliciesRequest.

        自定义安全策略的ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSecurityPoliciesRequest.

        自定义安全策略的ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListSecurityPoliciesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListSecurityPoliciesRequest.

        自定义安全策略的名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSecurityPoliciesRequest.

        自定义安全策略的名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListSecurityPoliciesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListSecurityPoliciesRequest.

        自定义安全策略的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :return: The description of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListSecurityPoliciesRequest.

        自定义安全策略的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :param description: The description of this ListSecurityPoliciesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def protocols(self):
        """Gets the protocols of this ListSecurityPoliciesRequest.

        空格分隔的自定义安全策略的TLS协议。  支持多值查询，查询条件格式：*protocols=xxx&protocols=xxx*。

        :return: The protocols of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this ListSecurityPoliciesRequest.

        空格分隔的自定义安全策略的TLS协议。  支持多值查询，查询条件格式：*protocols=xxx&protocols=xxx*。

        :param protocols: The protocols of this ListSecurityPoliciesRequest.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this ListSecurityPoliciesRequest.

        冒号分隔的自定义安全策略的加密套件。  支持多值查询，查询条件格式：*ciphers=xxx&ciphers=xxx*。

        :return: The ciphers of this ListSecurityPoliciesRequest.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this ListSecurityPoliciesRequest.

        冒号分隔的自定义安全策略的加密套件。  支持多值查询，查询条件格式：*ciphers=xxx&ciphers=xxx*。

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
