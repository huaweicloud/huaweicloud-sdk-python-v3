# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResolverQueryLogConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolver_query_log_configs': 'list[ResolverQueryLogConfig]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resolver_query_log_configs': 'resolver_query_log_configs',
        'page_info': 'page_info'
    }

    def __init__(self, resolver_query_log_configs=None, page_info=None):
        r"""ListResolverQueryLogConfigsResponse

        The model defined in huaweicloud sdk

        :param resolver_query_log_configs: 解析器访问日志列表。
        :type resolver_query_log_configs: list[:class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        
        super().__init__()

        self._resolver_query_log_configs = None
        self._page_info = None
        self.discriminator = None

        if resolver_query_log_configs is not None:
            self.resolver_query_log_configs = resolver_query_log_configs
        if page_info is not None:
            self.page_info = page_info

    @property
    def resolver_query_log_configs(self):
        r"""Gets the resolver_query_log_configs of this ListResolverQueryLogConfigsResponse.

        解析器访问日志列表。

        :return: The resolver_query_log_configs of this ListResolverQueryLogConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`]
        """
        return self._resolver_query_log_configs

    @resolver_query_log_configs.setter
    def resolver_query_log_configs(self, resolver_query_log_configs):
        r"""Sets the resolver_query_log_configs of this ListResolverQueryLogConfigsResponse.

        解析器访问日志列表。

        :param resolver_query_log_configs: The resolver_query_log_configs of this ListResolverQueryLogConfigsResponse.
        :type resolver_query_log_configs: list[:class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`]
        """
        self._resolver_query_log_configs = resolver_query_log_configs

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResolverQueryLogConfigsResponse.

        :return: The page_info of this ListResolverQueryLogConfigsResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResolverQueryLogConfigsResponse.

        :param page_info: The page_info of this ListResolverQueryLogConfigsResponse.
        :type page_info: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListResolverQueryLogConfigsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListResolverQueryLogConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
