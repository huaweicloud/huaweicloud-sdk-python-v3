# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogEntity:

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
        'create_time': 'int',
        'parameters': 'dict(str, str)',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'create_time': 'create_time',
        'parameters': 'parameters',
        'description': 'description'
    }

    def __init__(self, name=None, create_time=None, parameters=None, description=None):
        """CatalogEntity

        The model defined in huaweicloud sdk

        :param name: DLI侧catalog映射名称。
        :type name: str
        :param create_time: 创建时间
        :type create_time: int
        :param parameters: 属性中包含type和externalCatalog
        :type parameters: dict(str, str)
        :param description: 描述
        :type description: str
        """
        
        

        self._name = None
        self._create_time = None
        self._parameters = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if parameters is not None:
            self.parameters = parameters
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CatalogEntity.

        DLI侧catalog映射名称。

        :return: The name of this CatalogEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogEntity.

        DLI侧catalog映射名称。

        :param name: The name of this CatalogEntity.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        """Gets the create_time of this CatalogEntity.

        创建时间

        :return: The create_time of this CatalogEntity.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CatalogEntity.

        创建时间

        :param create_time: The create_time of this CatalogEntity.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def parameters(self):
        """Gets the parameters of this CatalogEntity.

        属性中包含type和externalCatalog

        :return: The parameters of this CatalogEntity.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CatalogEntity.

        属性中包含type和externalCatalog

        :param parameters: The parameters of this CatalogEntity.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def description(self):
        """Gets the description of this CatalogEntity.

        描述

        :return: The description of this CatalogEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CatalogEntity.

        描述

        :param description: The description of this CatalogEntity.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CatalogEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
