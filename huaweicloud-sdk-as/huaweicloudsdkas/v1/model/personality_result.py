# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersonalityResult:

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
        r"""PersonalityResult

        The model defined in huaweicloud sdk

        :param path: 注入文件路径信息。
        :type path: str
        :param content: 注入文件内容，base64格式编码。
        :type content: str
        """
        
        

        self._path = None
        self._content = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if content is not None:
            self.content = content

    @property
    def path(self):
        r"""Gets the path of this PersonalityResult.

        注入文件路径信息。

        :return: The path of this PersonalityResult.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PersonalityResult.

        注入文件路径信息。

        :param path: The path of this PersonalityResult.
        :type path: str
        """
        self._path = path

    @property
    def content(self):
        r"""Gets the content of this PersonalityResult.

        注入文件内容，base64格式编码。

        :return: The content of this PersonalityResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this PersonalityResult.

        注入文件内容，base64格式编码。

        :param content: The content of this PersonalityResult.
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
        if not isinstance(other, PersonalityResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
