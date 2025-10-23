# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyResourceLevelBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_level_name': 'str',
        'description': 'str',
        'apply_type': 'int',
        'apply_rule': 'str',
        'compliance_rule_id': 'str',
        'resource_level': 'int'
    }

    attribute_map = {
        'resource_level_name': 'resource_level_name',
        'description': 'description',
        'apply_type': 'apply_type',
        'apply_rule': 'apply_rule',
        'compliance_rule_id': 'compliance_rule_id',
        'resource_level': 'resource_level'
    }

    def __init__(self, resource_level_name=None, description=None, apply_type=None, apply_rule=None, compliance_rule_id=None, resource_level=None):
        r"""ModifyResourceLevelBody

        The model defined in huaweicloud sdk

        :param resource_level_name: 资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头
        :type resource_level_name: str
        :param description: 资源分级描述。
        :type description: str
        :param apply_type: 应用方式
        :type apply_type: int
        :param apply_rule: 应用规则
        :type apply_rule: str
        :param compliance_rule_id: 合规规则的id
        :type compliance_rule_id: str
        :param resource_level: 资源等级
        :type resource_level: int
        """
        
        

        self._resource_level_name = None
        self._description = None
        self._apply_type = None
        self._apply_rule = None
        self._compliance_rule_id = None
        self._resource_level = None
        self.discriminator = None

        if resource_level_name is not None:
            self.resource_level_name = resource_level_name
        if description is not None:
            self.description = description
        if apply_type is not None:
            self.apply_type = apply_type
        if apply_rule is not None:
            self.apply_rule = apply_rule
        if compliance_rule_id is not None:
            self.compliance_rule_id = compliance_rule_id
        if resource_level is not None:
            self.resource_level = resource_level

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this ModifyResourceLevelBody.

        资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头

        :return: The resource_level_name of this ModifyResourceLevelBody.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this ModifyResourceLevelBody.

        资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头

        :param resource_level_name: The resource_level_name of this ModifyResourceLevelBody.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def description(self):
        r"""Gets the description of this ModifyResourceLevelBody.

        资源分级描述。

        :return: The description of this ModifyResourceLevelBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyResourceLevelBody.

        资源分级描述。

        :param description: The description of this ModifyResourceLevelBody.
        :type description: str
        """
        self._description = description

    @property
    def apply_type(self):
        r"""Gets the apply_type of this ModifyResourceLevelBody.

        应用方式

        :return: The apply_type of this ModifyResourceLevelBody.
        :rtype: int
        """
        return self._apply_type

    @apply_type.setter
    def apply_type(self, apply_type):
        r"""Sets the apply_type of this ModifyResourceLevelBody.

        应用方式

        :param apply_type: The apply_type of this ModifyResourceLevelBody.
        :type apply_type: int
        """
        self._apply_type = apply_type

    @property
    def apply_rule(self):
        r"""Gets the apply_rule of this ModifyResourceLevelBody.

        应用规则

        :return: The apply_rule of this ModifyResourceLevelBody.
        :rtype: str
        """
        return self._apply_rule

    @apply_rule.setter
    def apply_rule(self, apply_rule):
        r"""Sets the apply_rule of this ModifyResourceLevelBody.

        应用规则

        :param apply_rule: The apply_rule of this ModifyResourceLevelBody.
        :type apply_rule: str
        """
        self._apply_rule = apply_rule

    @property
    def compliance_rule_id(self):
        r"""Gets the compliance_rule_id of this ModifyResourceLevelBody.

        合规规则的id

        :return: The compliance_rule_id of this ModifyResourceLevelBody.
        :rtype: str
        """
        return self._compliance_rule_id

    @compliance_rule_id.setter
    def compliance_rule_id(self, compliance_rule_id):
        r"""Sets the compliance_rule_id of this ModifyResourceLevelBody.

        合规规则的id

        :param compliance_rule_id: The compliance_rule_id of this ModifyResourceLevelBody.
        :type compliance_rule_id: str
        """
        self._compliance_rule_id = compliance_rule_id

    @property
    def resource_level(self):
        r"""Gets the resource_level of this ModifyResourceLevelBody.

        资源等级

        :return: The resource_level of this ModifyResourceLevelBody.
        :rtype: int
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this ModifyResourceLevelBody.

        资源等级

        :param resource_level: The resource_level of this ModifyResourceLevelBody.
        :type resource_level: int
        """
        self._resource_level = resource_level

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
        if not isinstance(other, ModifyResourceLevelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
