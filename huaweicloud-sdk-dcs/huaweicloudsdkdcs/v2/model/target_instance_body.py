# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetInstanceBody:

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
        'name': 'str',
        'password': 'str',
        'task_status': 'str',
        'ip': 'str',
        'port': 'str',
        'addrs': 'str',
        'proxy_multi_db': 'bool',
        'db': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'password': 'password',
        'task_status': 'task_status',
        'ip': 'ip',
        'port': 'port',
        'addrs': 'addrs',
        'proxy_multi_db': 'proxy_multi_db',
        'db': 'db'
    }

    def __init__(self, id=None, name=None, password=None, task_status=None, ip=None, port=None, addrs=None, proxy_multi_db=None, db=None):
        """TargetInstanceBody

        The model defined in huaweicloud sdk

        :param id: Redis实例ID（target_instance信息中必须填写）。
        :type id: str
        :param name: Redis实例名称(target_instance信息中填写)。
        :type name: str
        :param password: Redis密码，如果设置了密码，则必须填写。
        :type password: str
        :param task_status: 任务状态。
        :type task_status: str
        :param ip: Redis IP地址。
        :type ip: str
        :param port: Redis端口。
        :type port: str
        :param addrs: Redis实例地址。
        :type addrs: str
        :param proxy_multi_db: proxy实例是否开启了多DB。
        :type proxy_multi_db: bool
        :param db: Redis数据库。
        :type db: str
        """
        
        

        self._id = None
        self._name = None
        self._password = None
        self._task_status = None
        self._ip = None
        self._port = None
        self._addrs = None
        self._proxy_multi_db = None
        self._db = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if task_status is not None:
            self.task_status = task_status
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if addrs is not None:
            self.addrs = addrs
        if proxy_multi_db is not None:
            self.proxy_multi_db = proxy_multi_db
        if db is not None:
            self.db = db

    @property
    def id(self):
        """Gets the id of this TargetInstanceBody.

        Redis实例ID（target_instance信息中必须填写）。

        :return: The id of this TargetInstanceBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetInstanceBody.

        Redis实例ID（target_instance信息中必须填写）。

        :param id: The id of this TargetInstanceBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TargetInstanceBody.

        Redis实例名称(target_instance信息中填写)。

        :return: The name of this TargetInstanceBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetInstanceBody.

        Redis实例名称(target_instance信息中填写)。

        :param name: The name of this TargetInstanceBody.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this TargetInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :return: The password of this TargetInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TargetInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :param password: The password of this TargetInstanceBody.
        :type password: str
        """
        self._password = password

    @property
    def task_status(self):
        """Gets the task_status of this TargetInstanceBody.

        任务状态。

        :return: The task_status of this TargetInstanceBody.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this TargetInstanceBody.

        任务状态。

        :param task_status: The task_status of this TargetInstanceBody.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def ip(self):
        """Gets the ip of this TargetInstanceBody.

        Redis IP地址。

        :return: The ip of this TargetInstanceBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TargetInstanceBody.

        Redis IP地址。

        :param ip: The ip of this TargetInstanceBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this TargetInstanceBody.

        Redis端口。

        :return: The port of this TargetInstanceBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TargetInstanceBody.

        Redis端口。

        :param port: The port of this TargetInstanceBody.
        :type port: str
        """
        self._port = port

    @property
    def addrs(self):
        """Gets the addrs of this TargetInstanceBody.

        Redis实例地址。

        :return: The addrs of this TargetInstanceBody.
        :rtype: str
        """
        return self._addrs

    @addrs.setter
    def addrs(self, addrs):
        """Sets the addrs of this TargetInstanceBody.

        Redis实例地址。

        :param addrs: The addrs of this TargetInstanceBody.
        :type addrs: str
        """
        self._addrs = addrs

    @property
    def proxy_multi_db(self):
        """Gets the proxy_multi_db of this TargetInstanceBody.

        proxy实例是否开启了多DB。

        :return: The proxy_multi_db of this TargetInstanceBody.
        :rtype: bool
        """
        return self._proxy_multi_db

    @proxy_multi_db.setter
    def proxy_multi_db(self, proxy_multi_db):
        """Sets the proxy_multi_db of this TargetInstanceBody.

        proxy实例是否开启了多DB。

        :param proxy_multi_db: The proxy_multi_db of this TargetInstanceBody.
        :type proxy_multi_db: bool
        """
        self._proxy_multi_db = proxy_multi_db

    @property
    def db(self):
        """Gets the db of this TargetInstanceBody.

        Redis数据库。

        :return: The db of this TargetInstanceBody.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this TargetInstanceBody.

        Redis数据库。

        :param db: The db of this TargetInstanceBody.
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
        if not isinstance(other, TargetInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
