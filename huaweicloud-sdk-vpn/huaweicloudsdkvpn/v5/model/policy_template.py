# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ike_policy': 'VgwIkePolicy',
        'ipsec_policy': 'VgwIpsecPolicy'
    }

    attribute_map = {
        'ike_policy': 'ike_policy',
        'ipsec_policy': 'ipsec_policy'
    }

    def __init__(self, ike_policy=None, ipsec_policy=None):
        r"""PolicyTemplate

        The model defined in huaweicloud sdk

        :param ike_policy: 
        :type ike_policy: :class:`huaweicloudsdkvpn.v5.VgwIkePolicy`
        :param ipsec_policy: 
        :type ipsec_policy: :class:`huaweicloudsdkvpn.v5.VgwIpsecPolicy`
        """
        
        

        self._ike_policy = None
        self._ipsec_policy = None
        self.discriminator = None

        if ike_policy is not None:
            self.ike_policy = ike_policy
        if ipsec_policy is not None:
            self.ipsec_policy = ipsec_policy

    @property
    def ike_policy(self):
        r"""Gets the ike_policy of this PolicyTemplate.

        :return: The ike_policy of this PolicyTemplate.
        :rtype: :class:`huaweicloudsdkvpn.v5.VgwIkePolicy`
        """
        return self._ike_policy

    @ike_policy.setter
    def ike_policy(self, ike_policy):
        r"""Sets the ike_policy of this PolicyTemplate.

        :param ike_policy: The ike_policy of this PolicyTemplate.
        :type ike_policy: :class:`huaweicloudsdkvpn.v5.VgwIkePolicy`
        """
        self._ike_policy = ike_policy

    @property
    def ipsec_policy(self):
        r"""Gets the ipsec_policy of this PolicyTemplate.

        :return: The ipsec_policy of this PolicyTemplate.
        :rtype: :class:`huaweicloudsdkvpn.v5.VgwIpsecPolicy`
        """
        return self._ipsec_policy

    @ipsec_policy.setter
    def ipsec_policy(self, ipsec_policy):
        r"""Sets the ipsec_policy of this PolicyTemplate.

        :param ipsec_policy: The ipsec_policy of this PolicyTemplate.
        :type ipsec_policy: :class:`huaweicloudsdkvpn.v5.VgwIpsecPolicy`
        """
        self._ipsec_policy = ipsec_policy

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
        if not isinstance(other, PolicyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
