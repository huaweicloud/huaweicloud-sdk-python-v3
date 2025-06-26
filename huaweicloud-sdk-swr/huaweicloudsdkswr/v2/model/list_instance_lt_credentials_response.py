# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceLtCredentialsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'auth_tokens': 'list[AuthToken]'
    }

    attribute_map = {
        'total': 'total',
        'auth_tokens': 'auth_tokens'
    }

    def __init__(self, total=None, auth_tokens=None):
        r"""ListInstanceLtCredentialsResponse

        The model defined in huaweicloud sdk

        :param total: 长期访问凭据总数
        :type total: int
        :param auth_tokens: 长期访问凭证列表
        :type auth_tokens: list[:class:`huaweicloudsdkswr.v2.AuthToken`]
        """
        
        super(ListInstanceLtCredentialsResponse, self).__init__()

        self._total = None
        self._auth_tokens = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if auth_tokens is not None:
            self.auth_tokens = auth_tokens

    @property
    def total(self):
        r"""Gets the total of this ListInstanceLtCredentialsResponse.

        长期访问凭据总数

        :return: The total of this ListInstanceLtCredentialsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceLtCredentialsResponse.

        长期访问凭据总数

        :param total: The total of this ListInstanceLtCredentialsResponse.
        :type total: int
        """
        self._total = total

    @property
    def auth_tokens(self):
        r"""Gets the auth_tokens of this ListInstanceLtCredentialsResponse.

        长期访问凭证列表

        :return: The auth_tokens of this ListInstanceLtCredentialsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.AuthToken`]
        """
        return self._auth_tokens

    @auth_tokens.setter
    def auth_tokens(self, auth_tokens):
        r"""Sets the auth_tokens of this ListInstanceLtCredentialsResponse.

        长期访问凭证列表

        :param auth_tokens: The auth_tokens of this ListInstanceLtCredentialsResponse.
        :type auth_tokens: list[:class:`huaweicloudsdkswr.v2.AuthToken`]
        """
        self._auth_tokens = auth_tokens

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
        if not isinstance(other, ListInstanceLtCredentialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
