# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'log': 'str',
        'level': 'str',
        'analysis': 'str',
        'faq': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'log': 'log',
        'level': 'level',
        'analysis': 'analysis',
        'faq': 'faq'
    }

    def __init__(self, display_name=None, log=None, level=None, analysis=None, faq=None):
        r"""LogInfo

        The model defined in huaweicloud sdk

        :param display_name: 日志标题
        :type display_name: str
        :param log: 日志内容
        :type log: str
        :param level: 日志级别
        :type level: str
        :param analysis: 日志分析
        :type analysis: str
        :param faq: 常见问题解答
        :type faq: str
        """
        
        

        self._display_name = None
        self._log = None
        self._level = None
        self._analysis = None
        self._faq = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if log is not None:
            self.log = log
        if level is not None:
            self.level = level
        if analysis is not None:
            self.analysis = analysis
        if faq is not None:
            self.faq = faq

    @property
    def display_name(self):
        r"""Gets the display_name of this LogInfo.

        日志标题

        :return: The display_name of this LogInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this LogInfo.

        日志标题

        :param display_name: The display_name of this LogInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def log(self):
        r"""Gets the log of this LogInfo.

        日志内容

        :return: The log of this LogInfo.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this LogInfo.

        日志内容

        :param log: The log of this LogInfo.
        :type log: str
        """
        self._log = log

    @property
    def level(self):
        r"""Gets the level of this LogInfo.

        日志级别

        :return: The level of this LogInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this LogInfo.

        日志级别

        :param level: The level of this LogInfo.
        :type level: str
        """
        self._level = level

    @property
    def analysis(self):
        r"""Gets the analysis of this LogInfo.

        日志分析

        :return: The analysis of this LogInfo.
        :rtype: str
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        r"""Sets the analysis of this LogInfo.

        日志分析

        :param analysis: The analysis of this LogInfo.
        :type analysis: str
        """
        self._analysis = analysis

    @property
    def faq(self):
        r"""Gets the faq of this LogInfo.

        常见问题解答

        :return: The faq of this LogInfo.
        :rtype: str
        """
        return self._faq

    @faq.setter
    def faq(self, faq):
        r"""Sets the faq of this LogInfo.

        常见问题解答

        :param faq: The faq of this LogInfo.
        :type faq: str
        """
        self._faq = faq

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
        if not isinstance(other, LogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
