# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_user_name': 'str',
        'new_description': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'new_user_name': 'new_user_name',
        'new_description': 'new_description',
        'enabled': 'enabled'
    }

    def __init__(self, new_user_name=None, new_description=None, enabled=None):
        r"""UpdateUserReqBody

        The model defined in huaweicloud sdk

        :param new_user_name: IAM用户名，长度为1到64个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;-\&quot;、\&quot;.\&quot;和空格的字符串，且首位不能为数字。
        :type new_user_name: str
        :param new_description: IAM用户描述信息，长度为0到255个字符，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type new_description: str
        :param enabled: IAM用户是否启用。
        :type enabled: bool
        """
        
        

        self._new_user_name = None
        self._new_description = None
        self._enabled = None
        self.discriminator = None

        if new_user_name is not None:
            self.new_user_name = new_user_name
        if new_description is not None:
            self.new_description = new_description
        if enabled is not None:
            self.enabled = enabled

    @property
    def new_user_name(self):
        r"""Gets the new_user_name of this UpdateUserReqBody.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :return: The new_user_name of this UpdateUserReqBody.
        :rtype: str
        """
        return self._new_user_name

    @new_user_name.setter
    def new_user_name(self, new_user_name):
        r"""Sets the new_user_name of this UpdateUserReqBody.

        IAM用户名，长度为1到64个字符，只包含字母、数字、\"_\"、\"-\"、\".\"和空格的字符串，且首位不能为数字。

        :param new_user_name: The new_user_name of this UpdateUserReqBody.
        :type new_user_name: str
        """
        self._new_user_name = new_user_name

    @property
    def new_description(self):
        r"""Gets the new_description of this UpdateUserReqBody.

        IAM用户描述信息，长度为0到255个字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The new_description of this UpdateUserReqBody.
        :rtype: str
        """
        return self._new_description

    @new_description.setter
    def new_description(self, new_description):
        r"""Sets the new_description of this UpdateUserReqBody.

        IAM用户描述信息，长度为0到255个字符，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param new_description: The new_description of this UpdateUserReqBody.
        :type new_description: str
        """
        self._new_description = new_description

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateUserReqBody.

        IAM用户是否启用。

        :return: The enabled of this UpdateUserReqBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateUserReqBody.

        IAM用户是否启用。

        :param enabled: The enabled of this UpdateUserReqBody.
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
        if not isinstance(other, UpdateUserReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
