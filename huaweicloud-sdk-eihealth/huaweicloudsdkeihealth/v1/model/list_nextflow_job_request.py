# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNextflowJobRequest:

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
        'status': 'str',
        'workflow_name': 'str',
        'user_name': 'str',
        'create_start_time': 'int',
        'create_end_time': 'int',
        'finish_start_time': 'int',
        'finish_end_time': 'int'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'job_name': 'job_name',
        'labels': 'labels',
        'status': 'status',
        'workflow_name': 'workflow_name',
        'user_name': 'user_name',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'finish_start_time': 'finish_start_time',
        'finish_end_time': 'finish_end_time'
    }

    def __init__(self, eihealth_project_id=None, limit=None, offset=None, sort_dir=None, sort_key=None, job_name=None, labels=None, status=None, workflow_name=None, user_name=None, create_start_time=None, create_end_time=None, finish_start_time=None, finish_end_time=None):
        r"""ListNextflowJobRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param sort_dir: 排序规则 目前默认时间降序
        :type sort_dir: str
        :param sort_key: 排序规则 目前默认时间降序，支持根据status
        :type sort_key: str
        :param job_name: 作业名称
        :type job_name: str
        :param labels: 标签列表
        :type labels: list[str]
        :param status: 作业运行状态 取值（SUBMITTED|RUNNING|COMPLETED|FAILED|CANCELLED|UNKNOWN）
        :type status: str
        :param workflow_name: workflow名称
        :type workflow_name: str
        :param user_name: 作业创建者
        :type user_name: str
        :param create_start_time: 最小创建时间
        :type create_start_time: int
        :param create_end_time: 最大创建时间
        :type create_end_time: int
        :param finish_start_time: 最小结束时间
        :type finish_start_time: int
        :param finish_end_time: 最大结束时间
        :type finish_end_time: int
        """
        
        

        self._eihealth_project_id = None
        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._job_name = None
        self._labels = None
        self._status = None
        self._workflow_name = None
        self._user_name = None
        self._create_start_time = None
        self._create_end_time = None
        self._finish_start_time = None
        self._finish_end_time = None
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
        if status is not None:
            self.status = status
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if user_name is not None:
            self.user_name = user_name
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if finish_start_time is not None:
            self.finish_start_time = finish_start_time
        if finish_end_time is not None:
            self.finish_end_time = finish_end_time

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ListNextflowJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ListNextflowJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListNextflowJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListNextflowJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNextflowJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListNextflowJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNextflowJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNextflowJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListNextflowJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListNextflowJobRequest.

        排序规则 目前默认时间降序

        :return: The sort_dir of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListNextflowJobRequest.

        排序规则 目前默认时间降序

        :param sort_dir: The sort_dir of this ListNextflowJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListNextflowJobRequest.

        排序规则 目前默认时间降序，支持根据status

        :return: The sort_key of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListNextflowJobRequest.

        排序规则 目前默认时间降序，支持根据status

        :param sort_key: The sort_key of this ListNextflowJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def job_name(self):
        r"""Gets the job_name of this ListNextflowJobRequest.

        作业名称

        :return: The job_name of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListNextflowJobRequest.

        作业名称

        :param job_name: The job_name of this ListNextflowJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def labels(self):
        r"""Gets the labels of this ListNextflowJobRequest.

        标签列表

        :return: The labels of this ListNextflowJobRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListNextflowJobRequest.

        标签列表

        :param labels: The labels of this ListNextflowJobRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this ListNextflowJobRequest.

        作业运行状态 取值（SUBMITTED|RUNNING|COMPLETED|FAILED|CANCELLED|UNKNOWN）

        :return: The status of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListNextflowJobRequest.

        作业运行状态 取值（SUBMITTED|RUNNING|COMPLETED|FAILED|CANCELLED|UNKNOWN）

        :param status: The status of this ListNextflowJobRequest.
        :type status: str
        """
        self._status = status

    @property
    def workflow_name(self):
        r"""Gets the workflow_name of this ListNextflowJobRequest.

        workflow名称

        :return: The workflow_name of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        r"""Sets the workflow_name of this ListNextflowJobRequest.

        workflow名称

        :param workflow_name: The workflow_name of this ListNextflowJobRequest.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListNextflowJobRequest.

        作业创建者

        :return: The user_name of this ListNextflowJobRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListNextflowJobRequest.

        作业创建者

        :param user_name: The user_name of this ListNextflowJobRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_start_time(self):
        r"""Gets the create_start_time of this ListNextflowJobRequest.

        最小创建时间

        :return: The create_start_time of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        r"""Sets the create_start_time of this ListNextflowJobRequest.

        最小创建时间

        :param create_start_time: The create_start_time of this ListNextflowJobRequest.
        :type create_start_time: int
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        r"""Gets the create_end_time of this ListNextflowJobRequest.

        最大创建时间

        :return: The create_end_time of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        r"""Sets the create_end_time of this ListNextflowJobRequest.

        最大创建时间

        :param create_end_time: The create_end_time of this ListNextflowJobRequest.
        :type create_end_time: int
        """
        self._create_end_time = create_end_time

    @property
    def finish_start_time(self):
        r"""Gets the finish_start_time of this ListNextflowJobRequest.

        最小结束时间

        :return: The finish_start_time of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._finish_start_time

    @finish_start_time.setter
    def finish_start_time(self, finish_start_time):
        r"""Sets the finish_start_time of this ListNextflowJobRequest.

        最小结束时间

        :param finish_start_time: The finish_start_time of this ListNextflowJobRequest.
        :type finish_start_time: int
        """
        self._finish_start_time = finish_start_time

    @property
    def finish_end_time(self):
        r"""Gets the finish_end_time of this ListNextflowJobRequest.

        最大结束时间

        :return: The finish_end_time of this ListNextflowJobRequest.
        :rtype: int
        """
        return self._finish_end_time

    @finish_end_time.setter
    def finish_end_time(self, finish_end_time):
        r"""Sets the finish_end_time of this ListNextflowJobRequest.

        最大结束时间

        :param finish_end_time: The finish_end_time of this ListNextflowJobRequest.
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
        if not isinstance(other, ListNextflowJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
