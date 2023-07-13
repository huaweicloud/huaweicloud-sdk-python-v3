# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlProxyFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_flavor_groups': 'list[MysqlProxyFlavorGroups]'
    }

    attribute_map = {
        'proxy_flavor_groups': 'proxy_flavor_groups'
    }

    def __init__(self, proxy_flavor_groups=None):
        """ShowGaussMySqlProxyFlavorsResponse

        The model defined in huaweicloud sdk

        :param proxy_flavor_groups: 规格组信息。
        :type proxy_flavor_groups: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyFlavorGroups`]
        """
        
        super(ShowGaussMySqlProxyFlavorsResponse, self).__init__()

        self._proxy_flavor_groups = None
        self.discriminator = None

        if proxy_flavor_groups is not None:
            self.proxy_flavor_groups = proxy_flavor_groups

    @property
    def proxy_flavor_groups(self):
        """Gets the proxy_flavor_groups of this ShowGaussMySqlProxyFlavorsResponse.

        规格组信息。

        :return: The proxy_flavor_groups of this ShowGaussMySqlProxyFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyFlavorGroups`]
        """
        return self._proxy_flavor_groups

    @proxy_flavor_groups.setter
    def proxy_flavor_groups(self, proxy_flavor_groups):
        """Sets the proxy_flavor_groups of this ShowGaussMySqlProxyFlavorsResponse.

        规格组信息。

        :param proxy_flavor_groups: The proxy_flavor_groups of this ShowGaussMySqlProxyFlavorsResponse.
        :type proxy_flavor_groups: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyFlavorGroups`]
        """
        self._proxy_flavor_groups = proxy_flavor_groups

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
        if not isinstance(other, ShowGaussMySqlProxyFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
