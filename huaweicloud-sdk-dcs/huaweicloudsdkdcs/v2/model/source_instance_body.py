# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addrs': 'str',
        'password': 'str',
        'task_status': 'str',
        'id': 'str',
        'ip': 'str',
        'port': 'str',
        'name': 'str',
        'proxy_multi_db': 'bool',
        'db': 'str'
    }

    attribute_map = {
        'addrs': 'addrs',
        'password': 'password',
        'task_status': 'task_status',
        'id': 'id',
        'ip': 'ip',
        'port': 'port',
        'name': 'name',
        'proxy_multi_db': 'proxy_multi_db',
        'db': 'db'
    }

    def __init__(self, addrs=None, password=None, task_status=None, id=None, ip=None, port=None, name=None, proxy_multi_db=None, db=None):
        """SourceInstanceBody

        The model defined in huaweicloud sdk

        :param addrs: Redis实例名称(source_instance信息中填写)。
        :type addrs: str
        :param password: Redis密码，如果设置了密码，则必须填写。
        :type password: str
        :param task_status: 任务状态。
        :type task_status: str
        :param id: Redis实例ID。
        :type id: str
        :param ip: Redis IP地址。
        :type ip: str
        :param port: Redis端口。
        :type port: str
        :param name: Redis名称。
        :type name: str
        :param proxy_multi_db: proxy实例是否开启了多DB。
        :type proxy_multi_db: bool
        :param db: Redis数据库。
        :type db: str
        """
        
        

        self._addrs = None
        self._password = None
        self._task_status = None
        self._id = None
        self._ip = None
        self._port = None
        self._name = None
        self._proxy_multi_db = None
        self._db = None
        self.discriminator = None

        self.addrs = addrs
        if password is not None:
            self.password = password
        if task_status is not None:
            self.task_status = task_status
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if name is not None:
            self.name = name
        if proxy_multi_db is not None:
            self.proxy_multi_db = proxy_multi_db
        if db is not None:
            self.db = db

    @property
    def addrs(self):
        """Gets the addrs of this SourceInstanceBody.

        Redis实例名称(source_instance信息中填写)。

        :return: The addrs of this SourceInstanceBody.
        :rtype: str
        """
        return self._addrs

    @addrs.setter
    def addrs(self, addrs):
        """Sets the addrs of this SourceInstanceBody.

        Redis实例名称(source_instance信息中填写)。

        :param addrs: The addrs of this SourceInstanceBody.
        :type addrs: str
        """
        self._addrs = addrs

    @property
    def password(self):
        """Gets the password of this SourceInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :return: The password of this SourceInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SourceInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :param password: The password of this SourceInstanceBody.
        :type password: str
        """
        self._password = password

    @property
    def task_status(self):
        """Gets the task_status of this SourceInstanceBody.

        任务状态。

        :return: The task_status of this SourceInstanceBody.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this SourceInstanceBody.

        任务状态。

        :param task_status: The task_status of this SourceInstanceBody.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def id(self):
        """Gets the id of this SourceInstanceBody.

        Redis实例ID。

        :return: The id of this SourceInstanceBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceInstanceBody.

        Redis实例ID。

        :param id: The id of this SourceInstanceBody.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this SourceInstanceBody.

        Redis IP地址。

        :return: The ip of this SourceInstanceBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SourceInstanceBody.

        Redis IP地址。

        :param ip: The ip of this SourceInstanceBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this SourceInstanceBody.

        Redis端口。

        :return: The port of this SourceInstanceBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SourceInstanceBody.

        Redis端口。

        :param port: The port of this SourceInstanceBody.
        :type port: str
        """
        self._port = port

    @property
    def name(self):
        """Gets the name of this SourceInstanceBody.

        Redis名称。

        :return: The name of this SourceInstanceBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceInstanceBody.

        Redis名称。

        :param name: The name of this SourceInstanceBody.
        :type name: str
        """
        self._name = name

    @property
    def proxy_multi_db(self):
        """Gets the proxy_multi_db of this SourceInstanceBody.

        proxy实例是否开启了多DB。

        :return: The proxy_multi_db of this SourceInstanceBody.
        :rtype: bool
        """
        return self._proxy_multi_db

    @proxy_multi_db.setter
    def proxy_multi_db(self, proxy_multi_db):
        """Sets the proxy_multi_db of this SourceInstanceBody.

        proxy实例是否开启了多DB。

        :param proxy_multi_db: The proxy_multi_db of this SourceInstanceBody.
        :type proxy_multi_db: bool
        """
        self._proxy_multi_db = proxy_multi_db

    @property
    def db(self):
        """Gets the db of this SourceInstanceBody.

        Redis数据库。

        :return: The db of this SourceInstanceBody.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this SourceInstanceBody.

        Redis数据库。

        :param db: The db of this SourceInstanceBody.
        :type db: str
        """
        self._db = db

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
        if not isinstance(other, SourceInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
