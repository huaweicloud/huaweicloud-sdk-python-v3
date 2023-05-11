# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWtpProtectHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_name': 'str',
        'os_type': 'str',
        'protect_status': 'str',
        'agent_status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_name': 'group_name',
        'os_type': 'os_type',
        'protect_status': 'protect_status',
        'agent_status': 'agent_status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, region=None, enterprise_project_id=None, host_name=None, host_id=None, public_ip=None, private_ip=None, group_name=None, os_type=None, protect_status=None, agent_status=None, limit=None, offset=None):
        """ListWtpProtectHostRequest

        The model defined in huaweicloud sdk

        :param region: Region Id
        :type region: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 云服务器ID
        :type host_id: str
        :param public_ip: 弹性公网IP
        :type public_ip: str
        :param private_ip: 私有IP
        :type private_ip: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param os_type: 操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统
        :type os_type: str
        :param protect_status: 防护状态   - closed : 未开启   - opened : 防护中
        :type protect_status: str
        :param agent_status: 客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线
        :type agent_status: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._group_name = None
        self._os_type = None
        self._protect_status = None
        self._agent_status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_name is not None:
            self.group_name = group_name
        if os_type is not None:
            self.os_type = os_type
        if protect_status is not None:
            self.protect_status = protect_status
        if agent_status is not None:
            self.agent_status = agent_status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def region(self):
        """Gets the region of this ListWtpProtectHostRequest.

        Region Id

        :return: The region of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListWtpProtectHostRequest.

        Region Id

        :param region: The region of this ListWtpProtectHostRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListWtpProtectHostRequest.

        企业项目

        :return: The enterprise_project_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListWtpProtectHostRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListWtpProtectHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        """Gets the host_name of this ListWtpProtectHostRequest.

        服务器名称

        :return: The host_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListWtpProtectHostRequest.

        服务器名称

        :param host_name: The host_name of this ListWtpProtectHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this ListWtpProtectHostRequest.

        云服务器ID

        :return: The host_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListWtpProtectHostRequest.

        云服务器ID

        :param host_id: The host_id of this ListWtpProtectHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ListWtpProtectHostRequest.

        弹性公网IP

        :return: The public_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ListWtpProtectHostRequest.

        弹性公网IP

        :param public_ip: The public_ip of this ListWtpProtectHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this ListWtpProtectHostRequest.

        私有IP

        :return: The private_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListWtpProtectHostRequest.

        私有IP

        :param private_ip: The private_ip of this ListWtpProtectHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_name(self):
        """Gets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :return: The group_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :param group_name: The group_name of this ListWtpProtectHostRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def os_type(self):
        """Gets the os_type of this ListWtpProtectHostRequest.

        操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统

        :return: The os_type of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListWtpProtectHostRequest.

        操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统

        :param os_type: The os_type of this ListWtpProtectHostRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def protect_status(self):
        """Gets the protect_status of this ListWtpProtectHostRequest.

        防护状态   - closed : 未开启   - opened : 防护中

        :return: The protect_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListWtpProtectHostRequest.

        防护状态   - closed : 未开启   - opened : 防护中

        :param protect_status: The protect_status of this ListWtpProtectHostRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def agent_status(self):
        """Gets the agent_status of this ListWtpProtectHostRequest.

        客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :return: The agent_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ListWtpProtectHostRequest.

        客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :param agent_status: The agent_status of this ListWtpProtectHostRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def limit(self):
        """Gets the limit of this ListWtpProtectHostRequest.

        默认10

        :return: The limit of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWtpProtectHostRequest.

        默认10

        :param limit: The limit of this ListWtpProtectHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWtpProtectHostRequest.

        默认是0

        :return: The offset of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWtpProtectHostRequest.

        默认是0

        :param offset: The offset of this ListWtpProtectHostRequest.
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
        if not isinstance(other, ListWtpProtectHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
