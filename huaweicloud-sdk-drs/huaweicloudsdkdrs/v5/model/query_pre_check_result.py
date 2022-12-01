# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryPreCheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'process': 'str',
        'total_passed_rate': 'str',
        'rds_instance_id': 'str',
        'job_direction': 'str',
        'precheck_results': 'list[PrecheckResult]'
    }

    attribute_map = {
        'result': 'result',
        'process': 'process',
        'total_passed_rate': 'total_passed_rate',
        'rds_instance_id': 'rds_instance_id',
        'job_direction': 'job_direction',
        'precheck_results': 'precheck_results'
    }

    def __init__(self, result=None, process=None, total_passed_rate=None, rds_instance_id=None, job_direction=None, precheck_results=None):
        """QueryPreCheckResult

        The model defined in huaweicloud sdk

        :param result: 返回的预检查结果是否通过。
        :type result: bool
        :param process: 预检查进度百分比。
        :type process: str
        :param total_passed_rate: 预检查通过百分比。
        :type total_passed_rate: str
        :param rds_instance_id: 数据库实例ID。
        :type rds_instance_id: str
        :param job_direction: 迁移方向。
        :type job_direction: str
        :param precheck_results: 预检查各项结果。
        :type precheck_results: list[:class:`huaweicloudsdkdrs.v5.PrecheckResult`]
        """
        
        

        self._result = None
        self._process = None
        self._total_passed_rate = None
        self._rds_instance_id = None
        self._job_direction = None
        self._precheck_results = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if process is not None:
            self.process = process
        if total_passed_rate is not None:
            self.total_passed_rate = total_passed_rate
        if rds_instance_id is not None:
            self.rds_instance_id = rds_instance_id
        if job_direction is not None:
            self.job_direction = job_direction
        if precheck_results is not None:
            self.precheck_results = precheck_results

    @property
    def result(self):
        """Gets the result of this QueryPreCheckResult.

        返回的预检查结果是否通过。

        :return: The result of this QueryPreCheckResult.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QueryPreCheckResult.

        返回的预检查结果是否通过。

        :param result: The result of this QueryPreCheckResult.
        :type result: bool
        """
        self._result = result

    @property
    def process(self):
        """Gets the process of this QueryPreCheckResult.

        预检查进度百分比。

        :return: The process of this QueryPreCheckResult.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this QueryPreCheckResult.

        预检查进度百分比。

        :param process: The process of this QueryPreCheckResult.
        :type process: str
        """
        self._process = process

    @property
    def total_passed_rate(self):
        """Gets the total_passed_rate of this QueryPreCheckResult.

        预检查通过百分比。

        :return: The total_passed_rate of this QueryPreCheckResult.
        :rtype: str
        """
        return self._total_passed_rate

    @total_passed_rate.setter
    def total_passed_rate(self, total_passed_rate):
        """Sets the total_passed_rate of this QueryPreCheckResult.

        预检查通过百分比。

        :param total_passed_rate: The total_passed_rate of this QueryPreCheckResult.
        :type total_passed_rate: str
        """
        self._total_passed_rate = total_passed_rate

    @property
    def rds_instance_id(self):
        """Gets the rds_instance_id of this QueryPreCheckResult.

        数据库实例ID。

        :return: The rds_instance_id of this QueryPreCheckResult.
        :rtype: str
        """
        return self._rds_instance_id

    @rds_instance_id.setter
    def rds_instance_id(self, rds_instance_id):
        """Sets the rds_instance_id of this QueryPreCheckResult.

        数据库实例ID。

        :param rds_instance_id: The rds_instance_id of this QueryPreCheckResult.
        :type rds_instance_id: str
        """
        self._rds_instance_id = rds_instance_id

    @property
    def job_direction(self):
        """Gets the job_direction of this QueryPreCheckResult.

        迁移方向。

        :return: The job_direction of this QueryPreCheckResult.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this QueryPreCheckResult.

        迁移方向。

        :param job_direction: The job_direction of this QueryPreCheckResult.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def precheck_results(self):
        """Gets the precheck_results of this QueryPreCheckResult.

        预检查各项结果。

        :return: The precheck_results of this QueryPreCheckResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.PrecheckResult`]
        """
        return self._precheck_results

    @precheck_results.setter
    def precheck_results(self, precheck_results):
        """Sets the precheck_results of this QueryPreCheckResult.

        预检查各项结果。

        :param precheck_results: The precheck_results of this QueryPreCheckResult.
        :type precheck_results: list[:class:`huaweicloudsdkdrs.v5.PrecheckResult`]
        """
        self._precheck_results = precheck_results

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
        if not isinstance(other, QueryPreCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
