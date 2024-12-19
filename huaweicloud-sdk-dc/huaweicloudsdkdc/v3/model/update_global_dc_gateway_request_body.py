# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalDcGatewayRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_dc_gateway': 'UpdateGlobalDcGateway'
    }

    attribute_map = {
        'global_dc_gateway': 'global_dc_gateway'
    }

    def __init__(self, global_dc_gateway=None):
        """UpdateGlobalDcGatewayRequestBody

        The model defined in huaweicloud sdk

        :param global_dc_gateway: 
        :type global_dc_gateway: :class:`huaweicloudsdkdc.v3.UpdateGlobalDcGateway`
        """
        
        

        self._global_dc_gateway = None
        self.discriminator = None

        self.global_dc_gateway = global_dc_gateway

    @property
    def global_dc_gateway(self):
        """Gets the global_dc_gateway of this UpdateGlobalDcGatewayRequestBody.

        :return: The global_dc_gateway of this UpdateGlobalDcGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateGlobalDcGateway`
        """
        return self._global_dc_gateway

    @global_dc_gateway.setter
    def global_dc_gateway(self, global_dc_gateway):
        """Sets the global_dc_gateway of this UpdateGlobalDcGatewayRequestBody.

        :param global_dc_gateway: The global_dc_gateway of this UpdateGlobalDcGatewayRequestBody.
        :type global_dc_gateway: :class:`huaweicloudsdkdc.v3.UpdateGlobalDcGateway`
        """
        self._global_dc_gateway = global_dc_gateway

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
        if not isinstance(other, UpdateGlobalDcGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
