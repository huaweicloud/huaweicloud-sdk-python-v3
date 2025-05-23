# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyActionInfo:

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
        'description': 'str',
        'action_type': 'str',
        'action_id': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'action_type': 'action_type',
        'action_id': 'action_id',
        'sort_order': 'sort_order'
    }

    def __init__(self, name=None, description=None, action_type=None, action_id=None, sort_order=None):
        r"""ModifyActionInfo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param action_type: 类型，默认AOP_WORKFLOW.
        :type action_type: str
        :param action_id: 剧本动作ID
        :type action_id: str
        :param sort_order: 排序方式
        :type sort_order: str
        """
        
        

        self._name = None
        self._description = None
        self._action_type = None
        self._action_id = None
        self._sort_order = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if action_type is not None:
            self.action_type = action_type
        if action_id is not None:
            self.action_id = action_id
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def name(self):
        r"""Gets the name of this ModifyActionInfo.

        名称

        :return: The name of this ModifyActionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyActionInfo.

        名称

        :param name: The name of this ModifyActionInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModifyActionInfo.

        描述

        :return: The description of this ModifyActionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyActionInfo.

        描述

        :param description: The description of this ModifyActionInfo.
        :type description: str
        """
        self._description = description

    @property
    def action_type(self):
        r"""Gets the action_type of this ModifyActionInfo.

        类型，默认AOP_WORKFLOW.

        :return: The action_type of this ModifyActionInfo.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ModifyActionInfo.

        类型，默认AOP_WORKFLOW.

        :param action_type: The action_type of this ModifyActionInfo.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def action_id(self):
        r"""Gets the action_id of this ModifyActionInfo.

        剧本动作ID

        :return: The action_id of this ModifyActionInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this ModifyActionInfo.

        剧本动作ID

        :param action_id: The action_id of this ModifyActionInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ModifyActionInfo.

        排序方式

        :return: The sort_order of this ModifyActionInfo.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ModifyActionInfo.

        排序方式

        :param sort_order: The sort_order of this ModifyActionInfo.
        :type sort_order: str
        """
        self._sort_order = sort_order

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
        if not isinstance(other, ModifyActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
