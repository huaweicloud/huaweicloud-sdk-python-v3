# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAgenciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('access_token')

    openapi_types = {
        'access_token': 'str',
        'limit': 'int',
        'marker': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'access_token': 'access-token',
        'limit': 'limit',
        'marker': 'marker',
        'account_id': 'account_id'
    }

    def __init__(self, access_token=None, limit=None, marker=None, account_id=None):
        r"""ListAccountAgenciesRequest

        The model defined in huaweicloud sdk

        :param access_token: 创建令牌接口调用签发的访问令牌
        :type access_token: str
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param marker: 分页标记。非分页的接口，不使用该值。
        :type marker: str
        :param account_id: 帐户的全局唯一标识符（ID）
        :type account_id: str
        """
        
        

        self._access_token = None
        self._limit = None
        self._marker = None
        self._account_id = None
        self.discriminator = None

        self.access_token = access_token
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.account_id = account_id

    @property
    def access_token(self):
        r"""Gets the access_token of this ListAccountAgenciesRequest.

        创建令牌接口调用签发的访问令牌

        :return: The access_token of this ListAccountAgenciesRequest.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this ListAccountAgenciesRequest.

        创建令牌接口调用签发的访问令牌

        :param access_token: The access_token of this ListAccountAgenciesRequest.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def limit(self):
        r"""Gets the limit of this ListAccountAgenciesRequest.

        页面中最大结果数量。

        :return: The limit of this ListAccountAgenciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAccountAgenciesRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListAccountAgenciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAccountAgenciesRequest.

        分页标记。非分页的接口，不使用该值。

        :return: The marker of this ListAccountAgenciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAccountAgenciesRequest.

        分页标记。非分页的接口，不使用该值。

        :param marker: The marker of this ListAccountAgenciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def account_id(self):
        r"""Gets the account_id of this ListAccountAgenciesRequest.

        帐户的全局唯一标识符（ID）

        :return: The account_id of this ListAccountAgenciesRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ListAccountAgenciesRequest.

        帐户的全局唯一标识符（ID）

        :param account_id: The account_id of this ListAccountAgenciesRequest.
        :type account_id: str
        """
        self._account_id = account_id

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
        if not isinstance(other, ListAccountAgenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
