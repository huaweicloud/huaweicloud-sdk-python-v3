# coding: utf-8

import pprint
import re

import six





class ComponentCreate:


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
        'runtime': 'RuntimeType',
        'category': 'ComponentCategory',
        'sub_category': 'ComponentSubCategory',
        'description': 'str',
        'source': 'SourceObject',
        'build': 'Build'
    }

    attribute_map = {
        'name': 'name',
        'runtime': 'runtime',
        'category': 'category',
        'sub_category': 'sub_category',
        'description': 'description',
        'source': 'source',
        'build': 'build'
    }

    def __init__(self, name=None, runtime=None, category=None, sub_category=None, description=None, source=None, build=None):
        """ComponentCreate - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._runtime = None
        self._category = None
        self._sub_category = None
        self._description = None
        self._source = None
        self._build = None
        self.discriminator = None

        self.name = name
        self.runtime = runtime
        self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build

    @property
    def name(self):
        """Gets the name of this ComponentCreate.

        应用组件名称。

        :return: The name of this ComponentCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentCreate.

        应用组件名称。

        :param name: The name of this ComponentCreate.
        :type: str
        """
        self._name = name

    @property
    def runtime(self):
        """Gets the runtime of this ComponentCreate.


        :return: The runtime of this ComponentCreate.
        :rtype: RuntimeType
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ComponentCreate.


        :param runtime: The runtime of this ComponentCreate.
        :type: RuntimeType
        """
        self._runtime = runtime

    @property
    def category(self):
        """Gets the category of this ComponentCreate.


        :return: The category of this ComponentCreate.
        :rtype: ComponentCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ComponentCreate.


        :param category: The category of this ComponentCreate.
        :type: ComponentCategory
        """
        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this ComponentCreate.


        :return: The sub_category of this ComponentCreate.
        :rtype: ComponentSubCategory
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this ComponentCreate.


        :param sub_category: The sub_category of this ComponentCreate.
        :type: ComponentSubCategory
        """
        self._sub_category = sub_category

    @property
    def description(self):
        """Gets the description of this ComponentCreate.

        描述。

        :return: The description of this ComponentCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentCreate.

        描述。

        :param description: The description of this ComponentCreate.
        :type: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this ComponentCreate.


        :return: The source of this ComponentCreate.
        :rtype: SourceObject
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentCreate.


        :param source: The source of this ComponentCreate.
        :type: SourceObject
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this ComponentCreate.


        :return: The build of this ComponentCreate.
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ComponentCreate.


        :param build: The build of this ComponentCreate.
        :type: Build
        """
        self._build = build

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
