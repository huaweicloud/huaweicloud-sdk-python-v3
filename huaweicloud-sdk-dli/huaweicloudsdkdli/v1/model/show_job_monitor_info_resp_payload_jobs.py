# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobMonitorInfoRespPayloadJobs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'metrics': 'ShowJobMonitorInfoRespPayloadJobsMetrics'
    }

    attribute_map = {
        'job_id': 'job_id',
        'metrics': 'metrics'
    }

    def __init__(self, job_id=None, metrics=None):
        """ShowJobMonitorInfoRespPayloadJobs

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: int
        :param metrics: 
        :type metrics: :class:`huaweicloudsdkdli.v1.ShowJobMonitorInfoRespPayloadJobsMetrics`
        """
        
        

        self._job_id = None
        self._metrics = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if metrics is not None:
            self.metrics = metrics

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobMonitorInfoRespPayloadJobs.

        作业ID。

        :return: The job_id of this ShowJobMonitorInfoRespPayloadJobs.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobMonitorInfoRespPayloadJobs.

        作业ID。

        :param job_id: The job_id of this ShowJobMonitorInfoRespPayloadJobs.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def metrics(self):
        """Gets the metrics of this ShowJobMonitorInfoRespPayloadJobs.

        :return: The metrics of this ShowJobMonitorInfoRespPayloadJobs.
        :rtype: :class:`huaweicloudsdkdli.v1.ShowJobMonitorInfoRespPayloadJobsMetrics`
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowJobMonitorInfoRespPayloadJobs.

        :param metrics: The metrics of this ShowJobMonitorInfoRespPayloadJobs.
        :type metrics: :class:`huaweicloudsdkdli.v1.ShowJobMonitorInfoRespPayloadJobsMetrics`
        """
        self._metrics = metrics

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
        if not isinstance(other, ShowJobMonitorInfoRespPayloadJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
