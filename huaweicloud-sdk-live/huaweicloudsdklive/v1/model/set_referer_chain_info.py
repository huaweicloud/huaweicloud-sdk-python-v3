# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRefererChainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'guard_switch': 'str',
        'referer_config_empty': 'str',
        'referer_white_list': 'str',
        'referer_auth_list': 'list[str]'
    }

    attribute_map = {
        'domain': 'domain',
        'guard_switch': 'guard_switch',
        'referer_config_empty': 'referer_config_empty',
        'referer_white_list': 'referer_white_list',
        'referer_auth_list': 'referer_auth_list'
    }

    def __init__(self, domain=None, guard_switch=None, referer_config_empty=None, referer_white_list=None, referer_auth_list=None):
        r"""SetRefererChainInfo

        The model defined in huaweicloud sdk

        :param domain: 直播域名
        :type domain: str
        :param guard_switch: referer防盗链开关：true表示开启；false表示关闭
        :type guard_switch: str
        :param referer_config_empty: 是否包含referer头域：true表示包含；false表示不包含；guard_switch为true则必填
        :type referer_config_empty: str
        :param referer_white_list: 是否为referer白名单：true表示白名单；false表示黑名单；guard_switch为true则必填
        :type referer_white_list: str
        :param referer_auth_list: 域名列表，域名为正则表达式；最多支持配置100个域名，以英文“;”进行分隔；guard_switch为true则必填
        :type referer_auth_list: list[str]
        """
        
        

        self._domain = None
        self._guard_switch = None
        self._referer_config_empty = None
        self._referer_white_list = None
        self._referer_auth_list = None
        self.discriminator = None

        self.domain = domain
        self.guard_switch = guard_switch
        if referer_config_empty is not None:
            self.referer_config_empty = referer_config_empty
        if referer_white_list is not None:
            self.referer_white_list = referer_white_list
        if referer_auth_list is not None:
            self.referer_auth_list = referer_auth_list

    @property
    def domain(self):
        r"""Gets the domain of this SetRefererChainInfo.

        直播域名

        :return: The domain of this SetRefererChainInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this SetRefererChainInfo.

        直播域名

        :param domain: The domain of this SetRefererChainInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def guard_switch(self):
        r"""Gets the guard_switch of this SetRefererChainInfo.

        referer防盗链开关：true表示开启；false表示关闭

        :return: The guard_switch of this SetRefererChainInfo.
        :rtype: str
        """
        return self._guard_switch

    @guard_switch.setter
    def guard_switch(self, guard_switch):
        r"""Sets the guard_switch of this SetRefererChainInfo.

        referer防盗链开关：true表示开启；false表示关闭

        :param guard_switch: The guard_switch of this SetRefererChainInfo.
        :type guard_switch: str
        """
        self._guard_switch = guard_switch

    @property
    def referer_config_empty(self):
        r"""Gets the referer_config_empty of this SetRefererChainInfo.

        是否包含referer头域：true表示包含；false表示不包含；guard_switch为true则必填

        :return: The referer_config_empty of this SetRefererChainInfo.
        :rtype: str
        """
        return self._referer_config_empty

    @referer_config_empty.setter
    def referer_config_empty(self, referer_config_empty):
        r"""Sets the referer_config_empty of this SetRefererChainInfo.

        是否包含referer头域：true表示包含；false表示不包含；guard_switch为true则必填

        :param referer_config_empty: The referer_config_empty of this SetRefererChainInfo.
        :type referer_config_empty: str
        """
        self._referer_config_empty = referer_config_empty

    @property
    def referer_white_list(self):
        r"""Gets the referer_white_list of this SetRefererChainInfo.

        是否为referer白名单：true表示白名单；false表示黑名单；guard_switch为true则必填

        :return: The referer_white_list of this SetRefererChainInfo.
        :rtype: str
        """
        return self._referer_white_list

    @referer_white_list.setter
    def referer_white_list(self, referer_white_list):
        r"""Sets the referer_white_list of this SetRefererChainInfo.

        是否为referer白名单：true表示白名单；false表示黑名单；guard_switch为true则必填

        :param referer_white_list: The referer_white_list of this SetRefererChainInfo.
        :type referer_white_list: str
        """
        self._referer_white_list = referer_white_list

    @property
    def referer_auth_list(self):
        r"""Gets the referer_auth_list of this SetRefererChainInfo.

        域名列表，域名为正则表达式；最多支持配置100个域名，以英文“;”进行分隔；guard_switch为true则必填

        :return: The referer_auth_list of this SetRefererChainInfo.
        :rtype: list[str]
        """
        return self._referer_auth_list

    @referer_auth_list.setter
    def referer_auth_list(self, referer_auth_list):
        r"""Sets the referer_auth_list of this SetRefererChainInfo.

        域名列表，域名为正则表达式；最多支持配置100个域名，以英文“;”进行分隔；guard_switch为true则必填

        :param referer_auth_list: The referer_auth_list of this SetRefererChainInfo.
        :type referer_auth_list: list[str]
        """
        self._referer_auth_list = referer_auth_list

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
        if not isinstance(other, SetRefererChainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
