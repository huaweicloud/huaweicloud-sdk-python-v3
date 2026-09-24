# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRdsDBFaultPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'errmsg': 'str'
    }

    attribute_map = {
        'state': 'state',
        'errmsg': 'errmsg'
    }

    def __init__(self, state=None, errmsg=None):
        r"""SetRdsDBFaultPolicyResponse

        The model defined in huaweicloud sdk

        :param state: **参数解释**：  请求状态。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type state: str
        :param errmsg: **参数解释**：  错误信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type errmsg: str
        """
        
        super().__init__()

        self._state = None
        self._errmsg = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if errmsg is not None:
            self.errmsg = errmsg

    @property
    def state(self):
        r"""Gets the state of this SetRdsDBFaultPolicyResponse.

        **参数解释**：  请求状态。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The state of this SetRdsDBFaultPolicyResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SetRdsDBFaultPolicyResponse.

        **参数解释**：  请求状态。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param state: The state of this SetRdsDBFaultPolicyResponse.
        :type state: str
        """
        self._state = state

    @property
    def errmsg(self):
        r"""Gets the errmsg of this SetRdsDBFaultPolicyResponse.

        **参数解释**：  错误信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The errmsg of this SetRdsDBFaultPolicyResponse.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        r"""Sets the errmsg of this SetRdsDBFaultPolicyResponse.

        **参数解释**：  错误信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param errmsg: The errmsg of this SetRdsDBFaultPolicyResponse.
        :type errmsg: str
        """
        self._errmsg = errmsg

    def to_dict(self):
        import warnings
        warnings.warn("SetRdsDBFaultPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SetRdsDBFaultPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
