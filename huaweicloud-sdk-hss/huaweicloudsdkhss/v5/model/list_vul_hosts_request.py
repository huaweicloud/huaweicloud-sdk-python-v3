# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulHostsRequest:

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
        'host_name': 'str',
        'host_ip': 'str',
        'status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'vul_id': 'vul_id',
        'type': 'type',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, vul_id=None, type=None, host_name=None, host_ip=None, status=None, limit=None, offset=None):
        """ListVulHostsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业租户ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param type: 漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞
        :type type: str
        :param host_name: 受影响资产名称
        :type host_name: str
        :param host_ip: 受影响资产ip
        :type host_ip: str
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param limit: 每页条数
        :type limit: int
        :param offset: 偏移
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._vul_id = None
        self._type = None
        self._host_name = None
        self._host_ip = None
        self._status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.vul_id = vul_id
        self.type = type
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVulHostsRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListVulHostsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVulHostsRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListVulHostsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vul_id(self):
        """Gets the vul_id of this ListVulHostsRequest.

        漏洞ID

        :return: The vul_id of this ListVulHostsRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this ListVulHostsRequest.

        漏洞ID

        :param vul_id: The vul_id of this ListVulHostsRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def type(self):
        """Gets the type of this ListVulHostsRequest.

        漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞

        :return: The type of this ListVulHostsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListVulHostsRequest.

        漏洞类型   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞

        :param type: The type of this ListVulHostsRequest.
        :type type: str
        """
        self._type = type

    @property
    def host_name(self):
        """Gets the host_name of this ListVulHostsRequest.

        受影响资产名称

        :return: The host_name of this ListVulHostsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListVulHostsRequest.

        受影响资产名称

        :param host_name: The host_name of this ListVulHostsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ListVulHostsRequest.

        受影响资产ip

        :return: The host_ip of this ListVulHostsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListVulHostsRequest.

        受影响资产ip

        :param host_ip: The host_ip of this ListVulHostsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def status(self):
        """Gets the status of this ListVulHostsRequest.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this ListVulHostsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVulHostsRequest.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this ListVulHostsRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListVulHostsRequest.

        每页条数

        :return: The limit of this ListVulHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVulHostsRequest.

        每页条数

        :param limit: The limit of this ListVulHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVulHostsRequest.

        偏移

        :return: The offset of this ListVulHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVulHostsRequest.

        偏移

        :param offset: The offset of this ListVulHostsRequest.
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
        if not isinstance(other, ListVulHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
