# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'job_type': 'str',
        'job_name': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'job_type': 'jobType',
        'job_name': 'jobName',
        'tags': 'tags'
    }

    def __init__(self, workspace=None, limit=None, offset=None, job_type=None, job_name=None, tags=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param limit: 分页参数：每页限定数量
        :type limit: int
        :param offset: 分页参数：页数
        :type offset: int
        :param job_type: 作业类型:  - REAL_TIME: 实时处理   - BATCH: 批处理
        :type job_type: str
        :param job_name: 作业名称
        :type job_name: str
        :param tags: 作业标签
        :type tags: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._job_type = None
        self._job_name = None
        self._tags = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if job_type is not None:
            self.job_type = job_type
        if job_name is not None:
            self.job_name = job_name
        if tags is not None:
            self.tags = tags

    @property
    def workspace(self):
        """Gets the workspace of this ListJobsRequest.

        工作空间id

        :return: The workspace of this ListJobsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListJobsRequest.

        工作空间id

        :param workspace: The workspace of this ListJobsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListJobsRequest.

        分页参数：每页限定数量

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJobsRequest.

        分页参数：每页限定数量

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListJobsRequest.

        分页参数：页数

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJobsRequest.

        分页参数：页数

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsRequest.

        作业类型:  - REAL_TIME: 实时处理   - BATCH: 批处理

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsRequest.

        作业类型:  - REAL_TIME: 实时处理   - BATCH: 批处理

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_name(self):
        """Gets the job_name of this ListJobsRequest.

        作业名称

        :return: The job_name of this ListJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListJobsRequest.

        作业名称

        :param job_name: The job_name of this ListJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def tags(self):
        """Gets the tags of this ListJobsRequest.

        作业标签

        :return: The tags of this ListJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListJobsRequest.

        作业标签

        :param tags: The tags of this ListJobsRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
