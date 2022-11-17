# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVersionAliasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'body': 'CreateVersionAliasRequestBody'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'body': 'body'
    }

    def __init__(self, function_urn=None, body=None):
        """CreateVersionAliasRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN。
        :type function_urn: str
        :param body: Body of the CreateVersionAliasRequest
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasRequestBody`
        """
        
        

        self._function_urn = None
        self._body = None
        self.discriminator = None

        self.function_urn = function_urn
        if body is not None:
            self.body = body

    @property
    def function_urn(self):
        """Gets the function_urn of this CreateVersionAliasRequest.

        函数的URN。

        :return: The function_urn of this CreateVersionAliasRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this CreateVersionAliasRequest.

        函数的URN。

        :param function_urn: The function_urn of this CreateVersionAliasRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def body(self):
        """Gets the body of this CreateVersionAliasRequest.

        :return: The body of this CreateVersionAliasRequest.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateVersionAliasRequest.

        :param body: The body of this CreateVersionAliasRequest.
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasRequestBody`
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
        if not isinstance(other, CreateVersionAliasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
