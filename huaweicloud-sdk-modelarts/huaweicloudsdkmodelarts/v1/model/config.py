# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Config:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script': 'str',
        'type': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'script': 'script',
        'type': 'type',
        'mode': 'mode'
    }

    def __init__(self, script=None, type=None, mode=None):
        r"""Config

        The model defined in huaweicloud sdk

        :param script: **参数解释**：自定义脚本内容（base64编码）或脚本绝对路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type script: str
        :param type: **参数解释**：脚本类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMAND：script中需要指定脚本内容（base64编码）。 - SCRIPT：script中需要指定脚本路径。  **默认取值**：SCRIPT。
        :type type: str
        :param mode: **参数解释**：自定义脚本执行方式，同步或异步执行。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BLOCK：同步 - ASYNC：异步  **默认取值**：ASYNC
        :type mode: str
        """
        
        

        self._script = None
        self._type = None
        self._mode = None
        self.discriminator = None

        if script is not None:
            self.script = script
        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode

    @property
    def script(self):
        r"""Gets the script of this Config.

        **参数解释**：自定义脚本内容（base64编码）或脚本绝对路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The script of this Config.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this Config.

        **参数解释**：自定义脚本内容（base64编码）或脚本绝对路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param script: The script of this Config.
        :type script: str
        """
        self._script = script

    @property
    def type(self):
        r"""Gets the type of this Config.

        **参数解释**：脚本类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMAND：script中需要指定脚本内容（base64编码）。 - SCRIPT：script中需要指定脚本路径。  **默认取值**：SCRIPT。

        :return: The type of this Config.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Config.

        **参数解释**：脚本类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMAND：script中需要指定脚本内容（base64编码）。 - SCRIPT：script中需要指定脚本路径。  **默认取值**：SCRIPT。

        :param type: The type of this Config.
        :type type: str
        """
        self._type = type

    @property
    def mode(self):
        r"""Gets the mode of this Config.

        **参数解释**：自定义脚本执行方式，同步或异步执行。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BLOCK：同步 - ASYNC：异步  **默认取值**：ASYNC

        :return: The mode of this Config.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this Config.

        **参数解释**：自定义脚本执行方式，同步或异步执行。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BLOCK：同步 - ASYNC：异步  **默认取值**：ASYNC

        :param mode: The mode of this Config.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
