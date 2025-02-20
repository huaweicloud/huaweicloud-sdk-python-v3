# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBodyApplicationList:

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
        'parent_name': 'str',
        'level': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'parent_name': 'parent_name',
        'level': 'level'
    }

    def __init__(self, name=None, description=None, parent_name=None, level=None):
        """BatchCreateApplicationViewRequestBodyApplicationList

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param parent_name: 父节点名称
        :type parent_name: str
        :param level: 层级，从1开始
        :type level: str
        """
        
        

        self._name = None
        self._description = None
        self._parent_name = None
        self._level = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if parent_name is not None:
            self.parent_name = parent_name
        if level is not None:
            self.level = level

    @property
    def name(self):
        """Gets the name of this BatchCreateApplicationViewRequestBodyApplicationList.

        名称

        :return: The name of this BatchCreateApplicationViewRequestBodyApplicationList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateApplicationViewRequestBodyApplicationList.

        名称

        :param name: The name of this BatchCreateApplicationViewRequestBodyApplicationList.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BatchCreateApplicationViewRequestBodyApplicationList.

        描述

        :return: The description of this BatchCreateApplicationViewRequestBodyApplicationList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchCreateApplicationViewRequestBodyApplicationList.

        描述

        :param description: The description of this BatchCreateApplicationViewRequestBodyApplicationList.
        :type description: str
        """
        self._description = description

    @property
    def parent_name(self):
        """Gets the parent_name of this BatchCreateApplicationViewRequestBodyApplicationList.

        父节点名称

        :return: The parent_name of this BatchCreateApplicationViewRequestBodyApplicationList.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this BatchCreateApplicationViewRequestBodyApplicationList.

        父节点名称

        :param parent_name: The parent_name of this BatchCreateApplicationViewRequestBodyApplicationList.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def level(self):
        """Gets the level of this BatchCreateApplicationViewRequestBodyApplicationList.

        层级，从1开始

        :return: The level of this BatchCreateApplicationViewRequestBodyApplicationList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this BatchCreateApplicationViewRequestBodyApplicationList.

        层级，从1开始

        :param level: The level of this BatchCreateApplicationViewRequestBodyApplicationList.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, BatchCreateApplicationViewRequestBodyApplicationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
