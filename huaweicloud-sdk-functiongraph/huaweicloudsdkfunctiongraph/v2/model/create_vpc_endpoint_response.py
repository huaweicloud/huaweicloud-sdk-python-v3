# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcEndpointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[str]',
        'address': 'str'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'address': 'address'
    }

    def __init__(self, endpoints=None, address=None):
        r"""CreateVpcEndpointResponse

        The model defined in huaweicloud sdk

        :param endpoints: Ip列表
        :type endpoints: list[str]
        :param address: 域名地址
        :type address: str
        """
        
        super(CreateVpcEndpointResponse, self).__init__()

        self._endpoints = None
        self._address = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if address is not None:
            self.address = address

    @property
    def endpoints(self):
        r"""Gets the endpoints of this CreateVpcEndpointResponse.

        Ip列表

        :return: The endpoints of this CreateVpcEndpointResponse.
        :rtype: list[str]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this CreateVpcEndpointResponse.

        Ip列表

        :param endpoints: The endpoints of this CreateVpcEndpointResponse.
        :type endpoints: list[str]
        """
        self._endpoints = endpoints

    @property
    def address(self):
        r"""Gets the address of this CreateVpcEndpointResponse.

        域名地址

        :return: The address of this CreateVpcEndpointResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CreateVpcEndpointResponse.

        域名地址

        :param address: The address of this CreateVpcEndpointResponse.
        :type address: str
        """
        self._address = address

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
        if not isinstance(other, CreateVpcEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
