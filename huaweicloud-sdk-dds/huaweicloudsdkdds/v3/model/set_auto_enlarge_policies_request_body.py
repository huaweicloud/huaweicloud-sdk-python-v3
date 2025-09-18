# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAutoEnlargePoliciesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'str',
        'policies': 'list[DiskSetAutoExpansionPolicy]'
    }

    attribute_map = {
        'switch_option': 'switch_option',
        'policies': 'policies'
    }

    def __init__(self, switch_option=None, policies=None):
        r"""SetAutoEnlargePoliciesRequestBody

        The model defined in huaweicloud sdk

        :param switch_option: **参数解释：** 自动扩容开关。 **约束限制：** 不涉及。 **取值范围：** - on:开启磁盘自动扩容策略。 - off: 关闭磁盘自动扩容策略。 **默认取值：** on。
        :type switch_option: str
        :param policies: **参数解释：** 磁盘自动扩容策略。 **约束限制：** 最大支持设置10个实例的策略。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 **参数解释：** 不涉及。
        :type policies: list[:class:`huaweicloudsdkdds.v3.DiskSetAutoExpansionPolicy`]
        """
        
        

        self._switch_option = None
        self._policies = None
        self.discriminator = None

        if switch_option is not None:
            self.switch_option = switch_option
        self.policies = policies

    @property
    def switch_option(self):
        r"""Gets the switch_option of this SetAutoEnlargePoliciesRequestBody.

        **参数解释：** 自动扩容开关。 **约束限制：** 不涉及。 **取值范围：** - on:开启磁盘自动扩容策略。 - off: 关闭磁盘自动扩容策略。 **默认取值：** on。

        :return: The switch_option of this SetAutoEnlargePoliciesRequestBody.
        :rtype: str
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        r"""Sets the switch_option of this SetAutoEnlargePoliciesRequestBody.

        **参数解释：** 自动扩容开关。 **约束限制：** 不涉及。 **取值范围：** - on:开启磁盘自动扩容策略。 - off: 关闭磁盘自动扩容策略。 **默认取值：** on。

        :param switch_option: The switch_option of this SetAutoEnlargePoliciesRequestBody.
        :type switch_option: str
        """
        self._switch_option = switch_option

    @property
    def policies(self):
        r"""Gets the policies of this SetAutoEnlargePoliciesRequestBody.

        **参数解释：** 磁盘自动扩容策略。 **约束限制：** 最大支持设置10个实例的策略。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 **参数解释：** 不涉及。

        :return: The policies of this SetAutoEnlargePoliciesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.DiskSetAutoExpansionPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this SetAutoEnlargePoliciesRequestBody.

        **参数解释：** 磁盘自动扩容策略。 **约束限制：** 最大支持设置10个实例的策略。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 **参数解释：** 不涉及。

        :param policies: The policies of this SetAutoEnlargePoliciesRequestBody.
        :type policies: list[:class:`huaweicloudsdkdds.v3.DiskSetAutoExpansionPolicy`]
        """
        self._policies = policies

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
        if not isinstance(other, SetAutoEnlargePoliciesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
