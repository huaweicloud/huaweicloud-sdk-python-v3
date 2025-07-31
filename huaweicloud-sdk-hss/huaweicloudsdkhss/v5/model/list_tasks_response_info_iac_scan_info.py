# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponseInfoIacScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_type': 'str',
        'scan_file_num': 'int',
        'success_file_num': 'int',
        'failed_file_num': 'int'
    }

    attribute_map = {
        'file_type': 'file_type',
        'scan_file_num': 'scan_file_num',
        'success_file_num': 'success_file_num',
        'failed_file_num': 'failed_file_num'
    }

    def __init__(self, file_type=None, scan_file_num=None, success_file_num=None, failed_file_num=None):
        r"""ListTasksResponseInfoIacScanInfo

        The model defined in huaweicloud sdk

        :param file_type: 文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件
        :type file_type: str
        :param scan_file_num: 当前任务扫描的文件总数
        :type scan_file_num: int
        :param success_file_num: 当前任务扫描成功的文件数量
        :type success_file_num: int
        :param failed_file_num: 当前任务扫描失败的文件数量
        :type failed_file_num: int
        """
        
        

        self._file_type = None
        self._scan_file_num = None
        self._success_file_num = None
        self._failed_file_num = None
        self.discriminator = None

        if file_type is not None:
            self.file_type = file_type
        if scan_file_num is not None:
            self.scan_file_num = scan_file_num
        if success_file_num is not None:
            self.success_file_num = success_file_num
        if failed_file_num is not None:
            self.failed_file_num = failed_file_num

    @property
    def file_type(self):
        r"""Gets the file_type of this ListTasksResponseInfoIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :return: The file_type of this ListTasksResponseInfoIacScanInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ListTasksResponseInfoIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :param file_type: The file_type of this ListTasksResponseInfoIacScanInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def scan_file_num(self):
        r"""Gets the scan_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描的文件总数

        :return: The scan_file_num of this ListTasksResponseInfoIacScanInfo.
        :rtype: int
        """
        return self._scan_file_num

    @scan_file_num.setter
    def scan_file_num(self, scan_file_num):
        r"""Sets the scan_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描的文件总数

        :param scan_file_num: The scan_file_num of this ListTasksResponseInfoIacScanInfo.
        :type scan_file_num: int
        """
        self._scan_file_num = scan_file_num

    @property
    def success_file_num(self):
        r"""Gets the success_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描成功的文件数量

        :return: The success_file_num of this ListTasksResponseInfoIacScanInfo.
        :rtype: int
        """
        return self._success_file_num

    @success_file_num.setter
    def success_file_num(self, success_file_num):
        r"""Sets the success_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描成功的文件数量

        :param success_file_num: The success_file_num of this ListTasksResponseInfoIacScanInfo.
        :type success_file_num: int
        """
        self._success_file_num = success_file_num

    @property
    def failed_file_num(self):
        r"""Gets the failed_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描失败的文件数量

        :return: The failed_file_num of this ListTasksResponseInfoIacScanInfo.
        :rtype: int
        """
        return self._failed_file_num

    @failed_file_num.setter
    def failed_file_num(self, failed_file_num):
        r"""Sets the failed_file_num of this ListTasksResponseInfoIacScanInfo.

        当前任务扫描失败的文件数量

        :param failed_file_num: The failed_file_num of this ListTasksResponseInfoIacScanInfo.
        :type failed_file_num: int
        """
        self._failed_file_num = failed_file_num

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
        if not isinstance(other, ListTasksResponseInfoIacScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
