# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'scan_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'scan_vul_types': 'list[str]',
        'status': 'str',
        'scanning_host_num': 'int',
        'success_host_num': 'int',
        'failed_host_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'scan_type': 'scan_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'scan_vul_types': 'scan_vul_types',
        'status': 'status',
        'scanning_host_num': 'scanning_host_num',
        'success_host_num': 'success_host_num',
        'failed_host_num': 'failed_host_num'
    }

    def __init__(self, id=None, scan_type=None, start_time=None, end_time=None, scan_vul_types=None, status=None, scanning_host_num=None, success_host_num=None, failed_host_num=None):
        """VulScanTaskInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param scan_type: 扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务
        :type scan_type: str
        :param start_time: 扫描任务开始的时间
        :type start_time: int
        :param end_time: 扫描任务结束的时间
        :type end_time: int
        :param scan_vul_types: 该任务扫描的漏洞类型列表
        :type scan_vul_types: list[str]
        :param status: 扫描任务的执行状态，包含如下：   -running : 扫描中   -finished : 扫描完成
        :type status: str
        :param scanning_host_num: 该任务处于扫描中状态的主机数量
        :type scanning_host_num: int
        :param success_host_num: 该任务已扫描成功的主机数量
        :type success_host_num: int
        :param failed_host_num: 该任务已扫描失败的主机数量
        :type failed_host_num: int
        """
        
        

        self._id = None
        self._scan_type = None
        self._start_time = None
        self._end_time = None
        self._scan_vul_types = None
        self._status = None
        self._scanning_host_num = None
        self._success_host_num = None
        self._failed_host_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if scan_type is not None:
            self.scan_type = scan_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if scan_vul_types is not None:
            self.scan_vul_types = scan_vul_types
        if status is not None:
            self.status = status
        if scanning_host_num is not None:
            self.scanning_host_num = scanning_host_num
        if success_host_num is not None:
            self.success_host_num = success_host_num
        if failed_host_num is not None:
            self.failed_host_num = failed_host_num

    @property
    def id(self):
        """Gets the id of this VulScanTaskInfo.

        任务ID

        :return: The id of this VulScanTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VulScanTaskInfo.

        任务ID

        :param id: The id of this VulScanTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def scan_type(self):
        """Gets the scan_type of this VulScanTaskInfo.

        扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务

        :return: The scan_type of this VulScanTaskInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this VulScanTaskInfo.

        扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务

        :param scan_type: The scan_type of this VulScanTaskInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def start_time(self):
        """Gets the start_time of this VulScanTaskInfo.

        扫描任务开始的时间

        :return: The start_time of this VulScanTaskInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this VulScanTaskInfo.

        扫描任务开始的时间

        :param start_time: The start_time of this VulScanTaskInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this VulScanTaskInfo.

        扫描任务结束的时间

        :return: The end_time of this VulScanTaskInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this VulScanTaskInfo.

        扫描任务结束的时间

        :param end_time: The end_time of this VulScanTaskInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def scan_vul_types(self):
        """Gets the scan_vul_types of this VulScanTaskInfo.

        该任务扫描的漏洞类型列表

        :return: The scan_vul_types of this VulScanTaskInfo.
        :rtype: list[str]
        """
        return self._scan_vul_types

    @scan_vul_types.setter
    def scan_vul_types(self, scan_vul_types):
        """Sets the scan_vul_types of this VulScanTaskInfo.

        该任务扫描的漏洞类型列表

        :param scan_vul_types: The scan_vul_types of this VulScanTaskInfo.
        :type scan_vul_types: list[str]
        """
        self._scan_vul_types = scan_vul_types

    @property
    def status(self):
        """Gets the status of this VulScanTaskInfo.

        扫描任务的执行状态，包含如下：   -running : 扫描中   -finished : 扫描完成

        :return: The status of this VulScanTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VulScanTaskInfo.

        扫描任务的执行状态，包含如下：   -running : 扫描中   -finished : 扫描完成

        :param status: The status of this VulScanTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def scanning_host_num(self):
        """Gets the scanning_host_num of this VulScanTaskInfo.

        该任务处于扫描中状态的主机数量

        :return: The scanning_host_num of this VulScanTaskInfo.
        :rtype: int
        """
        return self._scanning_host_num

    @scanning_host_num.setter
    def scanning_host_num(self, scanning_host_num):
        """Sets the scanning_host_num of this VulScanTaskInfo.

        该任务处于扫描中状态的主机数量

        :param scanning_host_num: The scanning_host_num of this VulScanTaskInfo.
        :type scanning_host_num: int
        """
        self._scanning_host_num = scanning_host_num

    @property
    def success_host_num(self):
        """Gets the success_host_num of this VulScanTaskInfo.

        该任务已扫描成功的主机数量

        :return: The success_host_num of this VulScanTaskInfo.
        :rtype: int
        """
        return self._success_host_num

    @success_host_num.setter
    def success_host_num(self, success_host_num):
        """Sets the success_host_num of this VulScanTaskInfo.

        该任务已扫描成功的主机数量

        :param success_host_num: The success_host_num of this VulScanTaskInfo.
        :type success_host_num: int
        """
        self._success_host_num = success_host_num

    @property
    def failed_host_num(self):
        """Gets the failed_host_num of this VulScanTaskInfo.

        该任务已扫描失败的主机数量

        :return: The failed_host_num of this VulScanTaskInfo.
        :rtype: int
        """
        return self._failed_host_num

    @failed_host_num.setter
    def failed_host_num(self, failed_host_num):
        """Sets the failed_host_num of this VulScanTaskInfo.

        该任务已扫描失败的主机数量

        :param failed_host_num: The failed_host_num of this VulScanTaskInfo.
        :type failed_host_num: int
        """
        self._failed_host_num = failed_host_num

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
        if not isinstance(other, VulScanTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
