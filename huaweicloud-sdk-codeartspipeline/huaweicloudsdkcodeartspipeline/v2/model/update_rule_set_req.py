# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleSetReq:

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
        'parent_id': 'str',
        'rules': 'list[UpdateRuleInstance]'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'rules': 'rules'
    }

    def __init__(self, name=None, parent_id=None, rules=None):
        """UpdateRuleSetReq

        The model defined in huaweicloud sdk

        :param name: 规则模版实例名称
        :type name: str
        :param parent_id: 规则类型
        :type parent_id: str
        :param rules: 规则实例列表
        :type rules: list[:class:`huaweicloudsdkcodeartspipeline.v2.UpdateRuleInstance`]
        """
        
        

        self._name = None
        self._parent_id = None
        self._rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if rules is not None:
            self.rules = rules

    @property
    def name(self):
        """Gets the name of this UpdateRuleSetReq.

        规则模版实例名称

        :return: The name of this UpdateRuleSetReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRuleSetReq.

        规则模版实例名称

        :param name: The name of this UpdateRuleSetReq.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this UpdateRuleSetReq.

        规则类型

        :return: The parent_id of this UpdateRuleSetReq.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this UpdateRuleSetReq.

        规则类型

        :param parent_id: The parent_id of this UpdateRuleSetReq.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def rules(self):
        """Gets the rules of this UpdateRuleSetReq.

        规则实例列表

        :return: The rules of this UpdateRuleSetReq.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.UpdateRuleInstance`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateRuleSetReq.

        规则实例列表

        :param rules: The rules of this UpdateRuleSetReq.
        :type rules: list[:class:`huaweicloudsdkcodeartspipeline.v2.UpdateRuleInstance`]
        """
        self._rules = rules

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
        if not isinstance(other, UpdateRuleSetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
