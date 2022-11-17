# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQosThresholdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'threshold_type': 'str'
    }

    attribute_map = {
        'threshold_type': 'thresholdType'
    }

    def __init__(self, threshold_type=None):
        """ShowQosThresholdRequest

        The model defined in huaweicloud sdk

        :param threshold_type: 阈值类型。 * AUDIO：音频告警阈值 * VIDEO：视频告警阈值 * SCREEN：屏幕共享告警阈值 * CPU：CPU告警阈值
        :type threshold_type: str
        """
        
        

        self._threshold_type = None
        self.discriminator = None

        self.threshold_type = threshold_type

    @property
    def threshold_type(self):
        """Gets the threshold_type of this ShowQosThresholdRequest.

        阈值类型。 * AUDIO：音频告警阈值 * VIDEO：视频告警阈值 * SCREEN：屏幕共享告警阈值 * CPU：CPU告警阈值

        :return: The threshold_type of this ShowQosThresholdRequest.
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this ShowQosThresholdRequest.

        阈值类型。 * AUDIO：音频告警阈值 * VIDEO：视频告警阈值 * SCREEN：屏幕共享告警阈值 * CPU：CPU告警阈值

        :param threshold_type: The threshold_type of this ShowQosThresholdRequest.
        :type threshold_type: str
        """
        self._threshold_type = threshold_type

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
        if not isinstance(other, ShowQosThresholdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
