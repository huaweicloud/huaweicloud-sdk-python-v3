# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserEventRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'username': 'str',
        'workspace_id': 'str',
        'event_trace_id': 'str',
        'event_type': 'str',
        'event_time': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'client_type': 'str',
        'client_ip': 'str',
        'client_mac': 'str',
        'source_ip': 'str',
        'is_success': 'bool',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'username': 'username',
        'workspace_id': 'workspace_id',
        'event_trace_id': 'event_trace_id',
        'event_type': 'event_type',
        'event_time': 'event_time',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'client_type': 'client_type',
        'client_ip': 'client_ip',
        'client_mac': 'client_mac',
        'source_ip': 'source_ip',
        'is_success': 'is_success',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, project_id=None, username=None, workspace_id=None, event_trace_id=None, event_type=None, event_time=None, resource_type=None, resource_id=None, resource_name=None, client_type=None, client_ip=None, client_mac=None, source_ip=None, is_success=None, error_code=None, error_msg=None):
        """UserEventRsp

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param username: 用户名
        :type username: str
        :param workspace_id: 企业id
        :type workspace_id: str
        :param event_trace_id: 事件之间的关联id
        :type event_trace_id: str
        :param event_type: 事件类型
        :type event_type: str
        :param event_time: 事件时间，UTC时间
        :type event_time: str
        :param resource_type: 操作对象类型
        :type resource_type: str
        :param resource_id: 操作对象id
        :type resource_id: str
        :param resource_name: 操作对象名称
        :type resource_name: str
        :param client_type: 客户端类型
        :type client_type: str
        :param client_ip: 客户端ip
        :type client_ip: str
        :param client_mac: 客户端mac地址
        :type client_mac: str
        :param source_ip: 操作用户源ip
        :type source_ip: str
        :param is_success: 是否成功
        :type is_success: bool
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        """
        
        

        self._project_id = None
        self._username = None
        self._workspace_id = None
        self._event_trace_id = None
        self._event_type = None
        self._event_time = None
        self._resource_type = None
        self._resource_id = None
        self._resource_name = None
        self._client_type = None
        self._client_ip = None
        self._client_mac = None
        self._source_ip = None
        self._is_success = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if username is not None:
            self.username = username
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if event_trace_id is not None:
            self.event_trace_id = event_trace_id
        if event_type is not None:
            self.event_type = event_type
        if event_time is not None:
            self.event_time = event_time
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if client_type is not None:
            self.client_type = client_type
        if client_ip is not None:
            self.client_ip = client_ip
        if client_mac is not None:
            self.client_mac = client_mac
        if source_ip is not None:
            self.source_ip = source_ip
        if is_success is not None:
            self.is_success = is_success
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def project_id(self):
        """Gets the project_id of this UserEventRsp.

        项目id

        :return: The project_id of this UserEventRsp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UserEventRsp.

        项目id

        :param project_id: The project_id of this UserEventRsp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def username(self):
        """Gets the username of this UserEventRsp.

        用户名

        :return: The username of this UserEventRsp.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserEventRsp.

        用户名

        :param username: The username of this UserEventRsp.
        :type username: str
        """
        self._username = username

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UserEventRsp.

        企业id

        :return: The workspace_id of this UserEventRsp.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UserEventRsp.

        企业id

        :param workspace_id: The workspace_id of this UserEventRsp.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def event_trace_id(self):
        """Gets the event_trace_id of this UserEventRsp.

        事件之间的关联id

        :return: The event_trace_id of this UserEventRsp.
        :rtype: str
        """
        return self._event_trace_id

    @event_trace_id.setter
    def event_trace_id(self, event_trace_id):
        """Sets the event_trace_id of this UserEventRsp.

        事件之间的关联id

        :param event_trace_id: The event_trace_id of this UserEventRsp.
        :type event_trace_id: str
        """
        self._event_trace_id = event_trace_id

    @property
    def event_type(self):
        """Gets the event_type of this UserEventRsp.

        事件类型

        :return: The event_type of this UserEventRsp.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this UserEventRsp.

        事件类型

        :param event_type: The event_type of this UserEventRsp.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_time(self):
        """Gets the event_time of this UserEventRsp.

        事件时间，UTC时间

        :return: The event_time of this UserEventRsp.
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this UserEventRsp.

        事件时间，UTC时间

        :param event_time: The event_time of this UserEventRsp.
        :type event_time: str
        """
        self._event_time = event_time

    @property
    def resource_type(self):
        """Gets the resource_type of this UserEventRsp.

        操作对象类型

        :return: The resource_type of this UserEventRsp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UserEventRsp.

        操作对象类型

        :param resource_type: The resource_type of this UserEventRsp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this UserEventRsp.

        操作对象id

        :return: The resource_id of this UserEventRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UserEventRsp.

        操作对象id

        :param resource_id: The resource_id of this UserEventRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this UserEventRsp.

        操作对象名称

        :return: The resource_name of this UserEventRsp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this UserEventRsp.

        操作对象名称

        :param resource_name: The resource_name of this UserEventRsp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def client_type(self):
        """Gets the client_type of this UserEventRsp.

        客户端类型

        :return: The client_type of this UserEventRsp.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this UserEventRsp.

        客户端类型

        :param client_type: The client_type of this UserEventRsp.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def client_ip(self):
        """Gets the client_ip of this UserEventRsp.

        客户端ip

        :return: The client_ip of this UserEventRsp.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this UserEventRsp.

        客户端ip

        :param client_ip: The client_ip of this UserEventRsp.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_mac(self):
        """Gets the client_mac of this UserEventRsp.

        客户端mac地址

        :return: The client_mac of this UserEventRsp.
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        """Sets the client_mac of this UserEventRsp.

        客户端mac地址

        :param client_mac: The client_mac of this UserEventRsp.
        :type client_mac: str
        """
        self._client_mac = client_mac

    @property
    def source_ip(self):
        """Gets the source_ip of this UserEventRsp.

        操作用户源ip

        :return: The source_ip of this UserEventRsp.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this UserEventRsp.

        操作用户源ip

        :param source_ip: The source_ip of this UserEventRsp.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def is_success(self):
        """Gets the is_success of this UserEventRsp.

        是否成功

        :return: The is_success of this UserEventRsp.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this UserEventRsp.

        是否成功

        :param is_success: The is_success of this UserEventRsp.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def error_code(self):
        """Gets the error_code of this UserEventRsp.

        错误码

        :return: The error_code of this UserEventRsp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this UserEventRsp.

        错误码

        :param error_code: The error_code of this UserEventRsp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this UserEventRsp.

        错误描述

        :return: The error_msg of this UserEventRsp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this UserEventRsp.

        错误描述

        :param error_msg: The error_msg of this UserEventRsp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, UserEventRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
