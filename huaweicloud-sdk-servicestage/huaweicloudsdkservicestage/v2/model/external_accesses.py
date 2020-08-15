# coding: utf-8

import pprint
import re

import six





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
        'protocol': 'ExternalAccessProtocol',
        'address': 'str',
        'forward_port': 'int',
        'type': 'ExternalAccessType',
        'status': 'ExternalAccessStatus',
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
        """ExternalAccesses - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the id of this ExternalAccesses.

        ID。

        :return: The id of this ExternalAccesses.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalAccesses.

        ID。

        :param id: The id of this ExternalAccesses.
        :type: str
        """
        self._id = id

    @property
    def protocol(self):
        """Gets the protocol of this ExternalAccesses.


        :return: The protocol of this ExternalAccesses.
        :rtype: ExternalAccessProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ExternalAccesses.


        :param protocol: The protocol of this ExternalAccesses.
        :type: ExternalAccessProtocol
        """
        self._protocol = protocol

    @property
    def address(self):
        """Gets the address of this ExternalAccesses.

        访问地址。

        :return: The address of this ExternalAccesses.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ExternalAccesses.

        访问地址。

        :param address: The address of this ExternalAccesses.
        :type: str
        """
        self._address = address

    @property
    def forward_port(self):
        """Gets the forward_port of this ExternalAccesses.

        应用组件进程监听端口

        :return: The forward_port of this ExternalAccesses.
        :rtype: int
        """
        return self._forward_port

    @forward_port.setter
    def forward_port(self, forward_port):
        """Sets the forward_port of this ExternalAccesses.

        应用组件进程监听端口

        :param forward_port: The forward_port of this ExternalAccesses.
        :type: int
        """
        self._forward_port = forward_port

    @property
    def type(self):
        """Gets the type of this ExternalAccesses.


        :return: The type of this ExternalAccesses.
        :rtype: ExternalAccessType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalAccesses.


        :param type: The type of this ExternalAccesses.
        :type: ExternalAccessType
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ExternalAccesses.


        :return: The status of this ExternalAccesses.
        :rtype: ExternalAccessStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalAccesses.


        :param status: The status of this ExternalAccesses.
        :type: ExternalAccessStatus
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ExternalAccesses.

        创建时间。

        :return: The create_time of this ExternalAccesses.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ExternalAccesses.

        创建时间。

        :param create_time: The create_time of this ExternalAccesses.
        :type: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ExternalAccesses.

        修改时间。

        :return: The update_time of this ExternalAccesses.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ExternalAccesses.

        修改时间。

        :param update_time: The update_time of this ExternalAccesses.
        :type: int
        """
        self._update_time = update_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalAccesses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
