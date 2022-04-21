# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'count': 'count',
        'marker': 'marker'
    }

    def __init__(self, count=None, marker=None):
        """MetaData

        The model defined in huaweicloud sdk

        :param count: 标识本次查询事件列表返回的事件记录的总条数。
        :type count: int
        :param marker: 标识本次查询事件列表返回的最后一个事件ID。可以使用这个参数返回值作为分页请求参数next的值，如果marker返回为null，则表示当前请求条件下查询事件列表已经全部返回没有下一页。
        :type marker: str
        """
        
        

        self._count = None
        self._marker = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if marker is not None:
            self.marker = marker

    @property
    def count(self):
        """Gets the count of this MetaData.

        标识本次查询事件列表返回的事件记录的总条数。

        :return: The count of this MetaData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MetaData.

        标识本次查询事件列表返回的事件记录的总条数。

        :param count: The count of this MetaData.
        :type count: int
        """
        self._count = count

    @property
    def marker(self):
        """Gets the marker of this MetaData.

        标识本次查询事件列表返回的最后一个事件ID。可以使用这个参数返回值作为分页请求参数next的值，如果marker返回为null，则表示当前请求条件下查询事件列表已经全部返回没有下一页。

        :return: The marker of this MetaData.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this MetaData.

        标识本次查询事件列表返回的最后一个事件ID。可以使用这个参数返回值作为分页请求参数next的值，如果marker返回为null，则表示当前请求条件下查询事件列表已经全部返回没有下一页。

        :param marker: The marker of this MetaData.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
