# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Annotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'log_info': 'str',
        'current_value': 'str',
        'old_annotations': 'str'
    }

    attribute_map = {
        'message': 'message',
        'log_info': 'log_info',
        'current_value': 'current_value',
        'old_annotations': 'old_annotations'
    }

    def __init__(self, message=None, log_info=None, current_value=None, old_annotations=None):
        """Annotations

        The model defined in huaweicloud sdk

        :param message: 告警列表详情
        :type message: str
        :param log_info: 日志组/流id,名称
        :type log_info: str
        :param current_value: 当前值
        :type current_value: str
        :param old_annotations: (sql/关键词)告警详情原始数据
        :type old_annotations: str
        """
        
        

        self._message = None
        self._log_info = None
        self._current_value = None
        self._old_annotations = None
        self.discriminator = None

        self.message = message
        self.log_info = log_info
        self.current_value = current_value
        self.old_annotations = old_annotations

    @property
    def message(self):
        """Gets the message of this Annotations.

        告警列表详情

        :return: The message of this Annotations.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Annotations.

        告警列表详情

        :param message: The message of this Annotations.
        :type message: str
        """
        self._message = message

    @property
    def log_info(self):
        """Gets the log_info of this Annotations.

        日志组/流id,名称

        :return: The log_info of this Annotations.
        :rtype: str
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        """Sets the log_info of this Annotations.

        日志组/流id,名称

        :param log_info: The log_info of this Annotations.
        :type log_info: str
        """
        self._log_info = log_info

    @property
    def current_value(self):
        """Gets the current_value of this Annotations.

        当前值

        :return: The current_value of this Annotations.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this Annotations.

        当前值

        :param current_value: The current_value of this Annotations.
        :type current_value: str
        """
        self._current_value = current_value

    @property
    def old_annotations(self):
        """Gets the old_annotations of this Annotations.

        (sql/关键词)告警详情原始数据

        :return: The old_annotations of this Annotations.
        :rtype: str
        """
        return self._old_annotations

    @old_annotations.setter
    def old_annotations(self, old_annotations):
        """Sets the old_annotations of this Annotations.

        (sql/关键词)告警详情原始数据

        :param old_annotations: The old_annotations of this Annotations.
        :type old_annotations: str
        """
        self._old_annotations = old_annotations

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
        if not isinstance(other, Annotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
