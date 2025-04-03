# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsLogDump:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_dump': 'bool'
    }

    attribute_map = {
        'log_dump': 'log_dump'
    }

    def __init__(self, log_dump=None):
        """ObsLogDump

        The model defined in huaweicloud sdk

        :param log_dump: 是否开启Obs日志转储功能，true表示开启，false表示关闭。
        :type log_dump: bool
        """
        
        

        self._log_dump = None
        self.discriminator = None

        if log_dump is not None:
            self.log_dump = log_dump

    @property
    def log_dump(self):
        """Gets the log_dump of this ObsLogDump.

        是否开启Obs日志转储功能，true表示开启，false表示关闭。

        :return: The log_dump of this ObsLogDump.
        :rtype: bool
        """
        return self._log_dump

    @log_dump.setter
    def log_dump(self, log_dump):
        """Sets the log_dump of this ObsLogDump.

        是否开启Obs日志转储功能，true表示开启，false表示关闭。

        :param log_dump: The log_dump of this ObsLogDump.
        :type log_dump: bool
        """
        self._log_dump = log_dump

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
        if not isinstance(other, ObsLogDump):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
