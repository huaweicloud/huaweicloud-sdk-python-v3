# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateFirewallGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_group': 'NeutronFirewallGroup'
    }

    attribute_map = {
        'firewall_group': 'firewall_group'
    }

    def __init__(self, firewall_group=None):
        """NeutronCreateFirewallGroupResponse

        The model defined in huaweicloud sdk

        :param firewall_group: 
        :type firewall_group: :class:`huaweicloudsdkvpc.v2.NeutronFirewallGroup`
        """
        
        super(NeutronCreateFirewallGroupResponse, self).__init__()

        self._firewall_group = None
        self.discriminator = None

        if firewall_group is not None:
            self.firewall_group = firewall_group

    @property
    def firewall_group(self):
        """Gets the firewall_group of this NeutronCreateFirewallGroupResponse.


        :return: The firewall_group of this NeutronCreateFirewallGroupResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronFirewallGroup`
        """
        return self._firewall_group

    @firewall_group.setter
    def firewall_group(self, firewall_group):
        """Sets the firewall_group of this NeutronCreateFirewallGroupResponse.


        :param firewall_group: The firewall_group of this NeutronCreateFirewallGroupResponse.
        :type firewall_group: :class:`huaweicloudsdkvpc.v2.NeutronFirewallGroup`
        """
        self._firewall_group = firewall_group

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
        if not isinstance(other, NeutronCreateFirewallGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
