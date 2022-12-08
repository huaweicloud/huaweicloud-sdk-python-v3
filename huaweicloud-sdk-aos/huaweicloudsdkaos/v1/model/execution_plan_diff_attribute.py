# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanDiffAttribute:

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
        'previous_value': 'str',
        'target_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'previous_value': 'previous_value',
        'target_value': 'target_value'
    }

    def __init__(self, name=None, previous_value=None, target_value=None):
        """ExecutionPlanDiffAttribute

        The model defined in huaweicloud sdk

        :param name: 当前资源被修改的参数的名字。
        :type name: str
        :param previous_value: 当前资源被修改前参数的值，新创建时为空。
        :type previous_value: str
        :param target_value: 当前资源被修改的参数的目的值，删除时为空。
        :type target_value: str
        """
        
        

        self._name = None
        self._previous_value = None
        self._target_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if previous_value is not None:
            self.previous_value = previous_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def name(self):
        """Gets the name of this ExecutionPlanDiffAttribute.

        当前资源被修改的参数的名字。

        :return: The name of this ExecutionPlanDiffAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecutionPlanDiffAttribute.

        当前资源被修改的参数的名字。

        :param name: The name of this ExecutionPlanDiffAttribute.
        :type name: str
        """
        self._name = name

    @property
    def previous_value(self):
        """Gets the previous_value of this ExecutionPlanDiffAttribute.

        当前资源被修改前参数的值，新创建时为空。

        :return: The previous_value of this ExecutionPlanDiffAttribute.
        :rtype: str
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        """Sets the previous_value of this ExecutionPlanDiffAttribute.

        当前资源被修改前参数的值，新创建时为空。

        :param previous_value: The previous_value of this ExecutionPlanDiffAttribute.
        :type previous_value: str
        """
        self._previous_value = previous_value

    @property
    def target_value(self):
        """Gets the target_value of this ExecutionPlanDiffAttribute.

        当前资源被修改的参数的目的值，删除时为空。

        :return: The target_value of this ExecutionPlanDiffAttribute.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this ExecutionPlanDiffAttribute.

        当前资源被修改的参数的目的值，删除时为空。

        :param target_value: The target_value of this ExecutionPlanDiffAttribute.
        :type target_value: str
        """
        self._target_value = target_value

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
        if not isinstance(other, ExecutionPlanDiffAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
