# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Group:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'created_at': 'datetime',
        'urn': 'str',
        'description': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'created_at': 'created_at',
        'urn': 'urn',
        'description': 'description'
    }

    def __init__(self, group_id=None, group_name=None, created_at=None, urn=None, description=None):
        r"""Group

        The model defined in huaweicloud sdk

        :param group_id: 用户组ID。
        :type group_id: str
        :param group_name: 用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\&quot;_\&quot;、\&quot;-\&quot;、\&quot;{\&quot;和\&quot;}\&quot;的字符串。
        :type group_name: str
        :param created_at: 用户组创建时间。
        :type created_at: datetime
        :param urn: 统一资源名称。
        :type urn: str
        :param description: 用户组描述信息，长度为0到255字符，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        """
        
        

        self._group_id = None
        self._group_name = None
        self._created_at = None
        self._urn = None
        self._description = None
        self.discriminator = None

        self.group_id = group_id
        self.group_name = group_name
        self.created_at = created_at
        self.urn = urn
        if description is not None:
            self.description = description

    @property
    def group_id(self):
        r"""Gets the group_id of this Group.

        用户组ID。

        :return: The group_id of this Group.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this Group.

        用户组ID。

        :param group_id: The group_id of this Group.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this Group.

        用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\"_\"、\"-\"、\"{\"和\"}\"的字符串。

        :return: The group_name of this Group.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this Group.

        用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\"_\"、\"-\"、\"{\"和\"}\"的字符串。

        :param group_name: The group_name of this Group.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def created_at(self):
        r"""Gets the created_at of this Group.

        用户组创建时间。

        :return: The created_at of this Group.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Group.

        用户组创建时间。

        :param created_at: The created_at of this Group.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def urn(self):
        r"""Gets the urn of this Group.

        统一资源名称。

        :return: The urn of this Group.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this Group.

        统一资源名称。

        :param urn: The urn of this Group.
        :type urn: str
        """
        self._urn = urn

    @property
    def description(self):
        r"""Gets the description of this Group.

        用户组描述信息，长度为0到255字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this Group.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Group.

        用户组描述信息，长度为0到255字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this Group.
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
