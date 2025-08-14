# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayDataDto:

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
        'icon_url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'icon_url': 'icon_url'
    }

    def __init__(self, description=None, display_name=None, icon_url=None):
        r"""DisplayDataDto

        The model defined in huaweicloud sdk

        :param description: 应用程序提供商描述
        :type description: str
        :param display_name: 应用程序提供商显示名
        :type display_name: str
        :param icon_url: 应用程序提供商图标
        :type icon_url: str
        """
        
        

        self._description = None
        self._display_name = None
        self._icon_url = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if icon_url is not None:
            self.icon_url = icon_url

    @property
    def description(self):
        r"""Gets the description of this DisplayDataDto.

        应用程序提供商描述

        :return: The description of this DisplayDataDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DisplayDataDto.

        应用程序提供商描述

        :param description: The description of this DisplayDataDto.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this DisplayDataDto.

        应用程序提供商显示名

        :return: The display_name of this DisplayDataDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this DisplayDataDto.

        应用程序提供商显示名

        :param display_name: The display_name of this DisplayDataDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def icon_url(self):
        r"""Gets the icon_url of this DisplayDataDto.

        应用程序提供商图标

        :return: The icon_url of this DisplayDataDto.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this DisplayDataDto.

        应用程序提供商图标

        :param icon_url: The icon_url of this DisplayDataDto.
        :type icon_url: str
        """
        self._icon_url = icon_url

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
        if not isinstance(other, DisplayDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
