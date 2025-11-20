# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PremiumWafAgencyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_name_list': 'list[str]'
    }

    attribute_map = {
        'role_name_list': 'role_name_list'
    }

    def __init__(self, role_name_list=None):
        r"""PremiumWafAgencyRequest

        The model defined in huaweicloud sdk

        :param role_name_list: **参数解释：** 创建独享引擎代理策略名列表 **约束限制：** 已经存在的策略，无法再次创建 **取值范围：** 列表中支持以下策略名字 - evs_to_waf_operate_policy - vpc_to_waf_operate_policy - ecs_to_waf_operate_policy - elb_to_waf_operate_policy **默认取值：** 不涉及
        :type role_name_list: list[str]
        """
        
        

        self._role_name_list = None
        self.discriminator = None

        if role_name_list is not None:
            self.role_name_list = role_name_list

    @property
    def role_name_list(self):
        r"""Gets the role_name_list of this PremiumWafAgencyRequest.

        **参数解释：** 创建独享引擎代理策略名列表 **约束限制：** 已经存在的策略，无法再次创建 **取值范围：** 列表中支持以下策略名字 - evs_to_waf_operate_policy - vpc_to_waf_operate_policy - ecs_to_waf_operate_policy - elb_to_waf_operate_policy **默认取值：** 不涉及

        :return: The role_name_list of this PremiumWafAgencyRequest.
        :rtype: list[str]
        """
        return self._role_name_list

    @role_name_list.setter
    def role_name_list(self, role_name_list):
        r"""Sets the role_name_list of this PremiumWafAgencyRequest.

        **参数解释：** 创建独享引擎代理策略名列表 **约束限制：** 已经存在的策略，无法再次创建 **取值范围：** 列表中支持以下策略名字 - evs_to_waf_operate_policy - vpc_to_waf_operate_policy - ecs_to_waf_operate_policy - elb_to_waf_operate_policy **默认取值：** 不涉及

        :param role_name_list: The role_name_list of this PremiumWafAgencyRequest.
        :type role_name_list: list[str]
        """
        self._role_name_list = role_name_list

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
        if not isinstance(other, PremiumWafAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
