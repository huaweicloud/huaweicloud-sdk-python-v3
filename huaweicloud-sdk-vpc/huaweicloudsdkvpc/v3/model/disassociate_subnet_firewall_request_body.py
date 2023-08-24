# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateSubnetFirewallRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnets': 'list[FirewallAssociation]'
    }

    attribute_map = {
        'subnets': 'subnets'
    }

    def __init__(self, subnets=None):
        """DisassociateSubnetFirewallRequestBody

        The model defined in huaweicloud sdk

        :param subnets: 解绑ACL的子网列表
        :type subnets: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        """
        
        

        self._subnets = None
        self.discriminator = None

        self.subnets = subnets

    @property
    def subnets(self):
        """Gets the subnets of this DisassociateSubnetFirewallRequestBody.

        解绑ACL的子网列表

        :return: The subnets of this DisassociateSubnetFirewallRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this DisassociateSubnetFirewallRequestBody.

        解绑ACL的子网列表

        :param subnets: The subnets of this DisassociateSubnetFirewallRequestBody.
        :type subnets: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        """
        self._subnets = subnets

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
        if not isinstance(other, DisassociateSubnetFirewallRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
