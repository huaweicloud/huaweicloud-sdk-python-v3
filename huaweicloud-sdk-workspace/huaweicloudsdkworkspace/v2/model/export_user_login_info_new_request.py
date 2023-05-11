# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUserLoginInfoNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'user_name': 'str',
        'computer_name': 'str',
        'terminal_type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'user_name': 'user_name',
        'computer_name': 'computer_name',
        'terminal_type': 'terminal_type',
        'language': 'language'
    }

    def __init__(self, start_time=None, end_time=None, user_name=None, computer_name=None, terminal_type=None, language=None):
        """ExportUserLoginInfoNewRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。
        :type start_time: str
        :param end_time: 查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。
        :type end_time: str
        :param user_name: 登录桌面的用户名。
        :type user_name: str
        :param computer_name: 计算机名（操作系统信息中可见）。
        :type computer_name: str
        :param terminal_type: 登录桌面的终端系统类型。
        :type terminal_type: str
        :param language: 导出语言，默认英文。 - zh_CN：中文 - en_US：英文
        :type language: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._user_name = None
        self._computer_name = None
        self._terminal_type = None
        self._language = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if user_name is not None:
            self.user_name = user_name
        if computer_name is not None:
            self.computer_name = computer_name
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if language is not None:
            self.language = language

    @property
    def start_time(self):
        """Gets the start_time of this ExportUserLoginInfoNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。

        :return: The start_time of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ExportUserLoginInfoNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。

        :param start_time: The start_time of this ExportUserLoginInfoNewRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ExportUserLoginInfoNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。

        :return: The end_time of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ExportUserLoginInfoNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。

        :param end_time: The end_time of this ExportUserLoginInfoNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def user_name(self):
        """Gets the user_name of this ExportUserLoginInfoNewRequest.

        登录桌面的用户名。

        :return: The user_name of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ExportUserLoginInfoNewRequest.

        登录桌面的用户名。

        :param user_name: The user_name of this ExportUserLoginInfoNewRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def computer_name(self):
        """Gets the computer_name of this ExportUserLoginInfoNewRequest.

        计算机名（操作系统信息中可见）。

        :return: The computer_name of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ExportUserLoginInfoNewRequest.

        计算机名（操作系统信息中可见）。

        :param computer_name: The computer_name of this ExportUserLoginInfoNewRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def terminal_type(self):
        """Gets the terminal_type of this ExportUserLoginInfoNewRequest.

        登录桌面的终端系统类型。

        :return: The terminal_type of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        """Sets the terminal_type of this ExportUserLoginInfoNewRequest.

        登录桌面的终端系统类型。

        :param terminal_type: The terminal_type of this ExportUserLoginInfoNewRequest.
        :type terminal_type: str
        """
        self._terminal_type = terminal_type

    @property
    def language(self):
        """Gets the language of this ExportUserLoginInfoNewRequest.

        导出语言，默认英文。 - zh_CN：中文 - en_US：英文

        :return: The language of this ExportUserLoginInfoNewRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ExportUserLoginInfoNewRequest.

        导出语言，默认英文。 - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportUserLoginInfoNewRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportUserLoginInfoNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
