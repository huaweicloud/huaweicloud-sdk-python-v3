# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalGatewayInfoOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_id': 'str'
    }

    attribute_map = {
        'network_id': 'network_id'
    }

    def __init__(self, network_id=None):
        """ExternalGatewayInfoOption

        The model defined in huaweicloud sdk

        :param network_id: 外部网络的ID。 外部网络的信息请通过GET /v2.0/networks?router:external&#x3D;True或neutron net-external-list方式查询。
        :type network_id: str
        """
        
        

        self._network_id = None
        self.discriminator = None

        if network_id is not None:
            self.network_id = network_id

    @property
    def network_id(self):
        """Gets the network_id of this ExternalGatewayInfoOption.

        外部网络的ID。 外部网络的信息请通过GET /v2.0/networks?router:external=True或neutron net-external-list方式查询。

        :return: The network_id of this ExternalGatewayInfoOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this ExternalGatewayInfoOption.

        外部网络的ID。 外部网络的信息请通过GET /v2.0/networks?router:external=True或neutron net-external-list方式查询。

        :param network_id: The network_id of this ExternalGatewayInfoOption.
        :type network_id: str
        """
        self._network_id = network_id

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
        if not isinstance(other, ExternalGatewayInfoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
