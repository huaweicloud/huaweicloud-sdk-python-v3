# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobRequest:

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
        'end_time': 'int',
        'job_name': 'str',
        'labels': 'list[str]',
        'limit': 'int',
        'offset': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'start_time': 'int',
        'status': 'str',
        'tool_name': 'str',
        'user_name': 'str',
        'finish_start_time': 'int',
        'finish_end_time': 'int'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'end_time': 'end_time',
        'job_name': 'job_name',
        'labels': 'labels',
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'start_time': 'start_time',
        'status': 'status',
        'tool_name': 'tool_name',
        'user_name': 'user_name',
        'finish_start_time': 'finish_start_time',
        'finish_end_time': 'finish_end_time'
    }

    def __init__(self, eihealth_project_id=None, end_time=None, job_name=None, labels=None, limit=None, offset=None, sort_dir=None, sort_key=None, start_time=None, status=None, tool_name=None, user_name=None, finish_start_time=None, finish_end_time=None):
        r"""ListJobRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param end_time: 最大开始时间
        :type end_time: int
        :param job_name: 作业名称 取值范围：长度为[1,63]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。
        :type job_name: str
        :param labels: 标签列表
        :type labels: list[str]
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param sort_dir: 排序规则 目前默认时间降序
        :type sort_dir: str
        :param sort_key: 排序规则 目前默认时间降序，支持根据status
        :type sort_key: str
        :param start_time: 最小开始时间
        :type start_time: int
        :param status: 作业运行状态 取值（Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown）
        :type status: str
        :param tool_name: 作业依赖的组件名称(有可能是Workflow，有可能是app), 取值范围：长度为[1,56]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。
        :type tool_name: str
        :param user_name: 作业创建者
        :type user_name: str
        :param finish_start_time: 最小结束时间
        :type finish_start_time: int
        :param finish_end_time: 最大结束时间
        :type finish_end_time: int
        """
        
        

        self._eihealth_project_id = None
        self._end_time = None
        self._job_name = None
        self._labels = None
        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._start_time = None
        self._status = None
        self._tool_name = None
        self._user_name = None
        self._finish_start_time = None
        self._finish_end_time = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if end_time is not None:
            self.end_time = end_time
        if job_name is not None:
            self.job_name = job_name
        if labels is not None:
            self.labels = labels
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if tool_name is not None:
            self.tool_name = tool_name
        if user_name is not None:
            self.user_name = user_name
        if finish_start_time is not None:
            self.finish_start_time = finish_start_time
        if finish_end_time is not None:
            self.finish_end_time = finish_end_time

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ListJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ListJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def end_time(self):
        r"""Gets the end_time of this ListJobRequest.

        最大开始时间

        :return: The end_time of this ListJobRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListJobRequest.

        最大开始时间

        :param end_time: The end_time of this ListJobRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def job_name(self):
        r"""Gets the job_name of this ListJobRequest.

        作业名称 取值范围：长度为[1,63]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :return: The job_name of this ListJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListJobRequest.

        作业名称 取值范围：长度为[1,63]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :param job_name: The job_name of this ListJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def labels(self):
        r"""Gets the labels of this ListJobRequest.

        标签列表

        :return: The labels of this ListJobRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListJobRequest.

        标签列表

        :param labels: The labels of this ListJobRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def limit(self):
        r"""Gets the limit of this ListJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListJobRequest.

        排序规则 目前默认时间降序

        :return: The sort_dir of this ListJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListJobRequest.

        排序规则 目前默认时间降序

        :param sort_dir: The sort_dir of this ListJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListJobRequest.

        排序规则 目前默认时间降序，支持根据status

        :return: The sort_key of this ListJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListJobRequest.

        排序规则 目前默认时间降序，支持根据status

        :param sort_key: The sort_key of this ListJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def start_time(self):
        r"""Gets the start_time of this ListJobRequest.

        最小开始时间

        :return: The start_time of this ListJobRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListJobRequest.

        最小开始时间

        :param start_time: The start_time of this ListJobRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this ListJobRequest.

        作业运行状态 取值（Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown）

        :return: The status of this ListJobRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobRequest.

        作业运行状态 取值（Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown）

        :param status: The status of this ListJobRequest.
        :type status: str
        """
        self._status = status

    @property
    def tool_name(self):
        r"""Gets the tool_name of this ListJobRequest.

        作业依赖的组件名称(有可能是Workflow，有可能是app), 取值范围：长度为[1,56]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :return: The tool_name of this ListJobRequest.
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        r"""Sets the tool_name of this ListJobRequest.

        作业依赖的组件名称(有可能是Workflow，有可能是app), 取值范围：长度为[1,56]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :param tool_name: The tool_name of this ListJobRequest.
        :type tool_name: str
        """
        self._tool_name = tool_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListJobRequest.

        作业创建者

        :return: The user_name of this ListJobRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListJobRequest.

        作业创建者

        :param user_name: The user_name of this ListJobRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def finish_start_time(self):
        r"""Gets the finish_start_time of this ListJobRequest.

        最小结束时间

        :return: The finish_start_time of this ListJobRequest.
        :rtype: int
        """
        return self._finish_start_time

    @finish_start_time.setter
    def finish_start_time(self, finish_start_time):
        r"""Sets the finish_start_time of this ListJobRequest.

        最小结束时间

        :param finish_start_time: The finish_start_time of this ListJobRequest.
        :type finish_start_time: int
        """
        self._finish_start_time = finish_start_time

    @property
    def finish_end_time(self):
        r"""Gets the finish_end_time of this ListJobRequest.

        最大结束时间

        :return: The finish_end_time of this ListJobRequest.
        :rtype: int
        """
        return self._finish_end_time

    @finish_end_time.setter
    def finish_end_time(self, finish_end_time):
        r"""Sets the finish_end_time of this ListJobRequest.

        最大结束时间

        :param finish_end_time: The finish_end_time of this ListJobRequest.
        :type finish_end_time: int
        """
        self._finish_end_time = finish_end_time

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
        if not isinstance(other, ListJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
