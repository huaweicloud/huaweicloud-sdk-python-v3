# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCentralNetworkErRouteTableAttachmentsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'central_network_er_route_table_attachment': 'CreateCentralNetworkErRouteTableAttachment'
    }

    attribute_map = {
        'central_network_er_route_table_attachment': 'central_network_er_route_table_attachment'
    }

    def __init__(self, central_network_er_route_table_attachment=None):
        """CreateCentralNetworkErRouteTableAttachmentsRequestBody

        The model defined in huaweicloud sdk

        :param central_network_er_route_table_attachment: 
        :type central_network_er_route_table_attachment: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkErRouteTableAttachment`
        """
        
        

        self._central_network_er_route_table_attachment = None
        self.discriminator = None

        self.central_network_er_route_table_attachment = central_network_er_route_table_attachment

    @property
    def central_network_er_route_table_attachment(self):
        """Gets the central_network_er_route_table_attachment of this CreateCentralNetworkErRouteTableAttachmentsRequestBody.

        :return: The central_network_er_route_table_attachment of this CreateCentralNetworkErRouteTableAttachmentsRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkErRouteTableAttachment`
        """
        return self._central_network_er_route_table_attachment

    @central_network_er_route_table_attachment.setter
    def central_network_er_route_table_attachment(self, central_network_er_route_table_attachment):
        """Sets the central_network_er_route_table_attachment of this CreateCentralNetworkErRouteTableAttachmentsRequestBody.

        :param central_network_er_route_table_attachment: The central_network_er_route_table_attachment of this CreateCentralNetworkErRouteTableAttachmentsRequestBody.
        :type central_network_er_route_table_attachment: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkErRouteTableAttachment`
        """
        self._central_network_er_route_table_attachment = central_network_er_route_table_attachment

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
        if not isinstance(other, CreateCentralNetworkErRouteTableAttachmentsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
