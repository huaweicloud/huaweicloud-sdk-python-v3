# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePeerLinkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_dc_gateway_id': 'str',
        'body': 'CreateExternalPeerLinkRequestBody'
    }

    attribute_map = {
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'body': 'body'
    }

    def __init__(self, global_dc_gateway_id=None, body=None):
        r"""CreatePeerLinkRequest

        The model defined in huaweicloud sdk

        :param global_dc_gateway_id: 全域接入网关ID
        :type global_dc_gateway_id: str
        :param body: Body of the CreatePeerLinkRequest
        :type body: :class:`huaweicloudsdkdc.v3.CreateExternalPeerLinkRequestBody`
        """
        
        

        self._global_dc_gateway_id = None
        self._body = None
        self.discriminator = None

        self.global_dc_gateway_id = global_dc_gateway_id
        if body is not None:
            self.body = body

    @property
    def global_dc_gateway_id(self):
        r"""Gets the global_dc_gateway_id of this CreatePeerLinkRequest.

        全域接入网关ID

        :return: The global_dc_gateway_id of this CreatePeerLinkRequest.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        r"""Sets the global_dc_gateway_id of this CreatePeerLinkRequest.

        全域接入网关ID

        :param global_dc_gateway_id: The global_dc_gateway_id of this CreatePeerLinkRequest.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def body(self):
        r"""Gets the body of this CreatePeerLinkRequest.

        :return: The body of this CreatePeerLinkRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateExternalPeerLinkRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreatePeerLinkRequest.

        :param body: The body of this CreatePeerLinkRequest.
        :type body: :class:`huaweicloudsdkdc.v3.CreateExternalPeerLinkRequestBody`
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
        if not isinstance(other, CreatePeerLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
