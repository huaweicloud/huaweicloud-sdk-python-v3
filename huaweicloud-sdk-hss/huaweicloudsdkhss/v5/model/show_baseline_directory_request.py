# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineDirectoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'support_os': 'str',
        'select_type': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'support_os': 'support_os',
        'select_type': 'select_type',
        'group_id': 'group_id'
    }

    def __init__(self, enterprise_project_id=None, support_os=None, select_type=None, group_id=None):
        r"""ShowBaselineDirectoryRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param support_os: **参数解释** 基线检查的操作系统 **约束限制** 不涉及 **取值范围** - Linux - Windows  **默认取值** Linux
        :type support_os: str
        :param select_type: **参数解释** 决定目录结构的顺序 **约束限制** 不涉及 **取值范围** - check_type : 二级目录为基线名称 - tag        : 二级目录为检查项的类型  **默认取值** 不涉及
        :type select_type: str
        :param group_id: **参数解释** 展示该策略组选中哪些检查项 **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及
        :type group_id: str
        """
        
        

        self._enterprise_project_id = None
        self._support_os = None
        self._select_type = None
        self._group_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.support_os = support_os
        self.select_type = select_type
        if group_id is not None:
            self.group_id = group_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowBaselineDirectoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowBaselineDirectoryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowBaselineDirectoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowBaselineDirectoryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def support_os(self):
        r"""Gets the support_os of this ShowBaselineDirectoryRequest.

        **参数解释** 基线检查的操作系统 **约束限制** 不涉及 **取值范围** - Linux - Windows  **默认取值** Linux

        :return: The support_os of this ShowBaselineDirectoryRequest.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this ShowBaselineDirectoryRequest.

        **参数解释** 基线检查的操作系统 **约束限制** 不涉及 **取值范围** - Linux - Windows  **默认取值** Linux

        :param support_os: The support_os of this ShowBaselineDirectoryRequest.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def select_type(self):
        r"""Gets the select_type of this ShowBaselineDirectoryRequest.

        **参数解释** 决定目录结构的顺序 **约束限制** 不涉及 **取值范围** - check_type : 二级目录为基线名称 - tag        : 二级目录为检查项的类型  **默认取值** 不涉及

        :return: The select_type of this ShowBaselineDirectoryRequest.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        r"""Sets the select_type of this ShowBaselineDirectoryRequest.

        **参数解释** 决定目录结构的顺序 **约束限制** 不涉及 **取值范围** - check_type : 二级目录为基线名称 - tag        : 二级目录为检查项的类型  **默认取值** 不涉及

        :param select_type: The select_type of this ShowBaselineDirectoryRequest.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowBaselineDirectoryRequest.

        **参数解释** 展示该策略组选中哪些检查项 **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :return: The group_id of this ShowBaselineDirectoryRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowBaselineDirectoryRequest.

        **参数解释** 展示该策略组选中哪些检查项 **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :param group_id: The group_id of this ShowBaselineDirectoryRequest.
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
        if not isinstance(other, ShowBaselineDirectoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
