# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderRuleAclDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dest_rule_id': 'str',
        'top': 'int',
        'bottom': 'int'
    }

    attribute_map = {
        'dest_rule_id': 'dest_rule_id',
        'top': 'top',
        'bottom': 'bottom'
    }

    def __init__(self, dest_rule_id=None, top=None, bottom=None):
        """OrderRuleAclDto

        The model defined in huaweicloud sdk

        :param dest_rule_id: 目标规则id，添加规则位于此规则之后，非置顶时不能为空，置顶时为空
        :type dest_rule_id: str
        :param top: 是否置顶，0代表非置顶，1代表置顶
        :type top: int
        :param bottom: 是否置底，0代表非置底，1代表置底
        :type bottom: int
        """
        
        

        self._dest_rule_id = None
        self._top = None
        self._bottom = None
        self.discriminator = None

        if dest_rule_id is not None:
            self.dest_rule_id = dest_rule_id
        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom

    @property
    def dest_rule_id(self):
        """Gets the dest_rule_id of this OrderRuleAclDto.

        目标规则id，添加规则位于此规则之后，非置顶时不能为空，置顶时为空

        :return: The dest_rule_id of this OrderRuleAclDto.
        :rtype: str
        """
        return self._dest_rule_id

    @dest_rule_id.setter
    def dest_rule_id(self, dest_rule_id):
        """Sets the dest_rule_id of this OrderRuleAclDto.

        目标规则id，添加规则位于此规则之后，非置顶时不能为空，置顶时为空

        :param dest_rule_id: The dest_rule_id of this OrderRuleAclDto.
        :type dest_rule_id: str
        """
        self._dest_rule_id = dest_rule_id

    @property
    def top(self):
        """Gets the top of this OrderRuleAclDto.

        是否置顶，0代表非置顶，1代表置顶

        :return: The top of this OrderRuleAclDto.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this OrderRuleAclDto.

        是否置顶，0代表非置顶，1代表置顶

        :param top: The top of this OrderRuleAclDto.
        :type top: int
        """
        self._top = top

    @property
    def bottom(self):
        """Gets the bottom of this OrderRuleAclDto.

        是否置底，0代表非置底，1代表置底

        :return: The bottom of this OrderRuleAclDto.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this OrderRuleAclDto.

        是否置底，0代表非置底，1代表置底

        :param bottom: The bottom of this OrderRuleAclDto.
        :type bottom: int
        """
        self._bottom = bottom

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
        if not isinstance(other, OrderRuleAclDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
