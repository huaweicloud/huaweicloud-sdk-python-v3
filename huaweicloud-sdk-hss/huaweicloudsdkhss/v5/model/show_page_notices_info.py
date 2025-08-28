# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPageNoticesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_location': 'str',
        'type': 'str',
        'content': 'str',
        'title': 'str',
        'url': 'str',
        'level': 'str'
    }

    attribute_map = {
        'page_location': 'page_location',
        'type': 'type',
        'content': 'content',
        'title': 'title',
        'url': 'url',
        'level': 'level'
    }

    def __init__(self, page_location=None, type=None, content=None, title=None, url=None, level=None):
        r"""ShowPageNoticesInfo

        The model defined in huaweicloud sdk

        :param page_location: 页面位置
        :type page_location: str
        :param type: 通知类型，包含如下两种。 - links：超链接 - text：文本
        :type type: str
        :param content: 通知内容
        :type content: str
        :param title: 通知标题
        :type title: str
        :param url: 超链接
        :type url: str
        :param level: **参数解释** 通知等级 **取值范围** - error：紧急 - warn：重要 - prompt：提示
        :type level: str
        """
        
        

        self._page_location = None
        self._type = None
        self._content = None
        self._title = None
        self._url = None
        self._level = None
        self.discriminator = None

        if page_location is not None:
            self.page_location = page_location
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if level is not None:
            self.level = level

    @property
    def page_location(self):
        r"""Gets the page_location of this ShowPageNoticesInfo.

        页面位置

        :return: The page_location of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._page_location

    @page_location.setter
    def page_location(self, page_location):
        r"""Sets the page_location of this ShowPageNoticesInfo.

        页面位置

        :param page_location: The page_location of this ShowPageNoticesInfo.
        :type page_location: str
        """
        self._page_location = page_location

    @property
    def type(self):
        r"""Gets the type of this ShowPageNoticesInfo.

        通知类型，包含如下两种。 - links：超链接 - text：文本

        :return: The type of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowPageNoticesInfo.

        通知类型，包含如下两种。 - links：超链接 - text：文本

        :param type: The type of this ShowPageNoticesInfo.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this ShowPageNoticesInfo.

        通知内容

        :return: The content of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowPageNoticesInfo.

        通知内容

        :param content: The content of this ShowPageNoticesInfo.
        :type content: str
        """
        self._content = content

    @property
    def title(self):
        r"""Gets the title of this ShowPageNoticesInfo.

        通知标题

        :return: The title of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowPageNoticesInfo.

        通知标题

        :param title: The title of this ShowPageNoticesInfo.
        :type title: str
        """
        self._title = title

    @property
    def url(self):
        r"""Gets the url of this ShowPageNoticesInfo.

        超链接

        :return: The url of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowPageNoticesInfo.

        超链接

        :param url: The url of this ShowPageNoticesInfo.
        :type url: str
        """
        self._url = url

    @property
    def level(self):
        r"""Gets the level of this ShowPageNoticesInfo.

        **参数解释** 通知等级 **取值范围** - error：紧急 - warn：重要 - prompt：提示

        :return: The level of this ShowPageNoticesInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowPageNoticesInfo.

        **参数解释** 通知等级 **取值范围** - error：紧急 - warn：重要 - prompt：提示

        :param level: The level of this ShowPageNoticesInfo.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, ShowPageNoticesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
