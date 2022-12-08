# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseGroup:

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
        'delete_allowed': 'bool',
        'group_desc': 'str',
        'group_name': 'str',
        'id': 'str',
        'rule_names': 'str',
        'task_names': 'str'
    }

    attribute_map = {
        'category': 'category',
        'delete_allowed': 'delete_allowed',
        'group_desc': 'group_desc',
        'group_name': 'group_name',
        'id': 'id',
        'rule_names': 'rule_names',
        'task_names': 'task_names'
    }

    def __init__(self, category=None, delete_allowed=None, group_desc=None, group_name=None, id=None, rule_names=None, task_names=None):
        """ResponseGroup

        The model defined in huaweicloud sdk

        :param category: 规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)
        :type category: str
        :param delete_allowed: 是否允许删除
        :type delete_allowed: bool
        :param group_desc: 规则组描述
        :type group_desc: str
        :param group_name: 规则组名称
        :type group_name: str
        :param id: 规则组ID
        :type id: str
        :param rule_names: 规则名称
        :type rule_names: str
        :param task_names: 扫描任务名称
        :type task_names: str
        """
        
        

        self._category = None
        self._delete_allowed = None
        self._group_desc = None
        self._group_name = None
        self._id = None
        self._rule_names = None
        self._task_names = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if delete_allowed is not None:
            self.delete_allowed = delete_allowed
        if group_desc is not None:
            self.group_desc = group_desc
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if rule_names is not None:
            self.rule_names = rule_names
        if task_names is not None:
            self.task_names = task_names

    @property
    def category(self):
        """Gets the category of this ResponseGroup.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :return: The category of this ResponseGroup.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ResponseGroup.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :param category: The category of this ResponseGroup.
        :type category: str
        """
        self._category = category

    @property
    def delete_allowed(self):
        """Gets the delete_allowed of this ResponseGroup.

        是否允许删除

        :return: The delete_allowed of this ResponseGroup.
        :rtype: bool
        """
        return self._delete_allowed

    @delete_allowed.setter
    def delete_allowed(self, delete_allowed):
        """Sets the delete_allowed of this ResponseGroup.

        是否允许删除

        :param delete_allowed: The delete_allowed of this ResponseGroup.
        :type delete_allowed: bool
        """
        self._delete_allowed = delete_allowed

    @property
    def group_desc(self):
        """Gets the group_desc of this ResponseGroup.

        规则组描述

        :return: The group_desc of this ResponseGroup.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        """Sets the group_desc of this ResponseGroup.

        规则组描述

        :param group_desc: The group_desc of this ResponseGroup.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def group_name(self):
        """Gets the group_name of this ResponseGroup.

        规则组名称

        :return: The group_name of this ResponseGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ResponseGroup.

        规则组名称

        :param group_name: The group_name of this ResponseGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this ResponseGroup.

        规则组ID

        :return: The id of this ResponseGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseGroup.

        规则组ID

        :param id: The id of this ResponseGroup.
        :type id: str
        """
        self._id = id

    @property
    def rule_names(self):
        """Gets the rule_names of this ResponseGroup.

        规则名称

        :return: The rule_names of this ResponseGroup.
        :rtype: str
        """
        return self._rule_names

    @rule_names.setter
    def rule_names(self, rule_names):
        """Sets the rule_names of this ResponseGroup.

        规则名称

        :param rule_names: The rule_names of this ResponseGroup.
        :type rule_names: str
        """
        self._rule_names = rule_names

    @property
    def task_names(self):
        """Gets the task_names of this ResponseGroup.

        扫描任务名称

        :return: The task_names of this ResponseGroup.
        :rtype: str
        """
        return self._task_names

    @task_names.setter
    def task_names(self, task_names):
        """Sets the task_names of this ResponseGroup.

        扫描任务名称

        :param task_names: The task_names of this ResponseGroup.
        :type task_names: str
        """
        self._task_names = task_names

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
        if not isinstance(other, ResponseGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
