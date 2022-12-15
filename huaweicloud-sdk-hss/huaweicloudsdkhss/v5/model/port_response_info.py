# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'status': 'str',
        'port': 'int',
        'type': 'str',
        'pid': 'int',
        'path': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'status': 'status',
        'port': 'port',
        'type': 'type',
        'pid': 'pid',
        'path': 'path'
    }

    def __init__(self, host_id=None, status=None, port=None, type=None, pid=None, path=None):
        """PortResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param status: port status, normal, danger or unknow   - \&quot;normal\&quot; : 正常   - \&quot;danger\&quot; : 危险   - \&quot;unknow\&quot; : 未知
        :type status: str
        :param port: 端口号
        :type port: int
        :param type: 类型
        :type type: str
        :param pid: 进程ID
        :type pid: int
        :param path: 程序文件
        :type path: str
        """
        
        

        self._host_id = None
        self._status = None
        self._port = None
        self._type = None
        self._pid = None
        self._path = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if pid is not None:
            self.pid = pid
        if path is not None:
            self.path = path

    @property
    def host_id(self):
        """Gets the host_id of this PortResponseInfo.

        主机id

        :return: The host_id of this PortResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this PortResponseInfo.

        主机id

        :param host_id: The host_id of this PortResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def status(self):
        """Gets the status of this PortResponseInfo.

        port status, normal, danger or unknow   - \"normal\" : 正常   - \"danger\" : 危险   - \"unknow\" : 未知

        :return: The status of this PortResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortResponseInfo.

        port status, normal, danger or unknow   - \"normal\" : 正常   - \"danger\" : 危险   - \"unknow\" : 未知

        :param status: The status of this PortResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        """Gets the port of this PortResponseInfo.

        端口号

        :return: The port of this PortResponseInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortResponseInfo.

        端口号

        :param port: The port of this PortResponseInfo.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this PortResponseInfo.

        类型

        :return: The type of this PortResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortResponseInfo.

        类型

        :param type: The type of this PortResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def pid(self):
        """Gets the pid of this PortResponseInfo.

        进程ID

        :return: The pid of this PortResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this PortResponseInfo.

        进程ID

        :param pid: The pid of this PortResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def path(self):
        """Gets the path of this PortResponseInfo.

        程序文件

        :return: The path of this PortResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PortResponseInfo.

        程序文件

        :param path: The path of this PortResponseInfo.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, PortResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
