# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Message:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'content': 'str'
    }

    attribute_map = {
        'role': 'role',
        'content': 'content'
    }

    def __init__(self, role=None, content=None):
        r"""Message

        The model defined in huaweicloud sdk

        :param role: 角色
        :type role: str
        :param content: 问答对文本内容，最小长度：1，最大长度：模型支持的max_tokens数量乘以系数，默认系数为1.5，并且所有content的总长度不能超过该最大长度
        :type content: str
        """
        
        

        self._role = None
        self._content = None
        self.discriminator = None

        if role is not None:
            self.role = role
        self.content = content

    @property
    def role(self):
        r"""Gets the role of this Message.

        角色

        :return: The role of this Message.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this Message.

        角色

        :param role: The role of this Message.
        :type role: str
        """
        self._role = role

    @property
    def content(self):
        r"""Gets the content of this Message.

        问答对文本内容，最小长度：1，最大长度：模型支持的max_tokens数量乘以系数，默认系数为1.5，并且所有content的总长度不能超过该最大长度

        :return: The content of this Message.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this Message.

        问答对文本内容，最小长度：1，最大长度：模型支持的max_tokens数量乘以系数，默认系数为1.5，并且所有content的总长度不能超过该最大长度

        :param content: The content of this Message.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
