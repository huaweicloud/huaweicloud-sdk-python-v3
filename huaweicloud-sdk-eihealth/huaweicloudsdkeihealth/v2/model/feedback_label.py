# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeedbackLabel:
    """
    allowed enum values
    """
    OTHERS = "others"
    PROFESSIONAL = "professional"
    HELPFUL = "helpful"
    UNPROFESSIONAL = "unprofessional"
    UNHELPFUL = "unhelpful"
    UNSAFE = "unsafe"
    MISINFORMATION = "misinformation"
    DOWNLOAD_SUCCESSFUL = "download_successful"
    PROMISING = "promising"
    SYNTHESIZABLE = "synthesizable"
    VALIDATED = "validated"
    DOWNLOAD_FAILED = "download_failed"
    UNPROMISING = "unpromising"
    HARD_TO_SYNTHESIZE = "hard_to_synthesize"
    NOT_VALIDATED = "not_validated"
    PLAN_VALIDATED = "plan_validated"
    ACCURATE_RESULTS = "accurate_results"
    HIGH_PERFORMANCE = "high_performance"
    PLAN_FLAWED = "plan_flawed"
    INACCURATE_RESULTS = "inaccurate_results"
    LOW_PERFORMANCE = "low_performance"
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):
        r"""FeedbackLabel

        The model defined in huaweicloud sdk

        """
        
        
        self.discriminator = None

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
        if not isinstance(other, FeedbackLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
