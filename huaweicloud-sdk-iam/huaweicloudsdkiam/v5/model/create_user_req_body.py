# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserReqBody:

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
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, enabled=None):
        r"""CreateUserReqBody

        The model defined in huaweicloud sdk

        :param name: IAM用户名，长度为1到64个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;-\&quot;、\&quot;.\&quot;和空格的字符串，且首位不能为数字。
        :type name: str
        :param description: IAM用户描述信息，长度为0到255个字符，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        :param enabled: IAM用户是否启用。
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this CreateUserReqBody.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :return: The name of this CreateUserReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateUserReqBody.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :param name: The name of this CreateUserReqBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateUserReqBody.

        IAM用户描述信息，长度为0到255个字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this CreateUserReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateUserReqBody.

        IAM用户描述信息，长度为0到255个字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this CreateUserReqBody.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateUserReqBody.

        IAM用户是否启用。

        :return: The enabled of this CreateUserReqBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateUserReqBody.

        IAM用户是否启用。

        :param enabled: The enabled of this CreateUserReqBody.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, CreateUserReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
