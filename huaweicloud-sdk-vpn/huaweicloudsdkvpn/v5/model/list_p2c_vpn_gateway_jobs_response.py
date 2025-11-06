# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListP2cVpnGatewayJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'jobs': 'list[Job]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'jobs': 'jobs'
    }

    def __init__(self, request_id=None, jobs=None):
        r"""ListP2cVpnGatewayJobsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param jobs: 任务列表
        :type jobs: list[:class:`huaweicloudsdkvpn.v5.Job`]
        """
        
        super().__init__()

        self._request_id = None
        self._jobs = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if jobs is not None:
            self.jobs = jobs

    @property
    def request_id(self):
        r"""Gets the request_id of this ListP2cVpnGatewayJobsResponse.

        请求ID

        :return: The request_id of this ListP2cVpnGatewayJobsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListP2cVpnGatewayJobsResponse.

        请求ID

        :param request_id: The request_id of this ListP2cVpnGatewayJobsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def jobs(self):
        r"""Gets the jobs of this ListP2cVpnGatewayJobsResponse.

        任务列表

        :return: The jobs of this ListP2cVpnGatewayJobsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListP2cVpnGatewayJobsResponse.

        任务列表

        :param jobs: The jobs of this ListP2cVpnGatewayJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkvpn.v5.Job`]
        """
        self._jobs = jobs

    def to_dict(self):
        import warnings
        warnings.warn("ListP2cVpnGatewayJobsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListP2cVpnGatewayJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
