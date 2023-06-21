# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Progress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overall': 'float',
        'estimated_finish_time': 'int'
    }

    attribute_map = {
        'overall': 'overall',
        'estimated_finish_time': 'estimated_finish_time'
    }

    def __init__(self, overall=None, estimated_finish_time=None):
        """Progress

        The model defined in huaweicloud sdk

        :param overall: 整体进度
        :type overall: float
        :param estimated_finish_time: 预计结束时间，毫秒
        :type estimated_finish_time: int
        """
        
        

        self._overall = None
        self._estimated_finish_time = None
        self.discriminator = None

        if overall is not None:
            self.overall = overall
        if estimated_finish_time is not None:
            self.estimated_finish_time = estimated_finish_time

    @property
    def overall(self):
        """Gets the overall of this Progress.

        整体进度

        :return: The overall of this Progress.
        :rtype: float
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this Progress.

        整体进度

        :param overall: The overall of this Progress.
        :type overall: float
        """
        self._overall = overall

    @property
    def estimated_finish_time(self):
        """Gets the estimated_finish_time of this Progress.

        预计结束时间，毫秒

        :return: The estimated_finish_time of this Progress.
        :rtype: int
        """
        return self._estimated_finish_time

    @estimated_finish_time.setter
    def estimated_finish_time(self, estimated_finish_time):
        """Sets the estimated_finish_time of this Progress.

        预计结束时间，毫秒

        :param estimated_finish_time: The estimated_finish_time of this Progress.
        :type estimated_finish_time: int
        """
        self._estimated_finish_time = estimated_finish_time

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
        if not isinstance(other, Progress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
