# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAdOusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain=None, limit=None, offset=None):
        r"""ListAdOusRequest

        The model defined in huaweicloud sdk

        :param domain: 域，默认查询主域。
        :type domain: str
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._domain = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain(self):
        r"""Gets the domain of this ListAdOusRequest.

        域，默认查询主域。

        :return: The domain of this ListAdOusRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListAdOusRequest.

        域，默认查询主域。

        :param domain: The domain of this ListAdOusRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def limit(self):
        r"""Gets the limit of this ListAdOusRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。

        :return: The limit of this ListAdOusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAdOusRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。

        :param limit: The limit of this ListAdOusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAdOusRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListAdOusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAdOusRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListAdOusRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAdOusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
