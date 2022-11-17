# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TpsBrokens:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average': 'list[float]',
        'tps': 'list[float]'
    }

    attribute_map = {
        'average': 'average',
        'tps': 'tps'
    }

    def __init__(self, average=None, tps=None):
        """TpsBrokens

        The model defined in huaweicloud sdk

        :param average: 平均响应时间
        :type average: list[float]
        :param tps: tps
        :type tps: list[float]
        """
        
        

        self._average = None
        self._tps = None
        self.discriminator = None

        if average is not None:
            self.average = average
        if tps is not None:
            self.tps = tps

    @property
    def average(self):
        """Gets the average of this TpsBrokens.

        平均响应时间

        :return: The average of this TpsBrokens.
        :rtype: list[float]
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this TpsBrokens.

        平均响应时间

        :param average: The average of this TpsBrokens.
        :type average: list[float]
        """
        self._average = average

    @property
    def tps(self):
        """Gets the tps of this TpsBrokens.

        tps

        :return: The tps of this TpsBrokens.
        :rtype: list[float]
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this TpsBrokens.

        tps

        :param tps: The tps of this TpsBrokens.
        :type tps: list[float]
        """
        self._tps = tps

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
        if not isinstance(other, TpsBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
