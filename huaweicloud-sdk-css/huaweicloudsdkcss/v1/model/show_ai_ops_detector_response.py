# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiOpsDetectorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_detection': 'list[AiOpsDetector]',
        'unavailability_detection': 'list[AiOpsDetector]'
    }

    attribute_map = {
        'full_detection': 'full_detection',
        'unavailability_detection': 'unavailability_detection'
    }

    def __init__(self, full_detection=None, unavailability_detection=None):
        r"""ShowAiOpsDetectorResponse

        The model defined in huaweicloud sdk

        :param full_detection: **参数解释**： 全量检测项，返回所有可用检测项ID、名称，以及检测描述。 **取值范围**： 不涉及
        :type full_detection: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        :param unavailability_detection: **参数解释**： 集群不可用检测项，返回所有集群不可用分类的检测项ID、名称，以及检测描述。 **取值范围**： 不涉及
        :type unavailability_detection: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        """
        
        super().__init__()

        self._full_detection = None
        self._unavailability_detection = None
        self.discriminator = None

        if full_detection is not None:
            self.full_detection = full_detection
        if unavailability_detection is not None:
            self.unavailability_detection = unavailability_detection

    @property
    def full_detection(self):
        r"""Gets the full_detection of this ShowAiOpsDetectorResponse.

        **参数解释**： 全量检测项，返回所有可用检测项ID、名称，以及检测描述。 **取值范围**： 不涉及

        :return: The full_detection of this ShowAiOpsDetectorResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        r"""Sets the full_detection of this ShowAiOpsDetectorResponse.

        **参数解释**： 全量检测项，返回所有可用检测项ID、名称，以及检测描述。 **取值范围**： 不涉及

        :param full_detection: The full_detection of this ShowAiOpsDetectorResponse.
        :type full_detection: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        """
        self._full_detection = full_detection

    @property
    def unavailability_detection(self):
        r"""Gets the unavailability_detection of this ShowAiOpsDetectorResponse.

        **参数解释**： 集群不可用检测项，返回所有集群不可用分类的检测项ID、名称，以及检测描述。 **取值范围**： 不涉及

        :return: The unavailability_detection of this ShowAiOpsDetectorResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        """
        return self._unavailability_detection

    @unavailability_detection.setter
    def unavailability_detection(self, unavailability_detection):
        r"""Sets the unavailability_detection of this ShowAiOpsDetectorResponse.

        **参数解释**： 集群不可用检测项，返回所有集群不可用分类的检测项ID、名称，以及检测描述。 **取值范围**： 不涉及

        :param unavailability_detection: The unavailability_detection of this ShowAiOpsDetectorResponse.
        :type unavailability_detection: list[:class:`huaweicloudsdkcss.v1.AiOpsDetector`]
        """
        self._unavailability_detection = unavailability_detection

    def to_dict(self):
        import warnings
        warnings.warn("ShowAiOpsDetectorResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowAiOpsDetectorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
