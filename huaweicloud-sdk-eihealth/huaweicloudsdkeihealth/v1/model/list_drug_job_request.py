# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'job_name': 'str',
        'labels': 'list[str]',
        'status_list': 'list[str]',
        'type_list': 'list[str]',
        'create_start_time': 'int',
        'create_end_time': 'int',
        'finish_start_time': 'int',
        'finish_end_time': 'int',
        'total_time_range': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'job_name': 'job_name',
        'labels': 'labels',
        'status_list': 'status_list',
        'type_list': 'type_list',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'finish_start_time': 'finish_start_time',
        'finish_end_time': 'finish_end_time',
        'total_time_range': 'total_time_range'
    }

    def __init__(self, eihealth_project_id=None, limit=None, offset=None, sort_dir=None, sort_key=None, job_name=None, labels=None, status_list=None, type_list=None, create_start_time=None, create_end_time=None, finish_start_time=None, finish_end_time=None, total_time_range=None):
        """ListDrugJobRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID。
        :type eihealth_project_id: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param sort_dir: 排序规则 目前默认时间降序
        :type sort_dir: str
        :param sort_key: 排序规则 目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序
        :type sort_key: str
        :param job_name: 作业名称
        :type job_name: str
        :param labels: 标签列表
        :type labels: list[str]
        :param status_list: 作业运行状态列表, 支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED
        :type status_list: list[str]
        :param type_list: 作业类型列表, 支持DOCKING|OPTIMIZATION|SYNTHESIS|FEP|POCKET_DETECTION|ADMET
        :type type_list: list[str]
        :param create_start_time: 最小创建时间
        :type create_start_time: int
        :param create_end_time: 最大创建时间
        :type create_end_time: int
        :param finish_start_time: 最小结束时间
        :type finish_start_time: int
        :param finish_end_time: 最大结束时间
        :type finish_end_time: int
        :param total_time_range: 总运行时长, 支持ONE_DAY_MORE|ONE_DAY|ONE_HOUR|TWELVE_HOUR
        :type total_time_range: str
        """
        
        

        self._eihealth_project_id = None
        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._job_name = None
        self._labels = None
        self._status_list = None
        self._type_list = None
        self._create_start_time = None
        self._create_end_time = None
        self._finish_start_time = None
        self._finish_end_time = None
        self._total_time_range = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if job_name is not None:
            self.job_name = job_name
        if labels is not None:
            self.labels = labels
        if status_list is not None:
            self.status_list = status_list
        if type_list is not None:
            self.type_list = type_list
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if finish_start_time is not None:
            self.finish_start_time = finish_start_time
        if finish_end_time is not None:
            self.finish_end_time = finish_end_time
        if total_time_range is not None:
            self.total_time_range = total_time_range

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListDrugJobRequest.

        平台项目ID。

        :return: The eihealth_project_id of this ListDrugJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListDrugJobRequest.

        平台项目ID。

        :param eihealth_project_id: The eihealth_project_id of this ListDrugJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def limit(self):
        """Gets the limit of this ListDrugJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListDrugJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDrugJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListDrugJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDrugJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListDrugJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDrugJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListDrugJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListDrugJobRequest.

        排序规则 目前默认时间降序

        :return: The sort_dir of this ListDrugJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListDrugJobRequest.

        排序规则 目前默认时间降序

        :param sort_dir: The sort_dir of this ListDrugJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListDrugJobRequest.

        排序规则 目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序

        :return: The sort_key of this ListDrugJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListDrugJobRequest.

        排序规则 目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序

        :param sort_key: The sort_key of this ListDrugJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def job_name(self):
        """Gets the job_name of this ListDrugJobRequest.

        作业名称

        :return: The job_name of this ListDrugJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListDrugJobRequest.

        作业名称

        :param job_name: The job_name of this ListDrugJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def labels(self):
        """Gets the labels of this ListDrugJobRequest.

        标签列表

        :return: The labels of this ListDrugJobRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ListDrugJobRequest.

        标签列表

        :param labels: The labels of this ListDrugJobRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status_list(self):
        """Gets the status_list of this ListDrugJobRequest.

        作业运行状态列表, 支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED

        :return: The status_list of this ListDrugJobRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this ListDrugJobRequest.

        作业运行状态列表, 支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED

        :param status_list: The status_list of this ListDrugJobRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def type_list(self):
        """Gets the type_list of this ListDrugJobRequest.

        作业类型列表, 支持DOCKING|OPTIMIZATION|SYNTHESIS|FEP|POCKET_DETECTION|ADMET

        :return: The type_list of this ListDrugJobRequest.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        """Sets the type_list of this ListDrugJobRequest.

        作业类型列表, 支持DOCKING|OPTIMIZATION|SYNTHESIS|FEP|POCKET_DETECTION|ADMET

        :param type_list: The type_list of this ListDrugJobRequest.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def create_start_time(self):
        """Gets the create_start_time of this ListDrugJobRequest.

        最小创建时间

        :return: The create_start_time of this ListDrugJobRequest.
        :rtype: int
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        """Sets the create_start_time of this ListDrugJobRequest.

        最小创建时间

        :param create_start_time: The create_start_time of this ListDrugJobRequest.
        :type create_start_time: int
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        """Gets the create_end_time of this ListDrugJobRequest.

        最大创建时间

        :return: The create_end_time of this ListDrugJobRequest.
        :rtype: int
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        """Sets the create_end_time of this ListDrugJobRequest.

        最大创建时间

        :param create_end_time: The create_end_time of this ListDrugJobRequest.
        :type create_end_time: int
        """
        self._create_end_time = create_end_time

    @property
    def finish_start_time(self):
        """Gets the finish_start_time of this ListDrugJobRequest.

        最小结束时间

        :return: The finish_start_time of this ListDrugJobRequest.
        :rtype: int
        """
        return self._finish_start_time

    @finish_start_time.setter
    def finish_start_time(self, finish_start_time):
        """Sets the finish_start_time of this ListDrugJobRequest.

        最小结束时间

        :param finish_start_time: The finish_start_time of this ListDrugJobRequest.
        :type finish_start_time: int
        """
        self._finish_start_time = finish_start_time

    @property
    def finish_end_time(self):
        """Gets the finish_end_time of this ListDrugJobRequest.

        最大结束时间

        :return: The finish_end_time of this ListDrugJobRequest.
        :rtype: int
        """
        return self._finish_end_time

    @finish_end_time.setter
    def finish_end_time(self, finish_end_time):
        """Sets the finish_end_time of this ListDrugJobRequest.

        最大结束时间

        :param finish_end_time: The finish_end_time of this ListDrugJobRequest.
        :type finish_end_time: int
        """
        self._finish_end_time = finish_end_time

    @property
    def total_time_range(self):
        """Gets the total_time_range of this ListDrugJobRequest.

        总运行时长, 支持ONE_DAY_MORE|ONE_DAY|ONE_HOUR|TWELVE_HOUR

        :return: The total_time_range of this ListDrugJobRequest.
        :rtype: str
        """
        return self._total_time_range

    @total_time_range.setter
    def total_time_range(self, total_time_range):
        """Sets the total_time_range of this ListDrugJobRequest.

        总运行时长, 支持ONE_DAY_MORE|ONE_DAY|ONE_HOUR|TWELVE_HOUR

        :param total_time_range: The total_time_range of this ListDrugJobRequest.
        :type total_time_range: str
        """
        self._total_time_range = total_time_range

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
        if not isinstance(other, ListDrugJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
