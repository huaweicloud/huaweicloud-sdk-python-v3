# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostProtectHistoryResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'occr_time': 'int',
        'file_path': 'str',
        'process_id': 'str',
        'process_name': 'str',
        'process_cmd': 'str'
    }

    attribute_map = {
        'occr_time': 'occr_time',
        'file_path': 'file_path',
        'process_id': 'process_id',
        'process_name': 'process_name',
        'process_cmd': 'process_cmd'
    }

    def __init__(self, occr_time=None, file_path=None, process_id=None, process_name=None, process_cmd=None):
        """HostProtectHistoryResponseInfo

        The model defined in huaweicloud sdk

        :param occr_time: 检测时间
        :type occr_time: int
        :param file_path: 被篡改文件路径
        :type file_path: str
        :param process_id: 进程ID，操作系统是Windows时返回
        :type process_id: str
        :param process_name: 进程名称，操作系统是Windows时返回
        :type process_name: str
        :param process_cmd: 进程命令行，操作系统是Windows时返回
        :type process_cmd: str
        """
        
        

        self._occr_time = None
        self._file_path = None
        self._process_id = None
        self._process_name = None
        self._process_cmd = None
        self.discriminator = None

        if occr_time is not None:
            self.occr_time = occr_time
        if file_path is not None:
            self.file_path = file_path
        if process_id is not None:
            self.process_id = process_id
        if process_name is not None:
            self.process_name = process_name
        if process_cmd is not None:
            self.process_cmd = process_cmd

    @property
    def occr_time(self):
        """Gets the occr_time of this HostProtectHistoryResponseInfo.

        检测时间

        :return: The occr_time of this HostProtectHistoryResponseInfo.
        :rtype: int
        """
        return self._occr_time

    @occr_time.setter
    def occr_time(self, occr_time):
        """Sets the occr_time of this HostProtectHistoryResponseInfo.

        检测时间

        :param occr_time: The occr_time of this HostProtectHistoryResponseInfo.
        :type occr_time: int
        """
        self._occr_time = occr_time

    @property
    def file_path(self):
        """Gets the file_path of this HostProtectHistoryResponseInfo.

        被篡改文件路径

        :return: The file_path of this HostProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this HostProtectHistoryResponseInfo.

        被篡改文件路径

        :param file_path: The file_path of this HostProtectHistoryResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def process_id(self):
        """Gets the process_id of this HostProtectHistoryResponseInfo.

        进程ID，操作系统是Windows时返回

        :return: The process_id of this HostProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this HostProtectHistoryResponseInfo.

        进程ID，操作系统是Windows时返回

        :param process_id: The process_id of this HostProtectHistoryResponseInfo.
        :type process_id: str
        """
        self._process_id = process_id

    @property
    def process_name(self):
        """Gets the process_name of this HostProtectHistoryResponseInfo.

        进程名称，操作系统是Windows时返回

        :return: The process_name of this HostProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """Sets the process_name of this HostProtectHistoryResponseInfo.

        进程名称，操作系统是Windows时返回

        :param process_name: The process_name of this HostProtectHistoryResponseInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_cmd(self):
        """Gets the process_cmd of this HostProtectHistoryResponseInfo.

        进程命令行，操作系统是Windows时返回

        :return: The process_cmd of this HostProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._process_cmd

    @process_cmd.setter
    def process_cmd(self, process_cmd):
        """Sets the process_cmd of this HostProtectHistoryResponseInfo.

        进程命令行，操作系统是Windows时返回

        :param process_cmd: The process_cmd of this HostProtectHistoryResponseInfo.
        :type process_cmd: str
        """
        self._process_cmd = process_cmd

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
        if not isinstance(other, HostProtectHistoryResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
