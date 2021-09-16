# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVariableResqJson:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'variable_id': 'int'
    }

    attribute_map = {
        'variable_id': 'variable_id'
    }

    def __init__(self, variable_id=None):
        """CreateVariableResqJson - a model defined in huaweicloud sdk"""
        
        

        self._variable_id = None
        self.discriminator = None

        if variable_id is not None:
            self.variable_id = variable_id

    @property
    def variable_id(self):
        """Gets the variable_id of this CreateVariableResqJson.

        variable_id

        :return: The variable_id of this CreateVariableResqJson.
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """Sets the variable_id of this CreateVariableResqJson.

        variable_id

        :param variable_id: The variable_id of this CreateVariableResqJson.
        :type: int
        """
        self._variable_id = variable_id

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
        if not isinstance(other, CreateVariableResqJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other