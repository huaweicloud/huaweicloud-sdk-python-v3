# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLdapConfigResponse(SdkResponse):

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
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, job_id=None, x_request_id=None):
        r"""DeleteLdapConfigResponse

        The model defined in huaweicloud sdk

        :param job_id: LDAP异步任务的id。可通过查询job的状态详情接口查询job的执行状态。
        :type job_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteLdapConfigResponse, self).__init__()

        self._job_id = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this DeleteLdapConfigResponse.

        LDAP异步任务的id。可通过查询job的状态详情接口查询job的执行状态。

        :return: The job_id of this DeleteLdapConfigResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DeleteLdapConfigResponse.

        LDAP异步任务的id。可通过查询job的状态详情接口查询job的执行状态。

        :param job_id: The job_id of this DeleteLdapConfigResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteLdapConfigResponse.

        :return: The x_request_id of this DeleteLdapConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteLdapConfigResponse.

        :param x_request_id: The x_request_id of this DeleteLdapConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DeleteLdapConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
