# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnInstanceInfo:

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
        'access_host': 'str',
        'access_port': 'int',
        'engine': 'str',
        'engine_version': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'access_host': 'access_host',
        'access_port': 'access_port',
        'engine': 'engine',
        'engine_version': 'engine_version'
    }

    def __init__(self, instance_id=None, instance_name=None, access_host=None, access_port=None, engine=None, engine_version=None):
        r"""DnInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param access_host: ip。
        :type access_host: str
        :param access_port: 端口。
        :type access_port: int
        :param engine: 引擎。
        :type engine: str
        :param engine_version: 引擎版本。
        :type engine_version: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._access_host = None
        self._access_port = None
        self._engine = None
        self._engine_version = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if access_host is not None:
            self.access_host = access_host
        if access_port is not None:
            self.access_port = access_port
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DnInstanceInfo.

        实例id。

        :return: The instance_id of this DnInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DnInstanceInfo.

        实例id。

        :param instance_id: The instance_id of this DnInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DnInstanceInfo.

        实例名称。

        :return: The instance_name of this DnInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DnInstanceInfo.

        实例名称。

        :param instance_name: The instance_name of this DnInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def access_host(self):
        r"""Gets the access_host of this DnInstanceInfo.

        ip。

        :return: The access_host of this DnInstanceInfo.
        :rtype: str
        """
        return self._access_host

    @access_host.setter
    def access_host(self, access_host):
        r"""Sets the access_host of this DnInstanceInfo.

        ip。

        :param access_host: The access_host of this DnInstanceInfo.
        :type access_host: str
        """
        self._access_host = access_host

    @property
    def access_port(self):
        r"""Gets the access_port of this DnInstanceInfo.

        端口。

        :return: The access_port of this DnInstanceInfo.
        :rtype: int
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        r"""Sets the access_port of this DnInstanceInfo.

        端口。

        :param access_port: The access_port of this DnInstanceInfo.
        :type access_port: int
        """
        self._access_port = access_port

    @property
    def engine(self):
        r"""Gets the engine of this DnInstanceInfo.

        引擎。

        :return: The engine of this DnInstanceInfo.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this DnInstanceInfo.

        引擎。

        :param engine: The engine of this DnInstanceInfo.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this DnInstanceInfo.

        引擎版本。

        :return: The engine_version of this DnInstanceInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this DnInstanceInfo.

        引擎版本。

        :param engine_version: The engine_version of this DnInstanceInfo.
        :type engine_version: str
        """
        self._engine_version = engine_version

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
        if not isinstance(other, DnInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
