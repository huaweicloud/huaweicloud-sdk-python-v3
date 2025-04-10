# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalDcGatewayPeerLinkId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_dc_gateway_peer_link_id': 'str'
    }

    attribute_map = {
        'global_dc_gateway_peer_link_id': 'global_dc_gateway_peer_link_id'
    }

    def __init__(self, global_dc_gateway_peer_link_id=None):
        r"""GlobalDcGatewayPeerLinkId

        The model defined in huaweicloud sdk

        :param global_dc_gateway_peer_link_id: GDGW的连接ID。
        :type global_dc_gateway_peer_link_id: str
        """
        
        

        self._global_dc_gateway_peer_link_id = None
        self.discriminator = None

        if global_dc_gateway_peer_link_id is not None:
            self.global_dc_gateway_peer_link_id = global_dc_gateway_peer_link_id

    @property
    def global_dc_gateway_peer_link_id(self):
        r"""Gets the global_dc_gateway_peer_link_id of this GlobalDcGatewayPeerLinkId.

        GDGW的连接ID。

        :return: The global_dc_gateway_peer_link_id of this GlobalDcGatewayPeerLinkId.
        :rtype: str
        """
        return self._global_dc_gateway_peer_link_id

    @global_dc_gateway_peer_link_id.setter
    def global_dc_gateway_peer_link_id(self, global_dc_gateway_peer_link_id):
        r"""Sets the global_dc_gateway_peer_link_id of this GlobalDcGatewayPeerLinkId.

        GDGW的连接ID。

        :param global_dc_gateway_peer_link_id: The global_dc_gateway_peer_link_id of this GlobalDcGatewayPeerLinkId.
        :type global_dc_gateway_peer_link_id: str
        """
        self._global_dc_gateway_peer_link_id = global_dc_gateway_peer_link_id

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
        if not isinstance(other, GlobalDcGatewayPeerLinkId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
