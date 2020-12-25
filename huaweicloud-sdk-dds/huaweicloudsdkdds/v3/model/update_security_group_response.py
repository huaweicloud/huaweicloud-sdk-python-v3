# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateSecurityGroupResponse(SdkResponse):


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
        'security_group_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, job_id=None, security_group_id=None):
        """UpdateSecurityGroupResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._job_id = None
        self._security_group_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if security_group_id is not None:
            self.security_group_id = security_group_id

    @property
    def job_id(self):
        """Gets the job_id of this UpdateSecurityGroupResponse.

        任务ID。

        :return: The job_id of this UpdateSecurityGroupResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateSecurityGroupResponse.

        任务ID。

        :param job_id: The job_id of this UpdateSecurityGroupResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this UpdateSecurityGroupResponse.

        实例当前安全组。

        :return: The security_group_id of this UpdateSecurityGroupResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this UpdateSecurityGroupResponse.

        实例当前安全组。

        :param security_group_id: The security_group_id of this UpdateSecurityGroupResponse.
        :type: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, UpdateSecurityGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
