# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateNatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway': 'PrivateNat',
        'request_id': 'str'
    }

    attribute_map = {
        'gateway': 'gateway',
        'request_id': 'request_id'
    }

    def __init__(self, gateway=None, request_id=None):
        r"""CreatePrivateNatResponse

        The model defined in huaweicloud sdk

        :param gateway: 
        :type gateway: :class:`huaweicloudsdknat.v2.PrivateNat`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(CreatePrivateNatResponse, self).__init__()

        self._gateway = None
        self._request_id = None
        self.discriminator = None

        if gateway is not None:
            self.gateway = gateway
        if request_id is not None:
            self.request_id = request_id

    @property
    def gateway(self):
        r"""Gets the gateway of this CreatePrivateNatResponse.

        :return: The gateway of this CreatePrivateNatResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PrivateNat`
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        r"""Sets the gateway of this CreatePrivateNatResponse.

        :param gateway: The gateway of this CreatePrivateNatResponse.
        :type gateway: :class:`huaweicloudsdknat.v2.PrivateNat`
        """
        self._gateway = gateway

    @property
    def request_id(self):
        r"""Gets the request_id of this CreatePrivateNatResponse.

        请求ID。

        :return: The request_id of this CreatePrivateNatResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreatePrivateNatResponse.

        请求ID。

        :param request_id: The request_id of this CreatePrivateNatResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, CreatePrivateNatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
