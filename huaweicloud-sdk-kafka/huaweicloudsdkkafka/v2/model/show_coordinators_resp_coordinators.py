# coding: utf-8

import pprint
import re

import six





class ShowCoordinatorsRespCoordinators:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'id': 'int',
        'host': 'str',
        'port': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'id': 'id',
        'host': 'host',
        'port': 'port'
    }

    def __init__(self, group_id=None, id=None, host=None, port=None):
        """ShowCoordinatorsRespCoordinators - a model defined in huaweicloud sdk"""
        
        

        self._group_id = None
        self._id = None
        self._host = None
        self._port = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

    @property
    def group_id(self):
        """Gets the group_id of this ShowCoordinatorsRespCoordinators.

        消费组ID。

        :return: The group_id of this ShowCoordinatorsRespCoordinators.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowCoordinatorsRespCoordinators.

        消费组ID。

        :param group_id: The group_id of this ShowCoordinatorsRespCoordinators.
        :type: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this ShowCoordinatorsRespCoordinators.

        对应协调器的broker id。

        :return: The id of this ShowCoordinatorsRespCoordinators.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowCoordinatorsRespCoordinators.

        对应协调器的broker id。

        :param id: The id of this ShowCoordinatorsRespCoordinators.
        :type: int
        """
        self._id = id

    @property
    def host(self):
        """Gets the host of this ShowCoordinatorsRespCoordinators.

        对应协调器的地址。

        :return: The host of this ShowCoordinatorsRespCoordinators.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ShowCoordinatorsRespCoordinators.

        对应协调器的地址。

        :param host: The host of this ShowCoordinatorsRespCoordinators.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this ShowCoordinatorsRespCoordinators.

        端口号。

        :return: The port of this ShowCoordinatorsRespCoordinators.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowCoordinatorsRespCoordinators.

        端口号。

        :param port: The port of this ShowCoordinatorsRespCoordinators.
        :type: int
        """
        self._port = port

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
        if not isinstance(other, ShowCoordinatorsRespCoordinators):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
