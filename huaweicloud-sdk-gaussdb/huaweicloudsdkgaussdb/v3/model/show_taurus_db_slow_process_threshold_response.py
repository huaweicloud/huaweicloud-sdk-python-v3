# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaurusDbSlowProcessThresholdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_process_threshold': 'int'
    }

    attribute_map = {
        'slow_process_threshold': 'slow_process_threshold'
    }

    def __init__(self, slow_process_threshold=None):
        r"""ShowTaurusDbSlowProcessThresholdResponse

        The model defined in huaweicloud sdk

        :param slow_process_threshold: **参数解释**:  慢会话阈值，单位为秒。  **取值范围**：  1-86400。 
        :type slow_process_threshold: int
        """
        
        super().__init__()

        self._slow_process_threshold = None
        self.discriminator = None

        if slow_process_threshold is not None:
            self.slow_process_threshold = slow_process_threshold

    @property
    def slow_process_threshold(self):
        r"""Gets the slow_process_threshold of this ShowTaurusDbSlowProcessThresholdResponse.

        **参数解释**:  慢会话阈值，单位为秒。  **取值范围**：  1-86400。 

        :return: The slow_process_threshold of this ShowTaurusDbSlowProcessThresholdResponse.
        :rtype: int
        """
        return self._slow_process_threshold

    @slow_process_threshold.setter
    def slow_process_threshold(self, slow_process_threshold):
        r"""Sets the slow_process_threshold of this ShowTaurusDbSlowProcessThresholdResponse.

        **参数解释**:  慢会话阈值，单位为秒。  **取值范围**：  1-86400。 

        :param slow_process_threshold: The slow_process_threshold of this ShowTaurusDbSlowProcessThresholdResponse.
        :type slow_process_threshold: int
        """
        self._slow_process_threshold = slow_process_threshold

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaurusDbSlowProcessThresholdResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTaurusDbSlowProcessThresholdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
