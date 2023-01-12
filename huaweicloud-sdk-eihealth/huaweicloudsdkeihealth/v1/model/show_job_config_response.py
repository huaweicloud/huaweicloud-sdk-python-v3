# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_retain_number': 'int'
    }

    attribute_map = {
        'job_retain_number': 'job_retain_number'
    }

    def __init__(self, job_retain_number=None):
        """ShowJobConfigResponse

        The model defined in huaweicloud sdk

        :param job_retain_number: 作业保存条数
        :type job_retain_number: int
        """
        
        super(ShowJobConfigResponse, self).__init__()

        self._job_retain_number = None
        self.discriminator = None

        if job_retain_number is not None:
            self.job_retain_number = job_retain_number

    @property
    def job_retain_number(self):
        """Gets the job_retain_number of this ShowJobConfigResponse.

        作业保存条数

        :return: The job_retain_number of this ShowJobConfigResponse.
        :rtype: int
        """
        return self._job_retain_number

    @job_retain_number.setter
    def job_retain_number(self, job_retain_number):
        """Sets the job_retain_number of this ShowJobConfigResponse.

        作业保存条数

        :param job_retain_number: The job_retain_number of this ShowJobConfigResponse.
        :type job_retain_number: int
        """
        self._job_retain_number = job_retain_number

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
        if not isinstance(other, ShowJobConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
