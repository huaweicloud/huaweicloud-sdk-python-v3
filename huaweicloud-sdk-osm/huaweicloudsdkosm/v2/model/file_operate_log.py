# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileOperateLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'duration': 'str',
        'operate_time': 'str',
        'operate_type': 'str',
        'file_name': 'str',
        'from_path': 'str',
        'to_path': 'str',
        'file_size': 'str',
        'oper_result': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'operate_time': 'operate_time',
        'operate_type': 'operate_type',
        'file_name': 'file_name',
        'from_path': 'from_path',
        'to_path': 'to_path',
        'file_size': 'file_size',
        'oper_result': 'oper_result'
    }

    def __init__(self, duration=None, operate_time=None, operate_type=None, file_name=None, from_path=None, to_path=None, file_size=None, oper_result=None):
        """FileOperateLog

        The model defined in huaweicloud sdk

        :param duration: 传输时间 格式：hh:ii:ss
        :type duration: str
        :param operate_time: 操作时间
        :type operate_time: str
        :param operate_type: 操作类型
        :type operate_type: str
        :param file_name: 文件名
        :type file_name: str
        :param from_path: 来源路径
        :type from_path: str
        :param to_path: 目标路径
        :type to_path: str
        :param file_size: 文件大小，多少k，多少M，多少G。
        :type file_size: str
        :param oper_result: 操作结果
        :type oper_result: str
        """
        
        

        self._duration = None
        self._operate_time = None
        self._operate_type = None
        self._file_name = None
        self._from_path = None
        self._to_path = None
        self._file_size = None
        self._oper_result = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if operate_time is not None:
            self.operate_time = operate_time
        if operate_type is not None:
            self.operate_type = operate_type
        if file_name is not None:
            self.file_name = file_name
        if from_path is not None:
            self.from_path = from_path
        if to_path is not None:
            self.to_path = to_path
        if file_size is not None:
            self.file_size = file_size
        if oper_result is not None:
            self.oper_result = oper_result

    @property
    def duration(self):
        """Gets the duration of this FileOperateLog.

        传输时间 格式：hh:ii:ss

        :return: The duration of this FileOperateLog.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FileOperateLog.

        传输时间 格式：hh:ii:ss

        :param duration: The duration of this FileOperateLog.
        :type duration: str
        """
        self._duration = duration

    @property
    def operate_time(self):
        """Gets the operate_time of this FileOperateLog.

        操作时间

        :return: The operate_time of this FileOperateLog.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this FileOperateLog.

        操作时间

        :param operate_time: The operate_time of this FileOperateLog.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def operate_type(self):
        """Gets the operate_type of this FileOperateLog.

        操作类型

        :return: The operate_type of this FileOperateLog.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this FileOperateLog.

        操作类型

        :param operate_type: The operate_type of this FileOperateLog.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def file_name(self):
        """Gets the file_name of this FileOperateLog.

        文件名

        :return: The file_name of this FileOperateLog.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileOperateLog.

        文件名

        :param file_name: The file_name of this FileOperateLog.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def from_path(self):
        """Gets the from_path of this FileOperateLog.

        来源路径

        :return: The from_path of this FileOperateLog.
        :rtype: str
        """
        return self._from_path

    @from_path.setter
    def from_path(self, from_path):
        """Sets the from_path of this FileOperateLog.

        来源路径

        :param from_path: The from_path of this FileOperateLog.
        :type from_path: str
        """
        self._from_path = from_path

    @property
    def to_path(self):
        """Gets the to_path of this FileOperateLog.

        目标路径

        :return: The to_path of this FileOperateLog.
        :rtype: str
        """
        return self._to_path

    @to_path.setter
    def to_path(self, to_path):
        """Sets the to_path of this FileOperateLog.

        目标路径

        :param to_path: The to_path of this FileOperateLog.
        :type to_path: str
        """
        self._to_path = to_path

    @property
    def file_size(self):
        """Gets the file_size of this FileOperateLog.

        文件大小，多少k，多少M，多少G。

        :return: The file_size of this FileOperateLog.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileOperateLog.

        文件大小，多少k，多少M，多少G。

        :param file_size: The file_size of this FileOperateLog.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def oper_result(self):
        """Gets the oper_result of this FileOperateLog.

        操作结果

        :return: The oper_result of this FileOperateLog.
        :rtype: str
        """
        return self._oper_result

    @oper_result.setter
    def oper_result(self, oper_result):
        """Sets the oper_result of this FileOperateLog.

        操作结果

        :param oper_result: The oper_result of this FileOperateLog.
        :type oper_result: str
        """
        self._oper_result = oper_result

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
        if not isinstance(other, FileOperateLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
