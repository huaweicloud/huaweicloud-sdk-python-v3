# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplicaBinlogReadConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported': 'bool',
        'enabled': 'bool'
    }

    attribute_map = {
        'supported': 'supported',
        'enabled': 'enabled'
    }

    def __init__(self, supported=None, enabled=None):
        r"""ShowReplicaBinlogReadConfigResponse

        The model defined in huaweicloud sdk

        :param supported: **参数解释**：  实例是否支持开启只读Binlog拉取。  **取值范围**：  - true：支持。 - false：不支持。
        :type supported: bool
        :param enabled: **参数解释**：  只读Binlog拉取开关状态。  **取值范围**：  - true：开启。 - false：关闭。
        :type enabled: bool
        """
        
        super().__init__()

        self._supported = None
        self._enabled = None
        self.discriminator = None

        if supported is not None:
            self.supported = supported
        if enabled is not None:
            self.enabled = enabled

    @property
    def supported(self):
        r"""Gets the supported of this ShowReplicaBinlogReadConfigResponse.

        **参数解释**：  实例是否支持开启只读Binlog拉取。  **取值范围**：  - true：支持。 - false：不支持。

        :return: The supported of this ShowReplicaBinlogReadConfigResponse.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        r"""Sets the supported of this ShowReplicaBinlogReadConfigResponse.

        **参数解释**：  实例是否支持开启只读Binlog拉取。  **取值范围**：  - true：支持。 - false：不支持。

        :param supported: The supported of this ShowReplicaBinlogReadConfigResponse.
        :type supported: bool
        """
        self._supported = supported

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowReplicaBinlogReadConfigResponse.

        **参数解释**：  只读Binlog拉取开关状态。  **取值范围**：  - true：开启。 - false：关闭。

        :return: The enabled of this ShowReplicaBinlogReadConfigResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowReplicaBinlogReadConfigResponse.

        **参数解释**：  只读Binlog拉取开关状态。  **取值范围**：  - true：开启。 - false：关闭。

        :param enabled: The enabled of this ShowReplicaBinlogReadConfigResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    def to_dict(self):
        import warnings
        warnings.warn("ShowReplicaBinlogReadConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReplicaBinlogReadConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
