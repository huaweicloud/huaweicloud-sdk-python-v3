# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyTransactionSplitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transaction_split': 'str',
        'proxy_id_list': 'list[str]'
    }

    attribute_map = {
        'transaction_split': 'transaction_split',
        'proxy_id_list': 'proxy_id_list'
    }

    def __init__(self, transaction_split=None, proxy_id_list=None):
        """ProxyTransactionSplitRequest

        The model defined in huaweicloud sdk

        :param transaction_split: 开启/关闭事务拆分，取值范围是[ON/OFF]
        :type transaction_split: str
        :param proxy_id_list: 实例的数据库代理列表，仅支持单proxy使用。
        :type proxy_id_list: list[str]
        """
        
        

        self._transaction_split = None
        self._proxy_id_list = None
        self.discriminator = None

        self.transaction_split = transaction_split
        self.proxy_id_list = proxy_id_list

    @property
    def transaction_split(self):
        """Gets the transaction_split of this ProxyTransactionSplitRequest.

        开启/关闭事务拆分，取值范围是[ON/OFF]

        :return: The transaction_split of this ProxyTransactionSplitRequest.
        :rtype: str
        """
        return self._transaction_split

    @transaction_split.setter
    def transaction_split(self, transaction_split):
        """Sets the transaction_split of this ProxyTransactionSplitRequest.

        开启/关闭事务拆分，取值范围是[ON/OFF]

        :param transaction_split: The transaction_split of this ProxyTransactionSplitRequest.
        :type transaction_split: str
        """
        self._transaction_split = transaction_split

    @property
    def proxy_id_list(self):
        """Gets the proxy_id_list of this ProxyTransactionSplitRequest.

        实例的数据库代理列表，仅支持单proxy使用。

        :return: The proxy_id_list of this ProxyTransactionSplitRequest.
        :rtype: list[str]
        """
        return self._proxy_id_list

    @proxy_id_list.setter
    def proxy_id_list(self, proxy_id_list):
        """Sets the proxy_id_list of this ProxyTransactionSplitRequest.

        实例的数据库代理列表，仅支持单proxy使用。

        :param proxy_id_list: The proxy_id_list of this ProxyTransactionSplitRequest.
        :type proxy_id_list: list[str]
        """
        self._proxy_id_list = proxy_id_list

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
        if not isinstance(other, ProxyTransactionSplitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
