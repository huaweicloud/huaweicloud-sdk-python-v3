# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUrgentVulnerabilitiesRequest:

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
        'offset': 'int',
        'limit': 'int',
        'severity_level': 'str',
        'handle_status': 'str',
        'vul_name': 'str',
        'is_container': 'bool',
        'cluster_id': 'str',
        'min_scan_time': 'int',
        'max_scan_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'severity_level': 'severity_level',
        'handle_status': 'handle_status',
        'vul_name': 'vul_name',
        'is_container': 'is_container',
        'cluster_id': 'cluster_id',
        'min_scan_time': 'min_scan_time',
        'max_scan_time': 'max_scan_time'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, severity_level=None, handle_status=None, vul_name=None, is_container=None, cluster_id=None, min_scan_time=None, max_scan_time=None):
        r"""ListUrgentVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param severity_level: **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 
        :type severity_level: str
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 
        :type vul_name: str
        :param is_container: **参数解释**： 是否是容器场景 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： 不涉及 
        :type is_container: bool
        :param cluster_id: **参数解释**： 集群Id **取值范围**： 字符长度0-256位 
        :type cluster_id: str
        :param min_scan_time: **参数解释**： 扫描任务开始时间的最小值 **取值范围**： 字符长度0-9223372036854775807位 
        :type min_scan_time: int
        :param max_scan_time: **参数解释**： 扫描任务开始时间的最大值 **取值范围**： 字符长度0-9223372036854775807位 
        :type max_scan_time: int
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._severity_level = None
        self._handle_status = None
        self._vul_name = None
        self._is_container = None
        self._cluster_id = None
        self._min_scan_time = None
        self._max_scan_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if severity_level is not None:
            self.severity_level = severity_level
        if handle_status is not None:
            self.handle_status = handle_status
        if vul_name is not None:
            self.vul_name = vul_name
        if is_container is not None:
            self.is_container = is_container
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if min_scan_time is not None:
            self.min_scan_time = min_scan_time
        if max_scan_time is not None:
            self.max_scan_time = max_scan_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListUrgentVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListUrgentVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListUrgentVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListUrgentVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListUrgentVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListUrgentVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 

        :return: The severity_level of this ListUrgentVulnerabilitiesRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this ListUrgentVulnerabilitiesRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListUrgentVulnerabilitiesRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListUrgentVulnerabilitiesRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListUrgentVulnerabilitiesRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :return: The vul_name of this ListUrgentVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :param vul_name: The vul_name of this ListUrgentVulnerabilitiesRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def is_container(self):
        r"""Gets the is_container of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 是否是容器场景 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： 不涉及 

        :return: The is_container of this ListUrgentVulnerabilitiesRequest.
        :rtype: bool
        """
        return self._is_container

    @is_container.setter
    def is_container(self, is_container):
        r"""Sets the is_container of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 是否是容器场景 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： 不涉及 

        :param is_container: The is_container of this ListUrgentVulnerabilitiesRequest.
        :type is_container: bool
        """
        self._is_container = is_container

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 集群Id **取值范围**： 字符长度0-256位 

        :return: The cluster_id of this ListUrgentVulnerabilitiesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 集群Id **取值范围**： 字符长度0-256位 

        :param cluster_id: The cluster_id of this ListUrgentVulnerabilitiesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def min_scan_time(self):
        r"""Gets the min_scan_time of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 扫描任务开始时间的最小值 **取值范围**： 字符长度0-9223372036854775807位 

        :return: The min_scan_time of this ListUrgentVulnerabilitiesRequest.
        :rtype: int
        """
        return self._min_scan_time

    @min_scan_time.setter
    def min_scan_time(self, min_scan_time):
        r"""Sets the min_scan_time of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 扫描任务开始时间的最小值 **取值范围**： 字符长度0-9223372036854775807位 

        :param min_scan_time: The min_scan_time of this ListUrgentVulnerabilitiesRequest.
        :type min_scan_time: int
        """
        self._min_scan_time = min_scan_time

    @property
    def max_scan_time(self):
        r"""Gets the max_scan_time of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 扫描任务开始时间的最大值 **取值范围**： 字符长度0-9223372036854775807位 

        :return: The max_scan_time of this ListUrgentVulnerabilitiesRequest.
        :rtype: int
        """
        return self._max_scan_time

    @max_scan_time.setter
    def max_scan_time(self, max_scan_time):
        r"""Sets the max_scan_time of this ListUrgentVulnerabilitiesRequest.

        **参数解释**： 扫描任务开始时间的最大值 **取值范围**： 字符长度0-9223372036854775807位 

        :param max_scan_time: The max_scan_time of this ListUrgentVulnerabilitiesRequest.
        :type max_scan_time: int
        """
        self._max_scan_time = max_scan_time

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
        if not isinstance(other, ListUrgentVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
