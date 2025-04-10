# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubAppUpdateParam:

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
        'display_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description'
    }

    def __init__(self, name=None, display_name=None, description=None):
        r"""SubAppUpdateParam

        The model defined in huaweicloud sdk

        :param name: 子应用唯一标识
        :type name: str
        :param display_name: 子应用节点显示名称
        :type display_name: str
        :param description: 子应用描述
        :type description: str
        """
        
        

        self._name = None
        self._display_name = None
        self._description = None
        self.discriminator = None

        self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this SubAppUpdateParam.

        子应用唯一标识

        :return: The name of this SubAppUpdateParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubAppUpdateParam.

        子应用唯一标识

        :param name: The name of this SubAppUpdateParam.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this SubAppUpdateParam.

        子应用节点显示名称

        :return: The display_name of this SubAppUpdateParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SubAppUpdateParam.

        子应用节点显示名称

        :param display_name: The display_name of this SubAppUpdateParam.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this SubAppUpdateParam.

        子应用描述

        :return: The description of this SubAppUpdateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SubAppUpdateParam.

        子应用描述

        :param description: The description of this SubAppUpdateParam.
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
        if not isinstance(other, SubAppUpdateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
