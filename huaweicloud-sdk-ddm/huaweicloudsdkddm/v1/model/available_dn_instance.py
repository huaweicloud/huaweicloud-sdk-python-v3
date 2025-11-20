# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableDnInstance:

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
        'private_ip': 'str',
        'port': 'int',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'private_ip': 'private_ip',
        'port': 'port',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, status=None, name=None, engine_name=None, engine_version=None, private_ip=None, port=None, time_zone=None):
        r"""AvailableDnInstance

        The model defined in huaweicloud sdk

        :param id: 实例id。
        :type id: str
        :param status: 实例状态。
        :type status: str
        :param name: 实例名称。
        :type name: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param engine_version: 引擎版本。
        :type engine_version: str
        :param private_ip: 私有ip。
        :type private_ip: str
        :param port: 端口。
        :type port: int
        :param time_zone: 时区。
        :type time_zone: str
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._private_ip = None
        self._port = None
        self._time_zone = None
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
        if private_ip is not None:
            self.private_ip = private_ip
        if port is not None:
            self.port = port
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        r"""Gets the id of this AvailableDnInstance.

        实例id。

        :return: The id of this AvailableDnInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AvailableDnInstance.

        实例id。

        :param id: The id of this AvailableDnInstance.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this AvailableDnInstance.

        实例状态。

        :return: The status of this AvailableDnInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AvailableDnInstance.

        实例状态。

        :param status: The status of this AvailableDnInstance.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this AvailableDnInstance.

        实例名称。

        :return: The name of this AvailableDnInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AvailableDnInstance.

        实例名称。

        :param name: The name of this AvailableDnInstance.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this AvailableDnInstance.

        引擎名称。

        :return: The engine_name of this AvailableDnInstance.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this AvailableDnInstance.

        引擎名称。

        :param engine_name: The engine_name of this AvailableDnInstance.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this AvailableDnInstance.

        引擎版本。

        :return: The engine_version of this AvailableDnInstance.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this AvailableDnInstance.

        引擎版本。

        :param engine_version: The engine_version of this AvailableDnInstance.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AvailableDnInstance.

        私有ip。

        :return: The private_ip of this AvailableDnInstance.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AvailableDnInstance.

        私有ip。

        :param private_ip: The private_ip of this AvailableDnInstance.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def port(self):
        r"""Gets the port of this AvailableDnInstance.

        端口。

        :return: The port of this AvailableDnInstance.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AvailableDnInstance.

        端口。

        :param port: The port of this AvailableDnInstance.
        :type port: int
        """
        self._port = port

    @property
    def time_zone(self):
        r"""Gets the time_zone of this AvailableDnInstance.

        时区。

        :return: The time_zone of this AvailableDnInstance.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this AvailableDnInstance.

        时区。

        :param time_zone: The time_zone of this AvailableDnInstance.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, AvailableDnInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
