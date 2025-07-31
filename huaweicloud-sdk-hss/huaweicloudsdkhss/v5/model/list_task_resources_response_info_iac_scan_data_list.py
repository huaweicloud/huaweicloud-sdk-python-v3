# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResourcesResponseInfoIacScanDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_type': 'str',
        'chart_name': 'str',
        'file_id': 'str',
        'file_size': 'int',
        'scan_status': 'str',
        'failed_reason': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_type': 'file_type',
        'chart_name': 'chart_name',
        'file_id': 'file_id',
        'file_size': 'file_size',
        'scan_status': 'scan_status',
        'failed_reason': 'failed_reason',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, file_name=None, file_type=None, chart_name=None, file_id=None, file_size=None, scan_status=None, failed_reason=None, start_time=None, end_time=None):
        r"""ListTaskResourcesResponseInfoIacScanDataList

        The model defined in huaweicloud sdk

        :param file_name: 文件名称
        :type file_name: str
        :param file_type: 文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件
        :type file_type: str
        :param chart_name: chart包名称
        :type chart_name: str
        :param file_id: 文件ID，服务生成的文件唯一ID
        :type file_id: str
        :param file_size: 文件大小
        :type file_size: int
        :param scan_status: 文件的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败
        :type scan_status: str
        :param failed_reason: 扫描失败的原因
        :type failed_reason: str
        :param start_time: 扫描开始的时间
        :type start_time: int
        :param end_time: 扫描结束的时间
        :type end_time: int
        """
        
        

        self._file_name = None
        self._file_type = None
        self._chart_name = None
        self._file_id = None
        self._file_size = None
        self._scan_status = None
        self._failed_reason = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if chart_name is not None:
            self.chart_name = chart_name
        if file_id is not None:
            self.file_id = file_id
        if file_size is not None:
            self.file_size = file_size
        if scan_status is not None:
            self.scan_status = scan_status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def file_name(self):
        r"""Gets the file_name of this ListTaskResourcesResponseInfoIacScanDataList.

        文件名称

        :return: The file_name of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListTaskResourcesResponseInfoIacScanDataList.

        文件名称

        :param file_name: The file_name of this ListTaskResourcesResponseInfoIacScanDataList.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this ListTaskResourcesResponseInfoIacScanDataList.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :return: The file_type of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ListTaskResourcesResponseInfoIacScanDataList.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :param file_type: The file_type of this ListTaskResourcesResponseInfoIacScanDataList.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def chart_name(self):
        r"""Gets the chart_name of this ListTaskResourcesResponseInfoIacScanDataList.

        chart包名称

        :return: The chart_name of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._chart_name

    @chart_name.setter
    def chart_name(self, chart_name):
        r"""Sets the chart_name of this ListTaskResourcesResponseInfoIacScanDataList.

        chart包名称

        :param chart_name: The chart_name of this ListTaskResourcesResponseInfoIacScanDataList.
        :type chart_name: str
        """
        self._chart_name = chart_name

    @property
    def file_id(self):
        r"""Gets the file_id of this ListTaskResourcesResponseInfoIacScanDataList.

        文件ID，服务生成的文件唯一ID

        :return: The file_id of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ListTaskResourcesResponseInfoIacScanDataList.

        文件ID，服务生成的文件唯一ID

        :param file_id: The file_id of this ListTaskResourcesResponseInfoIacScanDataList.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_size(self):
        r"""Gets the file_size of this ListTaskResourcesResponseInfoIacScanDataList.

        文件大小

        :return: The file_size of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this ListTaskResourcesResponseInfoIacScanDataList.

        文件大小

        :param file_size: The file_size of this ListTaskResourcesResponseInfoIacScanDataList.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ListTaskResourcesResponseInfoIacScanDataList.

        文件的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :return: The scan_status of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ListTaskResourcesResponseInfoIacScanDataList.

        文件的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :param scan_status: The scan_status of this ListTaskResourcesResponseInfoIacScanDataList.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描失败的原因

        :return: The failed_reason of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描失败的原因

        :param failed_reason: The failed_reason of this ListTaskResourcesResponseInfoIacScanDataList.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描开始的时间

        :return: The start_time of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描开始的时间

        :param start_time: The start_time of this ListTaskResourcesResponseInfoIacScanDataList.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描结束的时间

        :return: The end_time of this ListTaskResourcesResponseInfoIacScanDataList.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTaskResourcesResponseInfoIacScanDataList.

        扫描结束的时间

        :param end_time: The end_time of this ListTaskResourcesResponseInfoIacScanDataList.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListTaskResourcesResponseInfoIacScanDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
