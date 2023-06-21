# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePortResponseModelData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str',
        'port_type': 'int'
    }

    attribute_map = {
        'port': 'port',
        'port_type': 'port_type'
    }

    def __init__(self, port=None, port_type=None):
        """DeletePortResponseModelData

        The model defined in huaweicloud sdk

        :param port: 通道号。  
        :type port: str
        :param port_type: 通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  
        :type port_type: int
        """
        
        

        self._port = None
        self._port_type = None
        self.discriminator = None

        self.port = port
        self.port_type = port_type

    @property
    def port(self):
        """Gets the port of this DeletePortResponseModelData.

        通道号。  

        :return: The port of this DeletePortResponseModelData.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeletePortResponseModelData.

        通道号。  

        :param port: The port of this DeletePortResponseModelData.
        :type port: str
        """
        self._port = port

    @property
    def port_type(self):
        """Gets the port_type of this DeletePortResponseModelData.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  

        :return: The port_type of this DeletePortResponseModelData.
        :rtype: int
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this DeletePortResponseModelData.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  

        :param port_type: The port_type of this DeletePortResponseModelData.
        :type port_type: int
        """
        self._port_type = port_type

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
        if not isinstance(other, DeletePortResponseModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
