# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowConnectionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'connection_type': 'str',
        'config': 'object'
    }

    attribute_map = {
        'name': 'name',
        'connection_type': 'connectionType',
        'config': 'config'
    }

    def __init__(self, name=None, connection_type=None, config=None):
        """ShowConnectionResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._name = None
        self._connection_type = None
        self._config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if connection_type is not None:
            self.connection_type = connection_type
        if config is not None:
            self.config = config

    @property
    def name(self):
        """Gets the name of this ShowConnectionResponse.


        :return: The name of this ShowConnectionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowConnectionResponse.


        :param name: The name of this ShowConnectionResponse.
        :type: str
        """
        self._name = name

    @property
    def connection_type(self):
        """Gets the connection_type of this ShowConnectionResponse.


        :return: The connection_type of this ShowConnectionResponse.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this ShowConnectionResponse.


        :param connection_type: The connection_type of this ShowConnectionResponse.
        :type: str
        """
        self._connection_type = connection_type

    @property
    def config(self):
        """Gets the config of this ShowConnectionResponse.


        :return: The config of this ShowConnectionResponse.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ShowConnectionResponse.


        :param config: The config of this ShowConnectionResponse.
        :type: object
        """
        self._config = config

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
        if not isinstance(other, ShowConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
