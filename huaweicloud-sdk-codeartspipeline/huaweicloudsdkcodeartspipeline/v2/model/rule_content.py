# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'can_modify_when_inherit': 'bool',
        'properties': 'list[RuleProperty]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'can_modify_when_inherit': 'can_modify_when_inherit',
        'properties': 'properties'
    }

    def __init__(self, group_name=None, can_modify_when_inherit=None, properties=None):
        r"""RuleContent

        The model defined in huaweicloud sdk

        :param group_name: 分组名称
        :type group_name: str
        :param can_modify_when_inherit: 继承后的子策略是否可以修改阈值
        :type can_modify_when_inherit: bool
        :param properties: 规则属性列表
        :type properties: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleProperty`]
        """
        
        

        self._group_name = None
        self._can_modify_when_inherit = None
        self._properties = None
        self.discriminator = None

        self.group_name = group_name
        if can_modify_when_inherit is not None:
            self.can_modify_when_inherit = can_modify_when_inherit
        self.properties = properties

    @property
    def group_name(self):
        r"""Gets the group_name of this RuleContent.

        分组名称

        :return: The group_name of this RuleContent.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this RuleContent.

        分组名称

        :param group_name: The group_name of this RuleContent.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def can_modify_when_inherit(self):
        r"""Gets the can_modify_when_inherit of this RuleContent.

        继承后的子策略是否可以修改阈值

        :return: The can_modify_when_inherit of this RuleContent.
        :rtype: bool
        """
        return self._can_modify_when_inherit

    @can_modify_when_inherit.setter
    def can_modify_when_inherit(self, can_modify_when_inherit):
        r"""Sets the can_modify_when_inherit of this RuleContent.

        继承后的子策略是否可以修改阈值

        :param can_modify_when_inherit: The can_modify_when_inherit of this RuleContent.
        :type can_modify_when_inherit: bool
        """
        self._can_modify_when_inherit = can_modify_when_inherit

    @property
    def properties(self):
        r"""Gets the properties of this RuleContent.

        规则属性列表

        :return: The properties of this RuleContent.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this RuleContent.

        规则属性列表

        :param properties: The properties of this RuleContent.
        :type properties: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleProperty`]
        """
        self._properties = properties

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
        if not isinstance(other, RuleContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
