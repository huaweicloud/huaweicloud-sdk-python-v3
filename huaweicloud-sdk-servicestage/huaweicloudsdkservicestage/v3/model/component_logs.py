# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentLogs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_path': 'str',
        'rotate': 'str',
        'host_path': 'str',
        'host_extend_path': 'str'
    }

    attribute_map = {
        'log_path': 'log_path',
        'rotate': 'rotate',
        'host_path': 'host_path',
        'host_extend_path': 'host_extend_path'
    }

    def __init__(self, log_path=None, rotate=None, host_path=None, host_extend_path=None):
        r"""ComponentLogs

        The model defined in huaweicloud sdk

        :param log_path: 容器中日志路径
        :type log_path: str
        :param rotate: 日志转储周期
        :type rotate: str
        :param host_path: 挂载的主机路径
        :type host_path: str
        :param host_extend_path: 主机扩展路径
        :type host_extend_path: str
        """
        
        

        self._log_path = None
        self._rotate = None
        self._host_path = None
        self._host_extend_path = None
        self.discriminator = None

        self.log_path = log_path
        self.rotate = rotate
        self.host_path = host_path
        self.host_extend_path = host_extend_path

    @property
    def log_path(self):
        r"""Gets the log_path of this ComponentLogs.

        容器中日志路径

        :return: The log_path of this ComponentLogs.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this ComponentLogs.

        容器中日志路径

        :param log_path: The log_path of this ComponentLogs.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def rotate(self):
        r"""Gets the rotate of this ComponentLogs.

        日志转储周期

        :return: The rotate of this ComponentLogs.
        :rtype: str
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        r"""Sets the rotate of this ComponentLogs.

        日志转储周期

        :param rotate: The rotate of this ComponentLogs.
        :type rotate: str
        """
        self._rotate = rotate

    @property
    def host_path(self):
        r"""Gets the host_path of this ComponentLogs.

        挂载的主机路径

        :return: The host_path of this ComponentLogs.
        :rtype: str
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        r"""Sets the host_path of this ComponentLogs.

        挂载的主机路径

        :param host_path: The host_path of this ComponentLogs.
        :type host_path: str
        """
        self._host_path = host_path

    @property
    def host_extend_path(self):
        r"""Gets the host_extend_path of this ComponentLogs.

        主机扩展路径

        :return: The host_extend_path of this ComponentLogs.
        :rtype: str
        """
        return self._host_extend_path

    @host_extend_path.setter
    def host_extend_path(self, host_extend_path):
        r"""Sets the host_extend_path of this ComponentLogs.

        主机扩展路径

        :param host_extend_path: The host_extend_path of this ComponentLogs.
        :type host_extend_path: str
        """
        self._host_extend_path = host_extend_path

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
        if not isinstance(other, ComponentLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
