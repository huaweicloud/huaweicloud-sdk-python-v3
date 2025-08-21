# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryInheritSettingUpdateBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'inherit_mod': 'str'
    }

    attribute_map = {
        'name': 'name',
        'inherit_mod': 'inherit_mod'
    }

    def __init__(self, name=None, inherit_mod=None):
        r"""RepositoryInheritSettingUpdateBodyDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 设置源类型。 **约束限制：** 不涉及。 **取值范围：** - protected_branches，保护分支设置。 - protected_tags，保护Tag设置。 - repository_settings，仓库设置。 - push_rules，提交规则设置。 - merge_requests，合并请求设置。 - e2e_settings，E2E设置。 - watermark，水印设置。 **默认取值：** 不涉及。
        :type name: str
        :param inherit_mod: **参数解释：** 继承设置。 **约束限制：** 不涉及。 **取值范围：** - inherit，继承上级配置。 - custom，使用当前仓库配置。 **默认取值：** 不涉及。
        :type inherit_mod: str
        """
        
        

        self._name = None
        self._inherit_mod = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if inherit_mod is not None:
            self.inherit_mod = inherit_mod

    @property
    def name(self):
        r"""Gets the name of this RepositoryInheritSettingUpdateBodyDto.

        **参数解释：** 设置源类型。 **约束限制：** 不涉及。 **取值范围：** - protected_branches，保护分支设置。 - protected_tags，保护Tag设置。 - repository_settings，仓库设置。 - push_rules，提交规则设置。 - merge_requests，合并请求设置。 - e2e_settings，E2E设置。 - watermark，水印设置。 **默认取值：** 不涉及。

        :return: The name of this RepositoryInheritSettingUpdateBodyDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryInheritSettingUpdateBodyDto.

        **参数解释：** 设置源类型。 **约束限制：** 不涉及。 **取值范围：** - protected_branches，保护分支设置。 - protected_tags，保护Tag设置。 - repository_settings，仓库设置。 - push_rules，提交规则设置。 - merge_requests，合并请求设置。 - e2e_settings，E2E设置。 - watermark，水印设置。 **默认取值：** 不涉及。

        :param name: The name of this RepositoryInheritSettingUpdateBodyDto.
        :type name: str
        """
        self._name = name

    @property
    def inherit_mod(self):
        r"""Gets the inherit_mod of this RepositoryInheritSettingUpdateBodyDto.

        **参数解释：** 继承设置。 **约束限制：** 不涉及。 **取值范围：** - inherit，继承上级配置。 - custom，使用当前仓库配置。 **默认取值：** 不涉及。

        :return: The inherit_mod of this RepositoryInheritSettingUpdateBodyDto.
        :rtype: str
        """
        return self._inherit_mod

    @inherit_mod.setter
    def inherit_mod(self, inherit_mod):
        r"""Sets the inherit_mod of this RepositoryInheritSettingUpdateBodyDto.

        **参数解释：** 继承设置。 **约束限制：** 不涉及。 **取值范围：** - inherit，继承上级配置。 - custom，使用当前仓库配置。 **默认取值：** 不涉及。

        :param inherit_mod: The inherit_mod of this RepositoryInheritSettingUpdateBodyDto.
        :type inherit_mod: str
        """
        self._inherit_mod = inherit_mod

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
        if not isinstance(other, RepositoryInheritSettingUpdateBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
