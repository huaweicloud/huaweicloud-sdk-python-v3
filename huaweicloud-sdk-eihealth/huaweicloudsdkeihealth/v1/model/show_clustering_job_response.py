# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusteringJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'DrugJobDto',
        'file': 'DrugFile',
        'failed_reasons': 'list[FailedReasonRecord]',
        'job_result': 'JobResult'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'file': 'file',
        'failed_reasons': 'failed_reasons',
        'job_result': 'job_result'
    }

    def __init__(self, basic_info=None, file=None, failed_reasons=None, job_result=None):
        r"""ShowClusteringJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param failed_reasons: 部分失败原因和数量。
        :type failed_reasons: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        
        super(ShowClusteringJobResponse, self).__init__()

        self._basic_info = None
        self._file = None
        self._failed_reasons = None
        self._job_result = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if file is not None:
            self.file = file
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons
        if job_result is not None:
            self.job_result = job_result

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowClusteringJobResponse.

        :return: The basic_info of this ShowClusteringJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowClusteringJobResponse.

        :param basic_info: The basic_info of this ShowClusteringJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def file(self):
        r"""Gets the file of this ShowClusteringJobResponse.

        :return: The file of this ShowClusteringJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ShowClusteringJobResponse.

        :param file: The file of this ShowClusteringJobResponse.
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._file = file

    @property
    def failed_reasons(self):
        r"""Gets the failed_reasons of this ShowClusteringJobResponse.

        部分失败原因和数量。

        :return: The failed_reasons of this ShowClusteringJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        r"""Sets the failed_reasons of this ShowClusteringJobResponse.

        部分失败原因和数量。

        :param failed_reasons: The failed_reasons of this ShowClusteringJobResponse.
        :type failed_reasons: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._failed_reasons = failed_reasons

    @property
    def job_result(self):
        r"""Gets the job_result of this ShowClusteringJobResponse.

        :return: The job_result of this ShowClusteringJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this ShowClusteringJobResponse.

        :param job_result: The job_result of this ShowClusteringJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

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
        if not isinstance(other, ShowClusteringJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
