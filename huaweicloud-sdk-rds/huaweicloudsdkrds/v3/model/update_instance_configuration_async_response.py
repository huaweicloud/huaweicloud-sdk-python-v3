# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceConfigurationAsyncResponse(SdkResponse):


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
        'restart_required': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'restart_required': 'restart_required'
    }

    def __init__(self, job_id=None, restart_required=None):
        """UpdateInstanceConfigurationAsyncResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateInstanceConfigurationAsyncResponse, self).__init__()

        self._job_id = None
        self._restart_required = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if restart_required is not None:
            self.restart_required = restart_required

    @property
    def job_id(self):
        """Gets the job_id of this UpdateInstanceConfigurationAsyncResponse.

        任务流id

        :return: The job_id of this UpdateInstanceConfigurationAsyncResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateInstanceConfigurationAsyncResponse.

        任务流id

        :param job_id: The job_id of this UpdateInstanceConfigurationAsyncResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def restart_required(self):
        """Gets the restart_required of this UpdateInstanceConfigurationAsyncResponse.

        实例是否需要重启。 - “true”需要重启。 - “false”不需要重启。

        :return: The restart_required of this UpdateInstanceConfigurationAsyncResponse.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        """Sets the restart_required of this UpdateInstanceConfigurationAsyncResponse.

        实例是否需要重启。 - “true”需要重启。 - “false”不需要重启。

        :param restart_required: The restart_required of this UpdateInstanceConfigurationAsyncResponse.
        :type: bool
        """
        self._restart_required = restart_required

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
        if not isinstance(other, UpdateInstanceConfigurationAsyncResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other