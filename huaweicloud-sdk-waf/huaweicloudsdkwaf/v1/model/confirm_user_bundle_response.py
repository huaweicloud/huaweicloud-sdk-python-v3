# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'upgrade': 'object',
        'feature': 'object'
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
        'upgrade': 'upgrade',
        'feature': 'feature'
    }

    def __init__(self, type=None, name=None, host=None, premium_type=None, premium_name=None, premium_host=None, options=None, rule=None, upgrade=None, feature=None):
        r"""ConfirmUserBundleResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 云模式套餐类型 **取值范围：** - -2：冻结 - -1：无 - 2：云模式 标准版（包周期） - 3：云模式 专业版（包周期） - 4：云模式 企业版（包周期） - 7：云模式 入门版（包周期） - 22：云模式（按需计费）
        :type type: int
        :param name: **参数解释：** 云模式套餐名称 **取值范围：** - None：无 - Basic：云模式 入门版（包周期） - Professional：云模式 标准版（包周期） - Enterprise：云模式 专业版（包周期） - Ultimate: 云模式 企业版（包周期） - cloud.waf.postpaid：云模式（按需计费）
        :type name: str
        :param host: **参数解释：** 云模式支持的域名配额相关信息 **取值范围：** 不涉及
        :type host: object
        :param premium_type: **参数解释：** 独享套餐类型 **取值范围：** - -2：冻结 - -1：无 - 12：独享模式 版本规格为WI-100 - 13：独享模式 版本规格为WI-500
        :type premium_type: int
        :param premium_name: **参数解释：** 独享模式套餐名称 **取值范围：** - None：无 - Instance.professional：独享模式 版本规格为WI-100 - Instance.enterprise：独享模式 版本规格为WI-500
        :type premium_name: str
        :param premium_host: **参数解释：** 独享支持的域名配额相关信息 **取值范围：** 不涉及
        :type premium_host: object
        :param options: **参数解释：** 支持的策略相关信息 **取值范围：** 不涉及
        :type options: object
        :param rule: **参数解释：** 支持的规则配额相关信息 **取值范围：** 不涉及
        :type rule: object
        :param upgrade: **参数解释：** 不同版本支持的规则信息 **取值范围：** 不涉及
        :type upgrade: object
        :param feature: **参数解释：** 支持的特性 **取值范围：** 不涉及
        :type feature: object
        """
        
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
        self._feature = None
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
        if feature is not None:
            self.feature = feature

    @property
    def type(self):
        r"""Gets the type of this ConfirmUserBundleResponse.

        **参数解释：** 云模式套餐类型 **取值范围：** - -2：冻结 - -1：无 - 2：云模式 标准版（包周期） - 3：云模式 专业版（包周期） - 4：云模式 企业版（包周期） - 7：云模式 入门版（包周期） - 22：云模式（按需计费）

        :return: The type of this ConfirmUserBundleResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfirmUserBundleResponse.

        **参数解释：** 云模式套餐类型 **取值范围：** - -2：冻结 - -1：无 - 2：云模式 标准版（包周期） - 3：云模式 专业版（包周期） - 4：云模式 企业版（包周期） - 7：云模式 入门版（包周期） - 22：云模式（按需计费）

        :param type: The type of this ConfirmUserBundleResponse.
        :type type: int
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ConfirmUserBundleResponse.

        **参数解释：** 云模式套餐名称 **取值范围：** - None：无 - Basic：云模式 入门版（包周期） - Professional：云模式 标准版（包周期） - Enterprise：云模式 专业版（包周期） - Ultimate: 云模式 企业版（包周期） - cloud.waf.postpaid：云模式（按需计费）

        :return: The name of this ConfirmUserBundleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfirmUserBundleResponse.

        **参数解释：** 云模式套餐名称 **取值范围：** - None：无 - Basic：云模式 入门版（包周期） - Professional：云模式 标准版（包周期） - Enterprise：云模式 专业版（包周期） - Ultimate: 云模式 企业版（包周期） - cloud.waf.postpaid：云模式（按需计费）

        :param name: The name of this ConfirmUserBundleResponse.
        :type name: str
        """
        self._name = name

    @property
    def host(self):
        r"""Gets the host of this ConfirmUserBundleResponse.

        **参数解释：** 云模式支持的域名配额相关信息 **取值范围：** 不涉及

        :return: The host of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ConfirmUserBundleResponse.

        **参数解释：** 云模式支持的域名配额相关信息 **取值范围：** 不涉及

        :param host: The host of this ConfirmUserBundleResponse.
        :type host: object
        """
        self._host = host

    @property
    def premium_type(self):
        r"""Gets the premium_type of this ConfirmUserBundleResponse.

        **参数解释：** 独享套餐类型 **取值范围：** - -2：冻结 - -1：无 - 12：独享模式 版本规格为WI-100 - 13：独享模式 版本规格为WI-500

        :return: The premium_type of this ConfirmUserBundleResponse.
        :rtype: int
        """
        return self._premium_type

    @premium_type.setter
    def premium_type(self, premium_type):
        r"""Sets the premium_type of this ConfirmUserBundleResponse.

        **参数解释：** 独享套餐类型 **取值范围：** - -2：冻结 - -1：无 - 12：独享模式 版本规格为WI-100 - 13：独享模式 版本规格为WI-500

        :param premium_type: The premium_type of this ConfirmUserBundleResponse.
        :type premium_type: int
        """
        self._premium_type = premium_type

    @property
    def premium_name(self):
        r"""Gets the premium_name of this ConfirmUserBundleResponse.

        **参数解释：** 独享模式套餐名称 **取值范围：** - None：无 - Instance.professional：独享模式 版本规格为WI-100 - Instance.enterprise：独享模式 版本规格为WI-500

        :return: The premium_name of this ConfirmUserBundleResponse.
        :rtype: str
        """
        return self._premium_name

    @premium_name.setter
    def premium_name(self, premium_name):
        r"""Sets the premium_name of this ConfirmUserBundleResponse.

        **参数解释：** 独享模式套餐名称 **取值范围：** - None：无 - Instance.professional：独享模式 版本规格为WI-100 - Instance.enterprise：独享模式 版本规格为WI-500

        :param premium_name: The premium_name of this ConfirmUserBundleResponse.
        :type premium_name: str
        """
        self._premium_name = premium_name

    @property
    def premium_host(self):
        r"""Gets the premium_host of this ConfirmUserBundleResponse.

        **参数解释：** 独享支持的域名配额相关信息 **取值范围：** 不涉及

        :return: The premium_host of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._premium_host

    @premium_host.setter
    def premium_host(self, premium_host):
        r"""Sets the premium_host of this ConfirmUserBundleResponse.

        **参数解释：** 独享支持的域名配额相关信息 **取值范围：** 不涉及

        :param premium_host: The premium_host of this ConfirmUserBundleResponse.
        :type premium_host: object
        """
        self._premium_host = premium_host

    @property
    def options(self):
        r"""Gets the options of this ConfirmUserBundleResponse.

        **参数解释：** 支持的策略相关信息 **取值范围：** 不涉及

        :return: The options of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ConfirmUserBundleResponse.

        **参数解释：** 支持的策略相关信息 **取值范围：** 不涉及

        :param options: The options of this ConfirmUserBundleResponse.
        :type options: object
        """
        self._options = options

    @property
    def rule(self):
        r"""Gets the rule of this ConfirmUserBundleResponse.

        **参数解释：** 支持的规则配额相关信息 **取值范围：** 不涉及

        :return: The rule of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ConfirmUserBundleResponse.

        **参数解释：** 支持的规则配额相关信息 **取值范围：** 不涉及

        :param rule: The rule of this ConfirmUserBundleResponse.
        :type rule: object
        """
        self._rule = rule

    @property
    def upgrade(self):
        r"""Gets the upgrade of this ConfirmUserBundleResponse.

        **参数解释：** 不同版本支持的规则信息 **取值范围：** 不涉及

        :return: The upgrade of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        r"""Sets the upgrade of this ConfirmUserBundleResponse.

        **参数解释：** 不同版本支持的规则信息 **取值范围：** 不涉及

        :param upgrade: The upgrade of this ConfirmUserBundleResponse.
        :type upgrade: object
        """
        self._upgrade = upgrade

    @property
    def feature(self):
        r"""Gets the feature of this ConfirmUserBundleResponse.

        **参数解释：** 支持的特性 **取值范围：** 不涉及

        :return: The feature of this ConfirmUserBundleResponse.
        :rtype: object
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ConfirmUserBundleResponse.

        **参数解释：** 支持的特性 **取值范围：** 不涉及

        :param feature: The feature of this ConfirmUserBundleResponse.
        :type feature: object
        """
        self._feature = feature

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
        if not isinstance(other, ConfirmUserBundleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
