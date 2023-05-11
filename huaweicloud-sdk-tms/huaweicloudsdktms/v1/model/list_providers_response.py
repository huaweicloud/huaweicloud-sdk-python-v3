# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'providers': 'list[ProviderResponseBody]',
        'total_count': 'int'
    }

    attribute_map = {
        'providers': 'providers',
        'total_count': 'total_count'
    }

    def __init__(self, providers=None, total_count=None):
        """ListProvidersResponse

        The model defined in huaweicloud sdk

        :param providers: 云服务列表
        :type providers: list[:class:`huaweicloudsdktms.v1.ProviderResponseBody`]
        :param total_count: 当前支持的云服务总数
        :type total_count: int
        """
        
        super(ListProvidersResponse, self).__init__()

        self._providers = None
        self._total_count = None
        self.discriminator = None

        if providers is not None:
            self.providers = providers
        if total_count is not None:
            self.total_count = total_count

    @property
    def providers(self):
        """Gets the providers of this ListProvidersResponse.

        云服务列表

        :return: The providers of this ListProvidersResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.ProviderResponseBody`]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this ListProvidersResponse.

        云服务列表

        :param providers: The providers of this ListProvidersResponse.
        :type providers: list[:class:`huaweicloudsdktms.v1.ProviderResponseBody`]
        """
        self._providers = providers

    @property
    def total_count(self):
        """Gets the total_count of this ListProvidersResponse.

        当前支持的云服务总数

        :return: The total_count of this ListProvidersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListProvidersResponse.

        当前支持的云服务总数

        :param total_count: The total_count of this ListProvidersResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
