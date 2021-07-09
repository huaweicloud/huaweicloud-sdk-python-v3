# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ConfirmUserBundleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'name': 'str',
        'host': 'object',
        'premium_type': 'int',
        'premium_name': 'str',
        'premium_host': 'object',
        'options': 'object',
        'rule': 'object',
        'upgrade': 'object'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'host': 'host',
        'premium_type': 'premium_type',
        'premium_name': 'premium_name',
        'premium_host': 'premium_host',
        'options': 'options',
        'rule': 'rule',
        'upgrade': 'upgrade'
    }

    def __init__(self, type=None, name=None, host=None, premium_type=None, premium_name=None, premium_host=None, options=None, rule=None, upgrade=None):
        """ConfirmUserBundleResponse - a model defined in huaweicloud sdk"""
        
        super(ConfirmUserBundleResponse, self).__init__()

        self._type = None
        self._name = None
        self._host = None
        self._premium_type = None
        self._premium_name = None
        self._premium_host = None
        self._options = None
        self._rule = None
        self._upgrade = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if premium_type is not None:
            self.premium_type = premium_type
        if premium_name is not None:
            self.premium_name = premium_name
        if premium_host is not None:
            self.premium_host = premium_host
        if options is not None:
            self.options = options
        if rule is not None:
            self.rule = rule
        if upgrade is not None:
            self.upgrade = upgrade

    @property
    def type(self):
        """Gets the type of this ConfirmUserBundleResponse.

        云模式套餐类型

        :return: The type of this ConfirmUserBundleResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfirmUserBundleResponse.

        云模式套餐类型

        :param type: The type of this ConfirmUserBundleResponse.
        :type: int
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ConfirmUserBundleResponse.

        云模式套餐名称

        :return: The name of this ConfirmUserBundleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfirmUserBundleResponse.

        云模式套餐名称

        :param name: The name of this ConfirmUserBundleResponse.
        :type: str
        """
        self._name = name

    @property
    def host(self):
        """Gets the host of this ConfirmUserBundleResponse.

        云模式支持的域名配额相关信息

        :return: The host of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ConfirmUserBundleResponse.

        云模式支持的域名配额相关信息

        :param host: The host of this ConfirmUserBundleResponse.
        :type: object
        """
        self._host = host

    @property
    def premium_type(self):
        """Gets the premium_type of this ConfirmUserBundleResponse.

        独享套餐类型

        :return: The premium_type of this ConfirmUserBundleResponse.
        :rtype: int
        """
        return self._premium_type

    @premium_type.setter
    def premium_type(self, premium_type):
        """Sets the premium_type of this ConfirmUserBundleResponse.

        独享套餐类型

        :param premium_type: The premium_type of this ConfirmUserBundleResponse.
        :type: int
        """
        self._premium_type = premium_type

    @property
    def premium_name(self):
        """Gets the premium_name of this ConfirmUserBundleResponse.

        独享套餐名称

        :return: The premium_name of this ConfirmUserBundleResponse.
        :rtype: str
        """
        return self._premium_name

    @premium_name.setter
    def premium_name(self, premium_name):
        """Sets the premium_name of this ConfirmUserBundleResponse.

        独享套餐名称

        :param premium_name: The premium_name of this ConfirmUserBundleResponse.
        :type: str
        """
        self._premium_name = premium_name

    @property
    def premium_host(self):
        """Gets the premium_host of this ConfirmUserBundleResponse.

        独享支持的域名配额相关信息

        :return: The premium_host of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._premium_host

    @premium_host.setter
    def premium_host(self, premium_host):
        """Sets the premium_host of this ConfirmUserBundleResponse.

        独享支持的域名配额相关信息

        :param premium_host: The premium_host of this ConfirmUserBundleResponse.
        :type: object
        """
        self._premium_host = premium_host

    @property
    def options(self):
        """Gets the options of this ConfirmUserBundleResponse.

        支持的策略相关信息

        :return: The options of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ConfirmUserBundleResponse.

        支持的策略相关信息

        :param options: The options of this ConfirmUserBundleResponse.
        :type: object
        """
        self._options = options

    @property
    def rule(self):
        """Gets the rule of this ConfirmUserBundleResponse.

        支持的规则配额相关信息

        :return: The rule of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ConfirmUserBundleResponse.

        支持的规则配额相关信息

        :param rule: The rule of this ConfirmUserBundleResponse.
        :type: object
        """
        self._rule = rule

    @property
    def upgrade(self):
        """Gets the upgrade of this ConfirmUserBundleResponse.

        不同版本支持的规则信息

        :return: The upgrade of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this ConfirmUserBundleResponse.

        不同版本支持的规则信息

        :param upgrade: The upgrade of this ConfirmUserBundleResponse.
        :type: object
        """
        self._upgrade = upgrade

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfirmUserBundleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
