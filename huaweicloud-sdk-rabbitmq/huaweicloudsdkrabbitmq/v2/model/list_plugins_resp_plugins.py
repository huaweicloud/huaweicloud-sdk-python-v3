# coding: utf-8

import pprint
import re

import six





class ListPluginsRespPlugins:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'running': 'bool',
        'enable': 'bool',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'running': 'running',
        'enable': 'enable',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, running=None, enable=None, name=None, version=None):
        """ListPluginsRespPlugins - a model defined in huaweicloud sdk"""
        
        

        self._running = None
        self._enable = None
        self._name = None
        self._version = None
        self.discriminator = None

        if running is not None:
            self.running = running
        if enable is not None:
            self.enable = enable
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def running(self):
        """Gets the running of this ListPluginsRespPlugins.

        是否运行。

        :return: The running of this ListPluginsRespPlugins.
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this ListPluginsRespPlugins.

        是否运行。

        :param running: The running of this ListPluginsRespPlugins.
        :type: bool
        """
        self._running = running

    @property
    def enable(self):
        """Gets the enable of this ListPluginsRespPlugins.

        是否启用。

        :return: The enable of this ListPluginsRespPlugins.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ListPluginsRespPlugins.

        是否启用。

        :param enable: The enable of this ListPluginsRespPlugins.
        :type: bool
        """
        self._enable = enable

    @property
    def name(self):
        """Gets the name of this ListPluginsRespPlugins.

        插件名称。

        :return: The name of this ListPluginsRespPlugins.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPluginsRespPlugins.

        插件名称。

        :param name: The name of this ListPluginsRespPlugins.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this ListPluginsRespPlugins.

        插件版本。

        :return: The version of this ListPluginsRespPlugins.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListPluginsRespPlugins.

        插件版本。

        :param version: The version of this ListPluginsRespPlugins.
        :type: str
        """
        self._version = version

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
        if not isinstance(other, ListPluginsRespPlugins):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
