# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorLogDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'node_id': 'str',
        'raw_message': 'str',
        'severity': 'str',
        'log_time': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'node_id': 'node_id',
        'raw_message': 'raw_message',
        'severity': 'severity',
        'log_time': 'log_time',
        'line_num': 'line_num'
    }

    def __init__(self, node_name=None, node_id=None, raw_message=None, severity=None, log_time=None, line_num=None):
        r"""ErrorLogDetail

        The model defined in huaweicloud sdk

        :param node_name: 节点名称。
        :type node_name: str
        :param node_id: 节点ID。
        :type node_id: str
        :param raw_message: 描述信息。
        :type raw_message: str
        :param severity: 日志级别。
        :type severity: str
        :param log_time: 日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type log_time: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        """
        
        

        self._node_name = None
        self._node_id = None
        self._raw_message = None
        self._severity = None
        self._log_time = None
        self._line_num = None
        self.discriminator = None

        self.node_name = node_name
        self.node_id = node_id
        self.raw_message = raw_message
        self.severity = severity
        self.log_time = log_time
        self.line_num = line_num

    @property
    def node_name(self):
        r"""Gets the node_name of this ErrorLogDetail.

        节点名称。

        :return: The node_name of this ErrorLogDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ErrorLogDetail.

        节点名称。

        :param node_name: The node_name of this ErrorLogDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_id(self):
        r"""Gets the node_id of this ErrorLogDetail.

        节点ID。

        :return: The node_id of this ErrorLogDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ErrorLogDetail.

        节点ID。

        :param node_id: The node_id of this ErrorLogDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def raw_message(self):
        r"""Gets the raw_message of this ErrorLogDetail.

        描述信息。

        :return: The raw_message of this ErrorLogDetail.
        :rtype: str
        """
        return self._raw_message

    @raw_message.setter
    def raw_message(self, raw_message):
        r"""Sets the raw_message of this ErrorLogDetail.

        描述信息。

        :param raw_message: The raw_message of this ErrorLogDetail.
        :type raw_message: str
        """
        self._raw_message = raw_message

    @property
    def severity(self):
        r"""Gets the severity of this ErrorLogDetail.

        日志级别。

        :return: The severity of this ErrorLogDetail.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ErrorLogDetail.

        日志级别。

        :param severity: The severity of this ErrorLogDetail.
        :type severity: str
        """
        self._severity = severity

    @property
    def log_time(self):
        r"""Gets the log_time of this ErrorLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The log_time of this ErrorLogDetail.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        r"""Sets the log_time of this ErrorLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param log_time: The log_time of this ErrorLogDetail.
        :type log_time: str
        """
        self._log_time = log_time

    @property
    def line_num(self):
        r"""Gets the line_num of this ErrorLogDetail.

        日志单行序列号。

        :return: The line_num of this ErrorLogDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ErrorLogDetail.

        日志单行序列号。

        :param line_num: The line_num of this ErrorLogDetail.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, ErrorLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
