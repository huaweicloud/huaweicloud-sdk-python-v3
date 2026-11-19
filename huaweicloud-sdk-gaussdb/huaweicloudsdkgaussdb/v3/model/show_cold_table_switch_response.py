# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowColdTableSwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_status': 'str',
        'kernel_version': 'str'
    }

    attribute_map = {
        'switch_status': 'switch_status',
        'kernel_version': 'kernel_version'
    }

    def __init__(self, switch_status=None, kernel_version=None):
        r"""ShowColdTableSwitchResponse

        The model defined in huaweicloud sdk

        :param switch_status: **参数解释**：  冷热分离开关状态。  **取值范围**： - off：关闭。 - on：开启。
        :type switch_status: str
        :param kernel_version: **参数解释**：  支持冷热分离的最低内核版本。  **取值范围**：  不涉及。
        :type kernel_version: str
        """
        
        super().__init__()

        self._switch_status = None
        self._kernel_version = None
        self.discriminator = None

        if switch_status is not None:
            self.switch_status = switch_status
        if kernel_version is not None:
            self.kernel_version = kernel_version

    @property
    def switch_status(self):
        r"""Gets the switch_status of this ShowColdTableSwitchResponse.

        **参数解释**：  冷热分离开关状态。  **取值范围**： - off：关闭。 - on：开启。

        :return: The switch_status of this ShowColdTableSwitchResponse.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        r"""Sets the switch_status of this ShowColdTableSwitchResponse.

        **参数解释**：  冷热分离开关状态。  **取值范围**： - off：关闭。 - on：开启。

        :param switch_status: The switch_status of this ShowColdTableSwitchResponse.
        :type switch_status: str
        """
        self._switch_status = switch_status

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this ShowColdTableSwitchResponse.

        **参数解释**：  支持冷热分离的最低内核版本。  **取值范围**：  不涉及。

        :return: The kernel_version of this ShowColdTableSwitchResponse.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this ShowColdTableSwitchResponse.

        **参数解释**：  支持冷热分离的最低内核版本。  **取值范围**：  不涉及。

        :param kernel_version: The kernel_version of this ShowColdTableSwitchResponse.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    def to_dict(self):
        import warnings
        warnings.warn("ShowColdTableSwitchResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowColdTableSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
