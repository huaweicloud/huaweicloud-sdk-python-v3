# coding: utf-8

import pprint
import re

import six





class ServiceCapability:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'service_type': 'str',
        'properties': 'list[ServiceProperty]',
        'commands': 'list[ServiceCommand]',
        'events': 'list[ServiceEvent]',
        'description': 'str',
        'option': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'service_type': 'service_type',
        'properties': 'properties',
        'commands': 'commands',
        'events': 'events',
        'description': 'description',
        'option': 'option'
    }

    def __init__(self, service_id=None, service_type=None, properties=None, commands=None, events=None, description=None, option='Optional'):
        """ServiceCapability - a model defined in huaweicloud sdk"""
        
        

        self._service_id = None
        self._service_type = None
        self._properties = None
        self._commands = None
        self._events = None
        self._description = None
        self._option = None
        self.discriminator = None

        self.service_id = service_id
        self.service_type = service_type
        if properties is not None:
            self.properties = properties
        if commands is not None:
            self.commands = commands
        if events is not None:
            self.events = events
        if description is not None:
            self.description = description
        if option is not None:
            self.option = option

    @property
    def service_id(self):
        """Gets the service_id of this ServiceCapability.

        设备的服务ID。

        :return: The service_id of this ServiceCapability.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ServiceCapability.

        设备的服务ID。

        :param service_id: The service_id of this ServiceCapability.
        :type: str
        """
        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this ServiceCapability.

        设备的服务类型。

        :return: The service_type of this ServiceCapability.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ServiceCapability.

        设备的服务类型。

        :param service_type: The service_type of this ServiceCapability.
        :type: str
        """
        self._service_type = service_type

    @property
    def properties(self):
        """Gets the properties of this ServiceCapability.

        设备服务支持的属性列表。

        :return: The properties of this ServiceCapability.
        :rtype: list[ServiceProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ServiceCapability.

        设备服务支持的属性列表。

        :param properties: The properties of this ServiceCapability.
        :type: list[ServiceProperty]
        """
        self._properties = properties

    @property
    def commands(self):
        """Gets the commands of this ServiceCapability.

        设备服务支持的命令列表。

        :return: The commands of this ServiceCapability.
        :rtype: list[ServiceCommand]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this ServiceCapability.

        设备服务支持的命令列表。

        :param commands: The commands of this ServiceCapability.
        :type: list[ServiceCommand]
        """
        self._commands = commands

    @property
    def events(self):
        """Gets the events of this ServiceCapability.

        设备服务支持的事件列表。

        :return: The events of this ServiceCapability.
        :rtype: list[ServiceEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ServiceCapability.

        设备服务支持的事件列表。

        :param events: The events of this ServiceCapability.
        :type: list[ServiceEvent]
        """
        self._events = events

    @property
    def description(self):
        """Gets the description of this ServiceCapability.

        设备服务的描述信息。

        :return: The description of this ServiceCapability.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceCapability.

        设备服务的描述信息。

        :param description: The description of this ServiceCapability.
        :type: str
        """
        self._description = description

    @property
    def option(self):
        """Gets the option of this ServiceCapability.

        指定设备服务是否必选。Master（主服务）, Mandatory（必选服务）, Optional（可选服务），目前本字段为非功能性字段，仅起到标识作用。默认为Optional（可选服务）。

        :return: The option of this ServiceCapability.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ServiceCapability.

        指定设备服务是否必选。Master（主服务）, Mandatory（必选服务）, Optional（可选服务），目前本字段为非功能性字段，仅起到标识作用。默认为Optional（可选服务）。

        :param option: The option of this ServiceCapability.
        :type: str
        """
        self._option = option

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
        if not isinstance(other, ServiceCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
