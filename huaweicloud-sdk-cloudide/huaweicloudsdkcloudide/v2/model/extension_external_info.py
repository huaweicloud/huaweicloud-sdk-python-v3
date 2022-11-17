# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionExternalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_id': 'str',
        'repo_url': 'str',
        'help_page': 'str',
        'website': 'str',
        'issue_link': 'str',
        'show_previews': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'repo_url': 'repo_url',
        'help_page': 'help_page',
        'website': 'website',
        'issue_link': 'issue_link',
        'show_previews': 'show_previews',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, extension_id=None, repo_url=None, help_page=None, website=None, issue_link=None, show_previews=None, created_at=None, updated_at=None):
        """ExtensionExternalInfo

        The model defined in huaweicloud sdk

        :param extension_id: 插件id
        :type extension_id: str
        :param repo_url: 源码仓地址
        :type repo_url: str
        :param help_page: 帮助页面
        :type help_page: str
        :param website: 产品首页
        :type website: str
        :param issue_link: 问题链接
        :type issue_link: str
        :param show_previews: 是否支持预览
        :type show_previews: bool
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._extension_id = None
        self._repo_url = None
        self._help_page = None
        self._website = None
        self._issue_link = None
        self._show_previews = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if extension_id is not None:
            self.extension_id = extension_id
        if repo_url is not None:
            self.repo_url = repo_url
        if help_page is not None:
            self.help_page = help_page
        if website is not None:
            self.website = website
        if issue_link is not None:
            self.issue_link = issue_link
        if show_previews is not None:
            self.show_previews = show_previews
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def extension_id(self):
        """Gets the extension_id of this ExtensionExternalInfo.

        插件id

        :return: The extension_id of this ExtensionExternalInfo.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this ExtensionExternalInfo.

        插件id

        :param extension_id: The extension_id of this ExtensionExternalInfo.
        :type extension_id: str
        """
        self._extension_id = extension_id

    @property
    def repo_url(self):
        """Gets the repo_url of this ExtensionExternalInfo.

        源码仓地址

        :return: The repo_url of this ExtensionExternalInfo.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this ExtensionExternalInfo.

        源码仓地址

        :param repo_url: The repo_url of this ExtensionExternalInfo.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def help_page(self):
        """Gets the help_page of this ExtensionExternalInfo.

        帮助页面

        :return: The help_page of this ExtensionExternalInfo.
        :rtype: str
        """
        return self._help_page

    @help_page.setter
    def help_page(self, help_page):
        """Sets the help_page of this ExtensionExternalInfo.

        帮助页面

        :param help_page: The help_page of this ExtensionExternalInfo.
        :type help_page: str
        """
        self._help_page = help_page

    @property
    def website(self):
        """Gets the website of this ExtensionExternalInfo.

        产品首页

        :return: The website of this ExtensionExternalInfo.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ExtensionExternalInfo.

        产品首页

        :param website: The website of this ExtensionExternalInfo.
        :type website: str
        """
        self._website = website

    @property
    def issue_link(self):
        """Gets the issue_link of this ExtensionExternalInfo.

        问题链接

        :return: The issue_link of this ExtensionExternalInfo.
        :rtype: str
        """
        return self._issue_link

    @issue_link.setter
    def issue_link(self, issue_link):
        """Sets the issue_link of this ExtensionExternalInfo.

        问题链接

        :param issue_link: The issue_link of this ExtensionExternalInfo.
        :type issue_link: str
        """
        self._issue_link = issue_link

    @property
    def show_previews(self):
        """Gets the show_previews of this ExtensionExternalInfo.

        是否支持预览

        :return: The show_previews of this ExtensionExternalInfo.
        :rtype: bool
        """
        return self._show_previews

    @show_previews.setter
    def show_previews(self, show_previews):
        """Sets the show_previews of this ExtensionExternalInfo.

        是否支持预览

        :param show_previews: The show_previews of this ExtensionExternalInfo.
        :type show_previews: bool
        """
        self._show_previews = show_previews

    @property
    def created_at(self):
        """Gets the created_at of this ExtensionExternalInfo.

        创建时间

        :return: The created_at of this ExtensionExternalInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ExtensionExternalInfo.

        创建时间

        :param created_at: The created_at of this ExtensionExternalInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ExtensionExternalInfo.

        更新时间

        :return: The updated_at of this ExtensionExternalInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ExtensionExternalInfo.

        更新时间

        :param updated_at: The updated_at of this ExtensionExternalInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ExtensionExternalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
