# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2TenantImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'image_name': 'str',
        'category': 'V2ImageCategory',
        'image_registry': 'str',
        'image_namespace': 'str',
        'version_count': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'visibility': 'str',
        'description': 'str',
        'instruction': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_name': 'image_name',
        'category': 'category',
        'image_registry': 'image_registry',
        'image_namespace': 'image_namespace',
        'version_count': 'version_count',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'visibility': 'visibility',
        'description': 'description',
        'instruction': 'instruction'
    }

    def __init__(self, id=None, image_name=None, category=None, image_registry=None, image_namespace=None, version_count=None, create_time=None, update_time=None, visibility=None, description=None, instruction=None):
        r"""ShowV2TenantImageResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type id: str
        :param image_name: **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 
        :type image_name: str
        :param category: 
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        :param image_registry: **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 
        :type image_registry: str
        :param image_namespace: **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 
        :type image_namespace: str
        :param version_count: **参数解释**：镜像版本数量。 **取值范围**：大于等于0。 
        :type version_count: int
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        :param visibility: **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。 
        :type visibility: str
        :param description: **参数解释**：镜像的描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 
        :type description: str
        :param instruction: **参数解释**：公共镜像使用说明。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度0~20000个字符。 
        :type instruction: str
        """
        
        super().__init__()

        self._id = None
        self._image_name = None
        self._category = None
        self._image_registry = None
        self._image_namespace = None
        self._version_count = None
        self._create_time = None
        self._update_time = None
        self._visibility = None
        self._description = None
        self._instruction = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_name is not None:
            self.image_name = image_name
        if category is not None:
            self.category = category
        if image_registry is not None:
            self.image_registry = image_registry
        if image_namespace is not None:
            self.image_namespace = image_namespace
        if version_count is not None:
            self.version_count = version_count
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if visibility is not None:
            self.visibility = visibility
        if description is not None:
            self.description = description
        if instruction is not None:
            self.instruction = instruction

    @property
    def id(self):
        r"""Gets the id of this ShowV2TenantImageResponse.

        **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The id of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowV2TenantImageResponse.

        **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param id: The id of this ShowV2TenantImageResponse.
        :type id: str
        """
        self._id = id

    @property
    def image_name(self):
        r"""Gets the image_name of this ShowV2TenantImageResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :return: The image_name of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ShowV2TenantImageResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :param image_name: The image_name of this ShowV2TenantImageResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def category(self):
        r"""Gets the category of this ShowV2TenantImageResponse.

        :return: The category of this ShowV2TenantImageResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowV2TenantImageResponse.

        :param category: The category of this ShowV2TenantImageResponse.
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        self._category = category

    @property
    def image_registry(self):
        r"""Gets the image_registry of this ShowV2TenantImageResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :return: The image_registry of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._image_registry

    @image_registry.setter
    def image_registry(self, image_registry):
        r"""Sets the image_registry of this ShowV2TenantImageResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :param image_registry: The image_registry of this ShowV2TenantImageResponse.
        :type image_registry: str
        """
        self._image_registry = image_registry

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this ShowV2TenantImageResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :return: The image_namespace of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this ShowV2TenantImageResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :param image_namespace: The image_namespace of this ShowV2TenantImageResponse.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def version_count(self):
        r"""Gets the version_count of this ShowV2TenantImageResponse.

        **参数解释**：镜像版本数量。 **取值范围**：大于等于0。 

        :return: The version_count of this ShowV2TenantImageResponse.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this ShowV2TenantImageResponse.

        **参数解释**：镜像版本数量。 **取值范围**：大于等于0。 

        :param version_count: The version_count of this ShowV2TenantImageResponse.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowV2TenantImageResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this ShowV2TenantImageResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowV2TenantImageResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this ShowV2TenantImageResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowV2TenantImageResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this ShowV2TenantImageResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowV2TenantImageResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this ShowV2TenantImageResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowV2TenantImageResponse.

        **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。 

        :return: The visibility of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowV2TenantImageResponse.

        **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。 

        :param visibility: The visibility of this ShowV2TenantImageResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def description(self):
        r"""Gets the description of this ShowV2TenantImageResponse.

        **参数解释**：镜像的描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 

        :return: The description of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowV2TenantImageResponse.

        **参数解释**：镜像的描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 

        :param description: The description of this ShowV2TenantImageResponse.
        :type description: str
        """
        self._description = description

    @property
    def instruction(self):
        r"""Gets the instruction of this ShowV2TenantImageResponse.

        **参数解释**：公共镜像使用说明。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度0~20000个字符。 

        :return: The instruction of this ShowV2TenantImageResponse.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this ShowV2TenantImageResponse.

        **参数解释**：公共镜像使用说明。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度0~20000个字符。 

        :param instruction: The instruction of this ShowV2TenantImageResponse.
        :type instruction: str
        """
        self._instruction = instruction

    def to_dict(self):
        import warnings
        warnings.warn("ShowV2TenantImageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowV2TenantImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
