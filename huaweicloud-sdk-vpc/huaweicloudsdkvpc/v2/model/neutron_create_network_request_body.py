# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateNetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network': 'NeutronCreateNetworkOption'
    }

    attribute_map = {
        'network': 'network'
    }

    def __init__(self, network=None):
        r"""NeutronCreateNetworkRequestBody

        The model defined in huaweicloud sdk

        :param network: 
        :type network: :class:`huaweicloudsdkvpc.v2.NeutronCreateNetworkOption`
        """
        
        

        self._network = None
        self.discriminator = None

        self.network = network

    @property
    def network(self):
        r"""Gets the network of this NeutronCreateNetworkRequestBody.

        :return: The network of this NeutronCreateNetworkRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateNetworkOption`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this NeutronCreateNetworkRequestBody.

        :param network: The network of this NeutronCreateNetworkRequestBody.
        :type network: :class:`huaweicloudsdkvpc.v2.NeutronCreateNetworkOption`
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
        if not isinstance(other, NeutronCreateNetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
