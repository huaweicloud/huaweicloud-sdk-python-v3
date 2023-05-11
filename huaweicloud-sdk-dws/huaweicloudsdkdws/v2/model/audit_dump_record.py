# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditDumpRecord:

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
        'exector_time': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'bucket_name': 'str',
        'location_prefix': 'str',
        'result': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'exector_time': 'exector_time',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'bucket_name': 'bucket_name',
        'location_prefix': 'location_prefix',
        'result': 'result',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, cluster_id=None, exector_time=None, begin_time=None, end_time=None, bucket_name=None, location_prefix=None, result=None, failed_reason=None):
        """AuditDumpRecord

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id。
        :type cluster_id: str
        :param exector_time: 执行时间。
        :type exector_time: str
        :param begin_time: 开始时间。
        :type begin_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param bucket_name: 桶名。
        :type bucket_name: str
        :param location_prefix: 前缀。
        :type location_prefix: str
        :param result: 结果。
        :type result: str
        :param failed_reason: 失败原因。
        :type failed_reason: str
        """
        
        

        self._cluster_id = None
        self._exector_time = None
        self._begin_time = None
        self._end_time = None
        self._bucket_name = None
        self._location_prefix = None
        self._result = None
        self._failed_reason = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if exector_time is not None:
            self.exector_time = exector_time
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if location_prefix is not None:
            self.location_prefix = location_prefix
        if result is not None:
            self.result = result
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AuditDumpRecord.

        集群id。

        :return: The cluster_id of this AuditDumpRecord.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AuditDumpRecord.

        集群id。

        :param cluster_id: The cluster_id of this AuditDumpRecord.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def exector_time(self):
        """Gets the exector_time of this AuditDumpRecord.

        执行时间。

        :return: The exector_time of this AuditDumpRecord.
        :rtype: str
        """
        return self._exector_time

    @exector_time.setter
    def exector_time(self, exector_time):
        """Sets the exector_time of this AuditDumpRecord.

        执行时间。

        :param exector_time: The exector_time of this AuditDumpRecord.
        :type exector_time: str
        """
        self._exector_time = exector_time

    @property
    def begin_time(self):
        """Gets the begin_time of this AuditDumpRecord.

        开始时间。

        :return: The begin_time of this AuditDumpRecord.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this AuditDumpRecord.

        开始时间。

        :param begin_time: The begin_time of this AuditDumpRecord.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this AuditDumpRecord.

        结束时间。

        :return: The end_time of this AuditDumpRecord.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AuditDumpRecord.

        结束时间。

        :param end_time: The end_time of this AuditDumpRecord.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def bucket_name(self):
        """Gets the bucket_name of this AuditDumpRecord.

        桶名。

        :return: The bucket_name of this AuditDumpRecord.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this AuditDumpRecord.

        桶名。

        :param bucket_name: The bucket_name of this AuditDumpRecord.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def location_prefix(self):
        """Gets the location_prefix of this AuditDumpRecord.

        前缀。

        :return: The location_prefix of this AuditDumpRecord.
        :rtype: str
        """
        return self._location_prefix

    @location_prefix.setter
    def location_prefix(self, location_prefix):
        """Sets the location_prefix of this AuditDumpRecord.

        前缀。

        :param location_prefix: The location_prefix of this AuditDumpRecord.
        :type location_prefix: str
        """
        self._location_prefix = location_prefix

    @property
    def result(self):
        """Gets the result of this AuditDumpRecord.

        结果。

        :return: The result of this AuditDumpRecord.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AuditDumpRecord.

        结果。

        :param result: The result of this AuditDumpRecord.
        :type result: str
        """
        self._result = result

    @property
    def failed_reason(self):
        """Gets the failed_reason of this AuditDumpRecord.

        失败原因。

        :return: The failed_reason of this AuditDumpRecord.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this AuditDumpRecord.

        失败原因。

        :param failed_reason: The failed_reason of this AuditDumpRecord.
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
        if not isinstance(other, AuditDumpRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
