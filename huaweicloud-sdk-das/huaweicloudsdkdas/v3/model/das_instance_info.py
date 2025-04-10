# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DASInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'version': 'str',
        'engine_type': 'str',
        'ip': 'str',
        'port': 'int',
        'cpu': 'int',
        'mem': 'int',
        'login_flag': 'bool',
        'slow_sql_flag': 'bool',
        'deadlock_flag': 'bool',
        'lock_blocking_flag': 'bool',
        'charge_flag': 'bool',
        'full_sql_flag': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'version': 'version',
        'engine_type': 'engine_type',
        'ip': 'ip',
        'port': 'port',
        'cpu': 'cpu',
        'mem': 'mem',
        'login_flag': 'login_flag',
        'slow_sql_flag': 'slow_sql_flag',
        'deadlock_flag': 'deadlock_flag',
        'lock_blocking_flag': 'lock_blocking_flag',
        'charge_flag': 'charge_flag',
        'full_sql_flag': 'full_sql_flag'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_status=None, version=None, engine_type=None, ip=None, port=None, cpu=None, mem=None, login_flag=None, slow_sql_flag=None, deadlock_flag=None, lock_blocking_flag=None, charge_flag=None, full_sql_flag=None):
        r"""DASInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。
        :type instance_status: str
        :param version: 实例版本号。
        :type version: str
        :param engine_type: 引擎类型。
        :type engine_type: str
        :param ip: ip
        :type ip: str
        :param port: 端口号
        :type port: int
        :param cpu: 实例cpu核数
        :type cpu: int
        :param mem: 实例内存大小
        :type mem: int
        :param login_flag: 实例登录是否启用
        :type login_flag: bool
        :param slow_sql_flag: 慢sql是否启用
        :type slow_sql_flag: bool
        :param deadlock_flag: 死锁分析是否启用
        :type deadlock_flag: bool
        :param lock_blocking_flag: 锁阻塞是否启用
        :type lock_blocking_flag: bool
        :param charge_flag: 当前实例是否计费
        :type charge_flag: bool
        :param full_sql_flag: 全量sql是否启用
        :type full_sql_flag: bool
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._version = None
        self._engine_type = None
        self._ip = None
        self._port = None
        self._cpu = None
        self._mem = None
        self._login_flag = None
        self._slow_sql_flag = None
        self._deadlock_flag = None
        self._lock_blocking_flag = None
        self._charge_flag = None
        self._full_sql_flag = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.version = version
        self.engine_type = engine_type
        self.ip = ip
        self.port = port
        self.cpu = cpu
        self.mem = mem
        self.login_flag = login_flag
        self.slow_sql_flag = slow_sql_flag
        self.deadlock_flag = deadlock_flag
        self.lock_blocking_flag = lock_blocking_flag
        self.charge_flag = charge_flag
        self.full_sql_flag = full_sql_flag

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DASInstanceInfo.

        实例id。

        :return: The instance_id of this DASInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DASInstanceInfo.

        实例id。

        :param instance_id: The instance_id of this DASInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DASInstanceInfo.

        实例名称。

        :return: The instance_name of this DASInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DASInstanceInfo.

        实例名称。

        :param instance_name: The instance_name of this DASInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this DASInstanceInfo.

        实例状态。

        :return: The instance_status of this DASInstanceInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this DASInstanceInfo.

        实例状态。

        :param instance_status: The instance_status of this DASInstanceInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def version(self):
        r"""Gets the version of this DASInstanceInfo.

        实例版本号。

        :return: The version of this DASInstanceInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DASInstanceInfo.

        实例版本号。

        :param version: The version of this DASInstanceInfo.
        :type version: str
        """
        self._version = version

    @property
    def engine_type(self):
        r"""Gets the engine_type of this DASInstanceInfo.

        引擎类型。

        :return: The engine_type of this DASInstanceInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this DASInstanceInfo.

        引擎类型。

        :param engine_type: The engine_type of this DASInstanceInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def ip(self):
        r"""Gets the ip of this DASInstanceInfo.

        ip

        :return: The ip of this DASInstanceInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this DASInstanceInfo.

        ip

        :param ip: The ip of this DASInstanceInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this DASInstanceInfo.

        端口号

        :return: The port of this DASInstanceInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this DASInstanceInfo.

        端口号

        :param port: The port of this DASInstanceInfo.
        :type port: int
        """
        self._port = port

    @property
    def cpu(self):
        r"""Gets the cpu of this DASInstanceInfo.

        实例cpu核数

        :return: The cpu of this DASInstanceInfo.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this DASInstanceInfo.

        实例cpu核数

        :param cpu: The cpu of this DASInstanceInfo.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this DASInstanceInfo.

        实例内存大小

        :return: The mem of this DASInstanceInfo.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this DASInstanceInfo.

        实例内存大小

        :param mem: The mem of this DASInstanceInfo.
        :type mem: int
        """
        self._mem = mem

    @property
    def login_flag(self):
        r"""Gets the login_flag of this DASInstanceInfo.

        实例登录是否启用

        :return: The login_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._login_flag

    @login_flag.setter
    def login_flag(self, login_flag):
        r"""Sets the login_flag of this DASInstanceInfo.

        实例登录是否启用

        :param login_flag: The login_flag of this DASInstanceInfo.
        :type login_flag: bool
        """
        self._login_flag = login_flag

    @property
    def slow_sql_flag(self):
        r"""Gets the slow_sql_flag of this DASInstanceInfo.

        慢sql是否启用

        :return: The slow_sql_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._slow_sql_flag

    @slow_sql_flag.setter
    def slow_sql_flag(self, slow_sql_flag):
        r"""Sets the slow_sql_flag of this DASInstanceInfo.

        慢sql是否启用

        :param slow_sql_flag: The slow_sql_flag of this DASInstanceInfo.
        :type slow_sql_flag: bool
        """
        self._slow_sql_flag = slow_sql_flag

    @property
    def deadlock_flag(self):
        r"""Gets the deadlock_flag of this DASInstanceInfo.

        死锁分析是否启用

        :return: The deadlock_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._deadlock_flag

    @deadlock_flag.setter
    def deadlock_flag(self, deadlock_flag):
        r"""Sets the deadlock_flag of this DASInstanceInfo.

        死锁分析是否启用

        :param deadlock_flag: The deadlock_flag of this DASInstanceInfo.
        :type deadlock_flag: bool
        """
        self._deadlock_flag = deadlock_flag

    @property
    def lock_blocking_flag(self):
        r"""Gets the lock_blocking_flag of this DASInstanceInfo.

        锁阻塞是否启用

        :return: The lock_blocking_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._lock_blocking_flag

    @lock_blocking_flag.setter
    def lock_blocking_flag(self, lock_blocking_flag):
        r"""Sets the lock_blocking_flag of this DASInstanceInfo.

        锁阻塞是否启用

        :param lock_blocking_flag: The lock_blocking_flag of this DASInstanceInfo.
        :type lock_blocking_flag: bool
        """
        self._lock_blocking_flag = lock_blocking_flag

    @property
    def charge_flag(self):
        r"""Gets the charge_flag of this DASInstanceInfo.

        当前实例是否计费

        :return: The charge_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._charge_flag

    @charge_flag.setter
    def charge_flag(self, charge_flag):
        r"""Sets the charge_flag of this DASInstanceInfo.

        当前实例是否计费

        :param charge_flag: The charge_flag of this DASInstanceInfo.
        :type charge_flag: bool
        """
        self._charge_flag = charge_flag

    @property
    def full_sql_flag(self):
        r"""Gets the full_sql_flag of this DASInstanceInfo.

        全量sql是否启用

        :return: The full_sql_flag of this DASInstanceInfo.
        :rtype: bool
        """
        return self._full_sql_flag

    @full_sql_flag.setter
    def full_sql_flag(self, full_sql_flag):
        r"""Sets the full_sql_flag of this DASInstanceInfo.

        全量sql是否启用

        :param full_sql_flag: The full_sql_flag of this DASInstanceInfo.
        :type full_sql_flag: bool
        """
        self._full_sql_flag = full_sql_flag

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
        if not isinstance(other, DASInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
