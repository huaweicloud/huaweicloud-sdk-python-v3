# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffinityRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'operator': 'str',
        'values': 'list[str]',
        'weight': 'int'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values',
        'weight': 'weight'
    }

    def __init__(self, key=None, operator=None, values=None, weight=None):
        r"""AffinityRule

        The model defined in huaweicloud sdk

        :param key: **参数解释**：亲和度描述具体信息。 该标签可以使用系统默认的标签，也可以使用自定义标签。系统默认的节点标签详情请参见[[管理节点标签](https://support.huaweicloud.com/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hc)[[管理节点标签](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hk)。 **约束限制**：标签是键值对。有效的标签键有两个段：可选的前缀和名称，用斜杠（/）分隔。 **取值范围**：名称段是必需的，必须小于等于 63 个字符，以字母数字字符（[a-z0-9A-Z]）开头和结尾， 带有破折号（-），下划线（_），点（ .）和之间的字母数字;前缀是可选的。如果指定，前缀必须是 DNS 子域：由点（.）分隔的一系列 DNS 标签，总共不超过 253 个字符， 后跟斜杠（/）.请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/) **默认取值**：不涉及。
        :type key: str
        :param operator: **参数解释**：操作符 **约束限制**：不涉及 **取值范围**：可以设置六种匹配关系（In、NotIn、Exists、DoesNotExist、Gt、Lt）。  In：亲和/反亲和对象的标签在标签值列表（values字段）中。 NotIn：亲和/反亲和对象的标签不在标签值列表（values字段）中。 Exists：亲和/反亲和对象存在指定标签名。 DoesNotExist：亲和/反亲和对象不存在指定标签名。 Gt：调度节点的标签值大于列表值 （字符串比较）。 Lt：调度节点的标签值小于列表值 （字符串比较）。 **默认取值**：不涉及。
        :type operator: str
        :param values: 参数解释：设置节点亲和性时，填写节点标签对应的标签值 约束限制：必须为 63 个字符或更少（可以为空），除非标签值为空，必须以字母数字字符（[a-z0-9A-Z]）开头和结尾，包含破折号（-）、下划线（_）、点（.）和字母或数字 请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/)
        :type values: list[str]
        :param weight: 设置弱亲和节点的权重值，该值的取值应为0-100之间，强亲和该值为NULL，弱亲和该值可选
        :type weight: int
        """
        
        

        self._key = None
        self._operator = None
        self._values = None
        self._weight = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if values is not None:
            self.values = values
        if weight is not None:
            self.weight = weight

    @property
    def key(self):
        r"""Gets the key of this AffinityRule.

        **参数解释**：亲和度描述具体信息。 该标签可以使用系统默认的标签，也可以使用自定义标签。系统默认的节点标签详情请参见[[管理节点标签](https://support.huaweicloud.com/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hc)[[管理节点标签](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hk)。 **约束限制**：标签是键值对。有效的标签键有两个段：可选的前缀和名称，用斜杠（/）分隔。 **取值范围**：名称段是必需的，必须小于等于 63 个字符，以字母数字字符（[a-z0-9A-Z]）开头和结尾， 带有破折号（-），下划线（_），点（ .）和之间的字母数字;前缀是可选的。如果指定，前缀必须是 DNS 子域：由点（.）分隔的一系列 DNS 标签，总共不超过 253 个字符， 后跟斜杠（/）.请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/) **默认取值**：不涉及。

        :return: The key of this AffinityRule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this AffinityRule.

        **参数解释**：亲和度描述具体信息。 该标签可以使用系统默认的标签，也可以使用自定义标签。系统默认的节点标签详情请参见[[管理节点标签](https://support.huaweicloud.com/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hc)[[管理节点标签](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0004.html#cce_10_0004__section74111324152813)](tag:hk)。 **约束限制**：标签是键值对。有效的标签键有两个段：可选的前缀和名称，用斜杠（/）分隔。 **取值范围**：名称段是必需的，必须小于等于 63 个字符，以字母数字字符（[a-z0-9A-Z]）开头和结尾， 带有破折号（-），下划线（_），点（ .）和之间的字母数字;前缀是可选的。如果指定，前缀必须是 DNS 子域：由点（.）分隔的一系列 DNS 标签，总共不超过 253 个字符， 后跟斜杠（/）.请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/) **默认取值**：不涉及。

        :param key: The key of this AffinityRule.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        r"""Gets the operator of this AffinityRule.

        **参数解释**：操作符 **约束限制**：不涉及 **取值范围**：可以设置六种匹配关系（In、NotIn、Exists、DoesNotExist、Gt、Lt）。  In：亲和/反亲和对象的标签在标签值列表（values字段）中。 NotIn：亲和/反亲和对象的标签不在标签值列表（values字段）中。 Exists：亲和/反亲和对象存在指定标签名。 DoesNotExist：亲和/反亲和对象不存在指定标签名。 Gt：调度节点的标签值大于列表值 （字符串比较）。 Lt：调度节点的标签值小于列表值 （字符串比较）。 **默认取值**：不涉及。

        :return: The operator of this AffinityRule.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this AffinityRule.

        **参数解释**：操作符 **约束限制**：不涉及 **取值范围**：可以设置六种匹配关系（In、NotIn、Exists、DoesNotExist、Gt、Lt）。  In：亲和/反亲和对象的标签在标签值列表（values字段）中。 NotIn：亲和/反亲和对象的标签不在标签值列表（values字段）中。 Exists：亲和/反亲和对象存在指定标签名。 DoesNotExist：亲和/反亲和对象不存在指定标签名。 Gt：调度节点的标签值大于列表值 （字符串比较）。 Lt：调度节点的标签值小于列表值 （字符串比较）。 **默认取值**：不涉及。

        :param operator: The operator of this AffinityRule.
        :type operator: str
        """
        self._operator = operator

    @property
    def values(self):
        r"""Gets the values of this AffinityRule.

        参数解释：设置节点亲和性时，填写节点标签对应的标签值 约束限制：必须为 63 个字符或更少（可以为空），除非标签值为空，必须以字母数字字符（[a-z0-9A-Z]）开头和结尾，包含破折号（-）、下划线（_）、点（.）和字母或数字 请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/)

        :return: The values of this AffinityRule.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this AffinityRule.

        参数解释：设置节点亲和性时，填写节点标签对应的标签值 约束限制：必须为 63 个字符或更少（可以为空），除非标签值为空，必须以字母数字字符（[a-z0-9A-Z]）开头和结尾，包含破折号（-）、下划线（_）、点（.）和字母或数字 请参见[标签和选择算符](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/)

        :param values: The values of this AffinityRule.
        :type values: list[str]
        """
        self._values = values

    @property
    def weight(self):
        r"""Gets the weight of this AffinityRule.

        设置弱亲和节点的权重值，该值的取值应为0-100之间，强亲和该值为NULL，弱亲和该值可选

        :return: The weight of this AffinityRule.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this AffinityRule.

        设置弱亲和节点的权重值，该值的取值应为0-100之间，强亲和该值为NULL，弱亲和该值可选

        :param weight: The weight of this AffinityRule.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, AffinityRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
