# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRespClusterBrokers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'port': 'int',
        'broker_id': 'str',
        'is_controller': 'bool',
        'version': 'str',
        'register_time': 'int',
        'is_health': 'bool'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'broker_id': 'broker_id',
        'is_controller': 'is_controller',
        'version': 'version',
        'register_time': 'register_time',
        'is_health': 'is_health'
    }

    def __init__(self, host=None, port=None, broker_id=None, is_controller=None, version=None, register_time=None, is_health=None):
        r"""ShowClusterRespClusterBrokers

        The model defined in huaweicloud sdk

        :param host: **参数解释**： 节点IP。 **取值范围**： 不涉及。
        :type host: str
        :param port: **参数解释**： 端口号。 **取值范围**： 不涉及。
        :type port: int
        :param broker_id: **参数解释**： 节点ID。 **取值范围**： 不涉及。
        :type broker_id: str
        :param is_controller: **参数解释**： 是否为controller节点。 **取值范围**： - true：是controller节点。 - false：不是controller节点。
        :type is_controller: bool
        :param version: **参数解释**： 服务端版本。 **取值范围**： [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc,ax) [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc) - 2.7 [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu,ax)
        :type version: str
        :param register_time: **参数解释**： broker注册时间，为unix时间戳格式。 **取值范围**： 不涉及。
        :type register_time: int
        :param is_health: **参数解释**： Kafka实例节点的连通性是否正常。 **取值范围**： - true：正常。 - false：不正常。
        :type is_health: bool
        """
        
        

        self._host = None
        self._port = None
        self._broker_id = None
        self._is_controller = None
        self._version = None
        self._register_time = None
        self._is_health = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if broker_id is not None:
            self.broker_id = broker_id
        if is_controller is not None:
            self.is_controller = is_controller
        if version is not None:
            self.version = version
        if register_time is not None:
            self.register_time = register_time
        if is_health is not None:
            self.is_health = is_health

    @property
    def host(self):
        r"""Gets the host of this ShowClusterRespClusterBrokers.

        **参数解释**： 节点IP。 **取值范围**： 不涉及。

        :return: The host of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowClusterRespClusterBrokers.

        **参数解释**： 节点IP。 **取值范围**： 不涉及。

        :param host: The host of this ShowClusterRespClusterBrokers.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        r"""Gets the port of this ShowClusterRespClusterBrokers.

        **参数解释**： 端口号。 **取值范围**： 不涉及。

        :return: The port of this ShowClusterRespClusterBrokers.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowClusterRespClusterBrokers.

        **参数解释**： 端口号。 **取值范围**： 不涉及。

        :param port: The port of this ShowClusterRespClusterBrokers.
        :type port: int
        """
        self._port = port

    @property
    def broker_id(self):
        r"""Gets the broker_id of this ShowClusterRespClusterBrokers.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :return: The broker_id of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._broker_id

    @broker_id.setter
    def broker_id(self, broker_id):
        r"""Sets the broker_id of this ShowClusterRespClusterBrokers.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :param broker_id: The broker_id of this ShowClusterRespClusterBrokers.
        :type broker_id: str
        """
        self._broker_id = broker_id

    @property
    def is_controller(self):
        r"""Gets the is_controller of this ShowClusterRespClusterBrokers.

        **参数解释**： 是否为controller节点。 **取值范围**： - true：是controller节点。 - false：不是controller节点。

        :return: The is_controller of this ShowClusterRespClusterBrokers.
        :rtype: bool
        """
        return self._is_controller

    @is_controller.setter
    def is_controller(self, is_controller):
        r"""Sets the is_controller of this ShowClusterRespClusterBrokers.

        **参数解释**： 是否为controller节点。 **取值范围**： - true：是controller节点。 - false：不是controller节点。

        :param is_controller: The is_controller of this ShowClusterRespClusterBrokers.
        :type is_controller: bool
        """
        self._is_controller = is_controller

    @property
    def version(self):
        r"""Gets the version of this ShowClusterRespClusterBrokers.

        **参数解释**： 服务端版本。 **取值范围**： [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc,ax) [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc) - 2.7 [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu,ax)

        :return: The version of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowClusterRespClusterBrokers.

        **参数解释**： 服务端版本。 **取值范围**： [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc,ax) [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc) - 2.7 [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu,ax)

        :param version: The version of this ShowClusterRespClusterBrokers.
        :type version: str
        """
        self._version = version

    @property
    def register_time(self):
        r"""Gets the register_time of this ShowClusterRespClusterBrokers.

        **参数解释**： broker注册时间，为unix时间戳格式。 **取值范围**： 不涉及。

        :return: The register_time of this ShowClusterRespClusterBrokers.
        :rtype: int
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this ShowClusterRespClusterBrokers.

        **参数解释**： broker注册时间，为unix时间戳格式。 **取值范围**： 不涉及。

        :param register_time: The register_time of this ShowClusterRespClusterBrokers.
        :type register_time: int
        """
        self._register_time = register_time

    @property
    def is_health(self):
        r"""Gets the is_health of this ShowClusterRespClusterBrokers.

        **参数解释**： Kafka实例节点的连通性是否正常。 **取值范围**： - true：正常。 - false：不正常。

        :return: The is_health of this ShowClusterRespClusterBrokers.
        :rtype: bool
        """
        return self._is_health

    @is_health.setter
    def is_health(self, is_health):
        r"""Sets the is_health of this ShowClusterRespClusterBrokers.

        **参数解释**： Kafka实例节点的连通性是否正常。 **取值范围**： - true：正常。 - false：不正常。

        :param is_health: The is_health of this ShowClusterRespClusterBrokers.
        :type is_health: bool
        """
        self._is_health = is_health

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
        if not isinstance(other, ShowClusterRespClusterBrokers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
