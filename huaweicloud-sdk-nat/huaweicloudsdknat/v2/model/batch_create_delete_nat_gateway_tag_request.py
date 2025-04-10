# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDeleteNatGatewayTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_gateway_id': 'str',
        'body': 'BatchCreateDeleteNatTagsRequestBody'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id',
        'body': 'body'
    }

    def __init__(self, nat_gateway_id=None, body=None):
        r"""BatchCreateDeleteNatGatewayTagRequest

        The model defined in huaweicloud sdk

        :param nat_gateway_id: 公网NAT网关ID。
        :type nat_gateway_id: str
        :param body: Body of the BatchCreateDeleteNatGatewayTagRequest
        :type body: :class:`huaweicloudsdknat.v2.BatchCreateDeleteNatTagsRequestBody`
        """
        
        

        self._nat_gateway_id = None
        self._body = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id
        if body is not None:
            self.body = body

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this BatchCreateDeleteNatGatewayTagRequest.

        公网NAT网关ID。

        :return: The nat_gateway_id of this BatchCreateDeleteNatGatewayTagRequest.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this BatchCreateDeleteNatGatewayTagRequest.

        公网NAT网关ID。

        :param nat_gateway_id: The nat_gateway_id of this BatchCreateDeleteNatGatewayTagRequest.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateDeleteNatGatewayTagRequest.

        :return: The body of this BatchCreateDeleteNatGatewayTagRequest.
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeleteNatTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateDeleteNatGatewayTagRequest.

        :param body: The body of this BatchCreateDeleteNatGatewayTagRequest.
        :type body: :class:`huaweicloudsdknat.v2.BatchCreateDeleteNatTagsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchCreateDeleteNatGatewayTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
