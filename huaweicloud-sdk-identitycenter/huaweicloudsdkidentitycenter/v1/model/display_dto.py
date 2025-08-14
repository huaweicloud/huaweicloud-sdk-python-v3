# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'display_name': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'icon': 'icon'
    }

    def __init__(self, description=None, display_name=None, icon=None):
        r"""DisplayDto

        The model defined in huaweicloud sdk

        :param description: 应用程序描述
        :type description: str
        :param display_name: 应用程序显示名称
        :type display_name: str
        :param icon: 应用程序图标
        :type icon: str
        """
        
        

        self._description = None
        self._display_name = None
        self._icon = None
        self.discriminator = None

        self.description = description
        self.display_name = display_name
        if icon is not None:
            self.icon = icon

    @property
    def description(self):
        r"""Gets the description of this DisplayDto.

        应用程序描述

        :return: The description of this DisplayDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DisplayDto.

        应用程序描述

        :param description: The description of this DisplayDto.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this DisplayDto.

        应用程序显示名称

        :return: The display_name of this DisplayDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this DisplayDto.

        应用程序显示名称

        :param display_name: The display_name of this DisplayDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def icon(self):
        r"""Gets the icon of this DisplayDto.

        应用程序图标

        :return: The icon of this DisplayDto.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this DisplayDto.

        应用程序图标

        :param icon: The icon of this DisplayDto.
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
        if not isinstance(other, DisplayDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
