# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'severity_level': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'cve_num': 'int',
        'cve_id_list': 'list[str]',
        'status': 'str',
        'repair_cmd': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'severity_level': 'severity_level',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'cve_num': 'cve_num',
        'cve_id_list': 'cve_id_list',
        'status': 'status',
        'repair_cmd': 'repair_cmd'
    }

    def __init__(self, host_id=None, severity_level=None, host_name=None, host_ip=None, cve_num=None, cve_id_list=None, status=None, repair_cmd=None):
        """VulHostInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param severity_level: 危险程度   - Critical : 高危   - High : 中危   - Medium : 中危   - Low : 低危
        :type severity_level: str
        :param host_name: 受影响资产名称
        :type host_name: str
        :param host_ip: 受影响资产ip
        :type host_ip: str
        :param cve_num: 漏洞cve数
        :type cve_num: int
        :param cve_id_list: cve列表
        :type cve_id_list: list[str]
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param repair_cmd: 修复命令行
        :type repair_cmd: str
        """
        
        

        self._host_id = None
        self._severity_level = None
        self._host_name = None
        self._host_ip = None
        self._cve_num = None
        self._cve_id_list = None
        self._status = None
        self._repair_cmd = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if severity_level is not None:
            self.severity_level = severity_level
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if cve_num is not None:
            self.cve_num = cve_num
        if cve_id_list is not None:
            self.cve_id_list = cve_id_list
        if status is not None:
            self.status = status
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd

    @property
    def host_id(self):
        """Gets the host_id of this VulHostInfo.

        主机id

        :return: The host_id of this VulHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this VulHostInfo.

        主机id

        :param host_id: The host_id of this VulHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def severity_level(self):
        """Gets the severity_level of this VulHostInfo.

        危险程度   - Critical : 高危   - High : 中危   - Medium : 中危   - Low : 低危

        :return: The severity_level of this VulHostInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        """Sets the severity_level of this VulHostInfo.

        危险程度   - Critical : 高危   - High : 中危   - Medium : 中危   - Low : 低危

        :param severity_level: The severity_level of this VulHostInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def host_name(self):
        """Gets the host_name of this VulHostInfo.

        受影响资产名称

        :return: The host_name of this VulHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this VulHostInfo.

        受影响资产名称

        :param host_name: The host_name of this VulHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this VulHostInfo.

        受影响资产ip

        :return: The host_ip of this VulHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this VulHostInfo.

        受影响资产ip

        :param host_ip: The host_ip of this VulHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def cve_num(self):
        """Gets the cve_num of this VulHostInfo.

        漏洞cve数

        :return: The cve_num of this VulHostInfo.
        :rtype: int
        """
        return self._cve_num

    @cve_num.setter
    def cve_num(self, cve_num):
        """Sets the cve_num of this VulHostInfo.

        漏洞cve数

        :param cve_num: The cve_num of this VulHostInfo.
        :type cve_num: int
        """
        self._cve_num = cve_num

    @property
    def cve_id_list(self):
        """Gets the cve_id_list of this VulHostInfo.

        cve列表

        :return: The cve_id_list of this VulHostInfo.
        :rtype: list[str]
        """
        return self._cve_id_list

    @cve_id_list.setter
    def cve_id_list(self, cve_id_list):
        """Sets the cve_id_list of this VulHostInfo.

        cve列表

        :param cve_id_list: The cve_id_list of this VulHostInfo.
        :type cve_id_list: list[str]
        """
        self._cve_id_list = cve_id_list

    @property
    def status(self):
        """Gets the status of this VulHostInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this VulHostInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VulHostInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this VulHostInfo.
        :type status: str
        """
        self._status = status

    @property
    def repair_cmd(self):
        """Gets the repair_cmd of this VulHostInfo.

        修复命令行

        :return: The repair_cmd of this VulHostInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        """Sets the repair_cmd of this VulHostInfo.

        修复命令行

        :param repair_cmd: The repair_cmd of this VulHostInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

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
        if not isinstance(other, VulHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
