# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostProcessResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pid': 'str',
        'host_ip': 'str',
        'path': 'str',
        'port_protocol': 'str',
        'version': 'str',
        'dependency_package': 'str',
        'cpu_use_rate': 'str'
    }

    attribute_map = {
        'pid': 'pid',
        'host_ip': 'host_ip',
        'path': 'path',
        'port_protocol': 'port_protocol',
        'version': 'version',
        'dependency_package': 'dependency_package',
        'cpu_use_rate': 'cpu_use_rate'
    }

    def __init__(self, pid=None, host_ip=None, path=None, port_protocol=None, version=None, dependency_package=None, cpu_use_rate=None):
        r"""VulHostProcessResponseInfoDataList

        The model defined in huaweicloud sdk

        :param pid: **参数解释**： 进程id **取值范围**： 字符长度0-256位 
        :type pid: str
        :param host_ip: **参数解释**： 绑定ip **取值范围**： 字符长度0-128位 
        :type host_ip: str
        :param path: **参数解释**： 自启动项的路径 **取值范围**： 字符长度0-256位 
        :type path: str
        :param port_protocol: **参数解释**： 端口/协议 **取值范围**： 字符长度0-32位 
        :type port_protocol: str
        :param version: **参数解释**： 版本 **取值范围**： 字符长度0-256位 
        :type version: str
        :param dependency_package: **参数解释**： 依赖包 **取值范围**： 字符长度0-256位 
        :type dependency_package: str
        :param cpu_use_rate: **参数解释**： cpu使用率 **取值范围**： 字符长度0-32位 
        :type cpu_use_rate: str
        """
        
        

        self._pid = None
        self._host_ip = None
        self._path = None
        self._port_protocol = None
        self._version = None
        self._dependency_package = None
        self._cpu_use_rate = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if host_ip is not None:
            self.host_ip = host_ip
        if path is not None:
            self.path = path
        if port_protocol is not None:
            self.port_protocol = port_protocol
        if version is not None:
            self.version = version
        if dependency_package is not None:
            self.dependency_package = dependency_package
        if cpu_use_rate is not None:
            self.cpu_use_rate = cpu_use_rate

    @property
    def pid(self):
        r"""Gets the pid of this VulHostProcessResponseInfoDataList.

        **参数解释**： 进程id **取值范围**： 字符长度0-256位 

        :return: The pid of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this VulHostProcessResponseInfoDataList.

        **参数解释**： 进程id **取值范围**： 字符长度0-256位 

        :param pid: The pid of this VulHostProcessResponseInfoDataList.
        :type pid: str
        """
        self._pid = pid

    @property
    def host_ip(self):
        r"""Gets the host_ip of this VulHostProcessResponseInfoDataList.

        **参数解释**： 绑定ip **取值范围**： 字符长度0-128位 

        :return: The host_ip of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this VulHostProcessResponseInfoDataList.

        **参数解释**： 绑定ip **取值范围**： 字符长度0-128位 

        :param host_ip: The host_ip of this VulHostProcessResponseInfoDataList.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def path(self):
        r"""Gets the path of this VulHostProcessResponseInfoDataList.

        **参数解释**： 自启动项的路径 **取值范围**： 字符长度0-256位 

        :return: The path of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this VulHostProcessResponseInfoDataList.

        **参数解释**： 自启动项的路径 **取值范围**： 字符长度0-256位 

        :param path: The path of this VulHostProcessResponseInfoDataList.
        :type path: str
        """
        self._path = path

    @property
    def port_protocol(self):
        r"""Gets the port_protocol of this VulHostProcessResponseInfoDataList.

        **参数解释**： 端口/协议 **取值范围**： 字符长度0-32位 

        :return: The port_protocol of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._port_protocol

    @port_protocol.setter
    def port_protocol(self, port_protocol):
        r"""Sets the port_protocol of this VulHostProcessResponseInfoDataList.

        **参数解释**： 端口/协议 **取值范围**： 字符长度0-32位 

        :param port_protocol: The port_protocol of this VulHostProcessResponseInfoDataList.
        :type port_protocol: str
        """
        self._port_protocol = port_protocol

    @property
    def version(self):
        r"""Gets the version of this VulHostProcessResponseInfoDataList.

        **参数解释**： 版本 **取值范围**： 字符长度0-256位 

        :return: The version of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VulHostProcessResponseInfoDataList.

        **参数解释**： 版本 **取值范围**： 字符长度0-256位 

        :param version: The version of this VulHostProcessResponseInfoDataList.
        :type version: str
        """
        self._version = version

    @property
    def dependency_package(self):
        r"""Gets the dependency_package of this VulHostProcessResponseInfoDataList.

        **参数解释**： 依赖包 **取值范围**： 字符长度0-256位 

        :return: The dependency_package of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._dependency_package

    @dependency_package.setter
    def dependency_package(self, dependency_package):
        r"""Sets the dependency_package of this VulHostProcessResponseInfoDataList.

        **参数解释**： 依赖包 **取值范围**： 字符长度0-256位 

        :param dependency_package: The dependency_package of this VulHostProcessResponseInfoDataList.
        :type dependency_package: str
        """
        self._dependency_package = dependency_package

    @property
    def cpu_use_rate(self):
        r"""Gets the cpu_use_rate of this VulHostProcessResponseInfoDataList.

        **参数解释**： cpu使用率 **取值范围**： 字符长度0-32位 

        :return: The cpu_use_rate of this VulHostProcessResponseInfoDataList.
        :rtype: str
        """
        return self._cpu_use_rate

    @cpu_use_rate.setter
    def cpu_use_rate(self, cpu_use_rate):
        r"""Sets the cpu_use_rate of this VulHostProcessResponseInfoDataList.

        **参数解释**： cpu使用率 **取值范围**： 字符长度0-32位 

        :param cpu_use_rate: The cpu_use_rate of this VulHostProcessResponseInfoDataList.
        :type cpu_use_rate: str
        """
        self._cpu_use_rate = cpu_use_rate

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
        if not isinstance(other, VulHostProcessResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
