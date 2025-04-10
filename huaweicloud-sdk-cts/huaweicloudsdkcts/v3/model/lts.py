# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Lts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_lts_enabled': 'bool',
        'log_group_name': 'str',
        'log_topic_name': 'str'
    }

    attribute_map = {
        'is_lts_enabled': 'is_lts_enabled',
        'log_group_name': 'log_group_name',
        'log_topic_name': 'log_topic_name'
    }

    def __init__(self, is_lts_enabled=None, log_group_name=None, log_topic_name=None):
        r"""Lts

        The model defined in huaweicloud sdk

        :param is_lts_enabled: 是否启用日志服务检索功能。
        :type is_lts_enabled: bool
        :param log_group_name: 云审计服务在日志服务中创建的日志组名称。
        :type log_group_name: str
        :param log_topic_name: 云审计服务在日志服务中创建的日志主题名称。
        :type log_topic_name: str
        """
        
        

        self._is_lts_enabled = None
        self._log_group_name = None
        self._log_topic_name = None
        self.discriminator = None

        if is_lts_enabled is not None:
            self.is_lts_enabled = is_lts_enabled
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_topic_name is not None:
            self.log_topic_name = log_topic_name

    @property
    def is_lts_enabled(self):
        r"""Gets the is_lts_enabled of this Lts.

        是否启用日志服务检索功能。

        :return: The is_lts_enabled of this Lts.
        :rtype: bool
        """
        return self._is_lts_enabled

    @is_lts_enabled.setter
    def is_lts_enabled(self, is_lts_enabled):
        r"""Sets the is_lts_enabled of this Lts.

        是否启用日志服务检索功能。

        :param is_lts_enabled: The is_lts_enabled of this Lts.
        :type is_lts_enabled: bool
        """
        self._is_lts_enabled = is_lts_enabled

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this Lts.

        云审计服务在日志服务中创建的日志组名称。

        :return: The log_group_name of this Lts.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this Lts.

        云审计服务在日志服务中创建的日志组名称。

        :param log_group_name: The log_group_name of this Lts.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_topic_name(self):
        r"""Gets the log_topic_name of this Lts.

        云审计服务在日志服务中创建的日志主题名称。

        :return: The log_topic_name of this Lts.
        :rtype: str
        """
        return self._log_topic_name

    @log_topic_name.setter
    def log_topic_name(self, log_topic_name):
        r"""Sets the log_topic_name of this Lts.

        云审计服务在日志服务中创建的日志主题名称。

        :param log_topic_name: The log_topic_name of this Lts.
        :type log_topic_name: str
        """
        self._log_topic_name = log_topic_name

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
        if not isinstance(other, Lts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
