# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProxyConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'str',
        'configurations': 'list[ProxyConfiguration]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'configurations': 'configurations'
    }

    def __init__(self, total_count=None, configurations=None):
        r"""ShowProxyConfigurationsResponse

        The model defined in huaweicloud sdk

        :param total_count: 数据总数
        :type total_count: str
        :param configurations: 内核可配置的参数列表
        :type configurations: list[:class:`huaweicloudsdkgaussdb.v3.ProxyConfiguration`]
        """
        
        super(ShowProxyConfigurationsResponse, self).__init__()

        self._total_count = None
        self._configurations = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if configurations is not None:
            self.configurations = configurations

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowProxyConfigurationsResponse.

        数据总数

        :return: The total_count of this ShowProxyConfigurationsResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowProxyConfigurationsResponse.

        数据总数

        :param total_count: The total_count of this ShowProxyConfigurationsResponse.
        :type total_count: str
        """
        self._total_count = total_count

    @property
    def configurations(self):
        r"""Gets the configurations of this ShowProxyConfigurationsResponse.

        内核可配置的参数列表

        :return: The configurations of this ShowProxyConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ProxyConfiguration`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this ShowProxyConfigurationsResponse.

        内核可配置的参数列表

        :param configurations: The configurations of this ShowProxyConfigurationsResponse.
        :type configurations: list[:class:`huaweicloudsdkgaussdb.v3.ProxyConfiguration`]
        """
        self._configurations = configurations

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
        if not isinstance(other, ShowProxyConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
