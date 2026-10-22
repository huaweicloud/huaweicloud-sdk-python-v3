# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2ImageVersionInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'architectures': 'list[str]',
        'type': 'V2ImageVersionType',
        'container_softwares': 'list[ContainerSoftware]',
        'category': 'V2ImageCategory'
    }

    attribute_map = {
        'description': 'description',
        'architectures': 'architectures',
        'type': 'type',
        'container_softwares': 'container_softwares',
        'category': 'category'
    }

    def __init__(self, description=None, architectures=None, type=None, container_softwares=None, category=None):
        r"""UpdateV2ImageVersionInput

        The model defined in huaweicloud sdk

        :param description: **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 
        :type description: str
        :param architectures: **参数解释**：支持镜像架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。
        :type architectures: list[str]
        :param type: 
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        :param container_softwares: **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息，软件列表最小个数为0，最大个数为100。 **约束限制**：不涉及。
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        :param category: 
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        
        

        self._description = None
        self._architectures = None
        self._type = None
        self._container_softwares = None
        self._category = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if architectures is not None:
            self.architectures = architectures
        if type is not None:
            self.type = type
        if container_softwares is not None:
            self.container_softwares = container_softwares
        if category is not None:
            self.category = category

    @property
    def description(self):
        r"""Gets the description of this UpdateV2ImageVersionInput.

        **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 

        :return: The description of this UpdateV2ImageVersionInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2ImageVersionInput.

        **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 

        :param description: The description of this UpdateV2ImageVersionInput.
        :type description: str
        """
        self._description = description

    @property
    def architectures(self):
        r"""Gets the architectures of this UpdateV2ImageVersionInput.

        **参数解释**：支持镜像架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。

        :return: The architectures of this UpdateV2ImageVersionInput.
        :rtype: list[str]
        """
        return self._architectures

    @architectures.setter
    def architectures(self, architectures):
        r"""Sets the architectures of this UpdateV2ImageVersionInput.

        **参数解释**：支持镜像架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。

        :param architectures: The architectures of this UpdateV2ImageVersionInput.
        :type architectures: list[str]
        """
        self._architectures = architectures

    @property
    def type(self):
        r"""Gets the type of this UpdateV2ImageVersionInput.

        :return: The type of this UpdateV2ImageVersionInput.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateV2ImageVersionInput.

        :param type: The type of this UpdateV2ImageVersionInput.
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        self._type = type

    @property
    def container_softwares(self):
        r"""Gets the container_softwares of this UpdateV2ImageVersionInput.

        **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息，软件列表最小个数为0，最大个数为100。 **约束限制**：不涉及。

        :return: The container_softwares of this UpdateV2ImageVersionInput.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        return self._container_softwares

    @container_softwares.setter
    def container_softwares(self, container_softwares):
        r"""Sets the container_softwares of this UpdateV2ImageVersionInput.

        **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息，软件列表最小个数为0，最大个数为100。 **约束限制**：不涉及。

        :param container_softwares: The container_softwares of this UpdateV2ImageVersionInput.
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        self._container_softwares = container_softwares

    @property
    def category(self):
        r"""Gets the category of this UpdateV2ImageVersionInput.

        :return: The category of this UpdateV2ImageVersionInput.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateV2ImageVersionInput.

        :param category: The category of this UpdateV2ImageVersionInput.
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        self._category = category

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
        if not isinstance(other, UpdateV2ImageVersionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
