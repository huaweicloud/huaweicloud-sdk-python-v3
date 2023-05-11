# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFixtedResponseConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_code': 'str',
        'content_type': 'str',
        'message_body': 'str'
    }

    attribute_map = {
        'status_code': 'status_code',
        'content_type': 'content_type',
        'message_body': 'message_body'
    }

    def __init__(self, status_code=None, content_type=None, message_body=None):
        """UpdateFixtedResponseConfig

        The model defined in huaweicloud sdk

        :param status_code: 返回码。支持200~299,400~499,500~599。
        :type status_code: str
        :param content_type: 返回body的格式。  取值范围： - text/plain - text/css - text/html - application/javascript - application/json application/json
        :type content_type: str
        :param message_body: 返回消息内容。
        :type message_body: str
        """
        
        

        self._status_code = None
        self._content_type = None
        self._message_body = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if content_type is not None:
            self.content_type = content_type
        if message_body is not None:
            self.message_body = message_body

    @property
    def status_code(self):
        """Gets the status_code of this UpdateFixtedResponseConfig.

        返回码。支持200~299,400~499,500~599。

        :return: The status_code of this UpdateFixtedResponseConfig.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this UpdateFixtedResponseConfig.

        返回码。支持200~299,400~499,500~599。

        :param status_code: The status_code of this UpdateFixtedResponseConfig.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def content_type(self):
        """Gets the content_type of this UpdateFixtedResponseConfig.

        返回body的格式。  取值范围： - text/plain - text/css - text/html - application/javascript - application/json application/json

        :return: The content_type of this UpdateFixtedResponseConfig.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateFixtedResponseConfig.

        返回body的格式。  取值范围： - text/plain - text/css - text/html - application/javascript - application/json application/json

        :param content_type: The content_type of this UpdateFixtedResponseConfig.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def message_body(self):
        """Gets the message_body of this UpdateFixtedResponseConfig.

        返回消息内容。

        :return: The message_body of this UpdateFixtedResponseConfig.
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this UpdateFixtedResponseConfig.

        返回消息内容。

        :param message_body: The message_body of this UpdateFixtedResponseConfig.
        :type message_body: str
        """
        self._message_body = message_body

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
        if not isinstance(other, UpdateFixtedResponseConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
