# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainNameInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'support_public_resolve': 'bool',
        'is_latest_rules': 'bool',
        'zone_name': 'str',
        'history_domain_names': 'list[DomainNameEntity]'
    }

    attribute_map = {
        'support_public_resolve': 'support_public_resolve',
        'is_latest_rules': 'is_latest_rules',
        'zone_name': 'zone_name',
        'history_domain_names': 'history_domain_names'
    }

    def __init__(self, support_public_resolve=None, is_latest_rules=None, zone_name=None, history_domain_names=None):
        """DomainNameInfo

        The model defined in huaweicloud sdk

        :param support_public_resolve: 是否开启公网域名解析。 - true：开启 - false：未开启 
        :type support_public_resolve: bool
        :param is_latest_rules: 当前域名是否已为最新。 - true：是 - false：否 
        :type is_latest_rules: bool
        :param zone_name: 域名的区域后缀。
        :type zone_name: str
        :param history_domain_names: 历史域名信息。
        :type history_domain_names: list[:class:`huaweicloudsdkdcs.v2.DomainNameEntity`]
        """
        
        

        self._support_public_resolve = None
        self._is_latest_rules = None
        self._zone_name = None
        self._history_domain_names = None
        self.discriminator = None

        if support_public_resolve is not None:
            self.support_public_resolve = support_public_resolve
        if is_latest_rules is not None:
            self.is_latest_rules = is_latest_rules
        if zone_name is not None:
            self.zone_name = zone_name
        if history_domain_names is not None:
            self.history_domain_names = history_domain_names

    @property
    def support_public_resolve(self):
        """Gets the support_public_resolve of this DomainNameInfo.

        是否开启公网域名解析。 - true：开启 - false：未开启 

        :return: The support_public_resolve of this DomainNameInfo.
        :rtype: bool
        """
        return self._support_public_resolve

    @support_public_resolve.setter
    def support_public_resolve(self, support_public_resolve):
        """Sets the support_public_resolve of this DomainNameInfo.

        是否开启公网域名解析。 - true：开启 - false：未开启 

        :param support_public_resolve: The support_public_resolve of this DomainNameInfo.
        :type support_public_resolve: bool
        """
        self._support_public_resolve = support_public_resolve

    @property
    def is_latest_rules(self):
        """Gets the is_latest_rules of this DomainNameInfo.

        当前域名是否已为最新。 - true：是 - false：否 

        :return: The is_latest_rules of this DomainNameInfo.
        :rtype: bool
        """
        return self._is_latest_rules

    @is_latest_rules.setter
    def is_latest_rules(self, is_latest_rules):
        """Sets the is_latest_rules of this DomainNameInfo.

        当前域名是否已为最新。 - true：是 - false：否 

        :param is_latest_rules: The is_latest_rules of this DomainNameInfo.
        :type is_latest_rules: bool
        """
        self._is_latest_rules = is_latest_rules

    @property
    def zone_name(self):
        """Gets the zone_name of this DomainNameInfo.

        域名的区域后缀。

        :return: The zone_name of this DomainNameInfo.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this DomainNameInfo.

        域名的区域后缀。

        :param zone_name: The zone_name of this DomainNameInfo.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def history_domain_names(self):
        """Gets the history_domain_names of this DomainNameInfo.

        历史域名信息。

        :return: The history_domain_names of this DomainNameInfo.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DomainNameEntity`]
        """
        return self._history_domain_names

    @history_domain_names.setter
    def history_domain_names(self, history_domain_names):
        """Sets the history_domain_names of this DomainNameInfo.

        历史域名信息。

        :param history_domain_names: The history_domain_names of this DomainNameInfo.
        :type history_domain_names: list[:class:`huaweicloudsdkdcs.v2.DomainNameEntity`]
        """
        self._history_domain_names = history_domain_names

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
        if not isinstance(other, DomainNameInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
