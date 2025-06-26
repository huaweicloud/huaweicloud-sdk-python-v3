# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'CountDetail',
        'start_time': 'str'
    }

    attribute_map = {
        'count': 'count',
        'start_time': 'start_time'
    }

    def __init__(self, count=None, start_time=None):
        r"""StatisticsDetail

        The model defined in huaweicloud sdk

        :param count: 
        :type count: :class:`huaweicloudsdksmn.v2.CountDetail`
        :param start_time: 起始时间
        :type start_time: str
        """
        
        

        self._count = None
        self._start_time = None
        self.discriminator = None

        self.count = count
        self.start_time = start_time

    @property
    def count(self):
        r"""Gets the count of this StatisticsDetail.

        :return: The count of this StatisticsDetail.
        :rtype: :class:`huaweicloudsdksmn.v2.CountDetail`
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this StatisticsDetail.

        :param count: The count of this StatisticsDetail.
        :type count: :class:`huaweicloudsdksmn.v2.CountDetail`
        """
        self._count = count

    @property
    def start_time(self):
        r"""Gets the start_time of this StatisticsDetail.

        起始时间

        :return: The start_time of this StatisticsDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StatisticsDetail.

        起始时间

        :param start_time: The start_time of this StatisticsDetail.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, StatisticsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
