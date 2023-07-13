# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseMultiAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_customer_id': 'str',
        'balance_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'sub_customer_id': 'sub_customer_id',
        'balance_type': 'balance_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, sub_customer_id=None, balance_type=None, offset=None, limit=None):
        """ListEnterpriseMultiAccountRequest

        The model defined in huaweicloud sdk

        :param sub_customer_id: 企业子账户的账号ID。
        :type sub_customer_id: str
        :param balance_type: 账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户
        :type balance_type: str
        :param offset: 偏移量，默认值为0。只有信用账户有效。
        :type offset: int
        :param limit: 每次查询条数，默认值为10。只有信用账户有效。
        :type limit: int
        """
        
        

        self._sub_customer_id = None
        self._balance_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.sub_customer_id = sub_customer_id
        self.balance_type = balance_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListEnterpriseMultiAccountRequest.

        企业子账户的账号ID。

        :return: The sub_customer_id of this ListEnterpriseMultiAccountRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListEnterpriseMultiAccountRequest.

        企业子账户的账号ID。

        :param sub_customer_id: The sub_customer_id of this ListEnterpriseMultiAccountRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def balance_type(self):
        """Gets the balance_type of this ListEnterpriseMultiAccountRequest.

        账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户

        :return: The balance_type of this ListEnterpriseMultiAccountRequest.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this ListEnterpriseMultiAccountRequest.

        账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户

        :param balance_type: The balance_type of this ListEnterpriseMultiAccountRequest.
        :type balance_type: str
        """
        self._balance_type = balance_type

    @property
    def offset(self):
        """Gets the offset of this ListEnterpriseMultiAccountRequest.

        偏移量，默认值为0。只有信用账户有效。

        :return: The offset of this ListEnterpriseMultiAccountRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnterpriseMultiAccountRequest.

        偏移量，默认值为0。只有信用账户有效。

        :param offset: The offset of this ListEnterpriseMultiAccountRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnterpriseMultiAccountRequest.

        每次查询条数，默认值为10。只有信用账户有效。

        :return: The limit of this ListEnterpriseMultiAccountRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnterpriseMultiAccountRequest.

        每次查询条数，默认值为10。只有信用账户有效。

        :param limit: The limit of this ListEnterpriseMultiAccountRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEnterpriseMultiAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
