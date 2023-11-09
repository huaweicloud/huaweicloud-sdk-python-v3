# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_gateway': 'UpdateVgwRequestBodyContent'
    }

    attribute_map = {
        'vpn_gateway': 'vpn_gateway'
    }

    def __init__(self, vpn_gateway=None):
        """UpdateVgwRequestBody

        The model defined in huaweicloud sdk

        :param vpn_gateway: 
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBodyContent`
        """
        
        

        self._vpn_gateway = None
        self.discriminator = None

        self.vpn_gateway = vpn_gateway

    @property
    def vpn_gateway(self):
        """Gets the vpn_gateway of this UpdateVgwRequestBody.

        :return: The vpn_gateway of this UpdateVgwRequestBody.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBodyContent`
        """
        return self._vpn_gateway

    @vpn_gateway.setter
    def vpn_gateway(self, vpn_gateway):
        """Sets the vpn_gateway of this UpdateVgwRequestBody.

        :param vpn_gateway: The vpn_gateway of this UpdateVgwRequestBody.
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBodyContent`
        """
        self._vpn_gateway = vpn_gateway

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
        if not isinstance(other, UpdateVgwRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
