# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnosisTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'type': 'str',
        'status': 'str',
        'region': 'str',
        'creator': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'page_index': 'int',
        'page_size': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'type': 'type',
        'status': 'status',
        'region': 'region',
        'creator': 'creator',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, type=None, status=None, region=None, creator=None, start_time=None, end_time=None, page_index=None, page_size=None, offset=None, limit=None):
        r"""ListDiagnosisTasksRequest

        The model defined in huaweicloud sdk

        :param task_id: 诊断任务工单ID
        :type task_id: str
        :param type: 诊断任务实例类别
        :type type: str
        :param status: 诊断任务执行状态
        :type status: str
        :param region: 被诊断实例所在区域
        :type region: str
        :param creator: 诊断工单创建者
        :type creator: str
        :param start_time: 诊断工单的开始执行时间
        :type start_time: int
        :param end_time: 诊断工单的执行结束时间
        :type end_time: int
        :param page_index: 分页查询页索引
        :type page_index: int
        :param page_size: 分页查询页大小
        :type page_size: int
        :param offset: 分页查询页索引
        :type offset: int
        :param limit: 分页查询页大小
        :type limit: int
        """
        
        

        self._task_id = None
        self._type = None
        self._status = None
        self._region = None
        self._creator = None
        self._start_time = None
        self._end_time = None
        self._page_index = None
        self._page_size = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if creator is not None:
            self.creator = creator
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListDiagnosisTasksRequest.

        诊断任务工单ID

        :return: The task_id of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListDiagnosisTasksRequest.

        诊断任务工单ID

        :param task_id: The task_id of this ListDiagnosisTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def type(self):
        r"""Gets the type of this ListDiagnosisTasksRequest.

        诊断任务实例类别

        :return: The type of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDiagnosisTasksRequest.

        诊断任务实例类别

        :param type: The type of this ListDiagnosisTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListDiagnosisTasksRequest.

        诊断任务执行状态

        :return: The status of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDiagnosisTasksRequest.

        诊断任务执行状态

        :param status: The status of this ListDiagnosisTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ListDiagnosisTasksRequest.

        被诊断实例所在区域

        :return: The region of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListDiagnosisTasksRequest.

        被诊断实例所在区域

        :param region: The region of this ListDiagnosisTasksRequest.
        :type region: str
        """
        self._region = region

    @property
    def creator(self):
        r"""Gets the creator of this ListDiagnosisTasksRequest.

        诊断工单创建者

        :return: The creator of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListDiagnosisTasksRequest.

        诊断工单创建者

        :param creator: The creator of this ListDiagnosisTasksRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def start_time(self):
        r"""Gets the start_time of this ListDiagnosisTasksRequest.

        诊断工单的开始执行时间

        :return: The start_time of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListDiagnosisTasksRequest.

        诊断工单的开始执行时间

        :param start_time: The start_time of this ListDiagnosisTasksRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListDiagnosisTasksRequest.

        诊断工单的执行结束时间

        :return: The end_time of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListDiagnosisTasksRequest.

        诊断工单的执行结束时间

        :param end_time: The end_time of this ListDiagnosisTasksRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_index(self):
        r"""Gets the page_index of this ListDiagnosisTasksRequest.

        分页查询页索引

        :return: The page_index of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListDiagnosisTasksRequest.

        分页查询页索引

        :param page_index: The page_index of this ListDiagnosisTasksRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDiagnosisTasksRequest.

        分页查询页大小

        :return: The page_size of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDiagnosisTasksRequest.

        分页查询页大小

        :param page_size: The page_size of this ListDiagnosisTasksRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def offset(self):
        r"""Gets the offset of this ListDiagnosisTasksRequest.

        分页查询页索引

        :return: The offset of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDiagnosisTasksRequest.

        分页查询页索引

        :param offset: The offset of this ListDiagnosisTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDiagnosisTasksRequest.

        分页查询页大小

        :return: The limit of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDiagnosisTasksRequest.

        分页查询页大小

        :param limit: The limit of this ListDiagnosisTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDiagnosisTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
