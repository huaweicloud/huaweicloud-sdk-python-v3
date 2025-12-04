# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCVEAllowlistRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'namespace_id': 'int',
        'expires_at': 'int',
        'items': 'list[CVEAllowlistItem]'
    }

    attribute_map = {
        'id': 'id',
        'namespace_id': 'namespace_id',
        'expires_at': 'expires_at',
        'items': 'items'
    }

    def __init__(self, id=None, namespace_id=None, expires_at=None, items=None):
        r"""UpdateCVEAllowlistRequest

        The model defined in huaweicloud sdk

        :param id: 白名单ID，查询命名空间信息时，会返回白名单ID
        :type id: int
        :param namespace_id: 漏洞白名单列表所属的命名空间ID
        :type namespace_id: int
        :param expires_at: 漏洞白名单的有效期时间，以自 1970 年 1 月 1 日以来的秒数表示；如果没有配置，则永不过期
        :type expires_at: int
        :param items: 漏洞列表
        :type items: list[:class:`huaweicloudsdkswr.v2.CVEAllowlistItem`]
        """
        
        

        self._id = None
        self._namespace_id = None
        self._expires_at = None
        self._items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if expires_at is not None:
            self.expires_at = expires_at
        if items is not None:
            self.items = items

    @property
    def id(self):
        r"""Gets the id of this UpdateCVEAllowlistRequest.

        白名单ID，查询命名空间信息时，会返回白名单ID

        :return: The id of this UpdateCVEAllowlistRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateCVEAllowlistRequest.

        白名单ID，查询命名空间信息时，会返回白名单ID

        :param id: The id of this UpdateCVEAllowlistRequest.
        :type id: int
        """
        self._id = id

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this UpdateCVEAllowlistRequest.

        漏洞白名单列表所属的命名空间ID

        :return: The namespace_id of this UpdateCVEAllowlistRequest.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this UpdateCVEAllowlistRequest.

        漏洞白名单列表所属的命名空间ID

        :param namespace_id: The namespace_id of this UpdateCVEAllowlistRequest.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def expires_at(self):
        r"""Gets the expires_at of this UpdateCVEAllowlistRequest.

        漏洞白名单的有效期时间，以自 1970 年 1 月 1 日以来的秒数表示；如果没有配置，则永不过期

        :return: The expires_at of this UpdateCVEAllowlistRequest.
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this UpdateCVEAllowlistRequest.

        漏洞白名单的有效期时间，以自 1970 年 1 月 1 日以来的秒数表示；如果没有配置，则永不过期

        :param expires_at: The expires_at of this UpdateCVEAllowlistRequest.
        :type expires_at: int
        """
        self._expires_at = expires_at

    @property
    def items(self):
        r"""Gets the items of this UpdateCVEAllowlistRequest.

        漏洞列表

        :return: The items of this UpdateCVEAllowlistRequest.
        :rtype: list[:class:`huaweicloudsdkswr.v2.CVEAllowlistItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this UpdateCVEAllowlistRequest.

        漏洞列表

        :param items: The items of this UpdateCVEAllowlistRequest.
        :type items: list[:class:`huaweicloudsdkswr.v2.CVEAllowlistItem`]
        """
        self._items = items

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
        if not isinstance(other, UpdateCVEAllowlistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
