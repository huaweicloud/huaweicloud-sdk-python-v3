# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRecordListVoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_update_records': 'list[JobUpdateRecordListVoResultJobUpdateRecords]',
        'total': 'int'
    }

    attribute_map = {
        'job_update_records': 'job_update_records',
        'total': 'total'
    }

    def __init__(self, job_update_records=None, total=None):
        r"""JobUpdateRecordListVoResult

        The model defined in huaweicloud sdk

        :param job_update_records: job_update_records
        :type job_update_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResultJobUpdateRecords`]
        :param total: 总数
        :type total: int
        """
        
        

        self._job_update_records = None
        self._total = None
        self.discriminator = None

        if job_update_records is not None:
            self.job_update_records = job_update_records
        if total is not None:
            self.total = total

    @property
    def job_update_records(self):
        r"""Gets the job_update_records of this JobUpdateRecordListVoResult.

        job_update_records

        :return: The job_update_records of this JobUpdateRecordListVoResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResultJobUpdateRecords`]
        """
        return self._job_update_records

    @job_update_records.setter
    def job_update_records(self, job_update_records):
        r"""Sets the job_update_records of this JobUpdateRecordListVoResult.

        job_update_records

        :param job_update_records: The job_update_records of this JobUpdateRecordListVoResult.
        :type job_update_records: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResultJobUpdateRecords`]
        """
        self._job_update_records = job_update_records

    @property
    def total(self):
        r"""Gets the total of this JobUpdateRecordListVoResult.

        总数

        :return: The total of this JobUpdateRecordListVoResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this JobUpdateRecordListVoResult.

        总数

        :param total: The total of this JobUpdateRecordListVoResult.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, JobUpdateRecordListVoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
