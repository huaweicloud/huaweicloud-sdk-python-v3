# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulContainersRequest:

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
        'vul_id': 'str',
        'type': 'str',
        'container_name': 'str',
        'cluster_id': 'str',
        'status': 'str',
        'handle_status': 'str',
        'severity_level': 'str',
        'min_scan_time': 'int',
        'max_scan_time': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'vul_id': 'vul_id',
        'type': 'type',
        'container_name': 'container_name',
        'cluster_id': 'cluster_id',
        'status': 'status',
        'handle_status': 'handle_status',
        'severity_level': 'severity_level',
        'min_scan_time': 'min_scan_time',
        'max_scan_time': 'max_scan_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, vul_id=None, type=None, container_name=None, cluster_id=None, status=None, handle_status=None, severity_level=None, min_scan_time=None, max_scan_time=None, limit=None, offset=None):
        r"""ListVulContainersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param type: 漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞
        :type type: str
        :param container_name: 受影响容器名称
        :type container_name: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param severity_level: 危险程度 ，Critical，High，Medium，Low
        :type severity_level: str
        :param min_scan_time: 首次扫描时间最小值
        :type min_scan_time: int
        :param max_scan_time: 首次扫描时间最大值
        :type max_scan_time: int
        :param limit: 每页条数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._vul_id = None
        self._type = None
        self._container_name = None
        self._cluster_id = None
        self._status = None
        self._handle_status = None
        self._severity_level = None
        self._min_scan_time = None
        self._max_scan_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.vul_id = vul_id
        self.type = type
        if container_name is not None:
            self.container_name = container_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status
        if handle_status is not None:
            self.handle_status = handle_status
        if severity_level is not None:
            self.severity_level = severity_level
        if min_scan_time is not None:
            self.min_scan_time = min_scan_time
        if max_scan_time is not None:
            self.max_scan_time = max_scan_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulContainersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulContainersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulContainersRequest.

        漏洞ID

        :return: The vul_id of this ListVulContainersRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulContainersRequest.

        漏洞ID

        :param vul_id: The vul_id of this ListVulContainersRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def type(self):
        r"""Gets the type of this ListVulContainersRequest.

        漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :return: The type of this ListVulContainersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListVulContainersRequest.

        漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :param type: The type of this ListVulContainersRequest.
        :type type: str
        """
        self._type = type

    @property
    def container_name(self):
        r"""Gets the container_name of this ListVulContainersRequest.

        受影响容器名称

        :return: The container_name of this ListVulContainersRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListVulContainersRequest.

        受影响容器名称

        :param container_name: The container_name of this ListVulContainersRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListVulContainersRequest.

        集群ID

        :return: The cluster_id of this ListVulContainersRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListVulContainersRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListVulContainersRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def status(self):
        r"""Gets the status of this ListVulContainersRequest.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this ListVulContainersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulContainersRequest.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this ListVulContainersRequest.
        :type status: str
        """
        self._status = status

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListVulContainersRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListVulContainersRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListVulContainersRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListVulContainersRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListVulContainersRequest.

        危险程度 ，Critical，High，Medium，Low

        :return: The severity_level of this ListVulContainersRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListVulContainersRequest.

        危险程度 ，Critical，High，Medium，Low

        :param severity_level: The severity_level of this ListVulContainersRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def min_scan_time(self):
        r"""Gets the min_scan_time of this ListVulContainersRequest.

        首次扫描时间最小值

        :return: The min_scan_time of this ListVulContainersRequest.
        :rtype: int
        """
        return self._min_scan_time

    @min_scan_time.setter
    def min_scan_time(self, min_scan_time):
        r"""Sets the min_scan_time of this ListVulContainersRequest.

        首次扫描时间最小值

        :param min_scan_time: The min_scan_time of this ListVulContainersRequest.
        :type min_scan_time: int
        """
        self._min_scan_time = min_scan_time

    @property
    def max_scan_time(self):
        r"""Gets the max_scan_time of this ListVulContainersRequest.

        首次扫描时间最大值

        :return: The max_scan_time of this ListVulContainersRequest.
        :rtype: int
        """
        return self._max_scan_time

    @max_scan_time.setter
    def max_scan_time(self, max_scan_time):
        r"""Sets the max_scan_time of this ListVulContainersRequest.

        首次扫描时间最大值

        :param max_scan_time: The max_scan_time of this ListVulContainersRequest.
        :type max_scan_time: int
        """
        self._max_scan_time = max_scan_time

    @property
    def limit(self):
        r"""Gets the limit of this ListVulContainersRequest.

        每页条数

        :return: The limit of this ListVulContainersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulContainersRequest.

        每页条数

        :param limit: The limit of this ListVulContainersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulContainersRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListVulContainersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulContainersRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListVulContainersRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVulContainersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
