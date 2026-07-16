# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'create_at': 'int',
        'description': 'str',
        'dev_services': 'list[str]',
        'id': 'str',
        'name': 'str',
        'namespace': 'str',
        'origin': 'str',
        'resource_categories': 'list[str]',
        'service_type': 'str',
        'size': 'int',
        'status': 'str',
        'status_message': 'str',
        'support_res_categories': 'list[str]',
        'swr_path': 'str',
        'tag': 'str',
        'type': 'str',
        'update_at': 'int',
        'visibility': 'str',
        'workspace_id': 'str',
        'flavor_type': 'str',
        'swr_instance_id': 'str',
        'show_name': 'str',
        'show_tag': 'str',
        'tags': 'list[TmsTagResponse]'
    }

    attribute_map = {
        'arch': 'arch',
        'create_at': 'create_at',
        'description': 'description',
        'dev_services': 'dev_services',
        'id': 'id',
        'name': 'name',
        'namespace': 'namespace',
        'origin': 'origin',
        'resource_categories': 'resource_categories',
        'service_type': 'service_type',
        'size': 'size',
        'status': 'status',
        'status_message': 'status_message',
        'support_res_categories': 'support_res_categories',
        'swr_path': 'swr_path',
        'tag': 'tag',
        'type': 'type',
        'update_at': 'update_at',
        'visibility': 'visibility',
        'workspace_id': 'workspace_id',
        'flavor_type': 'flavor_type',
        'swr_instance_id': 'swr_instance_id',
        'show_name': 'show_name',
        'show_tag': 'show_tag',
        'tags': 'tags'
    }

    def __init__(self, arch=None, create_at=None, description=None, dev_services=None, id=None, name=None, namespace=None, origin=None, resource_categories=None, service_type=None, size=None, status=None, status_message=None, support_res_categories=None, swr_path=None, tag=None, type=None, update_at=None, visibility=None, workspace_id=None, flavor_type=None, swr_instance_id=None, show_name=None, show_tag=None, tags=None):
        r"""DeleteImageResponse

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：该镜像所支持处理器架构类型。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。
        :type arch: str
        :param create_at: **参数解释**：镜像创建的时间，UTC毫秒。 **取值范围**：不涉及。
        :type create_at: int
        :param description: **参数解释**：该镜像所对应的描述信息。 **取值范围**：长度限制512个字符。
        :type description: str
        :param dev_services: **参数解释**：镜像支持的服务。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。
        :type dev_services: list[str]
        :param id: **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。预置镜像的ID参考[查询支持的镜像列表](ListImage.xml)获取。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：镜像名称。 **取值范围**：长度限制512个字符，支持小写字母、数字、中划线、下划线和点。
        :type name: str
        :param namespace: **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **取值范围**：不涉及。
        :type namespace: str
        :param origin: **参数解释**：指定镜像来源。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE：用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。
        :type origin: str
        :param resource_categories: **参数解释**：镜像支持的规格。枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)
        :type resource_categories: list[str]
        :param service_type: **参数解释**：镜像支持服务类型。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE：建议仅在推理部署场景使用。 - TRAIN：建议仅在训练任务场景使用。 - DEV：建议仅在开发调测场景使用。 - UNKNOWN：未明确设置的镜像支持的服务类型。
        :type service_type: str
        :param size: **参数解释**：镜像大小（单位KB）。 **取值范围**：不涉及。
        :type size: int
        :param status: **参数解释**：镜像状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化。 - CREATING：镜像保存中，此时Notebook不可用。 - CREATE_FAILED：镜像保存失败。 - ERROR：错误。 - DELETED：已删除。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建Notebook实例。
        :type status: str
        :param status_message: **参数解释**：镜像保存操作过程中，构建信息展示。 **取值范围**：不涉及。
        :type status_message: str
        :param support_res_categories: **参数解释**：镜像支持的规格。 枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)
        :type support_res_categories: list[str]
        :param swr_path: **参数解释**：SWR镜像地址。 **取值范围**：不涉及。
        :type swr_path: str
        :param tag: **参数解释**：镜像Tag。 **取值范围**：不涉及。
        :type tag: str
        :param type: **参数解释**：镜像类型。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。
        :type type: str
        :param update_at: **参数解释**：镜像最后更新的时间，UTC毫秒。 **取值范围**：不涉及。
        :type update_at: int
        :param visibility: **参数解释**：镜像可见度。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC：所有用户可以根据image_id来进行只读使用。
        :type visibility: str
        :param workspace_id: **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。
        :type workspace_id: str
        :param flavor_type: **参数解释**：镜像的资源类型。 **取值范围**：枚举类型，取值如下： - ASCEND_SNT9：昇腾910芯片。 - ASCEND_SNT9B：昇腾910B芯片。 - ASCEND_SNT3：昇腾310芯片。
        :type flavor_type: str
        :param swr_instance_id: 参数解释：SWR企业仓库ID。未使用SWR企业仓时该字段为null。 约束限制：不涉及。 取值范围：128位UUID。 默认取值：null。
        :type swr_instance_id: str
        :param show_name: **参数解释**：镜像展示名称，仅预置镜像具备该字段。
        :type show_name: str
        :param show_tag: **参数解释**：镜像展示版本号，仅预置镜像具备该字段。
        :type show_tag: str
        :param tags: **参数解释**：镜像标签。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        
        super().__init__()

        self._arch = None
        self._create_at = None
        self._description = None
        self._dev_services = None
        self._id = None
        self._name = None
        self._namespace = None
        self._origin = None
        self._resource_categories = None
        self._service_type = None
        self._size = None
        self._status = None
        self._status_message = None
        self._support_res_categories = None
        self._swr_path = None
        self._tag = None
        self._type = None
        self._update_at = None
        self._visibility = None
        self._workspace_id = None
        self._flavor_type = None
        self._swr_instance_id = None
        self._show_name = None
        self._show_tag = None
        self._tags = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if create_at is not None:
            self.create_at = create_at
        if description is not None:
            self.description = description
        if dev_services is not None:
            self.dev_services = dev_services
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if origin is not None:
            self.origin = origin
        if resource_categories is not None:
            self.resource_categories = resource_categories
        if service_type is not None:
            self.service_type = service_type
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if support_res_categories is not None:
            self.support_res_categories = support_res_categories
        if swr_path is not None:
            self.swr_path = swr_path
        if tag is not None:
            self.tag = tag
        if type is not None:
            self.type = type
        if update_at is not None:
            self.update_at = update_at
        if visibility is not None:
            self.visibility = visibility
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id
        if show_name is not None:
            self.show_name = show_name
        if show_tag is not None:
            self.show_tag = show_tag
        if tags is not None:
            self.tags = tags

    @property
    def arch(self):
        r"""Gets the arch of this DeleteImageResponse.

        **参数解释**：该镜像所支持处理器架构类型。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。

        :return: The arch of this DeleteImageResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this DeleteImageResponse.

        **参数解释**：该镜像所支持处理器架构类型。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。

        :param arch: The arch of this DeleteImageResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def create_at(self):
        r"""Gets the create_at of this DeleteImageResponse.

        **参数解释**：镜像创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The create_at of this DeleteImageResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DeleteImageResponse.

        **参数解释**：镜像创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :param create_at: The create_at of this DeleteImageResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def description(self):
        r"""Gets the description of this DeleteImageResponse.

        **参数解释**：该镜像所对应的描述信息。 **取值范围**：长度限制512个字符。

        :return: The description of this DeleteImageResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeleteImageResponse.

        **参数解释**：该镜像所对应的描述信息。 **取值范围**：长度限制512个字符。

        :param description: The description of this DeleteImageResponse.
        :type description: str
        """
        self._description = description

    @property
    def dev_services(self):
        r"""Gets the dev_services of this DeleteImageResponse.

        **参数解释**：镜像支持的服务。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。

        :return: The dev_services of this DeleteImageResponse.
        :rtype: list[str]
        """
        return self._dev_services

    @dev_services.setter
    def dev_services(self, dev_services):
        r"""Sets the dev_services of this DeleteImageResponse.

        **参数解释**：镜像支持的服务。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。

        :param dev_services: The dev_services of this DeleteImageResponse.
        :type dev_services: list[str]
        """
        self._dev_services = dev_services

    @property
    def id(self):
        r"""Gets the id of this DeleteImageResponse.

        **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。预置镜像的ID参考[查询支持的镜像列表](ListImage.xml)获取。 **取值范围**：不涉及。

        :return: The id of this DeleteImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteImageResponse.

        **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。预置镜像的ID参考[查询支持的镜像列表](ListImage.xml)获取。 **取值范围**：不涉及。

        :param id: The id of this DeleteImageResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DeleteImageResponse.

        **参数解释**：镜像名称。 **取值范围**：长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :return: The name of this DeleteImageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteImageResponse.

        **参数解释**：镜像名称。 **取值范围**：长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :param name: The name of this DeleteImageResponse.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this DeleteImageResponse.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **取值范围**：不涉及。

        :return: The namespace of this DeleteImageResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this DeleteImageResponse.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **取值范围**：不涉及。

        :param namespace: The namespace of this DeleteImageResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def origin(self):
        r"""Gets the origin of this DeleteImageResponse.

        **参数解释**：指定镜像来源。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE：用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。

        :return: The origin of this DeleteImageResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this DeleteImageResponse.

        **参数解释**：指定镜像来源。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE：用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。

        :param origin: The origin of this DeleteImageResponse.
        :type origin: str
        """
        self._origin = origin

    @property
    def resource_categories(self):
        r"""Gets the resource_categories of this DeleteImageResponse.

        **参数解释**：镜像支持的规格。枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :return: The resource_categories of this DeleteImageResponse.
        :rtype: list[str]
        """
        return self._resource_categories

    @resource_categories.setter
    def resource_categories(self, resource_categories):
        r"""Sets the resource_categories of this DeleteImageResponse.

        **参数解释**：镜像支持的规格。枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :param resource_categories: The resource_categories of this DeleteImageResponse.
        :type resource_categories: list[str]
        """
        self._resource_categories = resource_categories

    @property
    def service_type(self):
        r"""Gets the service_type of this DeleteImageResponse.

        **参数解释**：镜像支持服务类型。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE：建议仅在推理部署场景使用。 - TRAIN：建议仅在训练任务场景使用。 - DEV：建议仅在开发调测场景使用。 - UNKNOWN：未明确设置的镜像支持的服务类型。

        :return: The service_type of this DeleteImageResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this DeleteImageResponse.

        **参数解释**：镜像支持服务类型。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE：建议仅在推理部署场景使用。 - TRAIN：建议仅在训练任务场景使用。 - DEV：建议仅在开发调测场景使用。 - UNKNOWN：未明确设置的镜像支持的服务类型。

        :param service_type: The service_type of this DeleteImageResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def size(self):
        r"""Gets the size of this DeleteImageResponse.

        **参数解释**：镜像大小（单位KB）。 **取值范围**：不涉及。

        :return: The size of this DeleteImageResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this DeleteImageResponse.

        **参数解释**：镜像大小（单位KB）。 **取值范围**：不涉及。

        :param size: The size of this DeleteImageResponse.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this DeleteImageResponse.

        **参数解释**：镜像状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化。 - CREATING：镜像保存中，此时Notebook不可用。 - CREATE_FAILED：镜像保存失败。 - ERROR：错误。 - DELETED：已删除。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建Notebook实例。

        :return: The status of this DeleteImageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteImageResponse.

        **参数解释**：镜像状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化。 - CREATING：镜像保存中，此时Notebook不可用。 - CREATE_FAILED：镜像保存失败。 - ERROR：错误。 - DELETED：已删除。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建Notebook实例。

        :param status: The status of this DeleteImageResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        r"""Gets the status_message of this DeleteImageResponse.

        **参数解释**：镜像保存操作过程中，构建信息展示。 **取值范围**：不涉及。

        :return: The status_message of this DeleteImageResponse.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        r"""Sets the status_message of this DeleteImageResponse.

        **参数解释**：镜像保存操作过程中，构建信息展示。 **取值范围**：不涉及。

        :param status_message: The status_message of this DeleteImageResponse.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def support_res_categories(self):
        r"""Gets the support_res_categories of this DeleteImageResponse.

        **参数解释**：镜像支持的规格。 枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :return: The support_res_categories of this DeleteImageResponse.
        :rtype: list[str]
        """
        return self._support_res_categories

    @support_res_categories.setter
    def support_res_categories(self, support_res_categories):
        r"""Sets the support_res_categories of this DeleteImageResponse.

        **参数解释**：镜像支持的规格。 枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :param support_res_categories: The support_res_categories of this DeleteImageResponse.
        :type support_res_categories: list[str]
        """
        self._support_res_categories = support_res_categories

    @property
    def swr_path(self):
        r"""Gets the swr_path of this DeleteImageResponse.

        **参数解释**：SWR镜像地址。 **取值范围**：不涉及。

        :return: The swr_path of this DeleteImageResponse.
        :rtype: str
        """
        return self._swr_path

    @swr_path.setter
    def swr_path(self, swr_path):
        r"""Sets the swr_path of this DeleteImageResponse.

        **参数解释**：SWR镜像地址。 **取值范围**：不涉及。

        :param swr_path: The swr_path of this DeleteImageResponse.
        :type swr_path: str
        """
        self._swr_path = swr_path

    @property
    def tag(self):
        r"""Gets the tag of this DeleteImageResponse.

        **参数解释**：镜像Tag。 **取值范围**：不涉及。

        :return: The tag of this DeleteImageResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this DeleteImageResponse.

        **参数解释**：镜像Tag。 **取值范围**：不涉及。

        :param tag: The tag of this DeleteImageResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def type(self):
        r"""Gets the type of this DeleteImageResponse.

        **参数解释**：镜像类型。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。

        :return: The type of this DeleteImageResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteImageResponse.

        **参数解释**：镜像类型。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。

        :param type: The type of this DeleteImageResponse.
        :type type: str
        """
        self._type = type

    @property
    def update_at(self):
        r"""Gets the update_at of this DeleteImageResponse.

        **参数解释**：镜像最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The update_at of this DeleteImageResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this DeleteImageResponse.

        **参数解释**：镜像最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :param update_at: The update_at of this DeleteImageResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def visibility(self):
        r"""Gets the visibility of this DeleteImageResponse.

        **参数解释**：镜像可见度。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC：所有用户可以根据image_id来进行只读使用。

        :return: The visibility of this DeleteImageResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this DeleteImageResponse.

        **参数解释**：镜像可见度。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC：所有用户可以根据image_id来进行只读使用。

        :param visibility: The visibility of this DeleteImageResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteImageResponse.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :return: The workspace_id of this DeleteImageResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteImageResponse.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this DeleteImageResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this DeleteImageResponse.

        **参数解释**：镜像的资源类型。 **取值范围**：枚举类型，取值如下： - ASCEND_SNT9：昇腾910芯片。 - ASCEND_SNT9B：昇腾910B芯片。 - ASCEND_SNT3：昇腾310芯片。

        :return: The flavor_type of this DeleteImageResponse.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this DeleteImageResponse.

        **参数解释**：镜像的资源类型。 **取值范围**：枚举类型，取值如下： - ASCEND_SNT9：昇腾910芯片。 - ASCEND_SNT9B：昇腾910B芯片。 - ASCEND_SNT3：昇腾310芯片。

        :param flavor_type: The flavor_type of this DeleteImageResponse.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this DeleteImageResponse.

        参数解释：SWR企业仓库ID。未使用SWR企业仓时该字段为null。 约束限制：不涉及。 取值范围：128位UUID。 默认取值：null。

        :return: The swr_instance_id of this DeleteImageResponse.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this DeleteImageResponse.

        参数解释：SWR企业仓库ID。未使用SWR企业仓时该字段为null。 约束限制：不涉及。 取值范围：128位UUID。 默认取值：null。

        :param swr_instance_id: The swr_instance_id of this DeleteImageResponse.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

    @property
    def show_name(self):
        r"""Gets the show_name of this DeleteImageResponse.

        **参数解释**：镜像展示名称，仅预置镜像具备该字段。

        :return: The show_name of this DeleteImageResponse.
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        r"""Sets the show_name of this DeleteImageResponse.

        **参数解释**：镜像展示名称，仅预置镜像具备该字段。

        :param show_name: The show_name of this DeleteImageResponse.
        :type show_name: str
        """
        self._show_name = show_name

    @property
    def show_tag(self):
        r"""Gets the show_tag of this DeleteImageResponse.

        **参数解释**：镜像展示版本号，仅预置镜像具备该字段。

        :return: The show_tag of this DeleteImageResponse.
        :rtype: str
        """
        return self._show_tag

    @show_tag.setter
    def show_tag(self, show_tag):
        r"""Sets the show_tag of this DeleteImageResponse.

        **参数解释**：镜像展示版本号，仅预置镜像具备该字段。

        :param show_tag: The show_tag of this DeleteImageResponse.
        :type show_tag: str
        """
        self._show_tag = show_tag

    @property
    def tags(self):
        r"""Gets the tags of this DeleteImageResponse.

        **参数解释**：镜像标签。

        :return: The tags of this DeleteImageResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeleteImageResponse.

        **参数解释**：镜像标签。

        :param tags: The tags of this DeleteImageResponse.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        self._tags = tags

    def to_dict(self):
        import warnings
        warnings.warn("DeleteImageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
