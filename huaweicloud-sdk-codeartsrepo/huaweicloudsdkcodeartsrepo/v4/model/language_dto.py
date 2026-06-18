# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LanguageDto:

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
        'extension_list': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'extension_list': 'extension_list'
    }

    def __init__(self, name=None, extension_list=None):
        r"""LanguageDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 语言名称。 **约束限制：** 不涉及。
        :type name: str
        :param extension_list: **参数解释：** 文件后缀名。 **约束限制：** 不涉及。
        :type extension_list: list[str]
        """
        
        

        self._name = None
        self._extension_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if extension_list is not None:
            self.extension_list = extension_list

    @property
    def name(self):
        r"""Gets the name of this LanguageDto.

        **参数解释：** 语言名称。 **约束限制：** 不涉及。

        :return: The name of this LanguageDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LanguageDto.

        **参数解释：** 语言名称。 **约束限制：** 不涉及。

        :param name: The name of this LanguageDto.
        :type name: str
        """
        self._name = name

    @property
    def extension_list(self):
        r"""Gets the extension_list of this LanguageDto.

        **参数解释：** 文件后缀名。 **约束限制：** 不涉及。

        :return: The extension_list of this LanguageDto.
        :rtype: list[str]
        """
        return self._extension_list

    @extension_list.setter
    def extension_list(self, extension_list):
        r"""Sets the extension_list of this LanguageDto.

        **参数解释：** 文件后缀名。 **约束限制：** 不涉及。

        :param extension_list: The extension_list of this LanguageDto.
        :type extension_list: list[str]
        """
        self._extension_list = extension_list

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
        if not isinstance(other, LanguageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
