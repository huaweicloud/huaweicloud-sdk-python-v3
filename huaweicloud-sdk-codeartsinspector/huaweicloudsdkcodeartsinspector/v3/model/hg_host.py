# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HGHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_status': 'int',
        'group_id': 'str',
        'id': 'str',
        'ip': 'str',
        'jumper_server_id': 'str',
        'last_scan_id': 'str',
        'last_scan_info': 'ScanInfoDetail',
        'name': 'str',
        'os_type': 'str',
        'smb_credential_id': 'str',
        'ssh_credential_id': 'str'
    }

    attribute_map = {
        'auth_status': 'auth_status',
        'group_id': 'group_id',
        'id': 'id',
        'ip': 'ip',
        'jumper_server_id': 'jumper_server_id',
        'last_scan_id': 'last_scan_id',
        'last_scan_info': 'last_scan_info',
        'name': 'name',
        'os_type': 'os_type',
        'smb_credential_id': 'smb_credential_id',
        'ssh_credential_id': 'ssh_credential_id'
    }

    def __init__(self, auth_status=None, group_id=None, id=None, ip=None, jumper_server_id=None, last_scan_id=None, last_scan_info=None, name=None, os_type=None, smb_credential_id=None, ssh_credential_id=None):
        """HGHost

        The model defined in huaweicloud sdk

        :param auth_status: 主机授权状态: * -1 未知 * 0 连接成功 * 1 不可达 * 2 登录失败 
        :type auth_status: int
        :param group_id: 主机组id
        :type group_id: str
        :param id: 主机id
        :type id: str
        :param ip: 主机ip
        :type ip: str
        :param jumper_server_id: 跳板机id
        :type jumper_server_id: str
        :param last_scan_id: 最后一次扫描的id
        :type last_scan_id: str
        :param last_scan_info: 
        :type last_scan_info: :class:`huaweicloudsdkcodeartsinspector.v3.ScanInfoDetail`
        :param name: 主机名
        :type name: str
        :param os_type: 主机操作系统类型
        :type os_type: str
        :param smb_credential_id: smb_credential_id
        :type smb_credential_id: str
        :param ssh_credential_id: ssh授权id
        :type ssh_credential_id: str
        """
        
        

        self._auth_status = None
        self._group_id = None
        self._id = None
        self._ip = None
        self._jumper_server_id = None
        self._last_scan_id = None
        self._last_scan_info = None
        self._name = None
        self._os_type = None
        self._smb_credential_id = None
        self._ssh_credential_id = None
        self.discriminator = None

        if auth_status is not None:
            self.auth_status = auth_status
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if jumper_server_id is not None:
            self.jumper_server_id = jumper_server_id
        if last_scan_id is not None:
            self.last_scan_id = last_scan_id
        if last_scan_info is not None:
            self.last_scan_info = last_scan_info
        if name is not None:
            self.name = name
        if os_type is not None:
            self.os_type = os_type
        if smb_credential_id is not None:
            self.smb_credential_id = smb_credential_id
        if ssh_credential_id is not None:
            self.ssh_credential_id = ssh_credential_id

    @property
    def auth_status(self):
        """Gets the auth_status of this HGHost.

        主机授权状态: * -1 未知 * 0 连接成功 * 1 不可达 * 2 登录失败 

        :return: The auth_status of this HGHost.
        :rtype: int
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        """Sets the auth_status of this HGHost.

        主机授权状态: * -1 未知 * 0 连接成功 * 1 不可达 * 2 登录失败 

        :param auth_status: The auth_status of this HGHost.
        :type auth_status: int
        """
        self._auth_status = auth_status

    @property
    def group_id(self):
        """Gets the group_id of this HGHost.

        主机组id

        :return: The group_id of this HGHost.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this HGHost.

        主机组id

        :param group_id: The group_id of this HGHost.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this HGHost.

        主机id

        :return: The id of this HGHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HGHost.

        主机id

        :param id: The id of this HGHost.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this HGHost.

        主机ip

        :return: The ip of this HGHost.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HGHost.

        主机ip

        :param ip: The ip of this HGHost.
        :type ip: str
        """
        self._ip = ip

    @property
    def jumper_server_id(self):
        """Gets the jumper_server_id of this HGHost.

        跳板机id

        :return: The jumper_server_id of this HGHost.
        :rtype: str
        """
        return self._jumper_server_id

    @jumper_server_id.setter
    def jumper_server_id(self, jumper_server_id):
        """Sets the jumper_server_id of this HGHost.

        跳板机id

        :param jumper_server_id: The jumper_server_id of this HGHost.
        :type jumper_server_id: str
        """
        self._jumper_server_id = jumper_server_id

    @property
    def last_scan_id(self):
        """Gets the last_scan_id of this HGHost.

        最后一次扫描的id

        :return: The last_scan_id of this HGHost.
        :rtype: str
        """
        return self._last_scan_id

    @last_scan_id.setter
    def last_scan_id(self, last_scan_id):
        """Sets the last_scan_id of this HGHost.

        最后一次扫描的id

        :param last_scan_id: The last_scan_id of this HGHost.
        :type last_scan_id: str
        """
        self._last_scan_id = last_scan_id

    @property
    def last_scan_info(self):
        """Gets the last_scan_info of this HGHost.

        :return: The last_scan_info of this HGHost.
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ScanInfoDetail`
        """
        return self._last_scan_info

    @last_scan_info.setter
    def last_scan_info(self, last_scan_info):
        """Sets the last_scan_info of this HGHost.

        :param last_scan_info: The last_scan_info of this HGHost.
        :type last_scan_info: :class:`huaweicloudsdkcodeartsinspector.v3.ScanInfoDetail`
        """
        self._last_scan_info = last_scan_info

    @property
    def name(self):
        """Gets the name of this HGHost.

        主机名

        :return: The name of this HGHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HGHost.

        主机名

        :param name: The name of this HGHost.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this HGHost.

        主机操作系统类型

        :return: The os_type of this HGHost.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this HGHost.

        主机操作系统类型

        :param os_type: The os_type of this HGHost.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def smb_credential_id(self):
        """Gets the smb_credential_id of this HGHost.

        smb_credential_id

        :return: The smb_credential_id of this HGHost.
        :rtype: str
        """
        return self._smb_credential_id

    @smb_credential_id.setter
    def smb_credential_id(self, smb_credential_id):
        """Sets the smb_credential_id of this HGHost.

        smb_credential_id

        :param smb_credential_id: The smb_credential_id of this HGHost.
        :type smb_credential_id: str
        """
        self._smb_credential_id = smb_credential_id

    @property
    def ssh_credential_id(self):
        """Gets the ssh_credential_id of this HGHost.

        ssh授权id

        :return: The ssh_credential_id of this HGHost.
        :rtype: str
        """
        return self._ssh_credential_id

    @ssh_credential_id.setter
    def ssh_credential_id(self, ssh_credential_id):
        """Sets the ssh_credential_id of this HGHost.

        ssh授权id

        :param ssh_credential_id: The ssh_credential_id of this HGHost.
        :type ssh_credential_id: str
        """
        self._ssh_credential_id = ssh_credential_id

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
        if not isinstance(other, HGHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
