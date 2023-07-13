# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFirewallResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'firewall': 'Firewall'
    }

    attribute_map = {
        'firewall': 'firewall'
    }

    def __init__(self, firewall=None):
        """ShowFirewallResponse

        The model defined in huaweicloud sdk

        :param firewall: 
        :type firewall: :class:`huaweicloudsdkiec.v1.Firewall`
        """
        
        super(ShowFirewallResponse, self).__init__()

        self._firewall = None
        self.discriminator = None

        if firewall is not None:
            self.firewall = firewall

    @property
    def firewall(self):
        """Gets the firewall of this ShowFirewallResponse.

        :return: The firewall of this ShowFirewallResponse.
        :rtype: :class:`huaweicloudsdkiec.v1.Firewall`
        """
        return self._firewall

    @firewall.setter
    def firewall(self, firewall):
        """Sets the firewall of this ShowFirewallResponse.

        :param firewall: The firewall of this ShowFirewallResponse.
        :type firewall: :class:`huaweicloudsdkiec.v1.Firewall`
        """
        self._firewall = firewall

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
        if not isinstance(other, ShowFirewallResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
