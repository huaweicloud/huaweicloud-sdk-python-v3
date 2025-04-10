# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerHdaDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'machine_name': 'str',
        'maintain_status': 'bool',
        'server_name': 'str',
        'server_group_id': 'str',
        'server_group_name': 'str',
        'sid': 'str',
        'session_count': 'int',
        'status': 'ServerStatus',
        'current_version': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'machine_name': 'machine_name',
        'maintain_status': 'maintain_status',
        'server_name': 'server_name',
        'server_group_id': 'server_group_id',
        'server_group_name': 'server_group_name',
        'sid': 'sid',
        'session_count': 'session_count',
        'status': 'status',
        'current_version': 'current_version'
    }

    def __init__(self, server_id=None, machine_name=None, maintain_status=None, server_name=None, server_group_id=None, server_group_name=None, sid=None, session_count=None, status=None, current_version=None):
        r"""ServerHdaDetails

        The model defined in huaweicloud sdk

        :param server_id: 服务器id。
        :type server_id: str
        :param machine_name: 机器名称。
        :type machine_name: str
        :param maintain_status: 是否是维护状态。
        :type maintain_status: bool
        :param server_name: 服务器名称。
        :type server_name: str
        :param server_group_id: 服务器组id。
        :type server_group_id: str
        :param server_group_name: 服务器组名称。
        :type server_group_name: str
        :param sid: 服务器的sid。
        :type sid: str
        :param session_count: 会话数量。
        :type session_count: int
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        :param current_version: 当前的accessAgent版本。
        :type current_version: str
        """
        
        

        self._server_id = None
        self._machine_name = None
        self._maintain_status = None
        self._server_name = None
        self._server_group_id = None
        self._server_group_name = None
        self._sid = None
        self._session_count = None
        self._status = None
        self._current_version = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if machine_name is not None:
            self.machine_name = machine_name
        if maintain_status is not None:
            self.maintain_status = maintain_status
        if server_name is not None:
            self.server_name = server_name
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if sid is not None:
            self.sid = sid
        if session_count is not None:
            self.session_count = session_count
        if status is not None:
            self.status = status
        if current_version is not None:
            self.current_version = current_version

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerHdaDetails.

        服务器id。

        :return: The server_id of this ServerHdaDetails.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerHdaDetails.

        服务器id。

        :param server_id: The server_id of this ServerHdaDetails.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def machine_name(self):
        r"""Gets the machine_name of this ServerHdaDetails.

        机器名称。

        :return: The machine_name of this ServerHdaDetails.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        r"""Sets the machine_name of this ServerHdaDetails.

        机器名称。

        :param machine_name: The machine_name of this ServerHdaDetails.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def maintain_status(self):
        r"""Gets the maintain_status of this ServerHdaDetails.

        是否是维护状态。

        :return: The maintain_status of this ServerHdaDetails.
        :rtype: bool
        """
        return self._maintain_status

    @maintain_status.setter
    def maintain_status(self, maintain_status):
        r"""Sets the maintain_status of this ServerHdaDetails.

        是否是维护状态。

        :param maintain_status: The maintain_status of this ServerHdaDetails.
        :type maintain_status: bool
        """
        self._maintain_status = maintain_status

    @property
    def server_name(self):
        r"""Gets the server_name of this ServerHdaDetails.

        服务器名称。

        :return: The server_name of this ServerHdaDetails.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ServerHdaDetails.

        服务器名称。

        :param server_name: The server_name of this ServerHdaDetails.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ServerHdaDetails.

        服务器组id。

        :return: The server_group_id of this ServerHdaDetails.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ServerHdaDetails.

        服务器组id。

        :param server_group_id: The server_group_id of this ServerHdaDetails.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_group_name(self):
        r"""Gets the server_group_name of this ServerHdaDetails.

        服务器组名称。

        :return: The server_group_name of this ServerHdaDetails.
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        r"""Sets the server_group_name of this ServerHdaDetails.

        服务器组名称。

        :param server_group_name: The server_group_name of this ServerHdaDetails.
        :type server_group_name: str
        """
        self._server_group_name = server_group_name

    @property
    def sid(self):
        r"""Gets the sid of this ServerHdaDetails.

        服务器的sid。

        :return: The sid of this ServerHdaDetails.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this ServerHdaDetails.

        服务器的sid。

        :param sid: The sid of this ServerHdaDetails.
        :type sid: str
        """
        self._sid = sid

    @property
    def session_count(self):
        r"""Gets the session_count of this ServerHdaDetails.

        会话数量。

        :return: The session_count of this ServerHdaDetails.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        r"""Sets the session_count of this ServerHdaDetails.

        会话数量。

        :param session_count: The session_count of this ServerHdaDetails.
        :type session_count: int
        """
        self._session_count = session_count

    @property
    def status(self):
        r"""Gets the status of this ServerHdaDetails.

        :return: The status of this ServerHdaDetails.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerHdaDetails.

        :param status: The status of this ServerHdaDetails.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        self._status = status

    @property
    def current_version(self):
        r"""Gets the current_version of this ServerHdaDetails.

        当前的accessAgent版本。

        :return: The current_version of this ServerHdaDetails.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this ServerHdaDetails.

        当前的accessAgent版本。

        :param current_version: The current_version of this ServerHdaDetails.
        :type current_version: str
        """
        self._current_version = current_version

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
        if not isinstance(other, ServerHdaDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
