# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPerformanceResourceStatRequest:

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
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, limit=None, offset=None):
        """ListPerformanceResourceStatRequest

        The model defined in huaweicloud sdk

        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        """
        
        

        self._limit = None
        self._offset = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPerformanceResourceStatRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListPerformanceResourceStatRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPerformanceResourceStatRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListPerformanceResourceStatRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPerformanceResourceStatRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListPerformanceResourceStatRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPerformanceResourceStatRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListPerformanceResourceStatRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPerformanceResourceStatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
