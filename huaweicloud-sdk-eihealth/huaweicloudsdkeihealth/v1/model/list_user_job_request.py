# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_creator': 'bool',
        'job_name': 'str',
        'eihealth_project_names': 'list[str]',
        'types': 'list[str]',
        'status_list': 'list[str]',
        'labels': 'list[str]',
        'start_create_time': 'int',
        'end_create_time': 'int',
        'start_finish_time': 'int',
        'end_finish_time': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'is_creator': 'is_creator',
        'job_name': 'job_name',
        'eihealth_project_names': 'eihealth_project_names',
        'types': 'types',
        'status_list': 'status_list',
        'labels': 'labels',
        'start_create_time': 'start_create_time',
        'end_create_time': 'end_create_time',
        'start_finish_time': 'start_finish_time',
        'end_finish_time': 'end_finish_time',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, is_creator=None, job_name=None, eihealth_project_names=None, types=None, status_list=None, labels=None, start_create_time=None, end_create_time=None, start_finish_time=None, end_finish_time=None, sort_key=None, sort_dir=None, limit=None, offset=None):
        r"""ListUserJobRequest

        The model defined in huaweicloud sdk

        :param is_creator: 是否仅展示本人创建资源。
        :type is_creator: bool
        :param job_name: 作业名称，取值范围：长度为[1,63]，以小写字母开头，允许出现中划线（-）、小写字母和数字，且必须以小写字母或数字结尾。
        :type job_name: str
        :param eihealth_project_names: 空间名称列表，多个值之间使用逗号分隔。
        :type eihealth_project_names: list[str]
        :param types: 作业类型列表，支持workflow|app。
        :type types: list[str]
        :param status_list: 作业运行状态列表，支持Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown。
        :type status_list: list[str]
        :param labels: 标签列表。
        :type labels: list[str]
        :param start_create_time: 开始创建时间。
        :type start_create_time: int
        :param end_create_time: 结束创建时间。
        :type end_create_time: int
        :param start_finish_time: 开始完成时间。
        :type start_finish_time: int
        :param end_finish_time: 结束完成时间。
        :type end_finish_time: int
        :param sort_key: 排序规则，默认根据创建时间降序，支持create_time|finish_time。
        :type sort_key: str
        :param sort_dir: 排序规则，目前默认时间降序。
        :type sort_dir: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。
        :type offset: int
        """
        
        

        self._is_creator = None
        self._job_name = None
        self._eihealth_project_names = None
        self._types = None
        self._status_list = None
        self._labels = None
        self._start_create_time = None
        self._end_create_time = None
        self._start_finish_time = None
        self._end_finish_time = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if is_creator is not None:
            self.is_creator = is_creator
        if job_name is not None:
            self.job_name = job_name
        if eihealth_project_names is not None:
            self.eihealth_project_names = eihealth_project_names
        if types is not None:
            self.types = types
        if status_list is not None:
            self.status_list = status_list
        if labels is not None:
            self.labels = labels
        if start_create_time is not None:
            self.start_create_time = start_create_time
        if end_create_time is not None:
            self.end_create_time = end_create_time
        if start_finish_time is not None:
            self.start_finish_time = start_finish_time
        if end_finish_time is not None:
            self.end_finish_time = end_finish_time
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def is_creator(self):
        r"""Gets the is_creator of this ListUserJobRequest.

        是否仅展示本人创建资源。

        :return: The is_creator of this ListUserJobRequest.
        :rtype: bool
        """
        return self._is_creator

    @is_creator.setter
    def is_creator(self, is_creator):
        r"""Sets the is_creator of this ListUserJobRequest.

        是否仅展示本人创建资源。

        :param is_creator: The is_creator of this ListUserJobRequest.
        :type is_creator: bool
        """
        self._is_creator = is_creator

    @property
    def job_name(self):
        r"""Gets the job_name of this ListUserJobRequest.

        作业名称，取值范围：长度为[1,63]，以小写字母开头，允许出现中划线（-）、小写字母和数字，且必须以小写字母或数字结尾。

        :return: The job_name of this ListUserJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListUserJobRequest.

        作业名称，取值范围：长度为[1,63]，以小写字母开头，允许出现中划线（-）、小写字母和数字，且必须以小写字母或数字结尾。

        :param job_name: The job_name of this ListUserJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def eihealth_project_names(self):
        r"""Gets the eihealth_project_names of this ListUserJobRequest.

        空间名称列表，多个值之间使用逗号分隔。

        :return: The eihealth_project_names of this ListUserJobRequest.
        :rtype: list[str]
        """
        return self._eihealth_project_names

    @eihealth_project_names.setter
    def eihealth_project_names(self, eihealth_project_names):
        r"""Sets the eihealth_project_names of this ListUserJobRequest.

        空间名称列表，多个值之间使用逗号分隔。

        :param eihealth_project_names: The eihealth_project_names of this ListUserJobRequest.
        :type eihealth_project_names: list[str]
        """
        self._eihealth_project_names = eihealth_project_names

    @property
    def types(self):
        r"""Gets the types of this ListUserJobRequest.

        作业类型列表，支持workflow|app。

        :return: The types of this ListUserJobRequest.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        r"""Sets the types of this ListUserJobRequest.

        作业类型列表，支持workflow|app。

        :param types: The types of this ListUserJobRequest.
        :type types: list[str]
        """
        self._types = types

    @property
    def status_list(self):
        r"""Gets the status_list of this ListUserJobRequest.

        作业运行状态列表，支持Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown。

        :return: The status_list of this ListUserJobRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListUserJobRequest.

        作业运行状态列表，支持Succeeded|Running|Pending|Failed|Cancelling|Cancelled|Unknown。

        :param status_list: The status_list of this ListUserJobRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def labels(self):
        r"""Gets the labels of this ListUserJobRequest.

        标签列表。

        :return: The labels of this ListUserJobRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListUserJobRequest.

        标签列表。

        :param labels: The labels of this ListUserJobRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def start_create_time(self):
        r"""Gets the start_create_time of this ListUserJobRequest.

        开始创建时间。

        :return: The start_create_time of this ListUserJobRequest.
        :rtype: int
        """
        return self._start_create_time

    @start_create_time.setter
    def start_create_time(self, start_create_time):
        r"""Sets the start_create_time of this ListUserJobRequest.

        开始创建时间。

        :param start_create_time: The start_create_time of this ListUserJobRequest.
        :type start_create_time: int
        """
        self._start_create_time = start_create_time

    @property
    def end_create_time(self):
        r"""Gets the end_create_time of this ListUserJobRequest.

        结束创建时间。

        :return: The end_create_time of this ListUserJobRequest.
        :rtype: int
        """
        return self._end_create_time

    @end_create_time.setter
    def end_create_time(self, end_create_time):
        r"""Sets the end_create_time of this ListUserJobRequest.

        结束创建时间。

        :param end_create_time: The end_create_time of this ListUserJobRequest.
        :type end_create_time: int
        """
        self._end_create_time = end_create_time

    @property
    def start_finish_time(self):
        r"""Gets the start_finish_time of this ListUserJobRequest.

        开始完成时间。

        :return: The start_finish_time of this ListUserJobRequest.
        :rtype: int
        """
        return self._start_finish_time

    @start_finish_time.setter
    def start_finish_time(self, start_finish_time):
        r"""Sets the start_finish_time of this ListUserJobRequest.

        开始完成时间。

        :param start_finish_time: The start_finish_time of this ListUserJobRequest.
        :type start_finish_time: int
        """
        self._start_finish_time = start_finish_time

    @property
    def end_finish_time(self):
        r"""Gets the end_finish_time of this ListUserJobRequest.

        结束完成时间。

        :return: The end_finish_time of this ListUserJobRequest.
        :rtype: int
        """
        return self._end_finish_time

    @end_finish_time.setter
    def end_finish_time(self, end_finish_time):
        r"""Sets the end_finish_time of this ListUserJobRequest.

        结束完成时间。

        :param end_finish_time: The end_finish_time of this ListUserJobRequest.
        :type end_finish_time: int
        """
        self._end_finish_time = end_finish_time

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListUserJobRequest.

        排序规则，默认根据创建时间降序，支持create_time|finish_time。

        :return: The sort_key of this ListUserJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListUserJobRequest.

        排序规则，默认根据创建时间降序，支持create_time|finish_time。

        :param sort_key: The sort_key of this ListUserJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListUserJobRequest.

        排序规则，目前默认时间降序。

        :return: The sort_dir of this ListUserJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListUserJobRequest.

        排序规则，目前默认时间降序。

        :param sort_dir: The sort_dir of this ListUserJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListUserJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :return: The limit of this ListUserJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :param limit: The limit of this ListUserJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :return: The offset of this ListUserJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :param offset: The offset of this ListUserJobRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListUserJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
