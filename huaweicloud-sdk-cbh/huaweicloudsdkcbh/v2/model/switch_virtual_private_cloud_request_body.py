# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchVirtualPrivateCloudRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'network': 'NetworkInfoCreate'
    }

    attribute_map = {
        'server_id': 'server_id',
        'network': 'network'
    }

    def __init__(self, server_id=None, network=None):
        """SwitchVirtualPrivateCloudRequestBody

        The model defined in huaweicloud sdk

        :param server_id: 需要切换vpc的实例id
        :type server_id: str
        :param network: 
        :type network: :class:`huaweicloudsdkcbh.v2.NetworkInfoCreate`
        """
        
        

        self._server_id = None
        self._network = None
        self.discriminator = None

        self.server_id = server_id
        self.network = network

    @property
    def server_id(self):
        """Gets the server_id of this SwitchVirtualPrivateCloudRequestBody.

        需要切换vpc的实例id

        :return: The server_id of this SwitchVirtualPrivateCloudRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this SwitchVirtualPrivateCloudRequestBody.

        需要切换vpc的实例id

        :param server_id: The server_id of this SwitchVirtualPrivateCloudRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def network(self):
        """Gets the network of this SwitchVirtualPrivateCloudRequestBody.

        :return: The network of this SwitchVirtualPrivateCloudRequestBody.
        :rtype: :class:`huaweicloudsdkcbh.v2.NetworkInfoCreate`
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this SwitchVirtualPrivateCloudRequestBody.

        :param network: The network of this SwitchVirtualPrivateCloudRequestBody.
        :type network: :class:`huaweicloudsdkcbh.v2.NetworkInfoCreate`
        """
        self._network = network

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
        if not isinstance(other, SwitchVirtualPrivateCloudRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
