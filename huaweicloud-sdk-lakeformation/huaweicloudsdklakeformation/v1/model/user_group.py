# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_source': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_source': 'group_source',
        'group_id': 'group_id'
    }

    def __init__(self, group_name=None, group_source=None, group_id=None):
        r"""UserGroup

        The model defined in huaweicloud sdk

        :param group_name: 用户组名
        :type group_name: str
        :param group_source: 用户组类型
        :type group_source: str
        :param group_id: 用户组id
        :type group_id: str
        """
        
        

        self._group_name = None
        self._group_source = None
        self._group_id = None
        self.discriminator = None

        self.group_name = group_name
        self.group_source = group_source
        self.group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this UserGroup.

        用户组名

        :return: The group_name of this UserGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this UserGroup.

        用户组名

        :param group_name: The group_name of this UserGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_source(self):
        r"""Gets the group_source of this UserGroup.

        用户组类型

        :return: The group_source of this UserGroup.
        :rtype: str
        """
        return self._group_source

    @group_source.setter
    def group_source(self, group_source):
        r"""Sets the group_source of this UserGroup.

        用户组类型

        :param group_source: The group_source of this UserGroup.
        :type group_source: str
        """
        self._group_source = group_source

    @property
    def group_id(self):
        r"""Gets the group_id of this UserGroup.

        用户组id

        :return: The group_id of this UserGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UserGroup.

        用户组id

        :param group_id: The group_id of this UserGroup.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
