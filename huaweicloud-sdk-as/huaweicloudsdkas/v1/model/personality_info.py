# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersonalityInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'content': 'str'
    }

    attribute_map = {
        'path': 'path',
        'content': 'content'
    }

    def __init__(self, path=None, content=None):
        """PersonalityInfo

        The model defined in huaweicloud sdk

        :param path: 注入文件路径信息。Linux系统请输入注入文件保存路径，例如 “/etc/foo.txt”。Windows系统注入文件自动保存在C盘根目录，只需要输入保存文件名，例如 “foo”，文件名只能包含字母（a~zA~Z）和数字（0~9）。
        :type path: str
        :param content: 注入文件内容。该值应指定为注入文件的内容进行base64格式编码后的信息。
        :type content: str
        """
        
        

        self._path = None
        self._content = None
        self.discriminator = None

        self.path = path
        self.content = content

    @property
    def path(self):
        """Gets the path of this PersonalityInfo.

        注入文件路径信息。Linux系统请输入注入文件保存路径，例如 “/etc/foo.txt”。Windows系统注入文件自动保存在C盘根目录，只需要输入保存文件名，例如 “foo”，文件名只能包含字母（a~zA~Z）和数字（0~9）。

        :return: The path of this PersonalityInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PersonalityInfo.

        注入文件路径信息。Linux系统请输入注入文件保存路径，例如 “/etc/foo.txt”。Windows系统注入文件自动保存在C盘根目录，只需要输入保存文件名，例如 “foo”，文件名只能包含字母（a~zA~Z）和数字（0~9）。

        :param path: The path of this PersonalityInfo.
        :type path: str
        """
        self._path = path

    @property
    def content(self):
        """Gets the content of this PersonalityInfo.

        注入文件内容。该值应指定为注入文件的内容进行base64格式编码后的信息。

        :return: The content of this PersonalityInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PersonalityInfo.

        注入文件内容。该值应指定为注入文件的内容进行base64格式编码后的信息。

        :param content: The content of this PersonalityInfo.
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
        if not isinstance(other, PersonalityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
