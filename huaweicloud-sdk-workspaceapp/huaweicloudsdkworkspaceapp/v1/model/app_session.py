# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppSession:

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
        'session_stamp': 'str',
        'os_session_id': 'str',
        'protocol_type': 'str',
        'login_user': 'str',
        'session_type': 'str',
        'app_group_id': 'str',
        'app_server_group_id': 'str',
        'pre_conn_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status_continue_time': 'str',
        'machine_sid': 'str',
        'machine_name': 'str',
        'session_state': 'str',
        'app_name': 'str',
        'client_mac': 'str',
        'client_name': 'str',
        'client_ip': 'str',
        'client_version': 'str',
        'client_type': 'str',
        'agent_version': 'str',
        'vm_ip': 'str',
        'failed_reason': 'str',
        'failed_code': 'str',
        'last_update_status_time': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'session_stamp': 'session_stamp',
        'os_session_id': 'os_session_id',
        'protocol_type': 'protocol_type',
        'login_user': 'login_user',
        'session_type': 'session_type',
        'app_group_id': 'app_group_id',
        'app_server_group_id': 'app_server_group_id',
        'pre_conn_time': 'pre_conn_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status_continue_time': 'status_continue_time',
        'machine_sid': 'machine_sid',
        'machine_name': 'machine_name',
        'session_state': 'session_state',
        'app_name': 'app_name',
        'client_mac': 'client_mac',
        'client_name': 'client_name',
        'client_ip': 'client_ip',
        'client_version': 'client_version',
        'client_type': 'client_type',
        'agent_version': 'agent_version',
        'vm_ip': 'vm_ip',
        'failed_reason': 'failed_reason',
        'failed_code': 'failed_code',
        'last_update_status_time': 'last_update_status_time',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, id=None, session_stamp=None, os_session_id=None, protocol_type=None, login_user=None, session_type=None, app_group_id=None, app_server_group_id=None, pre_conn_time=None, start_time=None, end_time=None, status_continue_time=None, machine_sid=None, machine_name=None, session_state=None, app_name=None, client_mac=None, client_name=None, client_ip=None, client_version=None, client_type=None, agent_version=None, vm_ip=None, failed_reason=None, failed_code=None, last_update_status_time=None, tenant_id=None):
        """AppSession

        The model defined in huaweicloud sdk

        :param id: 主键ID
        :type id: str
        :param session_stamp: 会话标识
        :type session_stamp: str
        :param os_session_id: 会话在hda的os中会话id
        :type os_session_id: str
        :param protocol_type: 协议类型
        :type protocol_type: str
        :param login_user: 当前会话的登录用户
        :type login_user: str
        :param session_type: 会话类型，1表示共享桌面，2表示应用
        :type session_type: str
        :param app_group_id: App组ID
        :type app_group_id: str
        :param app_server_group_id: AppServer组ID
        :type app_server_group_id: str
        :param pre_conn_time: 预连接时间
        :type pre_conn_time: str
        :param start_time: 会话开始时间
        :type start_time: str
        :param end_time: 会话结束时间
        :type end_time: str
        :param status_continue_time: 状态持续时间
        :type status_continue_time: str
        :param machine_sid: 服务器SID
        :type machine_sid: str
        :param machine_name: 服务器名称
        :type machine_name: str
        :param session_state: 会话状态
        :type session_state: str
        :param app_name: 会话中的应用名称
        :type app_name: str
        :param client_mac: 客户端Mac地址
        :type client_mac: str
        :param client_name: 客户端名称
        :type client_name: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param client_version: 客户端版本
        :type client_version: str
        :param client_type: 客户端类型
        :type client_type: str
        :param agent_version: agent版本
        :type agent_version: str
        :param vm_ip: 服务器IP
        :type vm_ip: str
        :param failed_reason: 错误原因消息
        :type failed_reason: str
        :param failed_code: 错误原因码
        :type failed_code: str
        :param last_update_status_time: 状态最后变化时间
        :type last_update_status_time: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        """
        
        

        self._id = None
        self._session_stamp = None
        self._os_session_id = None
        self._protocol_type = None
        self._login_user = None
        self._session_type = None
        self._app_group_id = None
        self._app_server_group_id = None
        self._pre_conn_time = None
        self._start_time = None
        self._end_time = None
        self._status_continue_time = None
        self._machine_sid = None
        self._machine_name = None
        self._session_state = None
        self._app_name = None
        self._client_mac = None
        self._client_name = None
        self._client_ip = None
        self._client_version = None
        self._client_type = None
        self._agent_version = None
        self._vm_ip = None
        self._failed_reason = None
        self._failed_code = None
        self._last_update_status_time = None
        self._tenant_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if session_stamp is not None:
            self.session_stamp = session_stamp
        if os_session_id is not None:
            self.os_session_id = os_session_id
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if login_user is not None:
            self.login_user = login_user
        if session_type is not None:
            self.session_type = session_type
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if app_server_group_id is not None:
            self.app_server_group_id = app_server_group_id
        if pre_conn_time is not None:
            self.pre_conn_time = pre_conn_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status_continue_time is not None:
            self.status_continue_time = status_continue_time
        if machine_sid is not None:
            self.machine_sid = machine_sid
        if machine_name is not None:
            self.machine_name = machine_name
        if session_state is not None:
            self.session_state = session_state
        if app_name is not None:
            self.app_name = app_name
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
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_code is not None:
            self.failed_code = failed_code
        if last_update_status_time is not None:
            self.last_update_status_time = last_update_status_time
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this AppSession.

        主键ID

        :return: The id of this AppSession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppSession.

        主键ID

        :param id: The id of this AppSession.
        :type id: str
        """
        self._id = id

    @property
    def session_stamp(self):
        """Gets the session_stamp of this AppSession.

        会话标识

        :return: The session_stamp of this AppSession.
        :rtype: str
        """
        return self._session_stamp

    @session_stamp.setter
    def session_stamp(self, session_stamp):
        """Sets the session_stamp of this AppSession.

        会话标识

        :param session_stamp: The session_stamp of this AppSession.
        :type session_stamp: str
        """
        self._session_stamp = session_stamp

    @property
    def os_session_id(self):
        """Gets the os_session_id of this AppSession.

        会话在hda的os中会话id

        :return: The os_session_id of this AppSession.
        :rtype: str
        """
        return self._os_session_id

    @os_session_id.setter
    def os_session_id(self, os_session_id):
        """Sets the os_session_id of this AppSession.

        会话在hda的os中会话id

        :param os_session_id: The os_session_id of this AppSession.
        :type os_session_id: str
        """
        self._os_session_id = os_session_id

    @property
    def protocol_type(self):
        """Gets the protocol_type of this AppSession.

        协议类型

        :return: The protocol_type of this AppSession.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this AppSession.

        协议类型

        :param protocol_type: The protocol_type of this AppSession.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def login_user(self):
        """Gets the login_user of this AppSession.

        当前会话的登录用户

        :return: The login_user of this AppSession.
        :rtype: str
        """
        return self._login_user

    @login_user.setter
    def login_user(self, login_user):
        """Sets the login_user of this AppSession.

        当前会话的登录用户

        :param login_user: The login_user of this AppSession.
        :type login_user: str
        """
        self._login_user = login_user

    @property
    def session_type(self):
        """Gets the session_type of this AppSession.

        会话类型，1表示共享桌面，2表示应用

        :return: The session_type of this AppSession.
        :rtype: str
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """Sets the session_type of this AppSession.

        会话类型，1表示共享桌面，2表示应用

        :param session_type: The session_type of this AppSession.
        :type session_type: str
        """
        self._session_type = session_type

    @property
    def app_group_id(self):
        """Gets the app_group_id of this AppSession.

        App组ID

        :return: The app_group_id of this AppSession.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this AppSession.

        App组ID

        :param app_group_id: The app_group_id of this AppSession.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def app_server_group_id(self):
        """Gets the app_server_group_id of this AppSession.

        AppServer组ID

        :return: The app_server_group_id of this AppSession.
        :rtype: str
        """
        return self._app_server_group_id

    @app_server_group_id.setter
    def app_server_group_id(self, app_server_group_id):
        """Sets the app_server_group_id of this AppSession.

        AppServer组ID

        :param app_server_group_id: The app_server_group_id of this AppSession.
        :type app_server_group_id: str
        """
        self._app_server_group_id = app_server_group_id

    @property
    def pre_conn_time(self):
        """Gets the pre_conn_time of this AppSession.

        预连接时间

        :return: The pre_conn_time of this AppSession.
        :rtype: str
        """
        return self._pre_conn_time

    @pre_conn_time.setter
    def pre_conn_time(self, pre_conn_time):
        """Sets the pre_conn_time of this AppSession.

        预连接时间

        :param pre_conn_time: The pre_conn_time of this AppSession.
        :type pre_conn_time: str
        """
        self._pre_conn_time = pre_conn_time

    @property
    def start_time(self):
        """Gets the start_time of this AppSession.

        会话开始时间

        :return: The start_time of this AppSession.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AppSession.

        会话开始时间

        :param start_time: The start_time of this AppSession.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AppSession.

        会话结束时间

        :return: The end_time of this AppSession.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AppSession.

        会话结束时间

        :param end_time: The end_time of this AppSession.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status_continue_time(self):
        """Gets the status_continue_time of this AppSession.

        状态持续时间

        :return: The status_continue_time of this AppSession.
        :rtype: str
        """
        return self._status_continue_time

    @status_continue_time.setter
    def status_continue_time(self, status_continue_time):
        """Sets the status_continue_time of this AppSession.

        状态持续时间

        :param status_continue_time: The status_continue_time of this AppSession.
        :type status_continue_time: str
        """
        self._status_continue_time = status_continue_time

    @property
    def machine_sid(self):
        """Gets the machine_sid of this AppSession.

        服务器SID

        :return: The machine_sid of this AppSession.
        :rtype: str
        """
        return self._machine_sid

    @machine_sid.setter
    def machine_sid(self, machine_sid):
        """Sets the machine_sid of this AppSession.

        服务器SID

        :param machine_sid: The machine_sid of this AppSession.
        :type machine_sid: str
        """
        self._machine_sid = machine_sid

    @property
    def machine_name(self):
        """Gets the machine_name of this AppSession.

        服务器名称

        :return: The machine_name of this AppSession.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this AppSession.

        服务器名称

        :param machine_name: The machine_name of this AppSession.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def session_state(self):
        """Gets the session_state of this AppSession.

        会话状态

        :return: The session_state of this AppSession.
        :rtype: str
        """
        return self._session_state

    @session_state.setter
    def session_state(self, session_state):
        """Sets the session_state of this AppSession.

        会话状态

        :param session_state: The session_state of this AppSession.
        :type session_state: str
        """
        self._session_state = session_state

    @property
    def app_name(self):
        """Gets the app_name of this AppSession.

        会话中的应用名称

        :return: The app_name of this AppSession.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppSession.

        会话中的应用名称

        :param app_name: The app_name of this AppSession.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def client_mac(self):
        """Gets the client_mac of this AppSession.

        客户端Mac地址

        :return: The client_mac of this AppSession.
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        """Sets the client_mac of this AppSession.

        客户端Mac地址

        :param client_mac: The client_mac of this AppSession.
        :type client_mac: str
        """
        self._client_mac = client_mac

    @property
    def client_name(self):
        """Gets the client_name of this AppSession.

        客户端名称

        :return: The client_name of this AppSession.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this AppSession.

        客户端名称

        :param client_name: The client_name of this AppSession.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_ip(self):
        """Gets the client_ip of this AppSession.

        客户端IP

        :return: The client_ip of this AppSession.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this AppSession.

        客户端IP

        :param client_ip: The client_ip of this AppSession.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_version(self):
        """Gets the client_version of this AppSession.

        客户端版本

        :return: The client_version of this AppSession.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this AppSession.

        客户端版本

        :param client_version: The client_version of this AppSession.
        :type client_version: str
        """
        self._client_version = client_version

    @property
    def client_type(self):
        """Gets the client_type of this AppSession.

        客户端类型

        :return: The client_type of this AppSession.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this AppSession.

        客户端类型

        :param client_type: The client_type of this AppSession.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def agent_version(self):
        """Gets the agent_version of this AppSession.

        agent版本

        :return: The agent_version of this AppSession.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this AppSession.

        agent版本

        :param agent_version: The agent_version of this AppSession.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def vm_ip(self):
        """Gets the vm_ip of this AppSession.

        服务器IP

        :return: The vm_ip of this AppSession.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """Sets the vm_ip of this AppSession.

        服务器IP

        :param vm_ip: The vm_ip of this AppSession.
        :type vm_ip: str
        """
        self._vm_ip = vm_ip

    @property
    def failed_reason(self):
        """Gets the failed_reason of this AppSession.

        错误原因消息

        :return: The failed_reason of this AppSession.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this AppSession.

        错误原因消息

        :param failed_reason: The failed_reason of this AppSession.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_code(self):
        """Gets the failed_code of this AppSession.

        错误原因码

        :return: The failed_code of this AppSession.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        """Sets the failed_code of this AppSession.

        错误原因码

        :param failed_code: The failed_code of this AppSession.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def last_update_status_time(self):
        """Gets the last_update_status_time of this AppSession.

        状态最后变化时间

        :return: The last_update_status_time of this AppSession.
        :rtype: str
        """
        return self._last_update_status_time

    @last_update_status_time.setter
    def last_update_status_time(self, last_update_status_time):
        """Sets the last_update_status_time of this AppSession.

        状态最后变化时间

        :param last_update_status_time: The last_update_status_time of this AppSession.
        :type last_update_status_time: str
        """
        self._last_update_status_time = last_update_status_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AppSession.

        租户ID

        :return: The tenant_id of this AppSession.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AppSession.

        租户ID

        :param tenant_id: The tenant_id of this AppSession.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, AppSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
