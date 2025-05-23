# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlProxyListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_list': 'list[MysqlShowProxyResponseV3]'
    }

    attribute_map = {
        'proxy_list': 'proxy_list'
    }

    def __init__(self, proxy_list=None):
        r"""ShowGaussMySqlProxyListResponse

        The model defined in huaweicloud sdk

        :param proxy_list: Proxy实例信息列表。
        :type proxy_list: list[:class:`huaweicloudsdkgaussdb.v3.MysqlShowProxyResponseV3`]
        """
        
        super(ShowGaussMySqlProxyListResponse, self).__init__()

        self._proxy_list = None
        self.discriminator = None

        if proxy_list is not None:
            self.proxy_list = proxy_list

    @property
    def proxy_list(self):
        r"""Gets the proxy_list of this ShowGaussMySqlProxyListResponse.

        Proxy实例信息列表。

        :return: The proxy_list of this ShowGaussMySqlProxyListResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlShowProxyResponseV3`]
        """
        return self._proxy_list

    @proxy_list.setter
    def proxy_list(self, proxy_list):
        r"""Sets the proxy_list of this ShowGaussMySqlProxyListResponse.

        Proxy实例信息列表。

        :param proxy_list: The proxy_list of this ShowGaussMySqlProxyListResponse.
        :type proxy_list: list[:class:`huaweicloudsdkgaussdb.v3.MysqlShowProxyResponseV3`]
        """
        self._proxy_list = proxy_list

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
        if not isinstance(other, ShowGaussMySqlProxyListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
