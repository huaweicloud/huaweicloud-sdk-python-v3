# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogtankOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_topic_id': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id'
    }

    def __init__(self, log_group_id=None, log_topic_id=None):
        """UpdateLogtankOption

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组别id，其他（非ELB）服务提供
        :type log_group_id: str
        :param log_topic_id: 日志订阅主题id，其他（非ELB）服务提供
        :type log_topic_id: str
        """
        
        

        self._log_group_id = None
        self._log_topic_id = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this UpdateLogtankOption.

        日志组别id，其他（非ELB）服务提供

        :return: The log_group_id of this UpdateLogtankOption.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this UpdateLogtankOption.

        日志组别id，其他（非ELB）服务提供

        :param log_group_id: The log_group_id of this UpdateLogtankOption.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this UpdateLogtankOption.

        日志订阅主题id，其他（非ELB）服务提供

        :return: The log_topic_id of this UpdateLogtankOption.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this UpdateLogtankOption.

        日志订阅主题id，其他（非ELB）服务提供

        :param log_topic_id: The log_topic_id of this UpdateLogtankOption.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

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
        if not isinstance(other, UpdateLogtankOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
