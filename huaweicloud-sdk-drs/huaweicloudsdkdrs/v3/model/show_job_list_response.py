# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'jobs': 'list[JobInfo]'
    }

    attribute_map = {
        'total_record': 'total_record',
        'jobs': 'jobs'
    }

    def __init__(self, total_record=None, jobs=None):
        """ShowJobListResponse

        The model defined in huaweicloud sdk

        :param total_record: 任务总数
        :type total_record: int
        :param jobs: 任务信息列表
        :type jobs: list[:class:`huaweicloudsdkdrs.v3.JobInfo`]
        """
        
        super(ShowJobListResponse, self).__init__()

        self._total_record = None
        self._jobs = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if jobs is not None:
            self.jobs = jobs

    @property
    def total_record(self):
        """Gets the total_record of this ShowJobListResponse.

        任务总数

        :return: The total_record of this ShowJobListResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ShowJobListResponse.

        任务总数

        :param total_record: The total_record of this ShowJobListResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def jobs(self):
        """Gets the jobs of this ShowJobListResponse.

        任务信息列表

        :return: The jobs of this ShowJobListResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.JobInfo`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ShowJobListResponse.

        任务信息列表

        :param jobs: The jobs of this ShowJobListResponse.
        :type jobs: list[:class:`huaweicloudsdkdrs.v3.JobInfo`]
        """
        self._jobs = jobs

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
        if not isinstance(other, ShowJobListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
