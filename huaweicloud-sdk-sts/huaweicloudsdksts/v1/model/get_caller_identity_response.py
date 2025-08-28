# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetCallerIdentityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'principal_urn': 'str',
        'principal_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'principal_urn': 'principal_urn',
        'principal_id': 'principal_id'
    }

    def __init__(self, account_id=None, principal_urn=None, principal_id=None):
        r"""GetCallerIdentityResponse

        The model defined in huaweicloud sdk

        :param account_id: 账号ID。
        :type account_id: str
        :param principal_urn: 主体URN。
        :type principal_urn: str
        :param principal_id: 主体ID。
        :type principal_id: str
        """
        
        super(GetCallerIdentityResponse, self).__init__()

        self._account_id = None
        self._principal_urn = None
        self._principal_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if principal_urn is not None:
            self.principal_urn = principal_urn
        if principal_id is not None:
            self.principal_id = principal_id

    @property
    def account_id(self):
        r"""Gets the account_id of this GetCallerIdentityResponse.

        账号ID。

        :return: The account_id of this GetCallerIdentityResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this GetCallerIdentityResponse.

        账号ID。

        :param account_id: The account_id of this GetCallerIdentityResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def principal_urn(self):
        r"""Gets the principal_urn of this GetCallerIdentityResponse.

        主体URN。

        :return: The principal_urn of this GetCallerIdentityResponse.
        :rtype: str
        """
        return self._principal_urn

    @principal_urn.setter
    def principal_urn(self, principal_urn):
        r"""Sets the principal_urn of this GetCallerIdentityResponse.

        主体URN。

        :param principal_urn: The principal_urn of this GetCallerIdentityResponse.
        :type principal_urn: str
        """
        self._principal_urn = principal_urn

    @property
    def principal_id(self):
        r"""Gets the principal_id of this GetCallerIdentityResponse.

        主体ID。

        :return: The principal_id of this GetCallerIdentityResponse.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this GetCallerIdentityResponse.

        主体ID。

        :param principal_id: The principal_id of this GetCallerIdentityResponse.
        :type principal_id: str
        """
        self._principal_id = principal_id

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
        if not isinstance(other, GetCallerIdentityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
