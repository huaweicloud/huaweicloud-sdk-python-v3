# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllocationPool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end': 'str',
        'start': 'str'
    }

    attribute_map = {
        'end': 'end',
        'start': 'start'
    }

    def __init__(self, end=None, start=None):
        r"""AllocationPool

        The model defined in huaweicloud sdk

        :param end: 网络池结束IP
        :type end: str
        :param start: 网络池起始IP
        :type start: str
        """
        
        

        self._end = None
        self._start = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if start is not None:
            self.start = start

    @property
    def end(self):
        r"""Gets the end of this AllocationPool.

        网络池结束IP

        :return: The end of this AllocationPool.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this AllocationPool.

        网络池结束IP

        :param end: The end of this AllocationPool.
        :type end: str
        """
        self._end = end

    @property
    def start(self):
        r"""Gets the start of this AllocationPool.

        网络池起始IP

        :return: The start of this AllocationPool.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this AllocationPool.

        网络池起始IP

        :param start: The start of this AllocationPool.
        :type start: str
        """
        self._start = start

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
        if not isinstance(other, AllocationPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
