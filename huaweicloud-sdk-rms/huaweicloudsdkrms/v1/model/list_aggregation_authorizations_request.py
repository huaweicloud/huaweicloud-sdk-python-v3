# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAggregationAuthorizationsRequest:

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
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, account_id=None, limit=None, marker=None):
        """ListAggregationAuthorizationsRequest

        The model defined in huaweicloud sdk

        :param account_id: 授权的帐号ID。
        :type account_id: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._account_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def account_id(self):
        """Gets the account_id of this ListAggregationAuthorizationsRequest.

        授权的帐号ID。

        :return: The account_id of this ListAggregationAuthorizationsRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ListAggregationAuthorizationsRequest.

        授权的帐号ID。

        :param account_id: The account_id of this ListAggregationAuthorizationsRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def limit(self):
        """Gets the limit of this ListAggregationAuthorizationsRequest.

        最大的返回数量

        :return: The limit of this ListAggregationAuthorizationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAggregationAuthorizationsRequest.

        最大的返回数量

        :param limit: The limit of this ListAggregationAuthorizationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAggregationAuthorizationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListAggregationAuthorizationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAggregationAuthorizationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListAggregationAuthorizationsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListAggregationAuthorizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
