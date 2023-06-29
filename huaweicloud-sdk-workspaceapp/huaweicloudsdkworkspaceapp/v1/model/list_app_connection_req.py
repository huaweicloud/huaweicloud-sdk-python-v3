# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppConnectionReq:

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
        'failed_code': 'str',
        'connection_failure_reason': 'str',
        'client_name': 'str',
        'client_version': 'str',
        'client_type': 'str',
        'agent_version': 'str',
        'vm_ip': 'str',
        'wi_ip': 'str',
        'tenant_id': 'str',
        'brokering_start_time': 'datetime',
        'brokering_end_time': 'datetime',
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
        'failed_code': 'failed_code',
        'connection_failure_reason': 'connection_failure_reason',
        'client_name': 'client_name',
        'client_version': 'client_version',
        'client_type': 'client_type',
        'agent_version': 'agent_version',
        'vm_ip': 'vm_ip',
        'wi_ip': 'wi_ip',
        'tenant_id': 'tenant_id',
        'brokering_start_time': 'brokering_start_time',
        'brokering_end_time': 'brokering_end_time',
        'virtual_ip': 'virtual_ip'
    }

    def __init__(self, id=None, sid=None, machine_name=None, user_name=None, app_group_name=None, app_group_id=None, app_name=None, failed_code=None, connection_failure_reason=None, client_name=None, client_version=None, client_type=None, agent_version=None, vm_ip=None, wi_ip=None, tenant_id=None, brokering_start_time=None, brokering_end_time=None, virtual_ip=None):
        """ListAppConnectionReq

        The model defined in huaweicloud sdk

        :param id: 主键
        :type id: str
        :param sid: 应用服务器sid
        :type sid: str
        :param machine_name: 应用服务器名称
        :type machine_name: str
        :param user_name: 登录用户，模糊查询
        :type user_name: str
        :param app_group_name: 应用组名称
        :type app_group_name: str
        :param app_group_id: 应用组id
        :type app_group_id: str
        :param app_name: 应用名称，模糊查询
        :type app_name: str
        :param failed_code: 连接失败状态码
        :type failed_code: str
        :param connection_failure_reason: 连接失败原因
        :type connection_failure_reason: str
        :param client_name: 客户端名称
        :type client_name: str
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
        :param brokering_start_time: 登录应用开始时间，格式 2022-10-31 08:07:39
        :type brokering_start_time: datetime
        :param brokering_end_time: 登录应用结束时间，格式 2022-10-31 08:07:39
        :type brokering_end_time: datetime
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
        self._failed_code = None
        self._connection_failure_reason = None
        self._client_name = None
        self._client_version = None
        self._client_type = None
        self._agent_version = None
        self._vm_ip = None
        self._wi_ip = None
        self._tenant_id = None
        self._brokering_start_time = None
        self._brokering_end_time = None
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
        if failed_code is not None:
            self.failed_code = failed_code
        if connection_failure_reason is not None:
            self.connection_failure_reason = connection_failure_reason
        if client_name is not None:
            self.client_name = client_name
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
        if brokering_start_time is not None:
            self.brokering_start_time = brokering_start_time
        if brokering_end_time is not None:
            self.brokering_end_time = brokering_end_time
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip

    @property
    def id(self):
        """Gets the id of this ListAppConnectionReq.

        主键

        :return: The id of this ListAppConnectionReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAppConnectionReq.

        主键

        :param id: The id of this ListAppConnectionReq.
        :type id: str
        """
        self._id = id

    @property
    def sid(self):
        """Gets the sid of this ListAppConnectionReq.

        应用服务器sid

        :return: The sid of this ListAppConnectionReq.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this ListAppConnectionReq.

        应用服务器sid

        :param sid: The sid of this ListAppConnectionReq.
        :type sid: str
        """
        self._sid = sid

    @property
    def machine_name(self):
        """Gets the machine_name of this ListAppConnectionReq.

        应用服务器名称

        :return: The machine_name of this ListAppConnectionReq.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this ListAppConnectionReq.

        应用服务器名称

        :param machine_name: The machine_name of this ListAppConnectionReq.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def user_name(self):
        """Gets the user_name of this ListAppConnectionReq.

        登录用户，模糊查询

        :return: The user_name of this ListAppConnectionReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListAppConnectionReq.

        登录用户，模糊查询

        :param user_name: The user_name of this ListAppConnectionReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def app_group_name(self):
        """Gets the app_group_name of this ListAppConnectionReq.

        应用组名称

        :return: The app_group_name of this ListAppConnectionReq.
        :rtype: str
        """
        return self._app_group_name

    @app_group_name.setter
    def app_group_name(self, app_group_name):
        """Sets the app_group_name of this ListAppConnectionReq.

        应用组名称

        :param app_group_name: The app_group_name of this ListAppConnectionReq.
        :type app_group_name: str
        """
        self._app_group_name = app_group_name

    @property
    def app_group_id(self):
        """Gets the app_group_id of this ListAppConnectionReq.

        应用组id

        :return: The app_group_id of this ListAppConnectionReq.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this ListAppConnectionReq.

        应用组id

        :param app_group_id: The app_group_id of this ListAppConnectionReq.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def app_name(self):
        """Gets the app_name of this ListAppConnectionReq.

        应用名称，模糊查询

        :return: The app_name of this ListAppConnectionReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAppConnectionReq.

        应用名称，模糊查询

        :param app_name: The app_name of this ListAppConnectionReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def failed_code(self):
        """Gets the failed_code of this ListAppConnectionReq.

        连接失败状态码

        :return: The failed_code of this ListAppConnectionReq.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        """Sets the failed_code of this ListAppConnectionReq.

        连接失败状态码

        :param failed_code: The failed_code of this ListAppConnectionReq.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def connection_failure_reason(self):
        """Gets the connection_failure_reason of this ListAppConnectionReq.

        连接失败原因

        :return: The connection_failure_reason of this ListAppConnectionReq.
        :rtype: str
        """
        return self._connection_failure_reason

    @connection_failure_reason.setter
    def connection_failure_reason(self, connection_failure_reason):
        """Sets the connection_failure_reason of this ListAppConnectionReq.

        连接失败原因

        :param connection_failure_reason: The connection_failure_reason of this ListAppConnectionReq.
        :type connection_failure_reason: str
        """
        self._connection_failure_reason = connection_failure_reason

    @property
    def client_name(self):
        """Gets the client_name of this ListAppConnectionReq.

        客户端名称

        :return: The client_name of this ListAppConnectionReq.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this ListAppConnectionReq.

        客户端名称

        :param client_name: The client_name of this ListAppConnectionReq.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_version(self):
        """Gets the client_version of this ListAppConnectionReq.

        客户端版本

        :return: The client_version of this ListAppConnectionReq.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this ListAppConnectionReq.

        客户端版本

        :param client_version: The client_version of this ListAppConnectionReq.
        :type client_version: str
        """
        self._client_version = client_version

    @property
    def client_type(self):
        """Gets the client_type of this ListAppConnectionReq.

        客户端操作系统类型

        :return: The client_type of this ListAppConnectionReq.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this ListAppConnectionReq.

        客户端操作系统类型

        :param client_type: The client_type of this ListAppConnectionReq.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def agent_version(self):
        """Gets the agent_version of this ListAppConnectionReq.

        aps hda版本

        :return: The agent_version of this ListAppConnectionReq.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this ListAppConnectionReq.

        aps hda版本

        :param agent_version: The agent_version of this ListAppConnectionReq.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def vm_ip(self):
        """Gets the vm_ip of this ListAppConnectionReq.

        应用服务器ip

        :return: The vm_ip of this ListAppConnectionReq.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """Sets the vm_ip of this ListAppConnectionReq.

        应用服务器ip

        :param vm_ip: The vm_ip of this ListAppConnectionReq.
        :type vm_ip: str
        """
        self._vm_ip = vm_ip

    @property
    def wi_ip(self):
        """Gets the wi_ip of this ListAppConnectionReq.

        连接IP

        :return: The wi_ip of this ListAppConnectionReq.
        :rtype: str
        """
        return self._wi_ip

    @wi_ip.setter
    def wi_ip(self, wi_ip):
        """Sets the wi_ip of this ListAppConnectionReq.

        连接IP

        :param wi_ip: The wi_ip of this ListAppConnectionReq.
        :type wi_ip: str
        """
        self._wi_ip = wi_ip

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListAppConnectionReq.

        租户id

        :return: The tenant_id of this ListAppConnectionReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListAppConnectionReq.

        租户id

        :param tenant_id: The tenant_id of this ListAppConnectionReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def brokering_start_time(self):
        """Gets the brokering_start_time of this ListAppConnectionReq.

        登录应用开始时间，格式 2022-10-31 08:07:39

        :return: The brokering_start_time of this ListAppConnectionReq.
        :rtype: datetime
        """
        return self._brokering_start_time

    @brokering_start_time.setter
    def brokering_start_time(self, brokering_start_time):
        """Sets the brokering_start_time of this ListAppConnectionReq.

        登录应用开始时间，格式 2022-10-31 08:07:39

        :param brokering_start_time: The brokering_start_time of this ListAppConnectionReq.
        :type brokering_start_time: datetime
        """
        self._brokering_start_time = brokering_start_time

    @property
    def brokering_end_time(self):
        """Gets the brokering_end_time of this ListAppConnectionReq.

        登录应用结束时间，格式 2022-10-31 08:07:39

        :return: The brokering_end_time of this ListAppConnectionReq.
        :rtype: datetime
        """
        return self._brokering_end_time

    @brokering_end_time.setter
    def brokering_end_time(self, brokering_end_time):
        """Sets the brokering_end_time of this ListAppConnectionReq.

        登录应用结束时间，格式 2022-10-31 08:07:39

        :param brokering_end_time: The brokering_end_time of this ListAppConnectionReq.
        :type brokering_end_time: datetime
        """
        self._brokering_end_time = brokering_end_time

    @property
    def virtual_ip(self):
        """Gets the virtual_ip of this ListAppConnectionReq.

        会话虚拟ip

        :return: The virtual_ip of this ListAppConnectionReq.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        """Sets the virtual_ip of this ListAppConnectionReq.

        会话虚拟ip

        :param virtual_ip: The virtual_ip of this ListAppConnectionReq.
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
        if not isinstance(other, ListAppConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
