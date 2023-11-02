# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterUpdateRecordResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'status': 'str',
        'record_type': 'str',
        'from_version': 'str',
        'to_version': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'job_id': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'status': 'status',
        'record_type': 'record_type',
        'from_version': 'from_version',
        'to_version': 'to_version',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'job_id': 'job_id',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, item_id=None, status=None, record_type=None, from_version=None, to_version=None, start_time=None, end_time=None, job_id=None, failed_reason=None):
        """ClusterUpdateRecordResp

        The model defined in huaweicloud sdk

        :param item_id: 升级项目ID
        :type item_id: str
        :param status: 升级状态
        :type status: str
        :param record_type: 升级类型
        :type record_type: str
        :param from_version: 升级前版本
        :type from_version: str
        :param to_version: 目标版本
        :type to_version: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param job_id: 升级任务ID
        :type job_id: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        

        self._item_id = None
        self._status = None
        self._record_type = None
        self._from_version = None
        self._to_version = None
        self._start_time = None
        self._end_time = None
        self._job_id = None
        self._failed_reason = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if status is not None:
            self.status = status
        if record_type is not None:
            self.record_type = record_type
        if from_version is not None:
            self.from_version = from_version
        if to_version is not None:
            self.to_version = to_version
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if job_id is not None:
            self.job_id = job_id
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def item_id(self):
        """Gets the item_id of this ClusterUpdateRecordResp.

        升级项目ID

        :return: The item_id of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ClusterUpdateRecordResp.

        升级项目ID

        :param item_id: The item_id of this ClusterUpdateRecordResp.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def status(self):
        """Gets the status of this ClusterUpdateRecordResp.

        升级状态

        :return: The status of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterUpdateRecordResp.

        升级状态

        :param status: The status of this ClusterUpdateRecordResp.
        :type status: str
        """
        self._status = status

    @property
    def record_type(self):
        """Gets the record_type of this ClusterUpdateRecordResp.

        升级类型

        :return: The record_type of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this ClusterUpdateRecordResp.

        升级类型

        :param record_type: The record_type of this ClusterUpdateRecordResp.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def from_version(self):
        """Gets the from_version of this ClusterUpdateRecordResp.

        升级前版本

        :return: The from_version of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._from_version

    @from_version.setter
    def from_version(self, from_version):
        """Sets the from_version of this ClusterUpdateRecordResp.

        升级前版本

        :param from_version: The from_version of this ClusterUpdateRecordResp.
        :type from_version: str
        """
        self._from_version = from_version

    @property
    def to_version(self):
        """Gets the to_version of this ClusterUpdateRecordResp.

        目标版本

        :return: The to_version of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        """Sets the to_version of this ClusterUpdateRecordResp.

        目标版本

        :param to_version: The to_version of this ClusterUpdateRecordResp.
        :type to_version: str
        """
        self._to_version = to_version

    @property
    def start_time(self):
        """Gets the start_time of this ClusterUpdateRecordResp.

        开始时间

        :return: The start_time of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ClusterUpdateRecordResp.

        开始时间

        :param start_time: The start_time of this ClusterUpdateRecordResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ClusterUpdateRecordResp.

        结束时间

        :return: The end_time of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ClusterUpdateRecordResp.

        结束时间

        :param end_time: The end_time of this ClusterUpdateRecordResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        """Gets the job_id of this ClusterUpdateRecordResp.

        升级任务ID

        :return: The job_id of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ClusterUpdateRecordResp.

        升级任务ID

        :param job_id: The job_id of this ClusterUpdateRecordResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ClusterUpdateRecordResp.

        失败原因

        :return: The failed_reason of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ClusterUpdateRecordResp.

        失败原因

        :param failed_reason: The failed_reason of this ClusterUpdateRecordResp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, ClusterUpdateRecordResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
