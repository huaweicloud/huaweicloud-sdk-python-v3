# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'name': 'str',
        'os_type': 'str',
        'group_id': 'str',
        'ssh_credential_id': 'str',
        'jumper_server_id': 'str',
        'smb_credential_id': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'name': 'name',
        'os_type': 'os_type',
        'group_id': 'group_id',
        'ssh_credential_id': 'ssh_credential_id',
        'jumper_server_id': 'jumper_server_id',
        'smb_credential_id': 'smb_credential_id'
    }

    def __init__(self, ip=None, name=None, os_type=None, group_id=None, ssh_credential_id=None, jumper_server_id=None, smb_credential_id=None):
        """HostItem

        The model defined in huaweicloud sdk

        :param ip: 主机IP
        :type ip: str
        :param name: 主机名称
        :type name: str
        :param os_type: 操作系统类型: * linux * windows 
        :type os_type: str
        :param group_id: 主机组id
        :type group_id: str
        :param ssh_credential_id: linux主机ssh授权登录信息ID
        :type ssh_credential_id: str
        :param jumper_server_id: linux跳板机信息ID
        :type jumper_server_id: str
        :param smb_credential_id: windows主机smb授权登录信息ID
        :type smb_credential_id: str
        """
        
        

        self._ip = None
        self._name = None
        self._os_type = None
        self._group_id = None
        self._ssh_credential_id = None
        self._jumper_server_id = None
        self._smb_credential_id = None
        self.discriminator = None

        self.ip = ip
        self.name = name
        self.os_type = os_type
        if group_id is not None:
            self.group_id = group_id
        if ssh_credential_id is not None:
            self.ssh_credential_id = ssh_credential_id
        if jumper_server_id is not None:
            self.jumper_server_id = jumper_server_id
        if smb_credential_id is not None:
            self.smb_credential_id = smb_credential_id

    @property
    def ip(self):
        """Gets the ip of this HostItem.

        主机IP

        :return: The ip of this HostItem.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HostItem.

        主机IP

        :param ip: The ip of this HostItem.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this HostItem.

        主机名称

        :return: The name of this HostItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostItem.

        主机名称

        :param name: The name of this HostItem.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this HostItem.

        操作系统类型: * linux * windows 

        :return: The os_type of this HostItem.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this HostItem.

        操作系统类型: * linux * windows 

        :param os_type: The os_type of this HostItem.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def group_id(self):
        """Gets the group_id of this HostItem.

        主机组id

        :return: The group_id of this HostItem.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this HostItem.

        主机组id

        :param group_id: The group_id of this HostItem.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def ssh_credential_id(self):
        """Gets the ssh_credential_id of this HostItem.

        linux主机ssh授权登录信息ID

        :return: The ssh_credential_id of this HostItem.
        :rtype: str
        """
        return self._ssh_credential_id

    @ssh_credential_id.setter
    def ssh_credential_id(self, ssh_credential_id):
        """Sets the ssh_credential_id of this HostItem.

        linux主机ssh授权登录信息ID

        :param ssh_credential_id: The ssh_credential_id of this HostItem.
        :type ssh_credential_id: str
        """
        self._ssh_credential_id = ssh_credential_id

    @property
    def jumper_server_id(self):
        """Gets the jumper_server_id of this HostItem.

        linux跳板机信息ID

        :return: The jumper_server_id of this HostItem.
        :rtype: str
        """
        return self._jumper_server_id

    @jumper_server_id.setter
    def jumper_server_id(self, jumper_server_id):
        """Sets the jumper_server_id of this HostItem.

        linux跳板机信息ID

        :param jumper_server_id: The jumper_server_id of this HostItem.
        :type jumper_server_id: str
        """
        self._jumper_server_id = jumper_server_id

    @property
    def smb_credential_id(self):
        """Gets the smb_credential_id of this HostItem.

        windows主机smb授权登录信息ID

        :return: The smb_credential_id of this HostItem.
        :rtype: str
        """
        return self._smb_credential_id

    @smb_credential_id.setter
    def smb_credential_id(self, smb_credential_id):
        """Sets the smb_credential_id of this HostItem.

        windows主机smb授权登录信息ID

        :param smb_credential_id: The smb_credential_id of this HostItem.
        :type smb_credential_id: str
        """
        self._smb_credential_id = smb_credential_id

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
        if not isinstance(other, HostItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
