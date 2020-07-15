# coding: utf-8

import pprint
import re

import six





class AvailableZones:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'port': 'str',
        'name': 'str',
        'id': 'str',
        'resource_availability': 'str'
    }

    attribute_map = {
        'code': 'code',
        'port': 'port',
        'name': 'name',
        'id': 'id',
        'resource_availability': 'resource_availability'
    }

    def __init__(self, code=None, port=None, name=None, id=None, resource_availability=None):
        """AvailableZones - a model defined in huaweicloud sdk"""
        
        

        self._code = None
        self._port = None
        self._name = None
        self._id = None
        self._resource_availability = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if port is not None:
            self.port = port
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if resource_availability is not None:
            self.resource_availability = resource_availability

    @property
    def code(self):
        """Gets the code of this AvailableZones.

        可用区编码。

        :return: The code of this AvailableZones.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AvailableZones.

        可用区编码。

        :param code: The code of this AvailableZones.
        :type: str
        """
        self._code = code

    @property
    def port(self):
        """Gets the port of this AvailableZones.

        可用区端口号。

        :return: The port of this AvailableZones.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AvailableZones.

        可用区端口号。

        :param port: The port of this AvailableZones.
        :type: str
        """
        self._port = port

    @property
    def name(self):
        """Gets the name of this AvailableZones.

        可用区名称。

        :return: The name of this AvailableZones.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AvailableZones.

        可用区名称。

        :param name: The name of this AvailableZones.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this AvailableZones.

        可用区ID。

        :return: The id of this AvailableZones.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvailableZones.

        可用区ID。

        :param id: The id of this AvailableZones.
        :type: str
        """
        self._id = id

    @property
    def resource_availability(self):
        """Gets the resource_availability of this AvailableZones.

        分区上是否还有可用资源。 - true：还有资源。 - false：资源已售罄。 

        :return: The resource_availability of this AvailableZones.
        :rtype: str
        """
        return self._resource_availability

    @resource_availability.setter
    def resource_availability(self, resource_availability):
        """Sets the resource_availability of this AvailableZones.

        分区上是否还有可用资源。 - true：还有资源。 - false：资源已售罄。 

        :param resource_availability: The resource_availability of this AvailableZones.
        :type: str
        """
        self._resource_availability = resource_availability

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
        if not isinstance(other, AvailableZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
