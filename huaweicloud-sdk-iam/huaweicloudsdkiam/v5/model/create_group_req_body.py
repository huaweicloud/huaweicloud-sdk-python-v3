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
        'group_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'description': 'description'
    }

    def __init__(self, group_name=None, description=None):
        r"""CreateGroupReqBody

        The model defined in huaweicloud sdk

        :param group_name: 用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\&quot;_\&quot;、\&quot;-\&quot;、\&quot;{\&quot;和\&quot;}\&quot;的字符串。
        :type group_name: str
        :param description: 用户组描述信息，长度为0到255字符，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        """
        
        

        self._group_name = None
        self._description = None
        self.discriminator = None

        self.group_name = group_name
        if description is not None:
            self.description = description

    @property
    def group_name(self):
        r"""Gets the group_name of this CreateGroupReqBody.

        用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\"_\"、\"-\"、\"{\"和\"}\"的字符串。

        :return: The group_name of this CreateGroupReqBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CreateGroupReqBody.

        用户组名，长度为1到128个字符，可包含中文、英文、数字、空格、\"_\"、\"-\"、\"{\"和\"}\"的字符串。

        :param group_name: The group_name of this CreateGroupReqBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def description(self):
        r"""Gets the description of this CreateGroupReqBody.

        用户组描述信息，长度为0到255字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this CreateGroupReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGroupReqBody.

        用户组描述信息，长度为0到255字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this CreateGroupReqBody.
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
        if not isinstance(other, CreateGroupReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
