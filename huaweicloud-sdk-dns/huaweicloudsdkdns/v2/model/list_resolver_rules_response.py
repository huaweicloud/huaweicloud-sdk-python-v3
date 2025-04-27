# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResolverRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolver_rules': 'list[ListResolverRuleParam]',
        'links': 'PageLink',
        'metadata': 'Metadata',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resolver_rules': 'resolver_rules',
        'links': 'links',
        'metadata': 'metadata',
        'page_info': 'page_info'
    }

    def __init__(self, resolver_rules=None, links=None, metadata=None, page_info=None):
        r"""ListResolverRulesResponse

        The model defined in huaweicloud sdk

        :param resolver_rules: 解析器转发规则列表。
        :type resolver_rules: list[:class:`huaweicloudsdkdns.v2.ListResolverRuleParam`]
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        
        super(ListResolverRulesResponse, self).__init__()

        self._resolver_rules = None
        self._links = None
        self._metadata = None
        self._page_info = None
        self.discriminator = None

        if resolver_rules is not None:
            self.resolver_rules = resolver_rules
        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata
        if page_info is not None:
            self.page_info = page_info

    @property
    def resolver_rules(self):
        r"""Gets the resolver_rules of this ListResolverRulesResponse.

        解析器转发规则列表。

        :return: The resolver_rules of this ListResolverRulesResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ListResolverRuleParam`]
        """
        return self._resolver_rules

    @resolver_rules.setter
    def resolver_rules(self, resolver_rules):
        r"""Sets the resolver_rules of this ListResolverRulesResponse.

        解析器转发规则列表。

        :param resolver_rules: The resolver_rules of this ListResolverRulesResponse.
        :type resolver_rules: list[:class:`huaweicloudsdkdns.v2.ListResolverRuleParam`]
        """
        self._resolver_rules = resolver_rules

    @property
    def links(self):
        r"""Gets the links of this ListResolverRulesResponse.

        :return: The links of this ListResolverRulesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListResolverRulesResponse.

        :param links: The links of this ListResolverRulesResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def metadata(self):
        r"""Gets the metadata of this ListResolverRulesResponse.

        :return: The metadata of this ListResolverRulesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListResolverRulesResponse.

        :param metadata: The metadata of this ListResolverRulesResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        self._metadata = metadata

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResolverRulesResponse.

        :return: The page_info of this ListResolverRulesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResolverRulesResponse.

        :param page_info: The page_info of this ListResolverRulesResponse.
        :type page_info: :class:`huaweicloudsdkdns.v2.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListResolverRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
