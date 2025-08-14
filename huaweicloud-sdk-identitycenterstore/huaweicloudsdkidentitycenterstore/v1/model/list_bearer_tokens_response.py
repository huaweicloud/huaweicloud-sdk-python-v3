# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBearerTokensResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bearer_tokens': 'list[BearerToken]'
    }

    attribute_map = {
        'bearer_tokens': 'bearer_tokens'
    }

    def __init__(self, bearer_tokens=None):
        r"""ListBearerTokensResponse

        The model defined in huaweicloud sdk

        :param bearer_tokens: 访问令牌列表
        :type bearer_tokens: list[:class:`huaweicloudsdkidentitycenterstore.v1.BearerToken`]
        """
        
        super(ListBearerTokensResponse, self).__init__()

        self._bearer_tokens = None
        self.discriminator = None

        if bearer_tokens is not None:
            self.bearer_tokens = bearer_tokens

    @property
    def bearer_tokens(self):
        r"""Gets the bearer_tokens of this ListBearerTokensResponse.

        访问令牌列表

        :return: The bearer_tokens of this ListBearerTokensResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.BearerToken`]
        """
        return self._bearer_tokens

    @bearer_tokens.setter
    def bearer_tokens(self, bearer_tokens):
        r"""Sets the bearer_tokens of this ListBearerTokensResponse.

        访问令牌列表

        :param bearer_tokens: The bearer_tokens of this ListBearerTokensResponse.
        :type bearer_tokens: list[:class:`huaweicloudsdkidentitycenterstore.v1.BearerToken`]
        """
        self._bearer_tokens = bearer_tokens

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
        if not isinstance(other, ListBearerTokensResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
