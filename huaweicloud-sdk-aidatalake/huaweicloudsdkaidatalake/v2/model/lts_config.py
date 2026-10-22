# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'lts_group_id': 'str',
        'lts_stream_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id'
    }

    def __init__(self, enable=None, lts_group_id=None, lts_stream_id=None):
        r"""LtsConfig

        The model defined in huaweicloud sdk

        :param enable: **参数解释**：是否开启LTS日志。 **约束限制**：不涉及。 **取值范围**：   - true：开启。   - false：不开启。 **默认取值**：false。
        :type enable: bool
        :param lts_group_id: **参数解释**：LTS日志组ID，可在云日志服务LTS控制台日志管理页面的日志组列表查看。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type lts_group_id: str
        :param lts_stream_id: **参数解释**：LTS日志流ID，可在云日志服务LTS控制台日志管理页面的日志组列表展开查看对应的日志流。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type lts_stream_id: str
        """
        
        

        self._enable = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_stream_id is not None:
            self.lts_stream_id = lts_stream_id

    @property
    def enable(self):
        r"""Gets the enable of this LtsConfig.

        **参数解释**：是否开启LTS日志。 **约束限制**：不涉及。 **取值范围**：   - true：开启。   - false：不开启。 **默认取值**：false。

        :return: The enable of this LtsConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this LtsConfig.

        **参数解释**：是否开启LTS日志。 **约束限制**：不涉及。 **取值范围**：   - true：开启。   - false：不开启。 **默认取值**：false。

        :param enable: The enable of this LtsConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this LtsConfig.

        **参数解释**：LTS日志组ID，可在云日志服务LTS控制台日志管理页面的日志组列表查看。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The lts_group_id of this LtsConfig.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this LtsConfig.

        **参数解释**：LTS日志组ID，可在云日志服务LTS控制台日志管理页面的日志组列表查看。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param lts_group_id: The lts_group_id of this LtsConfig.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this LtsConfig.

        **参数解释**：LTS日志流ID，可在云日志服务LTS控制台日志管理页面的日志组列表展开查看对应的日志流。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The lts_stream_id of this LtsConfig.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this LtsConfig.

        **参数解释**：LTS日志流ID，可在云日志服务LTS控制台日志管理页面的日志组列表展开查看对应的日志流。 **约束限制**：enable为true的时候需要配置。 **取值范围**：长度为1~36个字符，支持英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param lts_stream_id: The lts_stream_id of this LtsConfig.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

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
        if not isinstance(other, LtsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
