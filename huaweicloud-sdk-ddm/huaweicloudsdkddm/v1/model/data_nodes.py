# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataNodes:

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
        'status': 'str',
        'name': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'mem': 'int',
        'cpu': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'mem': 'mem',
        'cpu': 'cpu'
    }

    def __init__(self, id=None, status=None, name=None, engine_name=None, engine_version=None, mem=None, cpu=None):
        r"""DataNodes

        The model defined in huaweicloud sdk

        :param id: 后端DN的id。
        :type id: str
        :param status: 后端DN的状态。
        :type status: str
        :param name: 后端DN的名称。
        :type name: str
        :param engine_name: 后端DN的引擎名称。
        :type engine_name: str
        :param engine_version: 后端DN的引擎版本。
        :type engine_version: str
        :param mem: 后端DN的内存大小。
        :type mem: int
        :param cpu: 后端DN的CPU大小。
        :type cpu: int
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._mem = None
        self._cpu = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if mem is not None:
            self.mem = mem
        if cpu is not None:
            self.cpu = cpu

    @property
    def id(self):
        r"""Gets the id of this DataNodes.

        后端DN的id。

        :return: The id of this DataNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataNodes.

        后端DN的id。

        :param id: The id of this DataNodes.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this DataNodes.

        后端DN的状态。

        :return: The status of this DataNodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataNodes.

        后端DN的状态。

        :param status: The status of this DataNodes.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this DataNodes.

        后端DN的名称。

        :return: The name of this DataNodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataNodes.

        后端DN的名称。

        :param name: The name of this DataNodes.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this DataNodes.

        后端DN的引擎名称。

        :return: The engine_name of this DataNodes.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this DataNodes.

        后端DN的引擎名称。

        :param engine_name: The engine_name of this DataNodes.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this DataNodes.

        后端DN的引擎版本。

        :return: The engine_version of this DataNodes.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this DataNodes.

        后端DN的引擎版本。

        :param engine_version: The engine_version of this DataNodes.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def mem(self):
        r"""Gets the mem of this DataNodes.

        后端DN的内存大小。

        :return: The mem of this DataNodes.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this DataNodes.

        后端DN的内存大小。

        :param mem: The mem of this DataNodes.
        :type mem: int
        """
        self._mem = mem

    @property
    def cpu(self):
        r"""Gets the cpu of this DataNodes.

        后端DN的CPU大小。

        :return: The cpu of this DataNodes.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this DataNodes.

        后端DN的CPU大小。

        :param cpu: The cpu of this DataNodes.
        :type cpu: int
        """
        self._cpu = cpu

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
        if not isinstance(other, DataNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
