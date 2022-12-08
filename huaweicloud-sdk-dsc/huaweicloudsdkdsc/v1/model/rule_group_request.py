# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'default_status': 'bool',
        'group_desc': 'str',
        'group_name': 'str',
        'id': 'str',
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'default_status': 'default_status',
        'group_desc': 'group_desc',
        'group_name': 'group_name',
        'id': 'id',
        'rule_ids': 'rule_ids'
    }

    def __init__(self, category=None, default_status=None, group_desc=None, group_name=None, id=None, rule_ids=None):
        """RuleGroupRequest

        The model defined in huaweicloud sdk

        :param category: 规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)
        :type category: str
        :param default_status: 是否默认规则组
        :type default_status: bool
        :param group_desc: 规则组描述
        :type group_desc: str
        :param group_name: 规则组名称
        :type group_name: str
        :param id: 规则组ID
        :type id: str
        :param rule_ids: 包含的规则ID列表
        :type rule_ids: list[str]
        """
        
        

        self._category = None
        self._default_status = None
        self._group_desc = None
        self._group_name = None
        self._id = None
        self._rule_ids = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if default_status is not None:
            self.default_status = default_status
        if group_desc is not None:
            self.group_desc = group_desc
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def category(self):
        """Gets the category of this RuleGroupRequest.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :return: The category of this RuleGroupRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RuleGroupRequest.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :param category: The category of this RuleGroupRequest.
        :type category: str
        """
        self._category = category

    @property
    def default_status(self):
        """Gets the default_status of this RuleGroupRequest.

        是否默认规则组

        :return: The default_status of this RuleGroupRequest.
        :rtype: bool
        """
        return self._default_status

    @default_status.setter
    def default_status(self, default_status):
        """Sets the default_status of this RuleGroupRequest.

        是否默认规则组

        :param default_status: The default_status of this RuleGroupRequest.
        :type default_status: bool
        """
        self._default_status = default_status

    @property
    def group_desc(self):
        """Gets the group_desc of this RuleGroupRequest.

        规则组描述

        :return: The group_desc of this RuleGroupRequest.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        """Sets the group_desc of this RuleGroupRequest.

        规则组描述

        :param group_desc: The group_desc of this RuleGroupRequest.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def group_name(self):
        """Gets the group_name of this RuleGroupRequest.

        规则组名称

        :return: The group_name of this RuleGroupRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RuleGroupRequest.

        规则组名称

        :param group_name: The group_name of this RuleGroupRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this RuleGroupRequest.

        规则组ID

        :return: The id of this RuleGroupRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleGroupRequest.

        规则组ID

        :param id: The id of this RuleGroupRequest.
        :type id: str
        """
        self._id = id

    @property
    def rule_ids(self):
        """Gets the rule_ids of this RuleGroupRequest.

        包含的规则ID列表

        :return: The rule_ids of this RuleGroupRequest.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this RuleGroupRequest.

        包含的规则ID列表

        :param rule_ids: The rule_ids of this RuleGroupRequest.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

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
        if not isinstance(other, RuleGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
