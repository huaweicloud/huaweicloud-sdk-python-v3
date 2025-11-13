# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResolverQueryLogConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolver_query_log_config': 'ResolverQueryLogConfig'
    }

    attribute_map = {
        'resolver_query_log_config': 'resolver_query_log_config'
    }

    def __init__(self, resolver_query_log_config=None):
        r"""ShowResolverQueryLogConfigResponse

        The model defined in huaweicloud sdk

        :param resolver_query_log_config: 
        :type resolver_query_log_config: :class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`
        """
        
        super().__init__()

        self._resolver_query_log_config = None
        self.discriminator = None

        if resolver_query_log_config is not None:
            self.resolver_query_log_config = resolver_query_log_config

    @property
    def resolver_query_log_config(self):
        r"""Gets the resolver_query_log_config of this ShowResolverQueryLogConfigResponse.

        :return: The resolver_query_log_config of this ShowResolverQueryLogConfigResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`
        """
        return self._resolver_query_log_config

    @resolver_query_log_config.setter
    def resolver_query_log_config(self, resolver_query_log_config):
        r"""Sets the resolver_query_log_config of this ShowResolverQueryLogConfigResponse.

        :param resolver_query_log_config: The resolver_query_log_config of this ShowResolverQueryLogConfigResponse.
        :type resolver_query_log_config: :class:`huaweicloudsdkdns.v2.ResolverQueryLogConfig`
        """
        self._resolver_query_log_config = resolver_query_log_config

    def to_dict(self):
        import warnings
        warnings.warn("ShowResolverQueryLogConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowResolverQueryLogConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
