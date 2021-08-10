# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventResponseBodyHeaders:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_length': 'str',
        'host': 'str',
        'content_type': 'str',
        'user_agent': 'str',
        'accept': 'str'
    }

    attribute_map = {
        'content_length': 'content-length',
        'host': 'host',
        'content_type': 'content-type',
        'user_agent': 'user-agent',
        'accept': 'accept'
    }

    def __init__(self, content_length=None, host=None, content_type=None, user_agent=None, accept=None):
        """ListEventResponseBodyHeaders - a model defined in huaweicloud sdk"""
        
        

        self._content_length = None
        self._host = None
        self._content_type = None
        self._user_agent = None
        self._accept = None
        self.discriminator = None

        if content_length is not None:
            self.content_length = content_length
        if host is not None:
            self.host = host
        if content_type is not None:
            self.content_type = content_type
        if user_agent is not None:
            self.user_agent = user_agent
        if accept is not None:
            self.accept = accept

    @property
    def content_length(self):
        """Gets the content_length of this ListEventResponseBodyHeaders.

        请求长度

        :return: The content_length of this ListEventResponseBodyHeaders.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ListEventResponseBodyHeaders.

        请求长度

        :param content_length: The content_length of this ListEventResponseBodyHeaders.
        :type: str
        """
        self._content_length = content_length

    @property
    def host(self):
        """Gets the host of this ListEventResponseBodyHeaders.

        域名

        :return: The host of this ListEventResponseBodyHeaders.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListEventResponseBodyHeaders.

        域名

        :param host: The host of this ListEventResponseBodyHeaders.
        :type: str
        """
        self._host = host

    @property
    def content_type(self):
        """Gets the content_type of this ListEventResponseBodyHeaders.

        内容类型

        :return: The content_type of this ListEventResponseBodyHeaders.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListEventResponseBodyHeaders.

        内容类型

        :param content_type: The content_type of this ListEventResponseBodyHeaders.
        :type: str
        """
        self._content_type = content_type

    @property
    def user_agent(self):
        """Gets the user_agent of this ListEventResponseBodyHeaders.

        代理

        :return: The user_agent of this ListEventResponseBodyHeaders.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ListEventResponseBodyHeaders.

        代理

        :param user_agent: The user_agent of this ListEventResponseBodyHeaders.
        :type: str
        """
        self._user_agent = user_agent

    @property
    def accept(self):
        """Gets the accept of this ListEventResponseBodyHeaders.

        接收内容类型

        :return: The accept of this ListEventResponseBodyHeaders.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        """Sets the accept of this ListEventResponseBodyHeaders.

        接收内容类型

        :param accept: The accept of this ListEventResponseBodyHeaders.
        :type: str
        """
        self._accept = accept

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
        if not isinstance(other, ListEventResponseBodyHeaders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
