# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterV2ImageRequestInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_url': 'str',
        'category': 'V2ImageCategory',
        'architectures': 'list[str]',
        'type': 'V2ImageVersionType',
        'container_softwares': 'list[ContainerSoftware]',
        'description': 'str',
        'base_image_id': 'str',
        'base_image_version_id': 'str'
    }

    attribute_map = {
        'image_url': 'image_url',
        'category': 'category',
        'architectures': 'architectures',
        'type': 'type',
        'container_softwares': 'container_softwares',
        'description': 'description',
        'base_image_id': 'base_image_id',
        'base_image_version_id': 'base_image_version_id'
    }

    def __init__(self, image_url=None, category=None, architectures=None, type=None, container_softwares=None, description=None, base_image_id=None, base_image_version_id=None):
        r"""RegisterV2ImageRequestInput

        The model defined in huaweicloud sdk

        :param image_url: **参数解释**：自定义镜像的URL地址，由镜像仓库地址、镜像命名空间、镜像名称和镜像版本组成。 **约束限制**：不涉及。 **取值范围**：由大小写英文字母、数字、小数点(.)、斜杠(/)、冒号(:)、下划线(_)和连字符(-)组成的容器镜像地址。长度为1~2000个字符。 **默认取值**：不涉及。 
        :type image_url: str
        :param category: 
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        :param architectures: **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。
        :type architectures: list[str]
        :param type: 
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        :param container_softwares: **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：软件列表最小个数为0，最大个数为100。
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        :param description: **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 
        :type description: str
        :param base_image_id: **参数解释**：基础镜像ID，可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：Spark类型镜像必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 
        :type base_image_id: str
        :param base_image_version_id: **参数解释**：基础镜像版本ID，可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：当镜像分类为Spark类型时此字段必填，其余情况可选。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 
        :type base_image_version_id: str
        """
        
        

        self._image_url = None
        self._category = None
        self._architectures = None
        self._type = None
        self._container_softwares = None
        self._description = None
        self._base_image_id = None
        self._base_image_version_id = None
        self.discriminator = None

        self.image_url = image_url
        self.category = category
        if architectures is not None:
            self.architectures = architectures
        self.type = type
        if container_softwares is not None:
            self.container_softwares = container_softwares
        if description is not None:
            self.description = description
        if base_image_id is not None:
            self.base_image_id = base_image_id
        if base_image_version_id is not None:
            self.base_image_version_id = base_image_version_id

    @property
    def image_url(self):
        r"""Gets the image_url of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像的URL地址，由镜像仓库地址、镜像命名空间、镜像名称和镜像版本组成。 **约束限制**：不涉及。 **取值范围**：由大小写英文字母、数字、小数点(.)、斜杠(/)、冒号(:)、下划线(_)和连字符(-)组成的容器镜像地址。长度为1~2000个字符。 **默认取值**：不涉及。 

        :return: The image_url of this RegisterV2ImageRequestInput.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像的URL地址，由镜像仓库地址、镜像命名空间、镜像名称和镜像版本组成。 **约束限制**：不涉及。 **取值范围**：由大小写英文字母、数字、小数点(.)、斜杠(/)、冒号(:)、下划线(_)和连字符(-)组成的容器镜像地址。长度为1~2000个字符。 **默认取值**：不涉及。 

        :param image_url: The image_url of this RegisterV2ImageRequestInput.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def category(self):
        r"""Gets the category of this RegisterV2ImageRequestInput.

        :return: The category of this RegisterV2ImageRequestInput.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RegisterV2ImageRequestInput.

        :param category: The category of this RegisterV2ImageRequestInput.
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        self._category = category

    @property
    def architectures(self):
        r"""Gets the architectures of this RegisterV2ImageRequestInput.

        **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。

        :return: The architectures of this RegisterV2ImageRequestInput.
        :rtype: list[str]
        """
        return self._architectures

    @architectures.setter
    def architectures(self, architectures):
        r"""Sets the architectures of this RegisterV2ImageRequestInput.

        **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构），未传入该参数时默认为x86_64。 **约束限制**：不涉及。

        :param architectures: The architectures of this RegisterV2ImageRequestInput.
        :type architectures: list[str]
        """
        self._architectures = architectures

    @property
    def type(self):
        r"""Gets the type of this RegisterV2ImageRequestInput.

        :return: The type of this RegisterV2ImageRequestInput.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RegisterV2ImageRequestInput.

        :param type: The type of this RegisterV2ImageRequestInput.
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        self._type = type

    @property
    def container_softwares(self):
        r"""Gets the container_softwares of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：软件列表最小个数为0，最大个数为100。

        :return: The container_softwares of this RegisterV2ImageRequestInput.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        return self._container_softwares

    @container_softwares.setter
    def container_softwares(self, container_softwares):
        r"""Sets the container_softwares of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像包含的软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：软件列表最小个数为0，最大个数为100。

        :param container_softwares: The container_softwares of this RegisterV2ImageRequestInput.
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        self._container_softwares = container_softwares

    @property
    def description(self):
        r"""Gets the description of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 

        :return: The description of this RegisterV2ImageRequestInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RegisterV2ImageRequestInput.

        **参数解释**：自定义镜像的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~2000个字符。 **默认取值**：不涉及。 

        :param description: The description of this RegisterV2ImageRequestInput.
        :type description: str
        """
        self._description = description

    @property
    def base_image_id(self):
        r"""Gets the base_image_id of this RegisterV2ImageRequestInput.

        **参数解释**：基础镜像ID，可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：Spark类型镜像必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :return: The base_image_id of this RegisterV2ImageRequestInput.
        :rtype: str
        """
        return self._base_image_id

    @base_image_id.setter
    def base_image_id(self, base_image_id):
        r"""Sets the base_image_id of this RegisterV2ImageRequestInput.

        **参数解释**：基础镜像ID，可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：Spark类型镜像必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :param base_image_id: The base_image_id of this RegisterV2ImageRequestInput.
        :type base_image_id: str
        """
        self._base_image_id = base_image_id

    @property
    def base_image_version_id(self):
        r"""Gets the base_image_version_id of this RegisterV2ImageRequestInput.

        **参数解释**：基础镜像版本ID，可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：当镜像分类为Spark类型时此字段必填，其余情况可选。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :return: The base_image_version_id of this RegisterV2ImageRequestInput.
        :rtype: str
        """
        return self._base_image_version_id

    @base_image_version_id.setter
    def base_image_version_id(self, base_image_version_id):
        r"""Sets the base_image_version_id of this RegisterV2ImageRequestInput.

        **参数解释**：基础镜像版本ID，可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：当镜像分类为Spark类型时此字段必填，其余情况可选。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :param base_image_version_id: The base_image_version_id of this RegisterV2ImageRequestInput.
        :type base_image_version_id: str
        """
        self._base_image_version_id = base_image_version_id

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
        if not isinstance(other, RegisterV2ImageRequestInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
