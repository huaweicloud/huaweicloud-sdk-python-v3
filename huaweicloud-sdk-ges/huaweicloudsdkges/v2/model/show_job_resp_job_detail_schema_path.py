# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobRespJobDetailSchemaPath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'log': 'str',
        'status': 'str',
        'cause': 'str',
        'total_lines': 'int',
        'failed_lines': 'int',
        'successful_lines': 'int'
    }

    attribute_map = {
        'path': 'path',
        'log': 'log',
        'status': 'status',
        'cause': 'cause',
        'total_lines': 'total_lines',
        'failed_lines': 'failed_lines',
        'successful_lines': 'successful_lines'
    }

    def __init__(self, path=None, log=None, status=None, cause=None, total_lines=None, failed_lines=None, successful_lines=None):
        """ShowJobRespJobDetailSchemaPath

        The model defined in huaweicloud sdk

        :param path: OBS文件路径。
        :type path: str
        :param log: OBS文件导入日志存储文件。
        :type log: str
        :param status: OBS文件导入状态。  - success：完全成功 - failed：完全失败 - partFailed：部分成功
        :type status: str
        :param cause: 导入失败原因。
        :type cause: str
        :param total_lines: 导入总行数。其值为-1时表示当前版本没有返回该字段。
        :type total_lines: int
        :param failed_lines: 导入失败行数。其值为-1时表示当前版本没有返回该字段。
        :type failed_lines: int
        :param successful_lines: 导入成功行数。其值为-1时表示当前版本没有返回该字段。
        :type successful_lines: int
        """
        
        

        self._path = None
        self._log = None
        self._status = None
        self._cause = None
        self._total_lines = None
        self._failed_lines = None
        self._successful_lines = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if log is not None:
            self.log = log
        if status is not None:
            self.status = status
        if cause is not None:
            self.cause = cause
        if total_lines is not None:
            self.total_lines = total_lines
        if failed_lines is not None:
            self.failed_lines = failed_lines
        if successful_lines is not None:
            self.successful_lines = successful_lines

    @property
    def path(self):
        """Gets the path of this ShowJobRespJobDetailSchemaPath.

        OBS文件路径。

        :return: The path of this ShowJobRespJobDetailSchemaPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowJobRespJobDetailSchemaPath.

        OBS文件路径。

        :param path: The path of this ShowJobRespJobDetailSchemaPath.
        :type path: str
        """
        self._path = path

    @property
    def log(self):
        """Gets the log of this ShowJobRespJobDetailSchemaPath.

        OBS文件导入日志存储文件。

        :return: The log of this ShowJobRespJobDetailSchemaPath.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this ShowJobRespJobDetailSchemaPath.

        OBS文件导入日志存储文件。

        :param log: The log of this ShowJobRespJobDetailSchemaPath.
        :type log: str
        """
        self._log = log

    @property
    def status(self):
        """Gets the status of this ShowJobRespJobDetailSchemaPath.

        OBS文件导入状态。  - success：完全成功 - failed：完全失败 - partFailed：部分成功

        :return: The status of this ShowJobRespJobDetailSchemaPath.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobRespJobDetailSchemaPath.

        OBS文件导入状态。  - success：完全成功 - failed：完全失败 - partFailed：部分成功

        :param status: The status of this ShowJobRespJobDetailSchemaPath.
        :type status: str
        """
        self._status = status

    @property
    def cause(self):
        """Gets the cause of this ShowJobRespJobDetailSchemaPath.

        导入失败原因。

        :return: The cause of this ShowJobRespJobDetailSchemaPath.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this ShowJobRespJobDetailSchemaPath.

        导入失败原因。

        :param cause: The cause of this ShowJobRespJobDetailSchemaPath.
        :type cause: str
        """
        self._cause = cause

    @property
    def total_lines(self):
        """Gets the total_lines of this ShowJobRespJobDetailSchemaPath.

        导入总行数。其值为-1时表示当前版本没有返回该字段。

        :return: The total_lines of this ShowJobRespJobDetailSchemaPath.
        :rtype: int
        """
        return self._total_lines

    @total_lines.setter
    def total_lines(self, total_lines):
        """Sets the total_lines of this ShowJobRespJobDetailSchemaPath.

        导入总行数。其值为-1时表示当前版本没有返回该字段。

        :param total_lines: The total_lines of this ShowJobRespJobDetailSchemaPath.
        :type total_lines: int
        """
        self._total_lines = total_lines

    @property
    def failed_lines(self):
        """Gets the failed_lines of this ShowJobRespJobDetailSchemaPath.

        导入失败行数。其值为-1时表示当前版本没有返回该字段。

        :return: The failed_lines of this ShowJobRespJobDetailSchemaPath.
        :rtype: int
        """
        return self._failed_lines

    @failed_lines.setter
    def failed_lines(self, failed_lines):
        """Sets the failed_lines of this ShowJobRespJobDetailSchemaPath.

        导入失败行数。其值为-1时表示当前版本没有返回该字段。

        :param failed_lines: The failed_lines of this ShowJobRespJobDetailSchemaPath.
        :type failed_lines: int
        """
        self._failed_lines = failed_lines

    @property
    def successful_lines(self):
        """Gets the successful_lines of this ShowJobRespJobDetailSchemaPath.

        导入成功行数。其值为-1时表示当前版本没有返回该字段。

        :return: The successful_lines of this ShowJobRespJobDetailSchemaPath.
        :rtype: int
        """
        return self._successful_lines

    @successful_lines.setter
    def successful_lines(self, successful_lines):
        """Sets the successful_lines of this ShowJobRespJobDetailSchemaPath.

        导入成功行数。其值为-1时表示当前版本没有返回该字段。

        :param successful_lines: The successful_lines of this ShowJobRespJobDetailSchemaPath.
        :type successful_lines: int
        """
        self._successful_lines = successful_lines

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
        if not isinstance(other, ShowJobRespJobDetailSchemaPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
