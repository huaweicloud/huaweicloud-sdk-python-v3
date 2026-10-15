# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotKeyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'command': 'str',
        'qps': 'int',
        'traffic_in': 'int',
        'traffic_out': 'int',
        'db_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'command': 'command',
        'qps': 'qps',
        'traffic_in': 'traffic_in',
        'traffic_out': 'traffic_out',
        'db_id': 'db_id'
    }

    def __init__(self, name=None, type=None, command=None, qps=None, traffic_in=None, traffic_out=None, db_id=None):
        r"""HotKeyInfo

        The model defined in huaweicloud sdk

        :param name: key名称
        :type name: str
        :param type: key类型。取值：string、hash、list、zset、set、stream、exhash
        :type type: str
        :param command: 最新执行命令
        :type command: str
        :param qps: QPS值
        :type qps: int
        :param traffic_in: 入口流量（字节/秒）
        :type traffic_in: int
        :param traffic_out: 出口流量（字节/秒）
        :type traffic_out: int
        :param db_id: DB ID
        :type db_id: str
        """
        
        

        self._name = None
        self._type = None
        self._command = None
        self._qps = None
        self._traffic_in = None
        self._traffic_out = None
        self._db_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if command is not None:
            self.command = command
        if qps is not None:
            self.qps = qps
        if traffic_in is not None:
            self.traffic_in = traffic_in
        if traffic_out is not None:
            self.traffic_out = traffic_out
        if db_id is not None:
            self.db_id = db_id

    @property
    def name(self):
        r"""Gets the name of this HotKeyInfo.

        key名称

        :return: The name of this HotKeyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HotKeyInfo.

        key名称

        :param name: The name of this HotKeyInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this HotKeyInfo.

        key类型。取值：string、hash、list、zset、set、stream、exhash

        :return: The type of this HotKeyInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HotKeyInfo.

        key类型。取值：string、hash、list、zset、set、stream、exhash

        :param type: The type of this HotKeyInfo.
        :type type: str
        """
        self._type = type

    @property
    def command(self):
        r"""Gets the command of this HotKeyInfo.

        最新执行命令

        :return: The command of this HotKeyInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this HotKeyInfo.

        最新执行命令

        :param command: The command of this HotKeyInfo.
        :type command: str
        """
        self._command = command

    @property
    def qps(self):
        r"""Gets the qps of this HotKeyInfo.

        QPS值

        :return: The qps of this HotKeyInfo.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        r"""Sets the qps of this HotKeyInfo.

        QPS值

        :param qps: The qps of this HotKeyInfo.
        :type qps: int
        """
        self._qps = qps

    @property
    def traffic_in(self):
        r"""Gets the traffic_in of this HotKeyInfo.

        入口流量（字节/秒）

        :return: The traffic_in of this HotKeyInfo.
        :rtype: int
        """
        return self._traffic_in

    @traffic_in.setter
    def traffic_in(self, traffic_in):
        r"""Sets the traffic_in of this HotKeyInfo.

        入口流量（字节/秒）

        :param traffic_in: The traffic_in of this HotKeyInfo.
        :type traffic_in: int
        """
        self._traffic_in = traffic_in

    @property
    def traffic_out(self):
        r"""Gets the traffic_out of this HotKeyInfo.

        出口流量（字节/秒）

        :return: The traffic_out of this HotKeyInfo.
        :rtype: int
        """
        return self._traffic_out

    @traffic_out.setter
    def traffic_out(self, traffic_out):
        r"""Sets the traffic_out of this HotKeyInfo.

        出口流量（字节/秒）

        :param traffic_out: The traffic_out of this HotKeyInfo.
        :type traffic_out: int
        """
        self._traffic_out = traffic_out

    @property
    def db_id(self):
        r"""Gets the db_id of this HotKeyInfo.

        DB ID

        :return: The db_id of this HotKeyInfo.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this HotKeyInfo.

        DB ID

        :param db_id: The db_id of this HotKeyInfo.
        :type db_id: str
        """
        self._db_id = db_id

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
        if not isinstance(other, HotKeyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
