# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePasswordAuthResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'AuthorizationVI'
    }

    attribute_map = {
        'authorization': 'authorization'
    }

    def __init__(self, authorization=None):
        """CreatePasswordAuthResponse

        The model defined in huaweicloud sdk

        :param authorization: 
        :type authorization: :class:`huaweicloudsdkservicestage.v2.AuthorizationVI`
        """
        
        super(CreatePasswordAuthResponse, self).__init__()

        self._authorization = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization

    @property
    def authorization(self):
        """Gets the authorization of this CreatePasswordAuthResponse.

        :return: The authorization of this CreatePasswordAuthResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.AuthorizationVI`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this CreatePasswordAuthResponse.

        :param authorization: The authorization of this CreatePasswordAuthResponse.
        :type authorization: :class:`huaweicloudsdkservicestage.v2.AuthorizationVI`
        """
        self._authorization = authorization

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
        if not isinstance(other, CreatePasswordAuthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
