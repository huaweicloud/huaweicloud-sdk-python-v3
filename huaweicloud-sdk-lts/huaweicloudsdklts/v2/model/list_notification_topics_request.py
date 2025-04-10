# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationTopicsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, offset=None, limit=None):
        r"""ListNotificationTopicsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询游标，初始传入0，后续从上一次的返回值中获取
        :type offset: int
        :param limit: 每页数据量，最大值为100
        :type limit: int
        """
        
        

        self._offset = None
        self._limit = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNotificationTopicsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :return: The offset of this ListNotificationTopicsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNotificationTopicsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :param offset: The offset of this ListNotificationTopicsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNotificationTopicsRequest.

        每页数据量，最大值为100

        :return: The limit of this ListNotificationTopicsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNotificationTopicsRequest.

        每页数据量，最大值为100

        :param limit: The limit of this ListNotificationTopicsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNotificationTopicsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
