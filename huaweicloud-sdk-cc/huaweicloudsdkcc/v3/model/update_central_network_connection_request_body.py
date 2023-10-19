# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCentralNetworkConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'central_network_connection': 'UpdateCentralNetworkConnection'
    }

    attribute_map = {
        'central_network_connection': 'central_network_connection'
    }

    def __init__(self, central_network_connection=None):
        """UpdateCentralNetworkConnectionRequestBody

        The model defined in huaweicloud sdk

        :param central_network_connection: 
        :type central_network_connection: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnection`
        """
        
        

        self._central_network_connection = None
        self.discriminator = None

        self.central_network_connection = central_network_connection

    @property
    def central_network_connection(self):
        """Gets the central_network_connection of this UpdateCentralNetworkConnectionRequestBody.

        :return: The central_network_connection of this UpdateCentralNetworkConnectionRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnection`
        """
        return self._central_network_connection

    @central_network_connection.setter
    def central_network_connection(self, central_network_connection):
        """Sets the central_network_connection of this UpdateCentralNetworkConnectionRequestBody.

        :param central_network_connection: The central_network_connection of this UpdateCentralNetworkConnectionRequestBody.
        :type central_network_connection: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnection`
        """
        self._central_network_connection = central_network_connection

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
        if not isinstance(other, UpdateCentralNetworkConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
