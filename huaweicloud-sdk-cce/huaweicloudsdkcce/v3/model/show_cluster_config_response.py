# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ttl_in_days': 'int',
        'log_configs': 'list[ClusterLogConfigLogConfigs]'
    }

    attribute_map = {
        'ttl_in_days': 'ttl_in_days',
        'log_configs': 'log_configs'
    }

    def __init__(self, ttl_in_days=None, log_configs=None):
        r"""ShowClusterConfigResponse

        The model defined in huaweicloud sdk

        :param ttl_in_days: **参数解释**：  存储时长，单位：天。  **约束限制**：  不涉及  **取值范围**： 0-30  **默认取值**： 不涉及
        :type ttl_in_days: int
        :param log_configs: **参数解释**： 日志配置项详细信息 **约束限制**: 不涉及
        :type log_configs: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
        """
        
        super().__init__()

        self._ttl_in_days = None
        self._log_configs = None
        self.discriminator = None

        if ttl_in_days is not None:
            self.ttl_in_days = ttl_in_days
        if log_configs is not None:
            self.log_configs = log_configs

    @property
    def ttl_in_days(self):
        r"""Gets the ttl_in_days of this ShowClusterConfigResponse.

        **参数解释**：  存储时长，单位：天。  **约束限制**：  不涉及  **取值范围**： 0-30  **默认取值**： 不涉及

        :return: The ttl_in_days of this ShowClusterConfigResponse.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        r"""Sets the ttl_in_days of this ShowClusterConfigResponse.

        **参数解释**：  存储时长，单位：天。  **约束限制**：  不涉及  **取值范围**： 0-30  **默认取值**： 不涉及

        :param ttl_in_days: The ttl_in_days of this ShowClusterConfigResponse.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def log_configs(self):
        r"""Gets the log_configs of this ShowClusterConfigResponse.

        **参数解释**： 日志配置项详细信息 **约束限制**: 不涉及

        :return: The log_configs of this ShowClusterConfigResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this ShowClusterConfigResponse.

        **参数解释**： 日志配置项详细信息 **约束限制**: 不涉及

        :param log_configs: The log_configs of this ShowClusterConfigResponse.
        :type log_configs: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
        """
        self._log_configs = log_configs

    def to_dict(self):
        import warnings
        warnings.warn("ShowClusterConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowClusterConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
