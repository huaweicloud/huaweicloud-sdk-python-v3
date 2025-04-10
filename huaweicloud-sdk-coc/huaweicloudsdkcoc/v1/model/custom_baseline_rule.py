# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomBaselineRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'rule_name': 'str',
        'product': 'str',
        'compliance_level': 'str',
        'patch_items': 'list[CustomBaselineRulePatchItem]'
    }

    attribute_map = {
        'id': 'id',
        'rule_name': 'rule_name',
        'product': 'product',
        'compliance_level': 'compliance_level',
        'patch_items': 'patch_items'
    }

    def __init__(self, id=None, rule_name=None, product=None, compliance_level=None, patch_items=None):
        r"""CustomBaselineRule

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param product: 产品
        :type product: str
        :param compliance_level: 合规性报告等级
        :type compliance_level: str
        :param patch_items: 基线补丁信息
        :type patch_items: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRulePatchItem`]
        """
        
        

        self._id = None
        self._rule_name = None
        self._product = None
        self._compliance_level = None
        self._patch_items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if rule_name is not None:
            self.rule_name = rule_name
        self.product = product
        self.compliance_level = compliance_level
        if patch_items is not None:
            self.patch_items = patch_items

    @property
    def id(self):
        r"""Gets the id of this CustomBaselineRule.

        id

        :return: The id of this CustomBaselineRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomBaselineRule.

        id

        :param id: The id of this CustomBaselineRule.
        :type id: str
        """
        self._id = id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this CustomBaselineRule.

        规则名称

        :return: The rule_name of this CustomBaselineRule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this CustomBaselineRule.

        规则名称

        :param rule_name: The rule_name of this CustomBaselineRule.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def product(self):
        r"""Gets the product of this CustomBaselineRule.

        产品

        :return: The product of this CustomBaselineRule.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        r"""Sets the product of this CustomBaselineRule.

        产品

        :param product: The product of this CustomBaselineRule.
        :type product: str
        """
        self._product = product

    @property
    def compliance_level(self):
        r"""Gets the compliance_level of this CustomBaselineRule.

        合规性报告等级

        :return: The compliance_level of this CustomBaselineRule.
        :rtype: str
        """
        return self._compliance_level

    @compliance_level.setter
    def compliance_level(self, compliance_level):
        r"""Sets the compliance_level of this CustomBaselineRule.

        合规性报告等级

        :param compliance_level: The compliance_level of this CustomBaselineRule.
        :type compliance_level: str
        """
        self._compliance_level = compliance_level

    @property
    def patch_items(self):
        r"""Gets the patch_items of this CustomBaselineRule.

        基线补丁信息

        :return: The patch_items of this CustomBaselineRule.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRulePatchItem`]
        """
        return self._patch_items

    @patch_items.setter
    def patch_items(self, patch_items):
        r"""Sets the patch_items of this CustomBaselineRule.

        基线补丁信息

        :param patch_items: The patch_items of this CustomBaselineRule.
        :type patch_items: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRulePatchItem`]
        """
        self._patch_items = patch_items

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
        if not isinstance(other, CustomBaselineRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
