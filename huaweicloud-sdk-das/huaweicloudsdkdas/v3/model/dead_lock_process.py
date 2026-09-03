# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLockProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spid': 'str',
        'process_id': 'str',
        'host_name': 'str',
        'login_name': 'str',
        'log_used': 'int',
        'sql': 'str'
    }

    attribute_map = {
        'spid': 'spid',
        'process_id': 'process_id',
        'host_name': 'host_name',
        'login_name': 'login_name',
        'log_used': 'log_used',
        'sql': 'sql'
    }

    def __init__(self, spid=None, process_id=None, host_name=None, login_name=None, log_used=None, sql=None):
        r"""DeadLockProcess

        The model defined in huaweicloud sdk

        :param spid: 服务进程ID
        :type spid: str
        :param process_id: 会话ID
        :type process_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param login_name: 用户名称
        :type login_name: str
        :param log_used: 任务使用的日志空间
        :type log_used: int
        :param sql: SQL语句
        :type sql: str
        """
        
        

        self._spid = None
        self._process_id = None
        self._host_name = None
        self._login_name = None
        self._log_used = None
        self._sql = None
        self.discriminator = None

        if spid is not None:
            self.spid = spid
        if process_id is not None:
            self.process_id = process_id
        if host_name is not None:
            self.host_name = host_name
        if login_name is not None:
            self.login_name = login_name
        if log_used is not None:
            self.log_used = log_used
        if sql is not None:
            self.sql = sql

    @property
    def spid(self):
        r"""Gets the spid of this DeadLockProcess.

        服务进程ID

        :return: The spid of this DeadLockProcess.
        :rtype: str
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        r"""Sets the spid of this DeadLockProcess.

        服务进程ID

        :param spid: The spid of this DeadLockProcess.
        :type spid: str
        """
        self._spid = spid

    @property
    def process_id(self):
        r"""Gets the process_id of this DeadLockProcess.

        会话ID

        :return: The process_id of this DeadLockProcess.
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        r"""Sets the process_id of this DeadLockProcess.

        会话ID

        :param process_id: The process_id of this DeadLockProcess.
        :type process_id: str
        """
        self._process_id = process_id

    @property
    def host_name(self):
        r"""Gets the host_name of this DeadLockProcess.

        主机名称

        :return: The host_name of this DeadLockProcess.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this DeadLockProcess.

        主机名称

        :param host_name: The host_name of this DeadLockProcess.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def login_name(self):
        r"""Gets the login_name of this DeadLockProcess.

        用户名称

        :return: The login_name of this DeadLockProcess.
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        r"""Sets the login_name of this DeadLockProcess.

        用户名称

        :param login_name: The login_name of this DeadLockProcess.
        :type login_name: str
        """
        self._login_name = login_name

    @property
    def log_used(self):
        r"""Gets the log_used of this DeadLockProcess.

        任务使用的日志空间

        :return: The log_used of this DeadLockProcess.
        :rtype: int
        """
        return self._log_used

    @log_used.setter
    def log_used(self, log_used):
        r"""Sets the log_used of this DeadLockProcess.

        任务使用的日志空间

        :param log_used: The log_used of this DeadLockProcess.
        :type log_used: int
        """
        self._log_used = log_used

    @property
    def sql(self):
        r"""Gets the sql of this DeadLockProcess.

        SQL语句

        :return: The sql of this DeadLockProcess.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this DeadLockProcess.

        SQL语句

        :param sql: The sql of this DeadLockProcess.
        :type sql: str
        """
        self._sql = sql

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeadLockProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
