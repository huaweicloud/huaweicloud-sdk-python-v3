# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'job_name': 'str',
        'filter': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'job_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'job_name': 'job_name',
        'filter': 'filter',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'job_type': 'jobType'
    }

    def __init__(self, cluster_id=None, job_name=None, filter=None, page_no=None, page_size=None, job_type=None):
        """ShowJobsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param job_name: 查询多个作业用all,查询单个作业输入作业名
        :type job_name: str
        :param filter: 当“job_name”为“all”时，此参数用于模糊过滤作业
        :type filter: str
        :param page_no: 指定作业页号
        :type page_no: int
        :param page_size: 每页作业数，值在10-100之间
        :type page_size: int
        :param job_type: 作业类型: - jobType&#x3D;NORMAL_JOB：表示查询表/文件迁移的作业。 - jobType&#x3D;BATCH_JOB：表示查询整库迁移的作业。 - jobType&#x3D;SCENARIO_JOB：表示查询场景迁移的作业。 - 不指定该参数时，默认只查询表/文件迁移的作业。
        :type job_type: str
        """
        
        

        self._cluster_id = None
        self._job_name = None
        self._filter = None
        self._page_no = None
        self._page_size = None
        self._job_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.job_name = job_name
        if filter is not None:
            self.filter = filter
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if job_type is not None:
            self.job_type = job_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowJobsRequest.

        集群ID

        :return: The cluster_id of this ShowJobsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowJobsRequest.

        集群ID

        :param cluster_id: The cluster_id of this ShowJobsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def job_name(self):
        """Gets the job_name of this ShowJobsRequest.

        查询多个作业用all,查询单个作业输入作业名

        :return: The job_name of this ShowJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowJobsRequest.

        查询多个作业用all,查询单个作业输入作业名

        :param job_name: The job_name of this ShowJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def filter(self):
        """Gets the filter of this ShowJobsRequest.

        当“job_name”为“all”时，此参数用于模糊过滤作业

        :return: The filter of this ShowJobsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ShowJobsRequest.

        当“job_name”为“all”时，此参数用于模糊过滤作业

        :param filter: The filter of this ShowJobsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def page_no(self):
        """Gets the page_no of this ShowJobsRequest.

        指定作业页号

        :return: The page_no of this ShowJobsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ShowJobsRequest.

        指定作业页号

        :param page_no: The page_no of this ShowJobsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ShowJobsRequest.

        每页作业数，值在10-100之间

        :return: The page_size of this ShowJobsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowJobsRequest.

        每页作业数，值在10-100之间

        :param page_size: The page_size of this ShowJobsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobsRequest.

        作业类型: - jobType=NORMAL_JOB：表示查询表/文件迁移的作业。 - jobType=BATCH_JOB：表示查询整库迁移的作业。 - jobType=SCENARIO_JOB：表示查询场景迁移的作业。 - 不指定该参数时，默认只查询表/文件迁移的作业。

        :return: The job_type of this ShowJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobsRequest.

        作业类型: - jobType=NORMAL_JOB：表示查询表/文件迁移的作业。 - jobType=BATCH_JOB：表示查询整库迁移的作业。 - jobType=SCENARIO_JOB：表示查询场景迁移的作业。 - 不指定该参数时，默认只查询表/文件迁移的作业。

        :param job_type: The job_type of this ShowJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

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
        if not isinstance(other, ShowJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
