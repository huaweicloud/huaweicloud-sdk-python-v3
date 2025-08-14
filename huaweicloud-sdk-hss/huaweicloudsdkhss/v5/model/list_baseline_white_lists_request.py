# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBaselineWhiteListsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'check_rule_name': 'str',
        'os_type': 'str',
        'rule_type': 'str',
        'tag': 'str',
        'description': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'check_rule_name': 'check_rule_name',
        'os_type': 'os_type',
        'rule_type': 'rule_type',
        'tag': 'tag',
        'description': 'description'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, check_rule_name=None, os_type=None, rule_type=None, tag=None, description=None):
        r"""ListBaselineWhiteListsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param check_rule_name: 基线检查的检查项名称
        :type check_rule_name: str
        :param os_type: 基线检查的操作系统 - Linux - Windows
        :type os_type: str
        :param rule_type: 基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机
        :type rule_type: str
        :param tag: 基线检查中检查项的检查类型 - 访问控制 - 服务配置
        :type tag: str
        :param description: 基线检查白名单备注
        :type description: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._check_rule_name = None
        self._os_type = None
        self._rule_type = None
        self._tag = None
        self._description = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if os_type is not None:
            self.os_type = os_type
        if rule_type is not None:
            self.rule_type = rule_type
        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBaselineWhiteListsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBaselineWhiteListsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListBaselineWhiteListsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListBaselineWhiteListsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListBaselineWhiteListsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBaselineWhiteListsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListBaselineWhiteListsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBaselineWhiteListsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListBaselineWhiteListsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBaselineWhiteListsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListBaselineWhiteListsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ListBaselineWhiteListsRequest.

        基线检查的检查项名称

        :return: The check_rule_name of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ListBaselineWhiteListsRequest.

        基线检查的检查项名称

        :param check_rule_name: The check_rule_name of this ListBaselineWhiteListsRequest.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListBaselineWhiteListsRequest.

        基线检查的操作系统 - Linux - Windows

        :return: The os_type of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListBaselineWhiteListsRequest.

        基线检查的操作系统 - Linux - Windows

        :param os_type: The os_type of this ListBaselineWhiteListsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ListBaselineWhiteListsRequest.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :return: The rule_type of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ListBaselineWhiteListsRequest.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :param rule_type: The rule_type of this ListBaselineWhiteListsRequest.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def tag(self):
        r"""Gets the tag of this ListBaselineWhiteListsRequest.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :return: The tag of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListBaselineWhiteListsRequest.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :param tag: The tag of this ListBaselineWhiteListsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def description(self):
        r"""Gets the description of this ListBaselineWhiteListsRequest.

        基线检查白名单备注

        :return: The description of this ListBaselineWhiteListsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListBaselineWhiteListsRequest.

        基线检查白名单备注

        :param description: The description of this ListBaselineWhiteListsRequest.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListBaselineWhiteListsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
