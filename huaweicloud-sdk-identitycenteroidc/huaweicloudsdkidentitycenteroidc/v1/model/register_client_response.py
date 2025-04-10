# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterClientResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_info': 'ClientInfoDto'
    }

    attribute_map = {
        'client_info': 'client_info'
    }

    def __init__(self, client_info=None):
        r"""RegisterClientResponse

        The model defined in huaweicloud sdk

        :param client_info: 
        :type client_info: :class:`huaweicloudsdkidentitycenteroidc.v1.ClientInfoDto`
        """
        
        super(RegisterClientResponse, self).__init__()

        self._client_info = None
        self.discriminator = None

        if client_info is not None:
            self.client_info = client_info

    @property
    def client_info(self):
        r"""Gets the client_info of this RegisterClientResponse.

        :return: The client_info of this RegisterClientResponse.
        :rtype: :class:`huaweicloudsdkidentitycenteroidc.v1.ClientInfoDto`
        """
        return self._client_info

    @client_info.setter
    def client_info(self, client_info):
        r"""Sets the client_info of this RegisterClientResponse.

        :param client_info: The client_info of this RegisterClientResponse.
        :type client_info: :class:`huaweicloudsdkidentitycenteroidc.v1.ClientInfoDto`
        """
        self._client_info = client_info

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
        if not isinstance(other, RegisterClientResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
