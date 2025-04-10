# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTokenWithIdTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_idp_id': 'str',
        'body': 'GetIdTokenRequestBody'
    }

    attribute_map = {
        'x_idp_id': 'X-Idp-Id',
        'body': 'body'
    }

    def __init__(self, x_idp_id=None, body=None):
        r"""CreateTokenWithIdTokenRequest

        The model defined in huaweicloud sdk

        :param x_idp_id: 身份提供商ID。
        :type x_idp_id: str
        :param body: Body of the CreateTokenWithIdTokenRequest
        :type body: :class:`huaweicloudsdkiam.v3.GetIdTokenRequestBody`
        """
        
        

        self._x_idp_id = None
        self._body = None
        self.discriminator = None

        self.x_idp_id = x_idp_id
        if body is not None:
            self.body = body

    @property
    def x_idp_id(self):
        r"""Gets the x_idp_id of this CreateTokenWithIdTokenRequest.

        身份提供商ID。

        :return: The x_idp_id of this CreateTokenWithIdTokenRequest.
        :rtype: str
        """
        return self._x_idp_id

    @x_idp_id.setter
    def x_idp_id(self, x_idp_id):
        r"""Sets the x_idp_id of this CreateTokenWithIdTokenRequest.

        身份提供商ID。

        :param x_idp_id: The x_idp_id of this CreateTokenWithIdTokenRequest.
        :type x_idp_id: str
        """
        self._x_idp_id = x_idp_id

    @property
    def body(self):
        r"""Gets the body of this CreateTokenWithIdTokenRequest.

        :return: The body of this CreateTokenWithIdTokenRequest.
        :rtype: :class:`huaweicloudsdkiam.v3.GetIdTokenRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateTokenWithIdTokenRequest.

        :param body: The body of this CreateTokenWithIdTokenRequest.
        :type body: :class:`huaweicloudsdkiam.v3.GetIdTokenRequestBody`
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
        if not isinstance(other, CreateTokenWithIdTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
