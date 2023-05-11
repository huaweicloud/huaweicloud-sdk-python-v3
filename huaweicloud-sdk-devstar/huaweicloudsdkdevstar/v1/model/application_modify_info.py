# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationModifyInfo:

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
        'icon': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'icon': 'icon'
    }

    def __init__(self, name=None, description=None, icon=None):
        """ApplicationModifyInfo

        The model defined in huaweicloud sdk

        :param name: 应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param icon: 应用图标(传入图片的Base64编码,大小限制15k)
        :type icon: str
        """
        
        

        self._name = None
        self._description = None
        self._icon = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon

    @property
    def name(self):
        """Gets the name of this ApplicationModifyInfo.

        应用名称

        :return: The name of this ApplicationModifyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationModifyInfo.

        应用名称

        :param name: The name of this ApplicationModifyInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ApplicationModifyInfo.

        应用描述

        :return: The description of this ApplicationModifyInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationModifyInfo.

        应用描述

        :param description: The description of this ApplicationModifyInfo.
        :type description: str
        """
        self._description = description

    @property
    def icon(self):
        """Gets the icon of this ApplicationModifyInfo.

        应用图标(传入图片的Base64编码,大小限制15k)

        :return: The icon of this ApplicationModifyInfo.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ApplicationModifyInfo.

        应用图标(传入图片的Base64编码,大小限制15k)

        :param icon: The icon of this ApplicationModifyInfo.
        :type icon: str
        """
        self._icon = icon

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
        if not isinstance(other, ApplicationModifyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
