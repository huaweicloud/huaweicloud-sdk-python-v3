# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLeaguesRequest:

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
        'offset': 'int',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, type=None):
        r"""ListLeaguesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页记录数，取值0-100
        :type limit: int
        :param offset: 记录数偏移量 
        :type offset: int
        :param type: 查询的联盟类型，owned:创建者，participativenormal:参与者
        :type type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._type = None
        self.discriminator = None

        self.limit = limit
        self.offset = offset
        self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListLeaguesRequest.

        每页记录数，取值0-100

        :return: The limit of this ListLeaguesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLeaguesRequest.

        每页记录数，取值0-100

        :param limit: The limit of this ListLeaguesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListLeaguesRequest.

        记录数偏移量 

        :return: The offset of this ListLeaguesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLeaguesRequest.

        记录数偏移量 

        :param offset: The offset of this ListLeaguesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def type(self):
        r"""Gets the type of this ListLeaguesRequest.

        查询的联盟类型，owned:创建者，participativenormal:参与者

        :return: The type of this ListLeaguesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListLeaguesRequest.

        查询的联盟类型，owned:创建者，participativenormal:参与者

        :param type: The type of this ListLeaguesRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListLeaguesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
