# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterLogRecord:


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
        'cluster_id': 'str',
        'create_at': 'str',
        'log_path': 'str',
        'status': 'str',
        'finished_at': 'int',
        'job_types': 'str',
        'failed_msg': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'clusterId',
        'create_at': 'createAt',
        'log_path': 'logPath',
        'status': 'status',
        'finished_at': 'finishedAt',
        'job_types': 'jobTypes',
        'failed_msg': 'failedMsg',
        'job_id': 'jobId'
    }

    def __init__(self, id=None, cluster_id=None, create_at=None, log_path=None, status=None, finished_at=None, job_types=None, failed_msg=None, job_id=None):
        """ClusterLogRecord - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._cluster_id = None
        self._create_at = None
        self._log_path = None
        self._status = None
        self._finished_at = None
        self._job_types = None
        self._failed_msg = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if create_at is not None:
            self.create_at = create_at
        if log_path is not None:
            self.log_path = log_path
        if status is not None:
            self.status = status
        if finished_at is not None:
            self.finished_at = finished_at
        if job_types is not None:
            self.job_types = job_types
        if failed_msg is not None:
            self.failed_msg = failed_msg
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        """Gets the id of this ClusterLogRecord.

        日志任务ID，通过系统uuid生成。

        :return: The id of this ClusterLogRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterLogRecord.

        日志任务ID，通过系统uuid生成。

        :param id: The id of this ClusterLogRecord.
        :type: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterLogRecord.

        集群ID。

        :return: The cluster_id of this ClusterLogRecord.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterLogRecord.

        集群ID。

        :param cluster_id: The cluster_id of this ClusterLogRecord.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def create_at(self):
        """Gets the create_at of this ClusterLogRecord.

        创建时间。

        :return: The create_at of this ClusterLogRecord.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ClusterLogRecord.

        创建时间。

        :param create_at: The create_at of this ClusterLogRecord.
        :type: str
        """
        self._create_at = create_at

    @property
    def log_path(self):
        """Gets the log_path of this ClusterLogRecord.

        备份路径。

        :return: The log_path of this ClusterLogRecord.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this ClusterLogRecord.

        备份路径。

        :param log_path: The log_path of this ClusterLogRecord.
        :type: str
        """
        self._log_path = log_path

    @property
    def status(self):
        """Gets the status of this ClusterLogRecord.

        任务状态。

        :return: The status of this ClusterLogRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterLogRecord.

        任务状态。

        :param status: The status of this ClusterLogRecord.
        :type: str
        """
        self._status = status

    @property
    def finished_at(self):
        """Gets the finished_at of this ClusterLogRecord.

        结束时间。

        :return: The finished_at of this ClusterLogRecord.
        :rtype: int
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ClusterLogRecord.

        结束时间。

        :param finished_at: The finished_at of this ClusterLogRecord.
        :type: int
        """
        self._finished_at = finished_at

    @property
    def job_types(self):
        """Gets the job_types of this ClusterLogRecord.

        任务类型。

        :return: The job_types of this ClusterLogRecord.
        :rtype: str
        """
        return self._job_types

    @job_types.setter
    def job_types(self, job_types):
        """Sets the job_types of this ClusterLogRecord.

        任务类型。

        :param job_types: The job_types of this ClusterLogRecord.
        :type: str
        """
        self._job_types = job_types

    @property
    def failed_msg(self):
        """Gets the failed_msg of this ClusterLogRecord.

        错误信息。

        :return: The failed_msg of this ClusterLogRecord.
        :rtype: str
        """
        return self._failed_msg

    @failed_msg.setter
    def failed_msg(self, failed_msg):
        """Sets the failed_msg of this ClusterLogRecord.

        错误信息。

        :param failed_msg: The failed_msg of this ClusterLogRecord.
        :type: str
        """
        self._failed_msg = failed_msg

    @property
    def job_id(self):
        """Gets the job_id of this ClusterLogRecord.

        任务ID。

        :return: The job_id of this ClusterLogRecord.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ClusterLogRecord.

        任务ID。

        :param job_id: The job_id of this ClusterLogRecord.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ClusterLogRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
