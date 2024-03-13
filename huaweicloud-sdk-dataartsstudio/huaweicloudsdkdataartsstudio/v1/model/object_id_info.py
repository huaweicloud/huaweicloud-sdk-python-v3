# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectIdInfo:

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
        'type_name': 'str',
        'qualified_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type_name': 'type_name',
        'qualified_name': 'qualified_name'
    }

    def __init__(self, name=None, type_name=None, qualified_name=None):
        """ObjectIdInfo

        The model defined in huaweicloud sdk

        :param name: 作业算子名称
        :type name: str
        :param type_name: 资产类型
        :type type_name: str
        :param qualified_name: 作业资产唯一限定名称
        :type qualified_name: str
        """
        
        

        self._name = None
        self._type_name = None
        self._qualified_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type_name is not None:
            self.type_name = type_name
        if qualified_name is not None:
            self.qualified_name = qualified_name

    @property
    def name(self):
        """Gets the name of this ObjectIdInfo.

        作业算子名称

        :return: The name of this ObjectIdInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectIdInfo.

        作业算子名称

        :param name: The name of this ObjectIdInfo.
        :type name: str
        """
        self._name = name

    @property
    def type_name(self):
        """Gets the type_name of this ObjectIdInfo.

        资产类型

        :return: The type_name of this ObjectIdInfo.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this ObjectIdInfo.

        资产类型

        :param type_name: The type_name of this ObjectIdInfo.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def qualified_name(self):
        """Gets the qualified_name of this ObjectIdInfo.

        作业资产唯一限定名称

        :return: The qualified_name of this ObjectIdInfo.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this ObjectIdInfo.

        作业资产唯一限定名称

        :param qualified_name: The qualified_name of this ObjectIdInfo.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

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
        if not isinstance(other, ObjectIdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
