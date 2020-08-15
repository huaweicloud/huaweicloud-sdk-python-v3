# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowJobStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job': 'Job',
        'ret_code': 'str',
        'ret_success': 'str'
    }

    attribute_map = {
        'job': 'job',
        'ret_code': 'retCode',
        'ret_success': 'retSuccess'
    }

    def __init__(self, job=None, ret_code=None, ret_success=None):
        """ShowJobStatusResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._job = None
        self._ret_code = None
        self._ret_success = None
        self.discriminator = None

        if job is not None:
            self.job = job
        if ret_code is not None:
            self.ret_code = ret_code
        if ret_success is not None:
            self.ret_success = ret_success

    @property
    def job(self):
        """Gets the job of this ShowJobStatusResponse.


        :return: The job of this ShowJobStatusResponse.
        :rtype: Job
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this ShowJobStatusResponse.


        :param job: The job of this ShowJobStatusResponse.
        :type: Job
        """
        self._job = job

    @property
    def ret_code(self):
        """Gets the ret_code of this ShowJobStatusResponse.

        任务返回码

        :return: The ret_code of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        """Sets the ret_code of this ShowJobStatusResponse.

        任务返回码

        :param ret_code: The ret_code of this ShowJobStatusResponse.
        :type: str
        """
        self._ret_code = ret_code

    @property
    def ret_success(self):
        """Gets the ret_success of this ShowJobStatusResponse.

        任务信息

        :return: The ret_success of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._ret_success

    @ret_success.setter
    def ret_success(self, ret_success):
        """Sets the ret_success of this ShowJobStatusResponse.

        任务信息

        :param ret_success: The ret_success of this ShowJobStatusResponse.
        :type: str
        """
        self._ret_success = ret_success

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
