# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserDrugJobRequest:

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
        'labels': 'list[str]',
        'status_list': 'list[str]',
        'types': 'list[str]',
        'create_start_time': 'int',
        'create_end_time': 'int',
        'finish_start_time': 'int',
        'finish_end_time': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'is_creator': 'is_creator',
        'job_name': 'job_name',
        'eihealth_project_names': 'eihealth_project_names',
        'labels': 'labels',
        'status_list': 'status_list',
        'types': 'types',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'finish_start_time': 'finish_start_time',
        'finish_end_time': 'finish_end_time',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, is_creator=None, job_name=None, eihealth_project_names=None, labels=None, status_list=None, types=None, create_start_time=None, create_end_time=None, finish_start_time=None, finish_end_time=None, sort_dir=None, sort_key=None, limit=None, offset=None):
        r"""ListUserDrugJobRequest

        The model defined in huaweicloud sdk

        :param is_creator: 是否仅展示本人创建资源。
        :type is_creator: bool
        :param job_name: 作业名称。
        :type job_name: str
        :param eihealth_project_names: 空间名称列表，多个值之间使用逗号分隔。
        :type eihealth_project_names: list[str]
        :param labels: 标签列表。
        :type labels: list[str]
        :param status_list: 作业运行状态列表，支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED。
        :type status_list: list[str]
        :param types: 作业类型列表，支持DOCKING|OPTIMIZATION|ADMET|POC_MOL_DESIGN|SEARCH|GENERATION|CPI|FEP|POCKET_DETECTION|TARGET_OPT|CLUSTERING。
        :type types: list[str]
        :param create_start_time: 最小创建时间。
        :type create_start_time: int
        :param create_end_time: 最大创建时间。
        :type create_end_time: int
        :param finish_start_time: 最小结束时间。
        :type finish_start_time: int
        :param finish_end_time: 最大结束时间。
        :type finish_end_time: int
        :param sort_dir: 排序规则，目前默认时间降序。
        :type sort_dir: str
        :param sort_key: 排序规则，目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序。
        :type sort_key: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。
        :type offset: int
        """
        
        

        self._is_creator = None
        self._job_name = None
        self._eihealth_project_names = None
        self._labels = None
        self._status_list = None
        self._types = None
        self._create_start_time = None
        self._create_end_time = None
        self._finish_start_time = None
        self._finish_end_time = None
        self._sort_dir = None
        self._sort_key = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if is_creator is not None:
            self.is_creator = is_creator
        if job_name is not None:
            self.job_name = job_name
        if eihealth_project_names is not None:
            self.eihealth_project_names = eihealth_project_names
        if labels is not None:
            self.labels = labels
        if status_list is not None:
            self.status_list = status_list
        if types is not None:
            self.types = types
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if finish_start_time is not None:
            self.finish_start_time = finish_start_time
        if finish_end_time is not None:
            self.finish_end_time = finish_end_time
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def is_creator(self):
        r"""Gets the is_creator of this ListUserDrugJobRequest.

        是否仅展示本人创建资源。

        :return: The is_creator of this ListUserDrugJobRequest.
        :rtype: bool
        """
        return self._is_creator

    @is_creator.setter
    def is_creator(self, is_creator):
        r"""Sets the is_creator of this ListUserDrugJobRequest.

        是否仅展示本人创建资源。

        :param is_creator: The is_creator of this ListUserDrugJobRequest.
        :type is_creator: bool
        """
        self._is_creator = is_creator

    @property
    def job_name(self):
        r"""Gets the job_name of this ListUserDrugJobRequest.

        作业名称。

        :return: The job_name of this ListUserDrugJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListUserDrugJobRequest.

        作业名称。

        :param job_name: The job_name of this ListUserDrugJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def eihealth_project_names(self):
        r"""Gets the eihealth_project_names of this ListUserDrugJobRequest.

        空间名称列表，多个值之间使用逗号分隔。

        :return: The eihealth_project_names of this ListUserDrugJobRequest.
        :rtype: list[str]
        """
        return self._eihealth_project_names

    @eihealth_project_names.setter
    def eihealth_project_names(self, eihealth_project_names):
        r"""Sets the eihealth_project_names of this ListUserDrugJobRequest.

        空间名称列表，多个值之间使用逗号分隔。

        :param eihealth_project_names: The eihealth_project_names of this ListUserDrugJobRequest.
        :type eihealth_project_names: list[str]
        """
        self._eihealth_project_names = eihealth_project_names

    @property
    def labels(self):
        r"""Gets the labels of this ListUserDrugJobRequest.

        标签列表。

        :return: The labels of this ListUserDrugJobRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListUserDrugJobRequest.

        标签列表。

        :param labels: The labels of this ListUserDrugJobRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status_list(self):
        r"""Gets the status_list of this ListUserDrugJobRequest.

        作业运行状态列表，支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED。

        :return: The status_list of this ListUserDrugJobRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListUserDrugJobRequest.

        作业运行状态列表，支持WAITING|RUNNING|FINISHED|FAILED|CANCELLED。

        :param status_list: The status_list of this ListUserDrugJobRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def types(self):
        r"""Gets the types of this ListUserDrugJobRequest.

        作业类型列表，支持DOCKING|OPTIMIZATION|ADMET|POC_MOL_DESIGN|SEARCH|GENERATION|CPI|FEP|POCKET_DETECTION|TARGET_OPT|CLUSTERING。

        :return: The types of this ListUserDrugJobRequest.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        r"""Sets the types of this ListUserDrugJobRequest.

        作业类型列表，支持DOCKING|OPTIMIZATION|ADMET|POC_MOL_DESIGN|SEARCH|GENERATION|CPI|FEP|POCKET_DETECTION|TARGET_OPT|CLUSTERING。

        :param types: The types of this ListUserDrugJobRequest.
        :type types: list[str]
        """
        self._types = types

    @property
    def create_start_time(self):
        r"""Gets the create_start_time of this ListUserDrugJobRequest.

        最小创建时间。

        :return: The create_start_time of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        r"""Sets the create_start_time of this ListUserDrugJobRequest.

        最小创建时间。

        :param create_start_time: The create_start_time of this ListUserDrugJobRequest.
        :type create_start_time: int
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        r"""Gets the create_end_time of this ListUserDrugJobRequest.

        最大创建时间。

        :return: The create_end_time of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        r"""Sets the create_end_time of this ListUserDrugJobRequest.

        最大创建时间。

        :param create_end_time: The create_end_time of this ListUserDrugJobRequest.
        :type create_end_time: int
        """
        self._create_end_time = create_end_time

    @property
    def finish_start_time(self):
        r"""Gets the finish_start_time of this ListUserDrugJobRequest.

        最小结束时间。

        :return: The finish_start_time of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._finish_start_time

    @finish_start_time.setter
    def finish_start_time(self, finish_start_time):
        r"""Sets the finish_start_time of this ListUserDrugJobRequest.

        最小结束时间。

        :param finish_start_time: The finish_start_time of this ListUserDrugJobRequest.
        :type finish_start_time: int
        """
        self._finish_start_time = finish_start_time

    @property
    def finish_end_time(self):
        r"""Gets the finish_end_time of this ListUserDrugJobRequest.

        最大结束时间。

        :return: The finish_end_time of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._finish_end_time

    @finish_end_time.setter
    def finish_end_time(self, finish_end_time):
        r"""Sets the finish_end_time of this ListUserDrugJobRequest.

        最大结束时间。

        :param finish_end_time: The finish_end_time of this ListUserDrugJobRequest.
        :type finish_end_time: int
        """
        self._finish_end_time = finish_end_time

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListUserDrugJobRequest.

        排序规则，目前默认时间降序。

        :return: The sort_dir of this ListUserDrugJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListUserDrugJobRequest.

        排序规则，目前默认时间降序。

        :param sort_dir: The sort_dir of this ListUserDrugJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListUserDrugJobRequest.

        排序规则，目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序。

        :return: The sort_key of this ListUserDrugJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListUserDrugJobRequest.

        排序规则，目前默认时间降序，支持根据create_time|finish_time|running_time|total_time排序。

        :param sort_key: The sort_key of this ListUserDrugJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListUserDrugJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :return: The limit of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserDrugJobRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :param limit: The limit of this ListUserDrugJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserDrugJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :return: The offset of this ListUserDrugJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserDrugJobRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :param offset: The offset of this ListUserDrugJobRequest.
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
        if not isinstance(other, ListUserDrugJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
