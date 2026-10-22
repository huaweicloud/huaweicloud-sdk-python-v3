# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2TenantImageVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'image_version': 'str',
        'category': 'str',
        'image_registry': 'str',
        'image_namespace': 'str',
        'image_name': 'str',
        'architectures': 'list[str]',
        'container_softwares': 'list[ContainerSoftware]',
        'status': 'V2ImageVersionStatus',
        'type': 'V2ImageVersionType',
        'visibility': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'description': 'str',
        'base_image_id': 'str',
        'base_image_version_id': 'str',
        'image_snapshot': 'V2ImageSnapshotInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'version_id': 'version_id',
        'image_version': 'image_version',
        'category': 'category',
        'image_registry': 'image_registry',
        'image_namespace': 'image_namespace',
        'image_name': 'image_name',
        'architectures': 'architectures',
        'container_softwares': 'container_softwares',
        'status': 'status',
        'type': 'type',
        'visibility': 'visibility',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'base_image_id': 'base_image_id',
        'base_image_version_id': 'base_image_version_id',
        'image_snapshot': 'image_snapshot',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, version_id=None, image_version=None, category=None, image_registry=None, image_namespace=None, image_name=None, architectures=None, container_softwares=None, status=None, type=None, visibility=None, create_time=None, update_time=None, description=None, base_image_id=None, base_image_version_id=None, image_snapshot=None, x_request_id=None):
        r"""UpdateV2TenantImageVersionResponse

        The model defined in huaweicloud sdk

        :param version_id: **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type version_id: str
        :param image_version: **参数解释**：镜像版本。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度2~32个字符。 
        :type image_version: str
        :param category: **参数解释**：镜像分类。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 
        :type category: str
        :param image_registry: **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 
        :type image_registry: str
        :param image_namespace: **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 
        :type image_namespace: str
        :param image_name: **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 
        :type image_name: str
        :param architectures: **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构）。
        :type architectures: list[str]
        :param container_softwares: **参数解释**：镜像软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：最小个数为0，最大个数为100。 
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionStatus`
        :param type: 
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        :param visibility: **参数解释**：镜像版本可见性。 **取值范围**：   - PRIVATE：私有，仅工作空间内可见。   - PUBLIC：公共，所有工作空间可见。 
        :type visibility: str
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        :param description: **参数解释**：镜像版本描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 
        :type description: str
        :param base_image_id: **参数解释**：关联的预置基础镜像ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 
        :type base_image_id: str
        :param base_image_version_id: **参数解释**：关联的预置基础镜像版本ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 
        :type base_image_version_id: str
        :param image_snapshot: 
        :type image_snapshot: :class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._version_id = None
        self._image_version = None
        self._category = None
        self._image_registry = None
        self._image_namespace = None
        self._image_name = None
        self._architectures = None
        self._container_softwares = None
        self._status = None
        self._type = None
        self._visibility = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._base_image_id = None
        self._base_image_version_id = None
        self._image_snapshot = None
        self._x_request_id = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if image_version is not None:
            self.image_version = image_version
        if category is not None:
            self.category = category
        if image_registry is not None:
            self.image_registry = image_registry
        if image_namespace is not None:
            self.image_namespace = image_namespace
        if image_name is not None:
            self.image_name = image_name
        if architectures is not None:
            self.architectures = architectures
        if container_softwares is not None:
            self.container_softwares = container_softwares
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if visibility is not None:
            self.visibility = visibility
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if base_image_id is not None:
            self.base_image_id = base_image_id
        if base_image_version_id is not None:
            self.base_image_version_id = base_image_version_id
        if image_snapshot is not None:
            self.image_snapshot = image_snapshot
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The version_id of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param version_id: The version_id of this UpdateV2TenantImageVersionResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def image_version(self):
        r"""Gets the image_version of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度2~32个字符。 

        :return: The image_version of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度2~32个字符。 

        :param image_version: The image_version of this UpdateV2TenantImageVersionResponse.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def category(self):
        r"""Gets the category of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像分类。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 

        :return: The category of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像分类。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 

        :param category: The category of this UpdateV2TenantImageVersionResponse.
        :type category: str
        """
        self._category = category

    @property
    def image_registry(self):
        r"""Gets the image_registry of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :return: The image_registry of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._image_registry

    @image_registry.setter
    def image_registry(self, image_registry):
        r"""Sets the image_registry of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :param image_registry: The image_registry of this UpdateV2TenantImageVersionResponse.
        :type image_registry: str
        """
        self._image_registry = image_registry

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :return: The image_namespace of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :param image_namespace: The image_namespace of this UpdateV2TenantImageVersionResponse.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :return: The image_name of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :param image_name: The image_name of this UpdateV2TenantImageVersionResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def architectures(self):
        r"""Gets the architectures of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构）。

        :return: The architectures of this UpdateV2TenantImageVersionResponse.
        :rtype: list[str]
        """
        return self._architectures

    @architectures.setter
    def architectures(self, architectures):
        r"""Sets the architectures of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像支持的架构列表，取值包括：x86_64（x86架构）、aarch64（ARM架构）。

        :param architectures: The architectures of this UpdateV2TenantImageVersionResponse.
        :type architectures: list[str]
        """
        self._architectures = architectures

    @property
    def container_softwares(self):
        r"""Gets the container_softwares of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：最小个数为0，最大个数为100。 

        :return: The container_softwares of this UpdateV2TenantImageVersionResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        return self._container_softwares

    @container_softwares.setter
    def container_softwares(self, container_softwares):
        r"""Sets the container_softwares of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像软件列表，每个元素为一个ContainerSoftware对象，包含软件名称和版本信息。 **约束限制**：最小个数为0，最大个数为100。 

        :param container_softwares: The container_softwares of this UpdateV2TenantImageVersionResponse.
        :type container_softwares: list[:class:`huaweicloudsdkaidatalake.v2.ContainerSoftware`]
        """
        self._container_softwares = container_softwares

    @property
    def status(self):
        r"""Gets the status of this UpdateV2TenantImageVersionResponse.

        :return: The status of this UpdateV2TenantImageVersionResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateV2TenantImageVersionResponse.

        :param status: The status of this UpdateV2TenantImageVersionResponse.
        :type status: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionStatus`
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this UpdateV2TenantImageVersionResponse.

        :return: The type of this UpdateV2TenantImageVersionResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateV2TenantImageVersionResponse.

        :param type: The type of this UpdateV2TenantImageVersionResponse.
        :type type: :class:`huaweicloudsdkaidatalake.v2.V2ImageVersionType`
        """
        self._type = type

    @property
    def visibility(self):
        r"""Gets the visibility of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本可见性。 **取值范围**：   - PRIVATE：私有，仅工作空间内可见。   - PUBLIC：公共，所有工作空间可见。 

        :return: The visibility of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本可见性。 **取值范围**：   - PRIVATE：私有，仅工作空间内可见。   - PUBLIC：公共，所有工作空间可见。 

        :param visibility: The visibility of this UpdateV2TenantImageVersionResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateV2TenantImageVersionResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this UpdateV2TenantImageVersionResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateV2TenantImageVersionResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this UpdateV2TenantImageVersionResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateV2TenantImageVersionResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this UpdateV2TenantImageVersionResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateV2TenantImageVersionResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this UpdateV2TenantImageVersionResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 

        :return: The description of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2TenantImageVersionResponse.

        **参数解释**：镜像版本描述。 **取值范围**：支持中文字符、英文字母、数字及常用符号（不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号），长度0~2000个字符。 

        :param description: The description of this UpdateV2TenantImageVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def base_image_id(self):
        r"""Gets the base_image_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：关联的预置基础镜像ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :return: The base_image_id of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._base_image_id

    @base_image_id.setter
    def base_image_id(self, base_image_id):
        r"""Sets the base_image_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：关联的预置基础镜像ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :param base_image_id: The base_image_id of this UpdateV2TenantImageVersionResponse.
        :type base_image_id: str
        """
        self._base_image_id = base_image_id

    @property
    def base_image_version_id(self):
        r"""Gets the base_image_version_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：关联的预置基础镜像版本ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :return: The base_image_version_id of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._base_image_version_id

    @base_image_version_id.setter
    def base_image_version_id(self, base_image_version_id):
        r"""Sets the base_image_version_id of this UpdateV2TenantImageVersionResponse.

        **参数解释**：关联的预置基础镜像版本ID。 **约束限制**：Spark类型自定义镜像时必填。 **取值范围**：支持英文字母、数字及中划线，长度0~64个字符。 **默认取值**：不涉及。 

        :param base_image_version_id: The base_image_version_id of this UpdateV2TenantImageVersionResponse.
        :type base_image_version_id: str
        """
        self._base_image_version_id = base_image_version_id

    @property
    def image_snapshot(self):
        r"""Gets the image_snapshot of this UpdateV2TenantImageVersionResponse.

        :return: The image_snapshot of this UpdateV2TenantImageVersionResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`
        """
        return self._image_snapshot

    @image_snapshot.setter
    def image_snapshot(self, image_snapshot):
        r"""Sets the image_snapshot of this UpdateV2TenantImageVersionResponse.

        :param image_snapshot: The image_snapshot of this UpdateV2TenantImageVersionResponse.
        :type image_snapshot: :class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`
        """
        self._image_snapshot = image_snapshot

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateV2TenantImageVersionResponse.

        :return: The x_request_id of this UpdateV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateV2TenantImageVersionResponse.

        :param x_request_id: The x_request_id of this UpdateV2TenantImageVersionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateV2TenantImageVersionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateV2TenantImageVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
