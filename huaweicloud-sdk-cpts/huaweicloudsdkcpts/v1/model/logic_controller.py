# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicController:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'for_loop_params': 'str',
        'condition': 'str'
    }

    attribute_map = {
        'for_loop_params': 'for_loop_params',
        'condition': 'condition'
    }

    def __init__(self, for_loop_params=None, condition=None):
        """LogicController

        The model defined in huaweicloud sdk

        :param for_loop_params: for_loop_params
        :type for_loop_params: str
        :param condition: condition
        :type condition: str
        """
        
        

        self._for_loop_params = None
        self._condition = None
        self.discriminator = None

        if for_loop_params is not None:
            self.for_loop_params = for_loop_params
        if condition is not None:
            self.condition = condition

    @property
    def for_loop_params(self):
        """Gets the for_loop_params of this LogicController.

        for_loop_params

        :return: The for_loop_params of this LogicController.
        :rtype: str
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        """Sets the for_loop_params of this LogicController.

        for_loop_params

        :param for_loop_params: The for_loop_params of this LogicController.
        :type for_loop_params: str
        """
        self._for_loop_params = for_loop_params

    @property
    def condition(self):
        """Gets the condition of this LogicController.

        condition

        :return: The condition of this LogicController.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this LogicController.

        condition

        :param condition: The condition of this LogicController.
        :type condition: str
        """
        self._condition = condition

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
        if not isinstance(other, LogicController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
