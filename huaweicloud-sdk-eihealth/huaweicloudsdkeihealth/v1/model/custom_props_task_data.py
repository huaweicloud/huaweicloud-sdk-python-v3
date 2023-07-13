# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomPropsTaskData:

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
        'type': 'str',
        'smiles': 'list[str]',
        'values': 'list[float]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'smiles': 'smiles',
        'values': 'values'
    }

    def __init__(self, name=None, description=None, type=None, smiles=None, values=None):
        """CustomPropsTaskData

        The model defined in huaweicloud sdk

        :param name: 自定义属性名称
        :type name: str
        :param description: 自定义属性描述信息
        :type description: str
        :param type: 属性预测类型
        :type type: str
        :param smiles: 用于建模的smiles列表
        :type smiles: list[str]
        :param values: 用于建模的属性值列表
        :type values: list[float]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._smiles = None
        self._values = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.smiles = smiles
        self.values = values

    @property
    def name(self):
        """Gets the name of this CustomPropsTaskData.

        自定义属性名称

        :return: The name of this CustomPropsTaskData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomPropsTaskData.

        自定义属性名称

        :param name: The name of this CustomPropsTaskData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomPropsTaskData.

        自定义属性描述信息

        :return: The description of this CustomPropsTaskData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomPropsTaskData.

        自定义属性描述信息

        :param description: The description of this CustomPropsTaskData.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this CustomPropsTaskData.

        属性预测类型

        :return: The type of this CustomPropsTaskData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomPropsTaskData.

        属性预测类型

        :param type: The type of this CustomPropsTaskData.
        :type type: str
        """
        self._type = type

    @property
    def smiles(self):
        """Gets the smiles of this CustomPropsTaskData.

        用于建模的smiles列表

        :return: The smiles of this CustomPropsTaskData.
        :rtype: list[str]
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CustomPropsTaskData.

        用于建模的smiles列表

        :param smiles: The smiles of this CustomPropsTaskData.
        :type smiles: list[str]
        """
        self._smiles = smiles

    @property
    def values(self):
        """Gets the values of this CustomPropsTaskData.

        用于建模的属性值列表

        :return: The values of this CustomPropsTaskData.
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CustomPropsTaskData.

        用于建模的属性值列表

        :param values: The values of this CustomPropsTaskData.
        :type values: list[float]
        """
        self._values = values

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
        if not isinstance(other, CustomPropsTaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
