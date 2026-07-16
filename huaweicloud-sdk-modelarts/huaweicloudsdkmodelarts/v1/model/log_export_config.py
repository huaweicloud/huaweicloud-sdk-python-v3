# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogExportConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'rotation_enabled': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'rotation_enabled': 'rotation_enabled'
    }

    def __init__(self, version=None, rotation_enabled=None):
        r"""LogExportConfig

        The model defined in huaweicloud sdk

        :param version: **参数解释**：日志版本号。 **约束限制**： - 日志版本取值为v0、v1，默认为v0。 **取值范围**：v0、v1 **默认取值**：v0。
        :type version: str
        :param rotation_enabled: **参数解释**：是否开启日志分时段下载。 **约束限制**：不涉及。 **取值范围**： - true：开启日志分时段下载 - false：关闭日志分时段下载 **默认取值**：false。
        :type rotation_enabled: bool
        """
        
        

        self._version = None
        self._rotation_enabled = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if rotation_enabled is not None:
            self.rotation_enabled = rotation_enabled

    @property
    def version(self):
        r"""Gets the version of this LogExportConfig.

        **参数解释**：日志版本号。 **约束限制**： - 日志版本取值为v0、v1，默认为v0。 **取值范围**：v0、v1 **默认取值**：v0。

        :return: The version of this LogExportConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this LogExportConfig.

        **参数解释**：日志版本号。 **约束限制**： - 日志版本取值为v0、v1，默认为v0。 **取值范围**：v0、v1 **默认取值**：v0。

        :param version: The version of this LogExportConfig.
        :type version: str
        """
        self._version = version

    @property
    def rotation_enabled(self):
        r"""Gets the rotation_enabled of this LogExportConfig.

        **参数解释**：是否开启日志分时段下载。 **约束限制**：不涉及。 **取值范围**： - true：开启日志分时段下载 - false：关闭日志分时段下载 **默认取值**：false。

        :return: The rotation_enabled of this LogExportConfig.
        :rtype: bool
        """
        return self._rotation_enabled

    @rotation_enabled.setter
    def rotation_enabled(self, rotation_enabled):
        r"""Sets the rotation_enabled of this LogExportConfig.

        **参数解释**：是否开启日志分时段下载。 **约束限制**：不涉及。 **取值范围**： - true：开启日志分时段下载 - false：关闭日志分时段下载 **默认取值**：false。

        :param rotation_enabled: The rotation_enabled of this LogExportConfig.
        :type rotation_enabled: bool
        """
        self._rotation_enabled = rotation_enabled

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
        if not isinstance(other, LogExportConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
