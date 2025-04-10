# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublisherSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publisher_id': 'str',
        'publisher_name': 'str',
        'display_name': 'str',
        'publisher_status': 'str',
        'email': 'str',
        'web_url': 'str',
        'open': 'bool'
    }

    attribute_map = {
        'publisher_id': 'publisher_id',
        'publisher_name': 'publisher_name',
        'display_name': 'display_name',
        'publisher_status': 'publisher_status',
        'email': 'email',
        'web_url': 'web_url',
        'open': 'open'
    }

    def __init__(self, publisher_id=None, publisher_name=None, display_name=None, publisher_status=None, email=None, web_url=None, open=None):
        r"""PublisherSnake

        The model defined in huaweicloud sdk

        :param publisher_id: 发布者id
        :type publisher_id: str
        :param publisher_name: 发布者名称
        :type publisher_name: str
        :param display_name: 发布者展示名
        :type display_name: str
        :param publisher_status: 插件作者状态 - DISABLED 验证不通过 - VERIFIED 验证通过
        :type publisher_status: str
        :param email: 发布者邮箱
        :type email: str
        :param web_url: 网页url
        :type web_url: str
        :param open: 是否开源
        :type open: bool
        """
        
        

        self._publisher_id = None
        self._publisher_name = None
        self._display_name = None
        self._publisher_status = None
        self._email = None
        self._web_url = None
        self._open = None
        self.discriminator = None

        if publisher_id is not None:
            self.publisher_id = publisher_id
        if publisher_name is not None:
            self.publisher_name = publisher_name
        if display_name is not None:
            self.display_name = display_name
        if publisher_status is not None:
            self.publisher_status = publisher_status
        if email is not None:
            self.email = email
        if web_url is not None:
            self.web_url = web_url
        if open is not None:
            self.open = open

    @property
    def publisher_id(self):
        r"""Gets the publisher_id of this PublisherSnake.

        发布者id

        :return: The publisher_id of this PublisherSnake.
        :rtype: str
        """
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        r"""Sets the publisher_id of this PublisherSnake.

        发布者id

        :param publisher_id: The publisher_id of this PublisherSnake.
        :type publisher_id: str
        """
        self._publisher_id = publisher_id

    @property
    def publisher_name(self):
        r"""Gets the publisher_name of this PublisherSnake.

        发布者名称

        :return: The publisher_name of this PublisherSnake.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        r"""Sets the publisher_name of this PublisherSnake.

        发布者名称

        :param publisher_name: The publisher_name of this PublisherSnake.
        :type publisher_name: str
        """
        self._publisher_name = publisher_name

    @property
    def display_name(self):
        r"""Gets the display_name of this PublisherSnake.

        发布者展示名

        :return: The display_name of this PublisherSnake.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PublisherSnake.

        发布者展示名

        :param display_name: The display_name of this PublisherSnake.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def publisher_status(self):
        r"""Gets the publisher_status of this PublisherSnake.

        插件作者状态 - DISABLED 验证不通过 - VERIFIED 验证通过

        :return: The publisher_status of this PublisherSnake.
        :rtype: str
        """
        return self._publisher_status

    @publisher_status.setter
    def publisher_status(self, publisher_status):
        r"""Sets the publisher_status of this PublisherSnake.

        插件作者状态 - DISABLED 验证不通过 - VERIFIED 验证通过

        :param publisher_status: The publisher_status of this PublisherSnake.
        :type publisher_status: str
        """
        self._publisher_status = publisher_status

    @property
    def email(self):
        r"""Gets the email of this PublisherSnake.

        发布者邮箱

        :return: The email of this PublisherSnake.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this PublisherSnake.

        发布者邮箱

        :param email: The email of this PublisherSnake.
        :type email: str
        """
        self._email = email

    @property
    def web_url(self):
        r"""Gets the web_url of this PublisherSnake.

        网页url

        :return: The web_url of this PublisherSnake.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this PublisherSnake.

        网页url

        :param web_url: The web_url of this PublisherSnake.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def open(self):
        r"""Gets the open of this PublisherSnake.

        是否开源

        :return: The open of this PublisherSnake.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        r"""Sets the open of this PublisherSnake.

        是否开源

        :param open: The open of this PublisherSnake.
        :type open: bool
        """
        self._open = open

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
        if not isinstance(other, PublisherSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
