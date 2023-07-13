# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpenIdConnectConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_id': 'str',
        'body': 'CreateOpenIdConnectConfigRequestBody'
    }

    attribute_map = {
        'idp_id': 'idp_id',
        'body': 'body'
    }

    def __init__(self, idp_id=None, body=None):
        """CreateOpenIdConnectConfigRequest

        The model defined in huaweicloud sdk

        :param idp_id: 身份提供商ID
        :type idp_id: str
        :param body: Body of the CreateOpenIdConnectConfigRequest
        :type body: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigRequestBody`
        """
        
        

        self._idp_id = None
        self._body = None
        self.discriminator = None

        self.idp_id = idp_id
        if body is not None:
            self.body = body

    @property
    def idp_id(self):
        """Gets the idp_id of this CreateOpenIdConnectConfigRequest.

        身份提供商ID

        :return: The idp_id of this CreateOpenIdConnectConfigRequest.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        """Sets the idp_id of this CreateOpenIdConnectConfigRequest.

        身份提供商ID

        :param idp_id: The idp_id of this CreateOpenIdConnectConfigRequest.
        :type idp_id: str
        """
        self._idp_id = idp_id

    @property
    def body(self):
        """Gets the body of this CreateOpenIdConnectConfigRequest.

        :return: The body of this CreateOpenIdConnectConfigRequest.
        :rtype: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateOpenIdConnectConfigRequest.

        :param body: The body of this CreateOpenIdConnectConfigRequest.
        :type body: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigRequestBody`
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
        if not isinstance(other, CreateOpenIdConnectConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
