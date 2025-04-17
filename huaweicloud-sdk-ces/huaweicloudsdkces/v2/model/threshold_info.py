# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThresholdInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'threshold': 'float',
        'threshold_color': 'str'
    }

    attribute_map = {
        'threshold': 'threshold',
        'threshold_color': 'threshold_color'
    }

    def __init__(self, threshold=None, threshold_color=None):
        r"""ThresholdInfo

        The model defined in huaweicloud sdk

        :param threshold: 监控视图辅助线的阈值
        :type threshold: float
        :param threshold_color: 监控视图辅助线的颜色,\&quot;#B50E65\&quot;紫色,\&quot;#F23030\&quot;红色,\&quot;#FF8800\&quot;橙色,\&quot;#F2E70C\&quot;黄色
        :type threshold_color: str
        """
        
        

        self._threshold = None
        self._threshold_color = None
        self.discriminator = None

        self.threshold = threshold
        self.threshold_color = threshold_color

    @property
    def threshold(self):
        r"""Gets the threshold of this ThresholdInfo.

        监控视图辅助线的阈值

        :return: The threshold of this ThresholdInfo.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ThresholdInfo.

        监控视图辅助线的阈值

        :param threshold: The threshold of this ThresholdInfo.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def threshold_color(self):
        r"""Gets the threshold_color of this ThresholdInfo.

        监控视图辅助线的颜色,\"#B50E65\"紫色,\"#F23030\"红色,\"#FF8800\"橙色,\"#F2E70C\"黄色

        :return: The threshold_color of this ThresholdInfo.
        :rtype: str
        """
        return self._threshold_color

    @threshold_color.setter
    def threshold_color(self, threshold_color):
        r"""Sets the threshold_color of this ThresholdInfo.

        监控视图辅助线的颜色,\"#B50E65\"紫色,\"#F23030\"红色,\"#FF8800\"橙色,\"#F2E70C\"黄色

        :param threshold_color: The threshold_color of this ThresholdInfo.
        :type threshold_color: str
        """
        self._threshold_color = threshold_color

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
        if not isinstance(other, ThresholdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
