# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSslResponse(SdkResponse):

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
        'ssl_option': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'ssl_option': 'ssl_option'
    }

    def __init__(self, job_id=None, ssl_option=None):
        """SwitchSslResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param ssl_option: SSL开关状态。
        :type ssl_option: str
        """
        
        super(SwitchSslResponse, self).__init__()

        self._job_id = None
        self._ssl_option = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if ssl_option is not None:
            self.ssl_option = ssl_option

    @property
    def job_id(self):
        """Gets the job_id of this SwitchSslResponse.

        任务ID。

        :return: The job_id of this SwitchSslResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SwitchSslResponse.

        任务ID。

        :param job_id: The job_id of this SwitchSslResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def ssl_option(self):
        """Gets the ssl_option of this SwitchSslResponse.

        SSL开关状态。

        :return: The ssl_option of this SwitchSslResponse.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this SwitchSslResponse.

        SSL开关状态。

        :param ssl_option: The ssl_option of this SwitchSslResponse.
        :type ssl_option: str
        """
        self._ssl_option = ssl_option

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
        if not isinstance(other, SwitchSslResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
