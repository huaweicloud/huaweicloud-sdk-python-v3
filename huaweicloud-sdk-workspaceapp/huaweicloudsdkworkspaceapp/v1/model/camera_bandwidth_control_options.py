# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CameraBandwidthControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'camera_bandwidth_control_value': 'int'
    }

    attribute_map = {
        'camera_bandwidth_control_value': 'camera_bandwidth_control_value'
    }

    def __init__(self, camera_bandwidth_control_value=None):
        """CameraBandwidthControlOptions

        The model defined in huaweicloud sdk

        :param camera_bandwidth_control_value: 摄像头带宽控制量（Kbps）。取值范围为[0-10000]。默认：10000。
        :type camera_bandwidth_control_value: int
        """
        
        

        self._camera_bandwidth_control_value = None
        self.discriminator = None

        if camera_bandwidth_control_value is not None:
            self.camera_bandwidth_control_value = camera_bandwidth_control_value

    @property
    def camera_bandwidth_control_value(self):
        """Gets the camera_bandwidth_control_value of this CameraBandwidthControlOptions.

        摄像头带宽控制量（Kbps）。取值范围为[0-10000]。默认：10000。

        :return: The camera_bandwidth_control_value of this CameraBandwidthControlOptions.
        :rtype: int
        """
        return self._camera_bandwidth_control_value

    @camera_bandwidth_control_value.setter
    def camera_bandwidth_control_value(self, camera_bandwidth_control_value):
        """Sets the camera_bandwidth_control_value of this CameraBandwidthControlOptions.

        摄像头带宽控制量（Kbps）。取值范围为[0-10000]。默认：10000。

        :param camera_bandwidth_control_value: The camera_bandwidth_control_value of this CameraBandwidthControlOptions.
        :type camera_bandwidth_control_value: int
        """
        self._camera_bandwidth_control_value = camera_bandwidth_control_value

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
        if not isinstance(other, CameraBandwidthControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
