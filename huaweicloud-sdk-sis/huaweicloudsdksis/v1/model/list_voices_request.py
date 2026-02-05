# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVoicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, limit=None, offset=None):
        r"""ListVoicesRequest

        The model defined in huaweicloud sdk

        :param limit: 查询已注册的声音列表，每页查询显示的条目数量，默认：10
        :type limit: int
        :param offset: 查询已注册的声音列表，页码偏移量，表示从此页码偏移量开始查询，offset大于等于0， 默认：0
        :type offset: str
        """
        
        

        self._limit = None
        self._offset = None
        self.discriminator = None

        self.limit = limit
        self.offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVoicesRequest.

        查询已注册的声音列表，每页查询显示的条目数量，默认：10

        :return: The limit of this ListVoicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVoicesRequest.

        查询已注册的声音列表，每页查询显示的条目数量，默认：10

        :param limit: The limit of this ListVoicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVoicesRequest.

        查询已注册的声音列表，页码偏移量，表示从此页码偏移量开始查询，offset大于等于0， 默认：0

        :return: The offset of this ListVoicesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVoicesRequest.

        查询已注册的声音列表，页码偏移量，表示从此页码偏移量开始查询，offset大于等于0， 默认：0

        :param offset: The offset of this ListVoicesRequest.
        :type offset: str
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
        if not isinstance(other, ListVoicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
