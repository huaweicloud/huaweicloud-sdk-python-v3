# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpressConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_level': 'str',
        'support_anonymous': 'bool'
    }

    attribute_map = {
        'log_level': 'log_level',
        'support_anonymous': 'support_anonymous'
    }

    def __init__(self, log_level=None, support_anonymous=None):
        r"""ExpressConfig

        The model defined in huaweicloud sdk

        :param log_level: 同步工作流执行时记录LTS的日志级别，NONE、ERROR\\ALL，默认NONE
        :type log_level: str
        :param support_anonymous: 同步工作流是否支持匿名访问
        :type support_anonymous: bool
        """
        
        

        self._log_level = None
        self._support_anonymous = None
        self.discriminator = None

        if log_level is not None:
            self.log_level = log_level
        if support_anonymous is not None:
            self.support_anonymous = support_anonymous

    @property
    def log_level(self):
        r"""Gets the log_level of this ExpressConfig.

        同步工作流执行时记录LTS的日志级别，NONE、ERROR\\ALL，默认NONE

        :return: The log_level of this ExpressConfig.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        r"""Sets the log_level of this ExpressConfig.

        同步工作流执行时记录LTS的日志级别，NONE、ERROR\\ALL，默认NONE

        :param log_level: The log_level of this ExpressConfig.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def support_anonymous(self):
        r"""Gets the support_anonymous of this ExpressConfig.

        同步工作流是否支持匿名访问

        :return: The support_anonymous of this ExpressConfig.
        :rtype: bool
        """
        return self._support_anonymous

    @support_anonymous.setter
    def support_anonymous(self, support_anonymous):
        r"""Sets the support_anonymous of this ExpressConfig.

        同步工作流是否支持匿名访问

        :param support_anonymous: The support_anonymous of this ExpressConfig.
        :type support_anonymous: bool
        """
        self._support_anonymous = support_anonymous

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
        if not isinstance(other, ExpressConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
