# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCgwRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_gateway_id': 'str'
    }

    attribute_map = {
        'customer_gateway_id': 'customer_gateway_id'
    }

    def __init__(self, customer_gateway_id=None):
        """DeleteCgwRequest

        The model defined in huaweicloud sdk

        :param customer_gateway_id: 对端网关ID
        :type customer_gateway_id: str
        """
        
        

        self._customer_gateway_id = None
        self.discriminator = None

        self.customer_gateway_id = customer_gateway_id

    @property
    def customer_gateway_id(self):
        """Gets the customer_gateway_id of this DeleteCgwRequest.

        对端网关ID

        :return: The customer_gateway_id of this DeleteCgwRequest.
        :rtype: str
        """
        return self._customer_gateway_id

    @customer_gateway_id.setter
    def customer_gateway_id(self, customer_gateway_id):
        """Sets the customer_gateway_id of this DeleteCgwRequest.

        对端网关ID

        :param customer_gateway_id: The customer_gateway_id of this DeleteCgwRequest.
        :type customer_gateway_id: str
        """
        self._customer_gateway_id = customer_gateway_id

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
        if not isinstance(other, DeleteCgwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
