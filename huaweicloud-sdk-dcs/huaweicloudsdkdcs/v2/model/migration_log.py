# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'log_level': 'str',
        'message': 'str',
        'log_code': 'str',
        'keyword': 'list[str]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'log_level': 'log_level',
        'message': 'message',
        'log_code': 'log_code',
        'keyword': 'keyword'
    }

    def __init__(self, created_at=None, log_level=None, message=None, log_code=None, keyword=None):
        r"""MigrationLog

        The model defined in huaweicloud sdk

        :param created_at: 迁移日志生成时间，形如：2023-05-15T09:11:25.449Z
        :type created_at: str
        :param log_level: 日志级别
        :type log_level: str
        :param message: 日志信息
        :type message: str
        :param log_code: 日志的编码
        :type log_code: str
        :param keyword: 日志中的关键字
        :type keyword: list[str]
        """
        
        

        self._created_at = None
        self._log_level = None
        self._message = None
        self._log_code = None
        self._keyword = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if log_level is not None:
            self.log_level = log_level
        if message is not None:
            self.message = message
        if log_code is not None:
            self.log_code = log_code
        if keyword is not None:
            self.keyword = keyword

    @property
    def created_at(self):
        r"""Gets the created_at of this MigrationLog.

        迁移日志生成时间，形如：2023-05-15T09:11:25.449Z

        :return: The created_at of this MigrationLog.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MigrationLog.

        迁移日志生成时间，形如：2023-05-15T09:11:25.449Z

        :param created_at: The created_at of this MigrationLog.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def log_level(self):
        r"""Gets the log_level of this MigrationLog.

        日志级别

        :return: The log_level of this MigrationLog.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        r"""Sets the log_level of this MigrationLog.

        日志级别

        :param log_level: The log_level of this MigrationLog.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def message(self):
        r"""Gets the message of this MigrationLog.

        日志信息

        :return: The message of this MigrationLog.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this MigrationLog.

        日志信息

        :param message: The message of this MigrationLog.
        :type message: str
        """
        self._message = message

    @property
    def log_code(self):
        r"""Gets the log_code of this MigrationLog.

        日志的编码

        :return: The log_code of this MigrationLog.
        :rtype: str
        """
        return self._log_code

    @log_code.setter
    def log_code(self, log_code):
        r"""Sets the log_code of this MigrationLog.

        日志的编码

        :param log_code: The log_code of this MigrationLog.
        :type log_code: str
        """
        self._log_code = log_code

    @property
    def keyword(self):
        r"""Gets the keyword of this MigrationLog.

        日志中的关键字

        :return: The keyword of this MigrationLog.
        :rtype: list[str]
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this MigrationLog.

        日志中的关键字

        :param keyword: The keyword of this MigrationLog.
        :type keyword: list[str]
        """
        self._keyword = keyword

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
        if not isinstance(other, MigrationLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
