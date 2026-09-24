# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAutoScalingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'status': 'status'
    }

    def __init__(self, instance_id=None, status=None):
        r"""SetAutoScalingPolicyResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param status: **参数解释**：  是否开启自动变配。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启自动变配 - OFF：关闭自动变配  **默认取值**：  不涉及。
        :type status: str
        """
        
        super().__init__()

        self._instance_id = None
        self._status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SetAutoScalingPolicyResponse.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this SetAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SetAutoScalingPolicyResponse.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this SetAutoScalingPolicyResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this SetAutoScalingPolicyResponse.

        **参数解释**：  是否开启自动变配。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启自动变配 - OFF：关闭自动变配  **默认取值**：  不涉及。

        :return: The status of this SetAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetAutoScalingPolicyResponse.

        **参数解释**：  是否开启自动变配。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启自动变配 - OFF：关闭自动变配  **默认取值**：  不涉及。

        :param status: The status of this SetAutoScalingPolicyResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("SetAutoScalingPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SetAutoScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
