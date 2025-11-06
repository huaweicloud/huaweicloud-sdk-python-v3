# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleLicenseAlarmConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blocking_within_border_score': 'int',
        'border_integrity_score': 'int'
    }

    attribute_map = {
        'blocking_within_border_score': 'blocking_within_border_score',
        'border_integrity_score': 'border_integrity_score'
    }

    def __init__(self, blocking_within_border_score=None, border_integrity_score=None):
        r"""VehicleLicenseAlarmConfidence

        The model defined in huaweicloud sdk

        :param blocking_within_border_score: 证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。
        :type blocking_within_border_score: int
        :param border_integrity_score: 证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。
        :type border_integrity_score: int
        """
        
        

        self._blocking_within_border_score = None
        self._border_integrity_score = None
        self.discriminator = None

        if blocking_within_border_score is not None:
            self.blocking_within_border_score = blocking_within_border_score
        if border_integrity_score is not None:
            self.border_integrity_score = border_integrity_score

    @property
    def blocking_within_border_score(self):
        r"""Gets the blocking_within_border_score of this VehicleLicenseAlarmConfidence.

        证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。

        :return: The blocking_within_border_score of this VehicleLicenseAlarmConfidence.
        :rtype: int
        """
        return self._blocking_within_border_score

    @blocking_within_border_score.setter
    def blocking_within_border_score(self, blocking_within_border_score):
        r"""Sets the blocking_within_border_score of this VehicleLicenseAlarmConfidence.

        证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。

        :param blocking_within_border_score: The blocking_within_border_score of this VehicleLicenseAlarmConfidence.
        :type blocking_within_border_score: int
        """
        self._blocking_within_border_score = blocking_within_border_score

    @property
    def border_integrity_score(self):
        r"""Gets the border_integrity_score of this VehicleLicenseAlarmConfidence.

        证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。

        :return: The border_integrity_score of this VehicleLicenseAlarmConfidence.
        :rtype: int
        """
        return self._border_integrity_score

    @border_integrity_score.setter
    def border_integrity_score(self, border_integrity_score):
        r"""Sets the border_integrity_score of this VehicleLicenseAlarmConfidence.

        证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。

        :param border_integrity_score: The border_integrity_score of this VehicleLicenseAlarmConfidence.
        :type border_integrity_score: int
        """
        self._border_integrity_score = border_integrity_score

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
        if not isinstance(other, VehicleLicenseAlarmConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
