# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PointCleanDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'silent_window': 'int',
        'deviation': 'float'
    }

    attribute_map = {
        'silent_window': 'silent_window',
        'deviation': 'deviation'
    }

    def __init__(self, silent_window=None, deviation=None):
        r"""PointCleanDTO

        The model defined in huaweicloud sdk

        :param silent_window: 静默时间窗口，在该时间窗口内，没有触发上报条件，点位将不会上
        :type silent_window: int
        :param deviation: 偏差，在该偏差范围内表示是正常波动，点位将不进行上报
        :type deviation: float
        """
        
        

        self._silent_window = None
        self._deviation = None
        self.discriminator = None

        self.silent_window = silent_window
        self.deviation = deviation

    @property
    def silent_window(self):
        r"""Gets the silent_window of this PointCleanDTO.

        静默时间窗口，在该时间窗口内，没有触发上报条件，点位将不会上

        :return: The silent_window of this PointCleanDTO.
        :rtype: int
        """
        return self._silent_window

    @silent_window.setter
    def silent_window(self, silent_window):
        r"""Sets the silent_window of this PointCleanDTO.

        静默时间窗口，在该时间窗口内，没有触发上报条件，点位将不会上

        :param silent_window: The silent_window of this PointCleanDTO.
        :type silent_window: int
        """
        self._silent_window = silent_window

    @property
    def deviation(self):
        r"""Gets the deviation of this PointCleanDTO.

        偏差，在该偏差范围内表示是正常波动，点位将不进行上报

        :return: The deviation of this PointCleanDTO.
        :rtype: float
        """
        return self._deviation

    @deviation.setter
    def deviation(self, deviation):
        r"""Sets the deviation of this PointCleanDTO.

        偏差，在该偏差范围内表示是正常波动，点位将不进行上报

        :param deviation: The deviation of this PointCleanDTO.
        :type deviation: float
        """
        self._deviation = deviation

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
        if not isinstance(other, PointCleanDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
