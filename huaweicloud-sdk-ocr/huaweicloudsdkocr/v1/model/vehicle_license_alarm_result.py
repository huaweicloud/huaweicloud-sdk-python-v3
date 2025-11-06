# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleLicenseAlarmResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detect_blocking_within_border_result': 'bool',
        'detect_border_integrity_result': 'bool'
    }

    attribute_map = {
        'detect_blocking_within_border_result': 'detect_blocking_within_border_result',
        'detect_border_integrity_result': 'detect_border_integrity_result'
    }

    def __init__(self, detect_blocking_within_border_result=None, detect_border_integrity_result=None):
        r"""VehicleLicenseAlarmResult

        The model defined in huaweicloud sdk

        :param detect_blocking_within_border_result: -| 证件图像框内遮挡告警结果。 true：表示证件图片内部有被遮挡。 false：表示证件图片内部未被遮挡。
        :type detect_blocking_within_border_result: bool
        :param detect_border_integrity_result: -| 证件图像边框完整性告警结果。 true：表示边框不完整。 false：表示边框完整。
        :type detect_border_integrity_result: bool
        """
        
        

        self._detect_blocking_within_border_result = None
        self._detect_border_integrity_result = None
        self.discriminator = None

        if detect_blocking_within_border_result is not None:
            self.detect_blocking_within_border_result = detect_blocking_within_border_result
        if detect_border_integrity_result is not None:
            self.detect_border_integrity_result = detect_border_integrity_result

    @property
    def detect_blocking_within_border_result(self):
        r"""Gets the detect_blocking_within_border_result of this VehicleLicenseAlarmResult.

        -| 证件图像框内遮挡告警结果。 true：表示证件图片内部有被遮挡。 false：表示证件图片内部未被遮挡。

        :return: The detect_blocking_within_border_result of this VehicleLicenseAlarmResult.
        :rtype: bool
        """
        return self._detect_blocking_within_border_result

    @detect_blocking_within_border_result.setter
    def detect_blocking_within_border_result(self, detect_blocking_within_border_result):
        r"""Sets the detect_blocking_within_border_result of this VehicleLicenseAlarmResult.

        -| 证件图像框内遮挡告警结果。 true：表示证件图片内部有被遮挡。 false：表示证件图片内部未被遮挡。

        :param detect_blocking_within_border_result: The detect_blocking_within_border_result of this VehicleLicenseAlarmResult.
        :type detect_blocking_within_border_result: bool
        """
        self._detect_blocking_within_border_result = detect_blocking_within_border_result

    @property
    def detect_border_integrity_result(self):
        r"""Gets the detect_border_integrity_result of this VehicleLicenseAlarmResult.

        -| 证件图像边框完整性告警结果。 true：表示边框不完整。 false：表示边框完整。

        :return: The detect_border_integrity_result of this VehicleLicenseAlarmResult.
        :rtype: bool
        """
        return self._detect_border_integrity_result

    @detect_border_integrity_result.setter
    def detect_border_integrity_result(self, detect_border_integrity_result):
        r"""Sets the detect_border_integrity_result of this VehicleLicenseAlarmResult.

        -| 证件图像边框完整性告警结果。 true：表示边框不完整。 false：表示边框完整。

        :param detect_border_integrity_result: The detect_border_integrity_result of this VehicleLicenseAlarmResult.
        :type detect_border_integrity_result: bool
        """
        self._detect_border_integrity_result = detect_border_integrity_result

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VehicleLicenseAlarmResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
