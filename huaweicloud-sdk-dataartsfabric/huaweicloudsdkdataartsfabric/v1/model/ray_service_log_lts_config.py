# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayServiceLogLtsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'log_group_id': 'str',
        'log_stream_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id'
    }

    def __init__(self, enabled=None, log_group_id=None, log_stream_id=None):
        r"""RayServiceLogLtsConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**：是否开启RayService日志转储到LTS。 **约束限制**：不涉及。 **取值范围**：true，false。 **默认取值**：false。 
        :type enabled: bool
        :param log_group_id: **参数解释**：RayService日志转储到的LTS日志组id。 **约束限制**：需要是已经存在的LTS日志组id。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type log_group_id: str
        :param log_stream_id: **参数解释**：RayService日志转储到的LTS日志流id。 **约束限制**：需要是已经存在的LTS日志流id。 **取值范围**：不涉及。 **默认取值**：不涉及 
        :type log_stream_id: str
        """
        
        

        self._enabled = None
        self._log_group_id = None
        self._log_stream_id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id

    @property
    def enabled(self):
        r"""Gets the enabled of this RayServiceLogLtsConfig.

        **参数解释**：是否开启RayService日志转储到LTS。 **约束限制**：不涉及。 **取值范围**：true，false。 **默认取值**：false。 

        :return: The enabled of this RayServiceLogLtsConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this RayServiceLogLtsConfig.

        **参数解释**：是否开启RayService日志转储到LTS。 **约束限制**：不涉及。 **取值范围**：true，false。 **默认取值**：false。 

        :param enabled: The enabled of this RayServiceLogLtsConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this RayServiceLogLtsConfig.

        **参数解释**：RayService日志转储到的LTS日志组id。 **约束限制**：需要是已经存在的LTS日志组id。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The log_group_id of this RayServiceLogLtsConfig.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this RayServiceLogLtsConfig.

        **参数解释**：RayService日志转储到的LTS日志组id。 **约束限制**：需要是已经存在的LTS日志组id。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param log_group_id: The log_group_id of this RayServiceLogLtsConfig.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this RayServiceLogLtsConfig.

        **参数解释**：RayService日志转储到的LTS日志流id。 **约束限制**：需要是已经存在的LTS日志流id。 **取值范围**：不涉及。 **默认取值**：不涉及 

        :return: The log_stream_id of this RayServiceLogLtsConfig.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this RayServiceLogLtsConfig.

        **参数解释**：RayService日志转储到的LTS日志流id。 **约束限制**：需要是已经存在的LTS日志流id。 **取值范围**：不涉及。 **默认取值**：不涉及 

        :param log_stream_id: The log_stream_id of this RayServiceLogLtsConfig.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

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
        if not isinstance(other, RayServiceLogLtsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
