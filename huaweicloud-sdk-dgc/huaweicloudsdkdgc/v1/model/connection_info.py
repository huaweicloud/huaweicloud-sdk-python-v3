# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionInfo:

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
        'type': 'str',
        'config': 'object',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'config': 'config',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, config=None, description=None):
        """ConnectionInfo

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param type: 
        :type type: str
        :param config: 
        :type config: object
        :param description: 
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._config = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.type = type
        if config is not None:
            self.config = config
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ConnectionInfo.

        :return: The name of this ConnectionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionInfo.

        :param name: The name of this ConnectionInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ConnectionInfo.

        :return: The type of this ConnectionInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectionInfo.

        :param type: The type of this ConnectionInfo.
        :type type: str
        """
        self._type = type

    @property
    def config(self):
        """Gets the config of this ConnectionInfo.

        :return: The config of this ConnectionInfo.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ConnectionInfo.

        :param config: The config of this ConnectionInfo.
        :type config: object
        """
        self._config = config

    @property
    def description(self):
        """Gets the description of this ConnectionInfo.

        :return: The description of this ConnectionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectionInfo.

        :param description: The description of this ConnectionInfo.
        :type description: str
        """
        self._description = description

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
