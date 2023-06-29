# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppConnectionInfo:

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
        'sid': 'str',
        'machine_name': 'str',
        'user_name': 'str',
        'app_group_name': 'str',
        'app_group_id': 'str',
        'app_name': 'str',
        'brokering_time': 'datetime',
        'failed_code': 'str',
        'connection_failure_reason': 'str',
        'client_mac': 'str',
        'client_name': 'str',
        'client_ip': 'str',
        'client_version': 'str',
        'client_type': 'str',
        'agent_version': 'str',
        'vm_ip': 'str',
        'wi_ip': 'str',
        'tenant_id': 'str',
        'virtual_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sid': 'sid',
        'machine_name': 'machine_name',
        'user_name': 'user_name',
        'app_group_name': 'app_group_name',
        'app_group_id': 'app_group_id',
        'app_name': 'app_name',
        'brokering_time': 'brokering_time',
        'failed_code': 'failed_code',
        'connection_failure_reason': 'connection_failure_reason',
        'client_mac': 'client_mac',
        'client_name': 'client_name',
        'client_ip': 'client_ip',
        'client_version': 'client_version',
        'client_type': 'client_type',
        'agent_version': 'agent_version',
        'vm_ip': 'vm_ip',
        'wi_ip': 'wi_ip',
        'tenant_id': 'tenant_id',
        'virtual_ip': 'virtual_ip'
    }

    def __init__(self, id=None, sid=None, machine_name=None, user_name=None, app_group_name=None, app_group_id=None, app_name=None, brokering_time=None, failed_code=None, connection_failure_reason=None, client_mac=None, client_name=None, client_ip=None, client_version=None, client_type=None, agent_version=None, vm_ip=None, wi_ip=None, tenant_id=None, virtual_ip=None):
        """AppConnectionInfo

        The model defined in huaweicloud sdk

        :param id: 应用连接唯一标识ID
        :type id: str
        :param sid: 应用服务器sid
        :type sid: str
        :param machine_name: 应用服务器名称
        :type machine_name: str
        :param user_name: 登录用户
        :type user_name: str
        :param app_group_name: 应用组名称
        :type app_group_name: str
        :param app_group_id: 应用组ID
        :type app_group_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param brokering_time: 登录应用时间
        :type brokering_time: datetime
        :param failed_code: 连接失败状态码
        :type failed_code: str
        :param connection_failure_reason: 连接失败原因
        :type connection_failure_reason: str
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
        :param wi_ip: 连接IP
        :type wi_ip: str
        :param tenant_id: 租户id
        :type tenant_id: str
        :param virtual_ip: 会话虚拟ip
        :type virtual_ip: str
        """
        
        

        self._id = None
        self._sid = None
        self._machine_name = None
        self._user_name = None
        self._app_group_name = None
        self._app_group_id = None
        self._app_name = None
        self._brokering_time = None
        self._failed_code = None
        self._connection_failure_reason = None
        self._client_mac = None
        self._client_name = None
        self._client_ip = None
        self._client_version = None
        self._client_type = None
        self._agent_version = None
        self._vm_ip = None
        self._wi_ip = None
        self._tenant_id = None
        self._virtual_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sid is not None:
            self.sid = sid
        if machine_name is not None:
            self.machine_name = machine_name
        if user_name is not None:
            self.user_name = user_name
        if app_group_name is not None:
            self.app_group_name = app_group_name
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if app_name is not None:
            self.app_name = app_name
        if brokering_time is not None:
            self.brokering_time = brokering_time
        if failed_code is not None:
            self.failed_code = failed_code
        if connection_failure_reason is not None:
            self.connection_failure_reason = connection_failure_reason
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
        if wi_ip is not None:
            self.wi_ip = wi_ip
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip

    @property
    def id(self):
        """Gets the id of this AppConnectionInfo.

        应用连接唯一标识ID

        :return: The id of this AppConnectionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppConnectionInfo.

        应用连接唯一标识ID

        :param id: The id of this AppConnectionInfo.
        :type id: str
        """
        self._id = id

    @property
    def sid(self):
        """Gets the sid of this AppConnectionInfo.

        应用服务器sid

        :return: The sid of this AppConnectionInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AppConnectionInfo.

        应用服务器sid

        :param sid: The sid of this AppConnectionInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def machine_name(self):
        """Gets the machine_name of this AppConnectionInfo.

        应用服务器名称

        :return: The machine_name of this AppConnectionInfo.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this AppConnectionInfo.

        应用服务器名称

        :param machine_name: The machine_name of this AppConnectionInfo.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def user_name(self):
        """Gets the user_name of this AppConnectionInfo.

        登录用户

        :return: The user_name of this AppConnectionInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AppConnectionInfo.

        登录用户

        :param user_name: The user_name of this AppConnectionInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def app_group_name(self):
        """Gets the app_group_name of this AppConnectionInfo.

        应用组名称

        :return: The app_group_name of this AppConnectionInfo.
        :rtype: str
        """
        return self._app_group_name

    @app_group_name.setter
    def app_group_name(self, app_group_name):
        """Sets the app_group_name of this AppConnectionInfo.

        应用组名称

        :param app_group_name: The app_group_name of this AppConnectionInfo.
        :type app_group_name: str
        """
        self._app_group_name = app_group_name

    @property
    def app_group_id(self):
        """Gets the app_group_id of this AppConnectionInfo.

        应用组ID

        :return: The app_group_id of this AppConnectionInfo.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this AppConnectionInfo.

        应用组ID

        :param app_group_id: The app_group_id of this AppConnectionInfo.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def app_name(self):
        """Gets the app_name of this AppConnectionInfo.

        应用名称

        :return: The app_name of this AppConnectionInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppConnectionInfo.

        应用名称

        :param app_name: The app_name of this AppConnectionInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def brokering_time(self):
        """Gets the brokering_time of this AppConnectionInfo.

        登录应用时间

        :return: The brokering_time of this AppConnectionInfo.
        :rtype: datetime
        """
        return self._brokering_time

    @brokering_time.setter
    def brokering_time(self, brokering_time):
        """Sets the brokering_time of this AppConnectionInfo.

        登录应用时间

        :param brokering_time: The brokering_time of this AppConnectionInfo.
        :type brokering_time: datetime
        """
        self._brokering_time = brokering_time

    @property
    def failed_code(self):
        """Gets the failed_code of this AppConnectionInfo.

        连接失败状态码

        :return: The failed_code of this AppConnectionInfo.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        """Sets the failed_code of this AppConnectionInfo.

        连接失败状态码

        :param failed_code: The failed_code of this AppConnectionInfo.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def connection_failure_reason(self):
        """Gets the connection_failure_reason of this AppConnectionInfo.

        连接失败原因

        :return: The connection_failure_reason of this AppConnectionInfo.
        :rtype: str
        """
        return self._connection_failure_reason

    @connection_failure_reason.setter
    def connection_failure_reason(self, connection_failure_reason):
        """Sets the connection_failure_reason of this AppConnectionInfo.

        连接失败原因

        :param connection_failure_reason: The connection_failure_reason of this AppConnectionInfo.
        :type connection_failure_reason: str
        """
        self._connection_failure_reason = connection_failure_reason

    @property
    def client_mac(self):
        """Gets the client_mac of this AppConnectionInfo.

        客户端Mac

        :return: The client_mac of this AppConnectionInfo.
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        """Sets the client_mac of this AppConnectionInfo.

        客户端Mac

        :param client_mac: The client_mac of this AppConnectionInfo.
        :type client_mac: str
        """
        self._client_mac = client_mac

    @property
    def client_name(self):
        """Gets the client_name of this AppConnectionInfo.

        客户端名称

        :return: The client_name of this AppConnectionInfo.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this AppConnectionInfo.

        客户端名称

        :param client_name: The client_name of this AppConnectionInfo.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_ip(self):
        """Gets the client_ip of this AppConnectionInfo.

        客户端ip

        :return: The client_ip of this AppConnectionInfo.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this AppConnectionInfo.

        客户端ip

        :param client_ip: The client_ip of this AppConnectionInfo.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_version(self):
        """Gets the client_version of this AppConnectionInfo.

        客户端版本

        :return: The client_version of this AppConnectionInfo.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this AppConnectionInfo.

        客户端版本

        :param client_version: The client_version of this AppConnectionInfo.
        :type client_version: str
        """
        self._client_version = client_version

    @property
    def client_type(self):
        """Gets the client_type of this AppConnectionInfo.

        客户端操作系统类型

        :return: The client_type of this AppConnectionInfo.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this AppConnectionInfo.

        客户端操作系统类型

        :param client_type: The client_type of this AppConnectionInfo.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def agent_version(self):
        """Gets the agent_version of this AppConnectionInfo.

        aps hda版本

        :return: The agent_version of this AppConnectionInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this AppConnectionInfo.

        aps hda版本

        :param agent_version: The agent_version of this AppConnectionInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def vm_ip(self):
        """Gets the vm_ip of this AppConnectionInfo.

        应用服务器ip

        :return: The vm_ip of this AppConnectionInfo.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """Sets the vm_ip of this AppConnectionInfo.

        应用服务器ip

        :param vm_ip: The vm_ip of this AppConnectionInfo.
        :type vm_ip: str
        """
        self._vm_ip = vm_ip

    @property
    def wi_ip(self):
        """Gets the wi_ip of this AppConnectionInfo.

        连接IP

        :return: The wi_ip of this AppConnectionInfo.
        :rtype: str
        """
        return self._wi_ip

    @wi_ip.setter
    def wi_ip(self, wi_ip):
        """Sets the wi_ip of this AppConnectionInfo.

        连接IP

        :param wi_ip: The wi_ip of this AppConnectionInfo.
        :type wi_ip: str
        """
        self._wi_ip = wi_ip

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AppConnectionInfo.

        租户id

        :return: The tenant_id of this AppConnectionInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AppConnectionInfo.

        租户id

        :param tenant_id: The tenant_id of this AppConnectionInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def virtual_ip(self):
        """Gets the virtual_ip of this AppConnectionInfo.

        会话虚拟ip

        :return: The virtual_ip of this AppConnectionInfo.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        """Sets the virtual_ip of this AppConnectionInfo.

        会话虚拟ip

        :param virtual_ip: The virtual_ip of this AppConnectionInfo.
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
        if not isinstance(other, AppConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
