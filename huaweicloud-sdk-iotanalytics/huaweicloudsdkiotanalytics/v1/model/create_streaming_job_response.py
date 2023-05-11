# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStreamingJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'check_info': 'dict(str, object)'
    }

    attribute_map = {
        'job_id': 'job_id',
        'check_info': 'check_info'
    }

    def __init__(self, job_id=None, check_info=None):
        """CreateStreamingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: str
        :param check_info: 作业错误详情
        :type check_info: dict(str, object)
        """
        
        super(CreateStreamingJobResponse, self).__init__()

        self._job_id = None
        self._check_info = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if check_info is not None:
            self.check_info = check_info

    @property
    def job_id(self):
        """Gets the job_id of this CreateStreamingJobResponse.

        作业ID

        :return: The job_id of this CreateStreamingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateStreamingJobResponse.

        作业ID

        :param job_id: The job_id of this CreateStreamingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def check_info(self):
        """Gets the check_info of this CreateStreamingJobResponse.

        作业错误详情

        :return: The check_info of this CreateStreamingJobResponse.
        :rtype: dict(str, object)
        """
        return self._check_info

    @check_info.setter
    def check_info(self, check_info):
        """Sets the check_info of this CreateStreamingJobResponse.

        作业错误详情

        :param check_info: The check_info of this CreateStreamingJobResponse.
        :type check_info: dict(str, object)
        """
        self._check_info = check_info

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
        if not isinstance(other, CreateStreamingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
