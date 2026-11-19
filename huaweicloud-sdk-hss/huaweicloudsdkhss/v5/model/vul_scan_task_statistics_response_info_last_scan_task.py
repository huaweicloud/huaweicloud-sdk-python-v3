# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskStatisticsResponseInfoLastScanTask:

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
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'scan_vul_types': 'list[str]',
        'scanning_host_num': 'int',
        'success_host_num': 'int',
        'risky_host_num': 'VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum',
        'failed_host_num': 'int',
        'estimated_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'scan_type': 'scan_type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'scan_vul_types': 'scan_vul_types',
        'scanning_host_num': 'scanning_host_num',
        'success_host_num': 'success_host_num',
        'risky_host_num': 'risky_host_num',
        'failed_host_num': 'failed_host_num',
        'estimated_time': 'estimated_time'
    }

    def __init__(self, id=None, scan_type=None, status=None, start_time=None, end_time=None, scan_vul_types=None, scanning_host_num=None, success_host_num=None, risky_host_num=None, failed_host_num=None, estimated_time=None):
        r"""VulScanTaskStatisticsResponseInfoLastScanTask

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 任务ID **取值范围**: 字符长度1-128位 
        :type id: str
        :param scan_type: **参数解释**: 扫描任务类型 **取值范围**: - manual：手动扫描 - automatic：自动扫描 
        :type scan_type: str
        :param status: **参数解释**: 任务状态 **取值范围**: - finished：已完成 - running：运行中 - failed：失败 
        :type status: str
        :param start_time: **参数解释**: 任务开始时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type start_time: int
        :param end_time: **参数解释**: 任务结束时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type end_time: int
        :param scan_vul_types: **参数解释**: 扫描的漏洞类型列表 **取值范围**: 0-100个漏洞类型 
        :type scan_vul_types: list[str]
        :param scanning_host_num: **参数解释**: 扫描中的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 
        :type scanning_host_num: int
        :param success_host_num: **参数解释**: 扫描成功的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 
        :type success_host_num: int
        :param risky_host_num: 
        :type risky_host_num: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum`
        :param failed_host_num: **参数解释**: 扫描失败的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 
        :type failed_host_num: int
        :param estimated_time: **参数解释**: 预计还需要多长时间，单位为秒 **取值范围**: 最小值0，最大值2147483647 
        :type estimated_time: int
        """
        
        

        self._id = None
        self._scan_type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._scan_vul_types = None
        self._scanning_host_num = None
        self._success_host_num = None
        self._risky_host_num = None
        self._failed_host_num = None
        self._estimated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if scan_type is not None:
            self.scan_type = scan_type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if scan_vul_types is not None:
            self.scan_vul_types = scan_vul_types
        if scanning_host_num is not None:
            self.scanning_host_num = scanning_host_num
        if success_host_num is not None:
            self.success_host_num = success_host_num
        if risky_host_num is not None:
            self.risky_host_num = risky_host_num
        if failed_host_num is not None:
            self.failed_host_num = failed_host_num
        if estimated_time is not None:
            self.estimated_time = estimated_time

    @property
    def id(self):
        r"""Gets the id of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务ID **取值范围**: 字符长度1-128位 

        :return: The id of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务ID **取值范围**: 字符长度1-128位 

        :param id: The id of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type id: str
        """
        self._id = id

    @property
    def scan_type(self):
        r"""Gets the scan_type of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描任务类型 **取值范围**: - manual：手动扫描 - automatic：自动扫描 

        :return: The scan_type of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描任务类型 **取值范围**: - manual：手动扫描 - automatic：自动扫描 

        :param scan_type: The scan_type of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def status(self):
        r"""Gets the status of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务状态 **取值范围**: - finished：已完成 - running：运行中 - failed：失败 

        :return: The status of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务状态 **取值范围**: - finished：已完成 - running：运行中 - failed：失败 

        :param status: The status of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务开始时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The start_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务开始时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param start_time: The start_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务结束时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The end_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 任务结束时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param end_time: The end_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def scan_vul_types(self):
        r"""Gets the scan_vul_types of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描的漏洞类型列表 **取值范围**: 0-100个漏洞类型 

        :return: The scan_vul_types of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: list[str]
        """
        return self._scan_vul_types

    @scan_vul_types.setter
    def scan_vul_types(self, scan_vul_types):
        r"""Sets the scan_vul_types of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描的漏洞类型列表 **取值范围**: 0-100个漏洞类型 

        :param scan_vul_types: The scan_vul_types of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type scan_vul_types: list[str]
        """
        self._scan_vul_types = scan_vul_types

    @property
    def scanning_host_num(self):
        r"""Gets the scanning_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描中的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The scanning_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._scanning_host_num

    @scanning_host_num.setter
    def scanning_host_num(self, scanning_host_num):
        r"""Sets the scanning_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描中的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :param scanning_host_num: The scanning_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type scanning_host_num: int
        """
        self._scanning_host_num = scanning_host_num

    @property
    def success_host_num(self):
        r"""Gets the success_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描成功的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The success_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._success_host_num

    @success_host_num.setter
    def success_host_num(self, success_host_num):
        r"""Sets the success_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描成功的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :param success_host_num: The success_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type success_host_num: int
        """
        self._success_host_num = success_host_num

    @property
    def risky_host_num(self):
        r"""Gets the risky_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        :return: The risky_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum`
        """
        return self._risky_host_num

    @risky_host_num.setter
    def risky_host_num(self, risky_host_num):
        r"""Sets the risky_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        :param risky_host_num: The risky_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type risky_host_num: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum`
        """
        self._risky_host_num = risky_host_num

    @property
    def failed_host_num(self):
        r"""Gets the failed_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描失败的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The failed_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._failed_host_num

    @failed_host_num.setter
    def failed_host_num(self, failed_host_num):
        r"""Sets the failed_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 扫描失败的主机数，Serverless场景下为POD实例数 **取值范围**: 最小值0，最大值2147483647 

        :param failed_host_num: The failed_host_num of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type failed_host_num: int
        """
        self._failed_host_num = failed_host_num

    @property
    def estimated_time(self):
        r"""Gets the estimated_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 预计还需要多长时间，单位为秒 **取值范围**: 最小值0，最大值2147483647 

        :return: The estimated_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :rtype: int
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        r"""Sets the estimated_time of this VulScanTaskStatisticsResponseInfoLastScanTask.

        **参数解释**: 预计还需要多长时间，单位为秒 **取值范围**: 最小值0，最大值2147483647 

        :param estimated_time: The estimated_time of this VulScanTaskStatisticsResponseInfoLastScanTask.
        :type estimated_time: int
        """
        self._estimated_time = estimated_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VulScanTaskStatisticsResponseInfoLastScanTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
