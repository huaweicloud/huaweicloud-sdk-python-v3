# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyInstanceSslConfigResponse(SdkResponse):

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
        'tls_mode': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'tls_mode': 'tls_mode'
    }

    def __init__(self, job_id=None, tls_mode=None):
        r"""ModifyInstanceSslConfigResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param tls_mode: 协议模式。
        :type tls_mode: str
        """
        
        super(ModifyInstanceSslConfigResponse, self).__init__()

        self._job_id = None
        self._tls_mode = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if tls_mode is not None:
            self.tls_mode = tls_mode

    @property
    def job_id(self):
        r"""Gets the job_id of this ModifyInstanceSslConfigResponse.

        任务ID。

        :return: The job_id of this ModifyInstanceSslConfigResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ModifyInstanceSslConfigResponse.

        任务ID。

        :param job_id: The job_id of this ModifyInstanceSslConfigResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def tls_mode(self):
        r"""Gets the tls_mode of this ModifyInstanceSslConfigResponse.

        协议模式。

        :return: The tls_mode of this ModifyInstanceSslConfigResponse.
        :rtype: str
        """
        return self._tls_mode

    @tls_mode.setter
    def tls_mode(self, tls_mode):
        r"""Sets the tls_mode of this ModifyInstanceSslConfigResponse.

        协议模式。

        :param tls_mode: The tls_mode of this ModifyInstanceSslConfigResponse.
        :type tls_mode: str
        """
        self._tls_mode = tls_mode

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
        if not isinstance(other, ModifyInstanceSslConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
