# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageRiskConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'image_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_id': 'str',
        'check_name': 'str',
        'severity': 'str',
        'standard': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'image_type': 'image_type',
        'offset': 'offset',
        'limit': 'limit',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_id': 'image_id',
        'check_name': 'check_name',
        'severity': 'severity',
        'standard': 'standard',
        'instance_id': 'instance_id'
    }

    def __init__(self, enterprise_project_id=None, image_type=None, offset=None, limit=None, namespace=None, image_name=None, image_version=None, image_id=None, check_name=None, severity=None, standard=None, instance_id=None):
        r"""ListImageRiskConfigsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param image_type: **参数解释** 用于筛选指定类型的镜像安全配置检测结果，不同类型对应不同镜像存储位置 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - private_image： 私有镜像仓库 - shared_image： 共享镜像仓库 - local_image： 本地镜像 - instance_image： 企业镜像 - registry： 仓库镜像 - local： 本地镜像，用于查询全局数据 **默认取值** 无 
        :type image_type: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param namespace: **参数解释** 镜像仓库的组织（命名空间）名称，用于筛选指定组织下的镜像检测结果，仅私有/共享镜像仓库有效 **约束限制** 仅当image_type为private_image或shared_image时有效，其他类型传参无效 **取值范围** 符合镜像仓库组织命名规范的字符串 **默认取值** 无 
        :type namespace: str
        :param image_name: **参数解释** 镜像的名称，用于精准筛选指定名称的镜像安全配置检测结果 **约束限制** 支持模糊匹配（如传入&#39;euler&#39;可匹配所有名称含&#39;euler&#39;的镜像） **取值范围** 符合镜像名称命名规范的字符串 **默认取值** 无 
        :type image_name: str
        :param image_version: **参数解释** 镜像的版本标识，用于筛选指定版本的镜像安全配置检测结果，与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 符合镜像版本命名规范的字符串、默认取值：无 
        :type image_version: str
        :param image_id: **参数解释** 镜像的唯一标识，用于精准筛选指定镜像的安全配置检测结果，优先级高于image_name+image_version **约束限制** 传入后将忽略image_name和image_version参数，直接按ID筛选 **默认取值** 无 
        :type image_id: str
        :param check_name: **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如&#39;CentOS 7&#39;、&#39;EulerOS&#39;等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 
        :type check_name: str
        :param severity: **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 
        :type severity: str
        :param standard: **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 
        :type standard: str
        :param instance_id: **参数解释** 华为云SWR（软件仓库）企业版实例的唯一标识，用于筛选指定企业仓库实例下的镜像检测结果 **约束限制** 仅当image_type为private_image且使用SWR企业版时有效，共享版/本地镜像传参无效 **取值范围** SWR企业版实例ID **默认取值** 无 
        :type instance_id: str
        """
        
        

        self._enterprise_project_id = None
        self._image_type = None
        self._offset = None
        self._limit = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_id = None
        self._check_name = None
        self._severity = None
        self._standard = None
        self._instance_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.image_type = image_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_id is not None:
            self.image_id = image_id
        if check_name is not None:
            self.check_name = check_name
        if severity is not None:
            self.severity = severity
        if standard is not None:
            self.standard = standard
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageRiskConfigsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageRiskConfigsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageRiskConfigsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageRiskConfigsRequest.

        **参数解释** 用于筛选指定类型的镜像安全配置检测结果，不同类型对应不同镜像存储位置 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - private_image： 私有镜像仓库 - shared_image： 共享镜像仓库 - local_image： 本地镜像 - instance_image： 企业镜像 - registry： 仓库镜像 - local： 本地镜像，用于查询全局数据 **默认取值** 无 

        :return: The image_type of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageRiskConfigsRequest.

        **参数解释** 用于筛选指定类型的镜像安全配置检测结果，不同类型对应不同镜像存储位置 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - private_image： 私有镜像仓库 - shared_image： 共享镜像仓库 - local_image： 本地镜像 - instance_image： 企业镜像 - registry： 仓库镜像 - local： 本地镜像，用于查询全局数据 **默认取值** 无 

        :param image_type: The image_type of this ListImageRiskConfigsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def offset(self):
        r"""Gets the offset of this ListImageRiskConfigsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageRiskConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageRiskConfigsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageRiskConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageRiskConfigsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageRiskConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageRiskConfigsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageRiskConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageRiskConfigsRequest.

        **参数解释** 镜像仓库的组织（命名空间）名称，用于筛选指定组织下的镜像检测结果，仅私有/共享镜像仓库有效 **约束限制** 仅当image_type为private_image或shared_image时有效，其他类型传参无效 **取值范围** 符合镜像仓库组织命名规范的字符串 **默认取值** 无 

        :return: The namespace of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageRiskConfigsRequest.

        **参数解释** 镜像仓库的组织（命名空间）名称，用于筛选指定组织下的镜像检测结果，仅私有/共享镜像仓库有效 **约束限制** 仅当image_type为private_image或shared_image时有效，其他类型传参无效 **取值范围** 符合镜像仓库组织命名规范的字符串 **默认取值** 无 

        :param namespace: The namespace of this ListImageRiskConfigsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的名称，用于精准筛选指定名称的镜像安全配置检测结果 **约束限制** 支持模糊匹配（如传入'euler'可匹配所有名称含'euler'的镜像） **取值范围** 符合镜像名称命名规范的字符串 **默认取值** 无 

        :return: The image_name of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的名称，用于精准筛选指定名称的镜像安全配置检测结果 **约束限制** 支持模糊匹配（如传入'euler'可匹配所有名称含'euler'的镜像） **取值范围** 符合镜像名称命名规范的字符串 **默认取值** 无 

        :param image_name: The image_name of this ListImageRiskConfigsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的版本标识，用于筛选指定版本的镜像安全配置检测结果，与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 符合镜像版本命名规范的字符串、默认取值：无 

        :return: The image_version of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的版本标识，用于筛选指定版本的镜像安全配置检测结果，与image_name配合使用 **约束限制** 仅当指定image_name时传参有效，否则筛选条件不生效 **取值范围** 符合镜像版本命名规范的字符串、默认取值：无 

        :param image_version: The image_version of this ListImageRiskConfigsRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的唯一标识，用于精准筛选指定镜像的安全配置检测结果，优先级高于image_name+image_version **约束限制** 传入后将忽略image_name和image_version参数，直接按ID筛选 **默认取值** 无 

        :return: The image_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageRiskConfigsRequest.

        **参数解释** 镜像的唯一标识，用于精准筛选指定镜像的安全配置检测结果，优先级高于image_name+image_version **约束限制** 传入后将忽略image_name和image_version参数，直接按ID筛选 **默认取值** 无 

        :param image_id: The image_id of this ListImageRiskConfigsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ListImageRiskConfigsRequest.

        **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如'CentOS 7'、'EulerOS'等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 

        :return: The check_name of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListImageRiskConfigsRequest.

        **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如'CentOS 7'、'EulerOS'等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 

        :param check_name: The check_name of this ListImageRiskConfigsRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def severity(self):
        r"""Gets the severity of this ListImageRiskConfigsRequest.

        **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 

        :return: The severity of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListImageRiskConfigsRequest.

        **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 

        :param severity: The severity of this ListImageRiskConfigsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def standard(self):
        r"""Gets the standard of this ListImageRiskConfigsRequest.

        **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 

        :return: The standard of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListImageRiskConfigsRequest.

        **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 

        :param standard: The standard of this ListImageRiskConfigsRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListImageRiskConfigsRequest.

        **参数解释** 华为云SWR（软件仓库）企业版实例的唯一标识，用于筛选指定企业仓库实例下的镜像检测结果 **约束限制** 仅当image_type为private_image且使用SWR企业版时有效，共享版/本地镜像传参无效 **取值范围** SWR企业版实例ID **默认取值** 无 

        :return: The instance_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListImageRiskConfigsRequest.

        **参数解释** 华为云SWR（软件仓库）企业版实例的唯一标识，用于筛选指定企业仓库实例下的镜像检测结果 **约束限制** 仅当image_type为private_image且使用SWR企业版时有效，共享版/本地镜像传参无效 **取值范围** SWR企业版实例ID **默认取值** 无 

        :param instance_id: The instance_id of this ListImageRiskConfigsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListImageRiskConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
