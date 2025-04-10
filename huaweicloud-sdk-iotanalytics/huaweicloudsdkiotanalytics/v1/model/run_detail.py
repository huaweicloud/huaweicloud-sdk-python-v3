# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail_id': 'str',
        'status': 'str',
        'sql_job': 'SqlJobRunDetail'
    }

    attribute_map = {
        'detail_id': 'detail_id',
        'status': 'status',
        'sql_job': 'sql_job'
    }

    def __init__(self, detail_id=None, status=None, sql_job=None):
        r"""RunDetail

        The model defined in huaweicloud sdk

        :param detail_id: 作业运行详情ID。
        :type detail_id: str
        :param status: 此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。
        :type status: str
        :param sql_job: 
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunDetail`
        """
        
        

        self._detail_id = None
        self._status = None
        self._sql_job = None
        self.discriminator = None

        self.detail_id = detail_id
        if status is not None:
            self.status = status
        if sql_job is not None:
            self.sql_job = sql_job

    @property
    def detail_id(self):
        r"""Gets the detail_id of this RunDetail.

        作业运行详情ID。

        :return: The detail_id of this RunDetail.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        r"""Sets the detail_id of this RunDetail.

        作业运行详情ID。

        :param detail_id: The detail_id of this RunDetail.
        :type detail_id: str
        """
        self._detail_id = detail_id

    @property
    def status(self):
        r"""Gets the status of this RunDetail.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :return: The status of this RunDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RunDetail.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :param status: The status of this RunDetail.
        :type status: str
        """
        self._status = status

    @property
    def sql_job(self):
        r"""Gets the sql_job of this RunDetail.

        :return: The sql_job of this RunDetail.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunDetail`
        """
        return self._sql_job

    @sql_job.setter
    def sql_job(self, sql_job):
        r"""Sets the sql_job of this RunDetail.

        :param sql_job: The sql_job of this RunDetail.
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunDetail`
        """
        self._sql_job = sql_job

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
        if not isinstance(other, RunDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
