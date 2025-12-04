# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'need_restart': 'bool'
    }

    attribute_map = {
        'config_name': 'config_name',
        'need_restart': 'need_restart'
    }

    def __init__(self, config_name=None, need_restart=None):
        r"""ResetConfigurationResponse

        The model defined in huaweicloud sdk

        :param config_name: **参数解释**：  参数组模板名称。  **约束限制**：  不涉及。
        :type config_name: str
        :param need_restart: **参数解释**：  是否涉及重启。（当前该字段不使用，默认为false）  **约束限制**：  不涉及。
        :type need_restart: bool
        """
        
        super().__init__()

        self._config_name = None
        self._need_restart = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if need_restart is not None:
            self.need_restart = need_restart

    @property
    def config_name(self):
        r"""Gets the config_name of this ResetConfigurationResponse.

        **参数解释**：  参数组模板名称。  **约束限制**：  不涉及。

        :return: The config_name of this ResetConfigurationResponse.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this ResetConfigurationResponse.

        **参数解释**：  参数组模板名称。  **约束限制**：  不涉及。

        :param config_name: The config_name of this ResetConfigurationResponse.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def need_restart(self):
        r"""Gets the need_restart of this ResetConfigurationResponse.

        **参数解释**：  是否涉及重启。（当前该字段不使用，默认为false）  **约束限制**：  不涉及。

        :return: The need_restart of this ResetConfigurationResponse.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        r"""Sets the need_restart of this ResetConfigurationResponse.

        **参数解释**：  是否涉及重启。（当前该字段不使用，默认为false）  **约束限制**：  不涉及。

        :param need_restart: The need_restart of this ResetConfigurationResponse.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    def to_dict(self):
        import warnings
        warnings.warn("ResetConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ResetConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
