# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRegRequest:

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
        'description': 'str',
        'origin': 'str',
        'resource_category': 'list[str]',
        'service_type': 'str',
        'services': 'list[str]',
        'swr_path': 'str',
        'visibility': 'str',
        'workspace_id': 'str',
        'flavor_type': 'str',
        'tags': 'list[str]',
        'swr_instance_id': 'str',
        'read_me': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'description': 'description',
        'origin': 'origin',
        'resource_category': 'resource_category',
        'service_type': 'service_type',
        'services': 'services',
        'swr_path': 'swr_path',
        'visibility': 'visibility',
        'workspace_id': 'workspace_id',
        'flavor_type': 'flavor_type',
        'tags': 'tags',
        'swr_instance_id': 'swr_instance_id',
        'read_me': 'read_me'
    }

    def __init__(self, arch=None, description=None, origin=None, resource_category=None, service_type=None, services=None, swr_path=None, visibility=None, workspace_id=None, flavor_type=None, tags=None, swr_instance_id=None, read_me=None):
        r"""ImageRegRequest

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：该镜像所支持处理器架构类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。  **默认取值**：X86_64。
        :type arch: str
        :param description: **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。
        :type description: str
        :param origin: **参数解释**：指定镜像来源，可选项。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE: 用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。  **默认取值**：CUSTOMIZE。
        :type origin: str
        :param resource_category: **参数解释**：镜像支持的规格，默认值CPU、GPU。 枚举值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)。  **约束限制**：不涉及。
        :type resource_category: list[str]
        :param service_type: **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。
        :type service_type: str
        :param services: **参数解释**：镜像支持的服务，默认值NOTEBOOK、SSH。枚举值如下: - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。  **约束限制**：不涉及。
        :type services: list[str]
        :param swr_path: **参数解释**：SWR镜像地址。 **约束限制**：不涉及。 **取值范围**：长度最长为2048个字符，最短为16个字符，地址格式为：[仓库地址[:端口]]/[命名空间]/[镜像名称]:[标签]。 **默认取值**：不涉及。
        :type swr_path: str
        :param visibility: **参数解释**：镜像可见度。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC: 所有用户可以根据image_id来进行只读使用。  **默认取值**：PRIVATE。
        :type visibility: str
        :param workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。
        :type workspace_id: str
        :param flavor_type: **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： -ASCEND_SNT9：昇腾910芯片。 -ASCEND_SNT9B：昇腾910B芯片。 -ASCEND_SNT3：昇腾310芯片。  **默认取值**：不涉及。
        :type flavor_type: str
        :param tags: **参数解释**：该镜像所属镜像组对应的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。
        :type tags: list[str]
        :param swr_instance_id: **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type swr_instance_id: str
        :param read_me: **参数解释**：镜像指导。 **参数约束**：不涉及。 **取值范围**：字符串长度限制为3000个字符。 **默认取值**：不涉及。
        :type read_me: str
        """
        
        

        self._arch = None
        self._description = None
        self._origin = None
        self._resource_category = None
        self._service_type = None
        self._services = None
        self._swr_path = None
        self._visibility = None
        self._workspace_id = None
        self._flavor_type = None
        self._tags = None
        self._swr_instance_id = None
        self._read_me = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if description is not None:
            self.description = description
        if origin is not None:
            self.origin = origin
        if resource_category is not None:
            self.resource_category = resource_category
        if service_type is not None:
            self.service_type = service_type
        if services is not None:
            self.services = services
        self.swr_path = swr_path
        if visibility is not None:
            self.visibility = visibility
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if tags is not None:
            self.tags = tags
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id
        if read_me is not None:
            self.read_me = read_me

    @property
    def arch(self):
        r"""Gets the arch of this ImageRegRequest.

        **参数解释**：该镜像所支持处理器架构类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。  **默认取值**：X86_64。

        :return: The arch of this ImageRegRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ImageRegRequest.

        **参数解释**：该镜像所支持处理器架构类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - X86_64：x86处理器架构。 - AARCH64：ARM体系架构。  **默认取值**：X86_64。

        :param arch: The arch of this ImageRegRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def description(self):
        r"""Gets the description of this ImageRegRequest.

        **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。

        :return: The description of this ImageRegRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageRegRequest.

        **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。

        :param description: The description of this ImageRegRequest.
        :type description: str
        """
        self._description = description

    @property
    def origin(self):
        r"""Gets the origin of this ImageRegRequest.

        **参数解释**：指定镜像来源，可选项。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE: 用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。  **默认取值**：CUSTOMIZE。

        :return: The origin of this ImageRegRequest.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this ImageRegRequest.

        **参数解释**：指定镜像来源，可选项。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - CUSTOMIZE: 用户自定义构建镜像。 - IMAGE_SAVE：Notebook实例保存镜像。  **默认取值**：CUSTOMIZE。

        :param origin: The origin of this ImageRegRequest.
        :type origin: str
        """
        self._origin = origin

    @property
    def resource_category(self):
        r"""Gets the resource_category of this ImageRegRequest.

        **参数解释**：镜像支持的规格，默认值CPU、GPU。 枚举值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)。  **约束限制**：不涉及。

        :return: The resource_category of this ImageRegRequest.
        :rtype: list[str]
        """
        return self._resource_category

    @resource_category.setter
    def resource_category(self, resource_category):
        r"""Sets the resource_category of this ImageRegRequest.

        **参数解释**：镜像支持的规格，默认值CPU、GPU。 枚举值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)。  **约束限制**：不涉及。

        :param resource_category: The resource_category of this ImageRegRequest.
        :type resource_category: list[str]
        """
        self._resource_category = resource_category

    @property
    def service_type(self):
        r"""Gets the service_type of this ImageRegRequest.

        **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。

        :return: The service_type of this ImageRegRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ImageRegRequest.

        **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。

        :param service_type: The service_type of this ImageRegRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def services(self):
        r"""Gets the services of this ImageRegRequest.

        **参数解释**：镜像支持的服务，默认值NOTEBOOK、SSH。枚举值如下: - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。  **约束限制**：不涉及。

        :return: The services of this ImageRegRequest.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        r"""Sets the services of this ImageRegRequest.

        **参数解释**：镜像支持的服务，默认值NOTEBOOK、SSH。枚举值如下: - NOTEBOOK：镜像支持通过https协议访问Notebook。 - SSH：镜像支持本地IDE通过SSH协议远程连接Notebook。  **约束限制**：不涉及。

        :param services: The services of this ImageRegRequest.
        :type services: list[str]
        """
        self._services = services

    @property
    def swr_path(self):
        r"""Gets the swr_path of this ImageRegRequest.

        **参数解释**：SWR镜像地址。 **约束限制**：不涉及。 **取值范围**：长度最长为2048个字符，最短为16个字符，地址格式为：[仓库地址[:端口]]/[命名空间]/[镜像名称]:[标签]。 **默认取值**：不涉及。

        :return: The swr_path of this ImageRegRequest.
        :rtype: str
        """
        return self._swr_path

    @swr_path.setter
    def swr_path(self, swr_path):
        r"""Sets the swr_path of this ImageRegRequest.

        **参数解释**：SWR镜像地址。 **约束限制**：不涉及。 **取值范围**：长度最长为2048个字符，最短为16个字符，地址格式为：[仓库地址[:端口]]/[命名空间]/[镜像名称]:[标签]。 **默认取值**：不涉及。

        :param swr_path: The swr_path of this ImageRegRequest.
        :type swr_path: str
        """
        self._swr_path = swr_path

    @property
    def visibility(self):
        r"""Gets the visibility of this ImageRegRequest.

        **参数解释**：镜像可见度。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC: 所有用户可以根据image_id来进行只读使用。  **默认取值**：PRIVATE。

        :return: The visibility of this ImageRegRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ImageRegRequest.

        **参数解释**：镜像可见度。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - PRIVATE：私有镜像。 - PUBLIC: 所有用户可以根据image_id来进行只读使用。  **默认取值**：PRIVATE。

        :param visibility: The visibility of this ImageRegRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ImageRegRequest.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :return: The workspace_id of this ImageRegRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ImageRegRequest.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ImageRegRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this ImageRegRequest.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： -ASCEND_SNT9：昇腾910芯片。 -ASCEND_SNT9B：昇腾910B芯片。 -ASCEND_SNT3：昇腾310芯片。  **默认取值**：不涉及。

        :return: The flavor_type of this ImageRegRequest.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this ImageRegRequest.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： -ASCEND_SNT9：昇腾910芯片。 -ASCEND_SNT9B：昇腾910B芯片。 -ASCEND_SNT3：昇腾310芯片。  **默认取值**：不涉及。

        :param flavor_type: The flavor_type of this ImageRegRequest.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def tags(self):
        r"""Gets the tags of this ImageRegRequest.

        **参数解释**：该镜像所属镜像组对应的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。

        :return: The tags of this ImageRegRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ImageRegRequest.

        **参数解释**：该镜像所属镜像组对应的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。

        :param tags: The tags of this ImageRegRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this ImageRegRequest.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The swr_instance_id of this ImageRegRequest.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this ImageRegRequest.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param swr_instance_id: The swr_instance_id of this ImageRegRequest.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

    @property
    def read_me(self):
        r"""Gets the read_me of this ImageRegRequest.

        **参数解释**：镜像指导。 **参数约束**：不涉及。 **取值范围**：字符串长度限制为3000个字符。 **默认取值**：不涉及。

        :return: The read_me of this ImageRegRequest.
        :rtype: str
        """
        return self._read_me

    @read_me.setter
    def read_me(self, read_me):
        r"""Sets the read_me of this ImageRegRequest.

        **参数解释**：镜像指导。 **参数约束**：不涉及。 **取值范围**：字符串长度限制为3000个字符。 **默认取值**：不涉及。

        :param read_me: The read_me of this ImageRegRequest.
        :type read_me: str
        """
        self._read_me = read_me

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
        if not isinstance(other, ImageRegRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
