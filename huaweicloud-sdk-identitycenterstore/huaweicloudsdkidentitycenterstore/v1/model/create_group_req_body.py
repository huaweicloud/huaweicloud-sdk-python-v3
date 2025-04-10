# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupReqBody:

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
        'display_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name'
    }

    def __init__(self, description=None, display_name=None):
        r"""CreateGroupReqBody

        The model defined in huaweicloud sdk

        :param description: 用户组描述
        :type description: str
        :param display_name: 用户组显示名称
        :type display_name: str
        """
        
        

        self._description = None
        self._display_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this CreateGroupReqBody.

        用户组描述

        :return: The description of this CreateGroupReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGroupReqBody.

        用户组描述

        :param description: The description of this CreateGroupReqBody.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateGroupReqBody.

        用户组显示名称

        :return: The display_name of this CreateGroupReqBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateGroupReqBody.

        用户组显示名称

        :param display_name: The display_name of this CreateGroupReqBody.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, CreateGroupReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
