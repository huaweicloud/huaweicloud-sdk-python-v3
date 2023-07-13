# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserConnectionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'connect_type': 'str',
        'user_name': 'str',
        'desktop_group_name': 'str',
        'pre_conn_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'machine_sid': 'str',
        'machine_name': 'str',
        'failed_reason': 'str',
        'failed_code': 'str',
        'client_mac': 'str',
        'client_name': 'str',
        'client_ip': 'str',
        'client_version': 'str',
        'client_type': 'str',
        'agent_version': 'str',
        'vm_ip': 'str',
        'connect_flag': 'str',
        'wi_ip': 'str',
        'update_time': 'datetime',
        'tenant_id': 'str',
        'virtual_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'connect_type': 'connect_type',
        'user_name': 'user_name',
        'desktop_group_name': 'desktop_group_name',
        'pre_conn_time': 'pre_conn_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'machine_sid': 'machine_sid',
        'machine_name': 'machine_name',
        'failed_reason': 'failed_reason',
        'failed_code': 'failed_code',
        'client_mac': 'client_mac',
        'client_name': 'client_name',
        'client_ip': 'client_ip',
        'client_version': 'client_version',
        'client_type': 'client_type',
        'agent_version': 'agent_version',
        'vm_ip': 'vm_ip',
        'connect_flag': 'connect_flag',
        'wi_ip': 'wi_ip',
        'update_time': 'update_time',
        'tenant_id': 'tenant_id',
        'virtual_ip': 'virtual_ip'
    }

    def __init__(self, id=None, connect_type=None, user_name=None, desktop_group_name=None, pre_conn_time=None, start_time=None, end_time=None, machine_sid=None, machine_name=None, failed_reason=None, failed_code=None, client_mac=None, client_name=None, client_ip=None, client_version=None, client_type=None, agent_version=None, vm_ip=None, connect_flag=None, wi_ip=None, update_time=None, tenant_id=None, virtual_ip=None):
        """UserConnectionInfo

        The model defined in huaweicloud sdk

        :param id: 主键
        :type id: str
        :param connect_type: 连接类型
        :type connect_type: str
        :param user_name: 登录用户
        :type user_name: str
        :param desktop_group_name: 桌面组名
        :type desktop_group_name: str
        :param pre_conn_time: 预连接时间
        :type pre_conn_time: datetime
        :param start_time: 开始时间
        :type start_time: datetime
        :param end_time: 结束时间
        :type end_time: datetime
        :param machine_sid: 应用服务器sid
        :type machine_sid: str
        :param machine_name: 应用服务器名称
        :type machine_name: str
        :param failed_reason: 连接失败原因
        :type failed_reason: str
        :param failed_code: 连接失败状态码
        :type failed_code: str
        :param client_mac: 客户端Mac
        :type client_mac: str
        :param client_name: 客户端名称
        :type client_name: str
        :param client_ip: 客户端ip
        :type client_ip: str
        :param client_version: 客户端版本
        :type client_version: str
        :param client_type: 客户端操作系统类型
        :type client_type: str
        :param agent_version: aps hda版本
        :type agent_version: str
        :param vm_ip: 应用服务器ip
        :type vm_ip: str
        :param connect_flag: 连接标志
        :type connect_flag: str
        :param wi_ip: 连接IP
        :type wi_ip: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param tenant_id: 租户id
        :type tenant_id: str
        :param virtual_ip: 会话虚拟ip
        :type virtual_ip: str
        """
        
        

        self._id = None
        self._connect_type = None
        self._user_name = None
        self._desktop_group_name = None
        self._pre_conn_time = None
        self._start_time = None
        self._end_time = None
        self._machine_sid = None
        self._machine_name = None
        self._failed_reason = None
        self._failed_code = None
        self._client_mac = None
        self._client_name = None
        self._client_ip = None
        self._client_version = None
        self._client_type = None
        self._agent_version = None
        self._vm_ip = None
        self._connect_flag = None
        self._wi_ip = None
        self._update_time = None
        self._tenant_id = None
        self._virtual_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if connect_type is not None:
            self.connect_type = connect_type
        if user_name is not None:
            self.user_name = user_name
        if desktop_group_name is not None:
            self.desktop_group_name = desktop_group_name
        if pre_conn_time is not None:
            self.pre_conn_time = pre_conn_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if machine_sid is not None:
            self.machine_sid = machine_sid
        if machine_name is not None:
            self.machine_name = machine_name
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_code is not None:
            self.failed_code = failed_code
        if client_mac is not None:
            self.client_mac = client_mac
        if client_name is not None:
            self.client_name = client_name
        if client_ip is not None:
            self.client_ip = client_ip
        if client_version is not None:
            self.client_version = client_version
        if client_type is not None:
            self.client_type = client_type
        if agent_version is not None:
            self.agent_version = agent_version
        if vm_ip is not None:
            self.vm_ip = vm_ip
        if connect_flag is not None:
            self.connect_flag = connect_flag
        if wi_ip is not None:
            self.wi_ip = wi_ip
        if update_time is not None:
            self.update_time = update_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip

    @property
    def id(self):
        """Gets the id of this UserConnectionInfo.

        主键

        :return: The id of this UserConnectionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserConnectionInfo.

        主键

        :param id: The id of this UserConnectionInfo.
        :type id: str
        """
        self._id = id

    @property
    def connect_type(self):
        """Gets the connect_type of this UserConnectionInfo.

        连接类型

        :return: The connect_type of this UserConnectionInfo.
        :rtype: str
        """
        return self._connect_type

    @connect_type.setter
    def connect_type(self, connect_type):
        """Sets the connect_type of this UserConnectionInfo.

        连接类型

        :param connect_type: The connect_type of this UserConnectionInfo.
        :type connect_type: str
        """
        self._connect_type = connect_type

    @property
    def user_name(self):
        """Gets the user_name of this UserConnectionInfo.

        登录用户

        :return: The user_name of this UserConnectionInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserConnectionInfo.

        登录用户

        :param user_name: The user_name of this UserConnectionInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def desktop_group_name(self):
        """Gets the desktop_group_name of this UserConnectionInfo.

        桌面组名

        :return: The desktop_group_name of this UserConnectionInfo.
        :rtype: str
        """
        return self._desktop_group_name

    @desktop_group_name.setter
    def desktop_group_name(self, desktop_group_name):
        """Sets the desktop_group_name of this UserConnectionInfo.

        桌面组名

        :param desktop_group_name: The desktop_group_name of this UserConnectionInfo.
        :type desktop_group_name: str
        """
        self._desktop_group_name = desktop_group_name

    @property
    def pre_conn_time(self):
        """Gets the pre_conn_time of this UserConnectionInfo.

        预连接时间

        :return: The pre_conn_time of this UserConnectionInfo.
        :rtype: datetime
        """
        return self._pre_conn_time

    @pre_conn_time.setter
    def pre_conn_time(self, pre_conn_time):
        """Sets the pre_conn_time of this UserConnectionInfo.

        预连接时间

        :param pre_conn_time: The pre_conn_time of this UserConnectionInfo.
        :type pre_conn_time: datetime
        """
        self._pre_conn_time = pre_conn_time

    @property
    def start_time(self):
        """Gets the start_time of this UserConnectionInfo.

        开始时间

        :return: The start_time of this UserConnectionInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UserConnectionInfo.

        开始时间

        :param start_time: The start_time of this UserConnectionInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UserConnectionInfo.

        结束时间

        :return: The end_time of this UserConnectionInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UserConnectionInfo.

        结束时间

        :param end_time: The end_time of this UserConnectionInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def machine_sid(self):
        """Gets the machine_sid of this UserConnectionInfo.

        应用服务器sid

        :return: The machine_sid of this UserConnectionInfo.
        :rtype: str
        """
        return self._machine_sid

    @machine_sid.setter
    def machine_sid(self, machine_sid):
        """Sets the machine_sid of this UserConnectionInfo.

        应用服务器sid

        :param machine_sid: The machine_sid of this UserConnectionInfo.
        :type machine_sid: str
        """
        self._machine_sid = machine_sid

    @property
    def machine_name(self):
        """Gets the machine_name of this UserConnectionInfo.

        应用服务器名称

        :return: The machine_name of this UserConnectionInfo.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this UserConnectionInfo.

        应用服务器名称

        :param machine_name: The machine_name of this UserConnectionInfo.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def failed_reason(self):
        """Gets the failed_reason of this UserConnectionInfo.

        连接失败原因

        :return: The failed_reason of this UserConnectionInfo.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this UserConnectionInfo.

        连接失败原因

        :param failed_reason: The failed_reason of this UserConnectionInfo.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_code(self):
        """Gets the failed_code of this UserConnectionInfo.

        连接失败状态码

        :return: The failed_code of this UserConnectionInfo.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        """Sets the failed_code of this UserConnectionInfo.

        连接失败状态码

        :param failed_code: The failed_code of this UserConnectionInfo.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def client_mac(self):
        """Gets the client_mac of this UserConnectionInfo.

        客户端Mac

        :return: The client_mac of this UserConnectionInfo.
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        """Sets the client_mac of this UserConnectionInfo.

        客户端Mac

        :param client_mac: The client_mac of this UserConnectionInfo.
        :type client_mac: str
        """
        self._client_mac = client_mac

    @property
    def client_name(self):
        """Gets the client_name of this UserConnectionInfo.

        客户端名称

        :return: The client_name of this UserConnectionInfo.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this UserConnectionInfo.

        客户端名称

        :param client_name: The client_name of this UserConnectionInfo.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_ip(self):
        """Gets the client_ip of this UserConnectionInfo.

        客户端ip

        :return: The client_ip of this UserConnectionInfo.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this UserConnectionInfo.

        客户端ip

        :param client_ip: The client_ip of this UserConnectionInfo.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_version(self):
        """Gets the client_version of this UserConnectionInfo.

        客户端版本

        :return: The client_version of this UserConnectionInfo.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this UserConnectionInfo.

        客户端版本

        :param client_version: The client_version of this UserConnectionInfo.
        :type client_version: str
        """
        self._client_version = client_version

    @property
    def client_type(self):
        """Gets the client_type of this UserConnectionInfo.

        客户端操作系统类型

        :return: The client_type of this UserConnectionInfo.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this UserConnectionInfo.

        客户端操作系统类型

        :param client_type: The client_type of this UserConnectionInfo.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def agent_version(self):
        """Gets the agent_version of this UserConnectionInfo.

        aps hda版本

        :return: The agent_version of this UserConnectionInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this UserConnectionInfo.

        aps hda版本

        :param agent_version: The agent_version of this UserConnectionInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def vm_ip(self):
        """Gets the vm_ip of this UserConnectionInfo.

        应用服务器ip

        :return: The vm_ip of this UserConnectionInfo.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """Sets the vm_ip of this UserConnectionInfo.

        应用服务器ip

        :param vm_ip: The vm_ip of this UserConnectionInfo.
        :type vm_ip: str
        """
        self._vm_ip = vm_ip

    @property
    def connect_flag(self):
        """Gets the connect_flag of this UserConnectionInfo.

        连接标志

        :return: The connect_flag of this UserConnectionInfo.
        :rtype: str
        """
        return self._connect_flag

    @connect_flag.setter
    def connect_flag(self, connect_flag):
        """Sets the connect_flag of this UserConnectionInfo.

        连接标志

        :param connect_flag: The connect_flag of this UserConnectionInfo.
        :type connect_flag: str
        """
        self._connect_flag = connect_flag

    @property
    def wi_ip(self):
        """Gets the wi_ip of this UserConnectionInfo.

        连接IP

        :return: The wi_ip of this UserConnectionInfo.
        :rtype: str
        """
        return self._wi_ip

    @wi_ip.setter
    def wi_ip(self, wi_ip):
        """Sets the wi_ip of this UserConnectionInfo.

        连接IP

        :param wi_ip: The wi_ip of this UserConnectionInfo.
        :type wi_ip: str
        """
        self._wi_ip = wi_ip

    @property
    def update_time(self):
        """Gets the update_time of this UserConnectionInfo.

        更新时间

        :return: The update_time of this UserConnectionInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UserConnectionInfo.

        更新时间

        :param update_time: The update_time of this UserConnectionInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserConnectionInfo.

        租户id

        :return: The tenant_id of this UserConnectionInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserConnectionInfo.

        租户id

        :param tenant_id: The tenant_id of this UserConnectionInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def virtual_ip(self):
        """Gets the virtual_ip of this UserConnectionInfo.

        会话虚拟ip

        :return: The virtual_ip of this UserConnectionInfo.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        """Sets the virtual_ip of this UserConnectionInfo.

        会话虚拟ip

        :param virtual_ip: The virtual_ip of this UserConnectionInfo.
        :type virtual_ip: str
        """
        self._virtual_ip = virtual_ip

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
        if not isinstance(other, UserConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
