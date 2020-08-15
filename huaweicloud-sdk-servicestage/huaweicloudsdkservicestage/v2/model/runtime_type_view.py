# coding: utf-8

import pprint
import re

import six





class RuntimeTypeView:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type_name': 'str',
        'display_name': 'str',
        'container_default_port': 'int',
        'type_desc': 'str'
    }

    attribute_map = {
        'type_name': 'type_name',
        'display_name': 'display_name',
        'container_default_port': 'container_default_port',
        'type_desc': 'type_desc'
    }

    def __init__(self, type_name=None, display_name=None, container_default_port=None, type_desc=None):
        """RuntimeTypeView - a model defined in huaweicloud sdk"""
        
        

        self._type_name = None
        self._display_name = None
        self._container_default_port = None
        self._type_desc = None
        self.discriminator = None

        if type_name is not None:
            self.type_name = type_name
        if display_name is not None:
            self.display_name = display_name
        if container_default_port is not None:
            self.container_default_port = container_default_port
        if type_desc is not None:
            self.type_desc = type_desc

    @property
    def type_name(self):
        """Gets the type_name of this RuntimeTypeView.

        类型名称。

        :return: The type_name of this RuntimeTypeView.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this RuntimeTypeView.

        类型名称。

        :param type_name: The type_name of this RuntimeTypeView.
        :type: str
        """
        self._type_name = type_name

    @property
    def display_name(self):
        """Gets the display_name of this RuntimeTypeView.

        显示名称。

        :return: The display_name of this RuntimeTypeView.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RuntimeTypeView.

        显示名称。

        :param display_name: The display_name of this RuntimeTypeView.
        :type: str
        """
        self._display_name = display_name

    @property
    def container_default_port(self):
        """Gets the container_default_port of this RuntimeTypeView.

        容器默认端口。

        :return: The container_default_port of this RuntimeTypeView.
        :rtype: int
        """
        return self._container_default_port

    @container_default_port.setter
    def container_default_port(self, container_default_port):
        """Sets the container_default_port of this RuntimeTypeView.

        容器默认端口。

        :param container_default_port: The container_default_port of this RuntimeTypeView.
        :type: int
        """
        self._container_default_port = container_default_port

    @property
    def type_desc(self):
        """Gets the type_desc of this RuntimeTypeView.

        类型描述。

        :return: The type_desc of this RuntimeTypeView.
        :rtype: str
        """
        return self._type_desc

    @type_desc.setter
    def type_desc(self, type_desc):
        """Sets the type_desc of this RuntimeTypeView.

        类型描述。

        :param type_desc: The type_desc of this RuntimeTypeView.
        :type: str
        """
        self._type_desc = type_desc

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
        if not isinstance(other, RuntimeTypeView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
