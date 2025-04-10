# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyFlavorsResponseComputeFlavors:

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
        'code': 'str',
        'cpu': 'str',
        'mem': 'str',
        'db_type': 'str',
        'az_status': 'object'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'cpu': 'cpu',
        'mem': 'mem',
        'db_type': 'db_type',
        'az_status': 'az_status'
    }

    def __init__(self, id=None, code=None, cpu=None, mem=None, db_type=None, az_status=None):
        r"""MysqlProxyFlavorsResponseComputeFlavors

        The model defined in huaweicloud sdk

        :param id: 数据库代理规格ID。
        :type id: str
        :param code: 数据库代理规格码。
        :type code: str
        :param cpu: CPU大小。例如：1表示1U。
        :type cpu: str
        :param mem: 内存大小，单位为GB。
        :type mem: str
        :param db_type: 数据库类型。
        :type db_type: str
        :param az_status: 可用区信息，其中key是该规格绑定的可用区，value是该规格在对应可用区中的状态。 取值范围：     normal：正常     abandon：禁用      - 仅展示数据库主实例所在可用区规格状态。
        :type az_status: object
        """
        
        

        self._id = None
        self._code = None
        self._cpu = None
        self._mem = None
        self._db_type = None
        self._az_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if db_type is not None:
            self.db_type = db_type
        if az_status is not None:
            self.az_status = az_status

    @property
    def id(self):
        r"""Gets the id of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库代理规格ID。

        :return: The id of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库代理规格ID。

        :param id: The id of this MysqlProxyFlavorsResponseComputeFlavors.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库代理规格码。

        :return: The code of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库代理规格码。

        :param code: The code of this MysqlProxyFlavorsResponseComputeFlavors.
        :type code: str
        """
        self._code = code

    @property
    def cpu(self):
        r"""Gets the cpu of this MysqlProxyFlavorsResponseComputeFlavors.

        CPU大小。例如：1表示1U。

        :return: The cpu of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this MysqlProxyFlavorsResponseComputeFlavors.

        CPU大小。例如：1表示1U。

        :param cpu: The cpu of this MysqlProxyFlavorsResponseComputeFlavors.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this MysqlProxyFlavorsResponseComputeFlavors.

        内存大小，单位为GB。

        :return: The mem of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this MysqlProxyFlavorsResponseComputeFlavors.

        内存大小，单位为GB。

        :param mem: The mem of this MysqlProxyFlavorsResponseComputeFlavors.
        :type mem: str
        """
        self._mem = mem

    @property
    def db_type(self):
        r"""Gets the db_type of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库类型。

        :return: The db_type of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this MysqlProxyFlavorsResponseComputeFlavors.

        数据库类型。

        :param db_type: The db_type of this MysqlProxyFlavorsResponseComputeFlavors.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def az_status(self):
        r"""Gets the az_status of this MysqlProxyFlavorsResponseComputeFlavors.

        可用区信息，其中key是该规格绑定的可用区，value是该规格在对应可用区中的状态。 取值范围：     normal：正常     abandon：禁用      - 仅展示数据库主实例所在可用区规格状态。

        :return: The az_status of this MysqlProxyFlavorsResponseComputeFlavors.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this MysqlProxyFlavorsResponseComputeFlavors.

        可用区信息，其中key是该规格绑定的可用区，value是该规格在对应可用区中的状态。 取值范围：     normal：正常     abandon：禁用      - 仅展示数据库主实例所在可用区规格状态。

        :param az_status: The az_status of this MysqlProxyFlavorsResponseComputeFlavors.
        :type az_status: object
        """
        self._az_status = az_status

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
        if not isinstance(other, MysqlProxyFlavorsResponseComputeFlavors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
