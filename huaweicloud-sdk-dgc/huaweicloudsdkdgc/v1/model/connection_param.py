# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionParam:

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
        'params': 'object'
    }

    attribute_map = {
        'name': 'name',
        'connection_type': 'connectionType',
        'params': 'params'
    }

    def __init__(self, name=None, connection_type=None, params=None):
        """ConnectionParam

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param connection_type: 
        :type connection_type: str
        :param params: 
        :type params: object
        """
        
        

        self._name = None
        self._connection_type = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if connection_type is not None:
            self.connection_type = connection_type
        if params is not None:
            self.params = params

    @property
    def name(self):
        """Gets the name of this ConnectionParam.

        :return: The name of this ConnectionParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionParam.

        :param name: The name of this ConnectionParam.
        :type name: str
        """
        self._name = name

    @property
    def connection_type(self):
        """Gets the connection_type of this ConnectionParam.

        :return: The connection_type of this ConnectionParam.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this ConnectionParam.

        :param connection_type: The connection_type of this ConnectionParam.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def params(self):
        """Gets the params of this ConnectionParam.

        :return: The params of this ConnectionParam.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ConnectionParam.

        :param params: The params of this ConnectionParam.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, ConnectionParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
