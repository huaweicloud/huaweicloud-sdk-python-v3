# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_limit': 'int',
        'type': 'str',
        'used': 'int',
        'user_domain_id': 'str'
    }

    attribute_map = {
        'quota_limit': 'quota_limit',
        'type': 'type',
        'used': 'used',
        'user_domain_id': 'user_domain_id'
    }

    def __init__(self, quota_limit=None, type=None, used=None, user_domain_id=None):
        r"""Quotas

        The model defined in huaweicloud sdk

        :param quota_limit: 配额上限。
        :type quota_limit: int
        :param type: 配额类型。取值意义： - file_refresh：文件级别刷新配额 - dir_refresh：目录级别刷新配额 - preheat：预热配额 - domain：加速域名配额 - ip_filter：IP黑白名单配额 - browser_cache_rule：浏览器缓存规则配额 - http_response_header：HTTP响应头配额 - referer：REFERER防盗链配额 - flexible_origin：高级回源配额 - flexible_origin_match_value：高级回源匹配内容配额 - cache_rule：缓存规则配额 - custom_cache_key：自定义CACHE KEY配额 - custom_cache_key_match_value：自定义CACHE KEY匹配内容配额 - rule：规则引擎配额 - edge_function：函数阶段配额 - origin_request_url_rewrite：回源URL改写配额 - origin_request_header：回源请求头配额 - request_url_rewrite：请求URL改写配额 - access_area_filter：区域访问控制配额 - request_limit_rules：请求限速配置配额 - user_agent：UA配额
        :type type: str
        :param used: 已使用配额数。
        :type used: int
        :param user_domain_id: 域名所属用户的domain_id。
        :type user_domain_id: str
        """
        
        

        self._quota_limit = None
        self._type = None
        self._used = None
        self._user_domain_id = None
        self.discriminator = None

        if quota_limit is not None:
            self.quota_limit = quota_limit
        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id

    @property
    def quota_limit(self):
        r"""Gets the quota_limit of this Quotas.

        配额上限。

        :return: The quota_limit of this Quotas.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        r"""Sets the quota_limit of this Quotas.

        配额上限。

        :param quota_limit: The quota_limit of this Quotas.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

    @property
    def type(self):
        r"""Gets the type of this Quotas.

        配额类型。取值意义： - file_refresh：文件级别刷新配额 - dir_refresh：目录级别刷新配额 - preheat：预热配额 - domain：加速域名配额 - ip_filter：IP黑白名单配额 - browser_cache_rule：浏览器缓存规则配额 - http_response_header：HTTP响应头配额 - referer：REFERER防盗链配额 - flexible_origin：高级回源配额 - flexible_origin_match_value：高级回源匹配内容配额 - cache_rule：缓存规则配额 - custom_cache_key：自定义CACHE KEY配额 - custom_cache_key_match_value：自定义CACHE KEY匹配内容配额 - rule：规则引擎配额 - edge_function：函数阶段配额 - origin_request_url_rewrite：回源URL改写配额 - origin_request_header：回源请求头配额 - request_url_rewrite：请求URL改写配额 - access_area_filter：区域访问控制配额 - request_limit_rules：请求限速配置配额 - user_agent：UA配额

        :return: The type of this Quotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Quotas.

        配额类型。取值意义： - file_refresh：文件级别刷新配额 - dir_refresh：目录级别刷新配额 - preheat：预热配额 - domain：加速域名配额 - ip_filter：IP黑白名单配额 - browser_cache_rule：浏览器缓存规则配额 - http_response_header：HTTP响应头配额 - referer：REFERER防盗链配额 - flexible_origin：高级回源配额 - flexible_origin_match_value：高级回源匹配内容配额 - cache_rule：缓存规则配额 - custom_cache_key：自定义CACHE KEY配额 - custom_cache_key_match_value：自定义CACHE KEY匹配内容配额 - rule：规则引擎配额 - edge_function：函数阶段配额 - origin_request_url_rewrite：回源URL改写配额 - origin_request_header：回源请求头配额 - request_url_rewrite：请求URL改写配额 - access_area_filter：区域访问控制配额 - request_limit_rules：请求限速配置配额 - user_agent：UA配额

        :param type: The type of this Quotas.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        r"""Gets the used of this Quotas.

        已使用配额数。

        :return: The used of this Quotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this Quotas.

        已使用配额数。

        :param used: The used of this Quotas.
        :type used: int
        """
        self._used = used

    @property
    def user_domain_id(self):
        r"""Gets the user_domain_id of this Quotas.

        域名所属用户的domain_id。

        :return: The user_domain_id of this Quotas.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        r"""Sets the user_domain_id of this Quotas.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this Quotas.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

    def to_dict(self):
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
        if not isinstance(other, Quotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
