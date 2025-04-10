# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateP2PSiteNetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'p2p_site_network': 'CreateP2PSiteNetwork'
    }

    attribute_map = {
        'p2p_site_network': 'p2p_site_network'
    }

    def __init__(self, p2p_site_network=None):
        r"""CreateP2PSiteNetworkRequestBody

        The model defined in huaweicloud sdk

        :param p2p_site_network: 
        :type p2p_site_network: :class:`huaweicloudsdkcc.v3.CreateP2PSiteNetwork`
        """
        
        

        self._p2p_site_network = None
        self.discriminator = None

        self.p2p_site_network = p2p_site_network

    @property
    def p2p_site_network(self):
        r"""Gets the p2p_site_network of this CreateP2PSiteNetworkRequestBody.

        :return: The p2p_site_network of this CreateP2PSiteNetworkRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.CreateP2PSiteNetwork`
        """
        return self._p2p_site_network

    @p2p_site_network.setter
    def p2p_site_network(self, p2p_site_network):
        r"""Sets the p2p_site_network of this CreateP2PSiteNetworkRequestBody.

        :param p2p_site_network: The p2p_site_network of this CreateP2PSiteNetworkRequestBody.
        :type p2p_site_network: :class:`huaweicloudsdkcc.v3.CreateP2PSiteNetwork`
        """
        self._p2p_site_network = p2p_site_network

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
        if not isinstance(other, CreateP2PSiteNetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
