# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobOutputResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'config': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'config': 'config'
    }

    def __init__(self, name=None, type=None, config=None):
        r"""JobOutputResp

        The model defined in huaweicloud sdk

        :param name: **参数解释**：输出数据的名称。 **取值范围**：不涉及。
        :type name: str
        :param type: **参数解释**：输出项类型。 **取值范围**：枚举值如下： - obs：OBS - model：AI应用元模型
        :type type: str
        :param config: **参数解释**：输出配置。
        :type config: dict(str, object)
        """
        
        

        self._name = None
        self._type = None
        self._config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if config is not None:
            self.config = config

    @property
    def name(self):
        r"""Gets the name of this JobOutputResp.

        **参数解释**：输出数据的名称。 **取值范围**：不涉及。

        :return: The name of this JobOutputResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobOutputResp.

        **参数解释**：输出数据的名称。 **取值范围**：不涉及。

        :param name: The name of this JobOutputResp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this JobOutputResp.

        **参数解释**：输出项类型。 **取值范围**：枚举值如下： - obs：OBS - model：AI应用元模型

        :return: The type of this JobOutputResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this JobOutputResp.

        **参数解释**：输出项类型。 **取值范围**：枚举值如下： - obs：OBS - model：AI应用元模型

        :param type: The type of this JobOutputResp.
        :type type: str
        """
        self._type = type

    @property
    def config(self):
        r"""Gets the config of this JobOutputResp.

        **参数解释**：输出配置。

        :return: The config of this JobOutputResp.
        :rtype: dict(str, object)
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this JobOutputResp.

        **参数解释**：输出配置。

        :param config: The config of this JobOutputResp.
        :type config: dict(str, object)
        """
        self._config = config

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
        if not isinstance(other, JobOutputResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
