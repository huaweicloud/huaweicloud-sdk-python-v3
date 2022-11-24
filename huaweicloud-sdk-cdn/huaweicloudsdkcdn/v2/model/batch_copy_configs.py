# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCopyConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_domain': 'str',
        'source_domain': 'str',
        'config_list': 'list[str]'
    }

    attribute_map = {
        'target_domain': 'target_domain',
        'source_domain': 'source_domain',
        'config_list': 'config_list'
    }

    def __init__(self, target_domain=None, source_domain=None, config_list=None):
        """BatchCopyConfigs

        The model defined in huaweicloud sdk

        :param target_domain: 目标域名列表,多个域名以逗号（半角）分隔,域名数最大10个。
        :type target_domain: str
        :param source_domain: 原域名
        :type source_domain: str
        :param config_list: 需要复制的域名配置项,多个配置项以逗号（半角）分隔，支持复制的配置项： - originRequestHeader（回源请求头） - httpResponseHeader（HTTP header配置） - cacheUrlParamsConfig（URL参数） - urlAuth（URL鉴权配置） - userAgentBlackAndWhiteList（User-Agent黑白名单） - ipv6Accelerate（IPv6开关） - rangeStatus（Range回源） - cacheRules（缓存规则） - followOrigin（缓存遵循源站） - privateBucketRetrieval（私有桶回源） - follow302Status（回源跟随） - sources（源站配置） - compress（智能压缩） - referer（防盗链） - ipBlackAndWhiteList（IP黑白名单）
        :type config_list: list[str]
        """
        
        

        self._target_domain = None
        self._source_domain = None
        self._config_list = None
        self.discriminator = None

        self.target_domain = target_domain
        self.source_domain = source_domain
        self.config_list = config_list

    @property
    def target_domain(self):
        """Gets the target_domain of this BatchCopyConfigs.

        目标域名列表,多个域名以逗号（半角）分隔,域名数最大10个。

        :return: The target_domain of this BatchCopyConfigs.
        :rtype: str
        """
        return self._target_domain

    @target_domain.setter
    def target_domain(self, target_domain):
        """Sets the target_domain of this BatchCopyConfigs.

        目标域名列表,多个域名以逗号（半角）分隔,域名数最大10个。

        :param target_domain: The target_domain of this BatchCopyConfigs.
        :type target_domain: str
        """
        self._target_domain = target_domain

    @property
    def source_domain(self):
        """Gets the source_domain of this BatchCopyConfigs.

        原域名

        :return: The source_domain of this BatchCopyConfigs.
        :rtype: str
        """
        return self._source_domain

    @source_domain.setter
    def source_domain(self, source_domain):
        """Sets the source_domain of this BatchCopyConfigs.

        原域名

        :param source_domain: The source_domain of this BatchCopyConfigs.
        :type source_domain: str
        """
        self._source_domain = source_domain

    @property
    def config_list(self):
        """Gets the config_list of this BatchCopyConfigs.

        需要复制的域名配置项,多个配置项以逗号（半角）分隔，支持复制的配置项： - originRequestHeader（回源请求头） - httpResponseHeader（HTTP header配置） - cacheUrlParamsConfig（URL参数） - urlAuth（URL鉴权配置） - userAgentBlackAndWhiteList（User-Agent黑白名单） - ipv6Accelerate（IPv6开关） - rangeStatus（Range回源） - cacheRules（缓存规则） - followOrigin（缓存遵循源站） - privateBucketRetrieval（私有桶回源） - follow302Status（回源跟随） - sources（源站配置） - compress（智能压缩） - referer（防盗链） - ipBlackAndWhiteList（IP黑白名单）

        :return: The config_list of this BatchCopyConfigs.
        :rtype: list[str]
        """
        return self._config_list

    @config_list.setter
    def config_list(self, config_list):
        """Sets the config_list of this BatchCopyConfigs.

        需要复制的域名配置项,多个配置项以逗号（半角）分隔，支持复制的配置项： - originRequestHeader（回源请求头） - httpResponseHeader（HTTP header配置） - cacheUrlParamsConfig（URL参数） - urlAuth（URL鉴权配置） - userAgentBlackAndWhiteList（User-Agent黑白名单） - ipv6Accelerate（IPv6开关） - rangeStatus（Range回源） - cacheRules（缓存规则） - followOrigin（缓存遵循源站） - privateBucketRetrieval（私有桶回源） - follow302Status（回源跟随） - sources（源站配置） - compress（智能压缩） - referer（防盗链） - ipBlackAndWhiteList（IP黑白名单）

        :param config_list: The config_list of this BatchCopyConfigs.
        :type config_list: list[str]
        """
        self._config_list = config_list

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
        if not isinstance(other, BatchCopyConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
