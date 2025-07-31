# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulContainerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'container_name': 'str',
        'severity_level': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'image_org': 'str',
        'registry_type': 'str',
        'registry_name': 'str',
        'host_name': 'str',
        'status': 'str',
        'host_ip': 'str',
        'private_ip': 'str',
        'remark': 'str',
        'first_scan_time': 'int',
        'scan_time': 'int'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_name': 'container_name',
        'severity_level': 'severity_level',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'image_org': 'image_org',
        'registry_type': 'registry_type',
        'registry_name': 'registry_name',
        'host_name': 'host_name',
        'status': 'status',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'remark': 'remark',
        'first_scan_time': 'first_scan_time',
        'scan_time': 'scan_time'
    }

    def __init__(self, container_id=None, container_name=None, severity_level=None, cluster_id=None, cluster_name=None, image_id=None, image_name=None, image_version=None, image_type=None, image_org=None, registry_type=None, registry_name=None, host_name=None, status=None, host_ip=None, private_ip=None, remark=None, first_scan_time=None, scan_time=None):
        r"""VulContainerInfo

        The model defined in huaweicloud sdk

        :param container_id: 受漏洞影响的容器id
        :type container_id: str
        :param container_name: 受影响容器名称
        :type container_name: str
        :param severity_level: 危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危
        :type severity_level: str
        :param cluster_id: 受漏洞影响的容器所处集群id
        :type cluster_id: str
        :param cluster_name: 受影响容器所处集群名称
        :type cluster_name: str
        :param image_id: 受漏洞影响的容器对应镜像id
        :type image_id: str
        :param image_name: 受影响容器对应镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_type: 镜像类型
        :type image_type: str
        :param image_org: 所属组织
        :type image_org: str
        :param registry_type: 仓库类型
        :type registry_type: str
        :param registry_name: 仓库名称
        :type registry_name: str
        :param host_name: 受影响容器对应主机名称
        :type host_name: str
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param host_ip: 服务器公网ip
        :type host_ip: str
        :param private_ip: 服务器私网ip
        :type private_ip: str
        :param remark: 处置操作的描述信息
        :type remark: str
        :param first_scan_time: 首次扫描时间
        :type first_scan_time: int
        :param scan_time: 扫描时间，时间戳单位：毫秒
        :type scan_time: int
        """
        
        

        self._container_id = None
        self._container_name = None
        self._severity_level = None
        self._cluster_id = None
        self._cluster_name = None
        self._image_id = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._image_org = None
        self._registry_type = None
        self._registry_name = None
        self._host_name = None
        self._status = None
        self._host_ip = None
        self._private_ip = None
        self._remark = None
        self._first_scan_time = None
        self._scan_time = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if severity_level is not None:
            self.severity_level = severity_level
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if image_org is not None:
            self.image_org = image_org
        if registry_type is not None:
            self.registry_type = registry_type
        if registry_name is not None:
            self.registry_name = registry_name
        if host_name is not None:
            self.host_name = host_name
        if status is not None:
            self.status = status
        if host_ip is not None:
            self.host_ip = host_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if remark is not None:
            self.remark = remark
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if scan_time is not None:
            self.scan_time = scan_time

    @property
    def container_id(self):
        r"""Gets the container_id of this VulContainerInfo.

        受漏洞影响的容器id

        :return: The container_id of this VulContainerInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this VulContainerInfo.

        受漏洞影响的容器id

        :param container_id: The container_id of this VulContainerInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this VulContainerInfo.

        受影响容器名称

        :return: The container_name of this VulContainerInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this VulContainerInfo.

        受影响容器名称

        :param container_name: The container_name of this VulContainerInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulContainerInfo.

        危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危

        :return: The severity_level of this VulContainerInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulContainerInfo.

        危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危

        :param severity_level: The severity_level of this VulContainerInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VulContainerInfo.

        受漏洞影响的容器所处集群id

        :return: The cluster_id of this VulContainerInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VulContainerInfo.

        受漏洞影响的容器所处集群id

        :param cluster_id: The cluster_id of this VulContainerInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this VulContainerInfo.

        受影响容器所处集群名称

        :return: The cluster_name of this VulContainerInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this VulContainerInfo.

        受影响容器所处集群名称

        :param cluster_name: The cluster_name of this VulContainerInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def image_id(self):
        r"""Gets the image_id of this VulContainerInfo.

        受漏洞影响的容器对应镜像id

        :return: The image_id of this VulContainerInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this VulContainerInfo.

        受漏洞影响的容器对应镜像id

        :param image_id: The image_id of this VulContainerInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this VulContainerInfo.

        受影响容器对应镜像名称

        :return: The image_name of this VulContainerInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this VulContainerInfo.

        受影响容器对应镜像名称

        :param image_name: The image_name of this VulContainerInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this VulContainerInfo.

        镜像版本

        :return: The image_version of this VulContainerInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this VulContainerInfo.

        镜像版本

        :param image_version: The image_version of this VulContainerInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this VulContainerInfo.

        镜像类型

        :return: The image_type of this VulContainerInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this VulContainerInfo.

        镜像类型

        :param image_type: The image_type of this VulContainerInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_org(self):
        r"""Gets the image_org of this VulContainerInfo.

        所属组织

        :return: The image_org of this VulContainerInfo.
        :rtype: str
        """
        return self._image_org

    @image_org.setter
    def image_org(self, image_org):
        r"""Sets the image_org of this VulContainerInfo.

        所属组织

        :param image_org: The image_org of this VulContainerInfo.
        :type image_org: str
        """
        self._image_org = image_org

    @property
    def registry_type(self):
        r"""Gets the registry_type of this VulContainerInfo.

        仓库类型

        :return: The registry_type of this VulContainerInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this VulContainerInfo.

        仓库类型

        :param registry_type: The registry_type of this VulContainerInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def registry_name(self):
        r"""Gets the registry_name of this VulContainerInfo.

        仓库名称

        :return: The registry_name of this VulContainerInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this VulContainerInfo.

        仓库名称

        :param registry_name: The registry_name of this VulContainerInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def host_name(self):
        r"""Gets the host_name of this VulContainerInfo.

        受影响容器对应主机名称

        :return: The host_name of this VulContainerInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulContainerInfo.

        受影响容器对应主机名称

        :param host_name: The host_name of this VulContainerInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def status(self):
        r"""Gets the status of this VulContainerInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this VulContainerInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulContainerInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this VulContainerInfo.
        :type status: str
        """
        self._status = status

    @property
    def host_ip(self):
        r"""Gets the host_ip of this VulContainerInfo.

        服务器公网ip

        :return: The host_ip of this VulContainerInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this VulContainerInfo.

        服务器公网ip

        :param host_ip: The host_ip of this VulContainerInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulContainerInfo.

        服务器私网ip

        :return: The private_ip of this VulContainerInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulContainerInfo.

        服务器私网ip

        :param private_ip: The private_ip of this VulContainerInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def remark(self):
        r"""Gets the remark of this VulContainerInfo.

        处置操作的描述信息

        :return: The remark of this VulContainerInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this VulContainerInfo.

        处置操作的描述信息

        :param remark: The remark of this VulContainerInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this VulContainerInfo.

        首次扫描时间

        :return: The first_scan_time of this VulContainerInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this VulContainerInfo.

        首次扫描时间

        :param first_scan_time: The first_scan_time of this VulContainerInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def scan_time(self):
        r"""Gets the scan_time of this VulContainerInfo.

        扫描时间，时间戳单位：毫秒

        :return: The scan_time of this VulContainerInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this VulContainerInfo.

        扫描时间，时间戳单位：毫秒

        :param scan_time: The scan_time of this VulContainerInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

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
        if not isinstance(other, VulContainerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
