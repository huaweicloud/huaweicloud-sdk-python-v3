# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Model:

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
        'url': 'str',
        'quant_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'quant_type': 'quant_type'
    }

    def __init__(self, name=None, url=None, quant_type=None):
        r"""Model

        The model defined in huaweicloud sdk

        :param name: **参数解释**：模型名称。 **取值范围**：不涉及。
        :type name: str
        :param url: **参数解释**：模型OBS路径。 **取值范围**：不涉及。
        :type url: str
        :param quant_type: **参数解释**：量化数据类型。 **取值范围**：- w8A8 - fp16
        :type quant_type: str
        """
        
        

        self._name = None
        self._url = None
        self._quant_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if quant_type is not None:
            self.quant_type = quant_type

    @property
    def name(self):
        r"""Gets the name of this Model.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Model.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :param name: The name of this Model.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        r"""Gets the url of this Model.

        **参数解释**：模型OBS路径。 **取值范围**：不涉及。

        :return: The url of this Model.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Model.

        **参数解释**：模型OBS路径。 **取值范围**：不涉及。

        :param url: The url of this Model.
        :type url: str
        """
        self._url = url

    @property
    def quant_type(self):
        r"""Gets the quant_type of this Model.

        **参数解释**：量化数据类型。 **取值范围**：- w8A8 - fp16

        :return: The quant_type of this Model.
        :rtype: str
        """
        return self._quant_type

    @quant_type.setter
    def quant_type(self, quant_type):
        r"""Sets the quant_type of this Model.

        **参数解释**：量化数据类型。 **取值范围**：- w8A8 - fp16

        :param quant_type: The quant_type of this Model.
        :type quant_type: str
        """
        self._quant_type = quant_type

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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
