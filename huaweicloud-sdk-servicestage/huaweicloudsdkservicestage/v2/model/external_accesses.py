# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalAccesses:

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
        'protocol': 'str',
        'address': 'str',
        'forward_port': 'int',
        'type': 'str',
        'status': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'protocol': 'protocol',
        'address': 'address',
        'forward_port': 'forward_port',
        'type': 'type',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, protocol=None, address=None, forward_port=None, type=None, status=None, create_time=None, update_time=None):
        r"""ExternalAccesses

        The model defined in huaweicloud sdk

        :param id: ID。
        :type id: str
        :param protocol: 协议。
        :type protocol: str
        :param address: 访问地址。
        :type address: str
        :param forward_port: 应用组件进程监听端口
        :type forward_port: int
        :param type: 类型。
        :type type: str
        :param status: 状态。
        :type status: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        """
        
        

        self._id = None
        self._protocol = None
        self._address = None
        self._forward_port = None
        self._type = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.protocol = protocol
        self.address = address
        self.forward_port = forward_port
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ExternalAccesses.

        ID。

        :return: The id of this ExternalAccesses.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExternalAccesses.

        ID。

        :param id: The id of this ExternalAccesses.
        :type id: str
        """
        self._id = id

    @property
    def protocol(self):
        r"""Gets the protocol of this ExternalAccesses.

        协议。

        :return: The protocol of this ExternalAccesses.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ExternalAccesses.

        协议。

        :param protocol: The protocol of this ExternalAccesses.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def address(self):
        r"""Gets the address of this ExternalAccesses.

        访问地址。

        :return: The address of this ExternalAccesses.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ExternalAccesses.

        访问地址。

        :param address: The address of this ExternalAccesses.
        :type address: str
        """
        self._address = address

    @property
    def forward_port(self):
        r"""Gets the forward_port of this ExternalAccesses.

        应用组件进程监听端口

        :return: The forward_port of this ExternalAccesses.
        :rtype: int
        """
        return self._forward_port

    @forward_port.setter
    def forward_port(self, forward_port):
        r"""Sets the forward_port of this ExternalAccesses.

        应用组件进程监听端口

        :param forward_port: The forward_port of this ExternalAccesses.
        :type forward_port: int
        """
        self._forward_port = forward_port

    @property
    def type(self):
        r"""Gets the type of this ExternalAccesses.

        类型。

        :return: The type of this ExternalAccesses.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExternalAccesses.

        类型。

        :param type: The type of this ExternalAccesses.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ExternalAccesses.

        状态。

        :return: The status of this ExternalAccesses.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExternalAccesses.

        状态。

        :param status: The status of this ExternalAccesses.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ExternalAccesses.

        创建时间。

        :return: The create_time of this ExternalAccesses.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExternalAccesses.

        创建时间。

        :param create_time: The create_time of this ExternalAccesses.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ExternalAccesses.

        修改时间。

        :return: The update_time of this ExternalAccesses.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ExternalAccesses.

        修改时间。

        :param update_time: The update_time of this ExternalAccesses.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ExternalAccesses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
