# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPolicyGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'group_id': 'group_id'
    }

    def __init__(self, description=None, name=None, group_id=None):
        r"""AddPolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param description: **参数解释**: 策略组的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度1-64，只能由中文字符、英文字母、数字、逗号、句号、空格及\&quot;_\&quot;、\&quot;-\&quot;组成 **默认取值**: 不涉及
        :type description: str
        :param name: **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-32，只能由中文字符、英文字母、数字、逗号、句号、空格及\&quot;_\&quot;、\&quot;-\&quot;组成，且不能以default_policy_group开头 **默认取值**: 不涉及
        :type name: str
        :param group_id: **参数解释**: 需要被复制的策略组的策略组ID，仅旗舰版和容器版策略组支持复制 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，support_version 等于 hss.version.container.enterprise 或 hss.version.premium 的 group_id 是可以被复制的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及
        :type group_id: str
        """
        
        

        self._description = None
        self._name = None
        self._group_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.group_id = group_id

    @property
    def description(self):
        r"""Gets the description of this AddPolicyGroupRequestInfo.

        **参数解释**: 策略组的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度1-64，只能由中文字符、英文字母、数字、逗号、句号、空格及\"_\"、\"-\"组成 **默认取值**: 不涉及

        :return: The description of this AddPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddPolicyGroupRequestInfo.

        **参数解释**: 策略组的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度1-64，只能由中文字符、英文字母、数字、逗号、句号、空格及\"_\"、\"-\"组成 **默认取值**: 不涉及

        :param description: The description of this AddPolicyGroupRequestInfo.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this AddPolicyGroupRequestInfo.

        **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-32，只能由中文字符、英文字母、数字、逗号、句号、空格及\"_\"、\"-\"组成，且不能以default_policy_group开头 **默认取值**: 不涉及

        :return: The name of this AddPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddPolicyGroupRequestInfo.

        **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-32，只能由中文字符、英文字母、数字、逗号、句号、空格及\"_\"、\"-\"组成，且不能以default_policy_group开头 **默认取值**: 不涉及

        :param name: The name of this AddPolicyGroupRequestInfo.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        r"""Gets the group_id of this AddPolicyGroupRequestInfo.

        **参数解释**: 需要被复制的策略组的策略组ID，仅旗舰版和容器版策略组支持复制 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，support_version 等于 hss.version.container.enterprise 或 hss.version.premium 的 group_id 是可以被复制的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及

        :return: The group_id of this AddPolicyGroupRequestInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddPolicyGroupRequestInfo.

        **参数解释**: 需要被复制的策略组的策略组ID，仅旗舰版和容器版策略组支持复制 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，support_version 等于 hss.version.container.enterprise 或 hss.version.premium 的 group_id 是可以被复制的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及

        :param group_id: The group_id of this AddPolicyGroupRequestInfo.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, AddPolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
