# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseMysqlProxyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_ids': 'list[str]'
    }

    attribute_map = {
        'proxy_ids': 'proxy_ids'
    }

    def __init__(self, proxy_ids=None):
        """CloseMysqlProxyRequestBody

        The model defined in huaweicloud sdk

        :param proxy_ids: 数据库代理ID列表。  如果实例只开启了一个代理，可不传该字段；如果实例开启了多个代理，则必须指定要关闭的代理。
        :type proxy_ids: list[str]
        """
        
        

        self._proxy_ids = None
        self.discriminator = None

        if proxy_ids is not None:
            self.proxy_ids = proxy_ids

    @property
    def proxy_ids(self):
        """Gets the proxy_ids of this CloseMysqlProxyRequestBody.

        数据库代理ID列表。  如果实例只开启了一个代理，可不传该字段；如果实例开启了多个代理，则必须指定要关闭的代理。

        :return: The proxy_ids of this CloseMysqlProxyRequestBody.
        :rtype: list[str]
        """
        return self._proxy_ids

    @proxy_ids.setter
    def proxy_ids(self, proxy_ids):
        """Sets the proxy_ids of this CloseMysqlProxyRequestBody.

        数据库代理ID列表。  如果实例只开启了一个代理，可不传该字段；如果实例开启了多个代理，则必须指定要关闭的代理。

        :param proxy_ids: The proxy_ids of this CloseMysqlProxyRequestBody.
        :type proxy_ids: list[str]
        """
        self._proxy_ids = proxy_ids

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
        if not isinstance(other, CloseMysqlProxyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
