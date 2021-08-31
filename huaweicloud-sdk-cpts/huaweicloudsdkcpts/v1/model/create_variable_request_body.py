# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVariableRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'variable_type': 'int',
        'variable': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'variable_type': 'variable_type',
        'variable': 'variable'
    }

    def __init__(self, id=None, name=None, variable_type=None, variable=None):
        """CreateVariableRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._variable_type = None
        self._variable = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.variable_type = variable_type
        self.variable = variable

    @property
    def id(self):
        """Gets the id of this CreateVariableRequestBody.

        id

        :return: The id of this CreateVariableRequestBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateVariableRequestBody.

        id

        :param id: The id of this CreateVariableRequestBody.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateVariableRequestBody.

        name

        :return: The name of this CreateVariableRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVariableRequestBody.

        name

        :param name: The name of this CreateVariableRequestBody.
        :type: str
        """
        self._name = name

    @property
    def variable_type(self):
        """Gets the variable_type of this CreateVariableRequestBody.

        variable_type

        :return: The variable_type of this CreateVariableRequestBody.
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        """Sets the variable_type of this CreateVariableRequestBody.

        variable_type

        :param variable_type: The variable_type of this CreateVariableRequestBody.
        :type: int
        """
        self._variable_type = variable_type

    @property
    def variable(self):
        """Gets the variable of this CreateVariableRequestBody.

        variable

        :return: The variable of this CreateVariableRequestBody.
        :rtype: list[object]
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this CreateVariableRequestBody.

        variable

        :param variable: The variable of this CreateVariableRequestBody.
        :type: list[object]
        """
        self._variable = variable

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
        if not isinstance(other, CreateVariableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
