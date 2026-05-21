# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteLoadbalancersResponse(SdkResponse):

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
        'job_id': 'str',
        'loadbalancer_ids': 'list[str]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'job_id': 'job_id',
        'loadbalancer_ids': 'loadbalancer_ids'
    }

    def __init__(self, request_id=None, job_id=None, loadbalancer_ids=None):
        r"""BatchDeleteLoadbalancersResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param job_id: 批量删除任务id
        :type job_id: str
        :param loadbalancer_ids: 待删除的负载均衡器id列表。
        :type loadbalancer_ids: list[str]
        """
        
        super().__init__()

        self._request_id = None
        self._job_id = None
        self._loadbalancer_ids = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if job_id is not None:
            self.job_id = job_id
        if loadbalancer_ids is not None:
            self.loadbalancer_ids = loadbalancer_ids

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchDeleteLoadbalancersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this BatchDeleteLoadbalancersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchDeleteLoadbalancersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this BatchDeleteLoadbalancersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchDeleteLoadbalancersResponse.

        批量删除任务id

        :return: The job_id of this BatchDeleteLoadbalancersResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchDeleteLoadbalancersResponse.

        批量删除任务id

        :param job_id: The job_id of this BatchDeleteLoadbalancersResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def loadbalancer_ids(self):
        r"""Gets the loadbalancer_ids of this BatchDeleteLoadbalancersResponse.

        待删除的负载均衡器id列表。

        :return: The loadbalancer_ids of this BatchDeleteLoadbalancersResponse.
        :rtype: list[str]
        """
        return self._loadbalancer_ids

    @loadbalancer_ids.setter
    def loadbalancer_ids(self, loadbalancer_ids):
        r"""Sets the loadbalancer_ids of this BatchDeleteLoadbalancersResponse.

        待删除的负载均衡器id列表。

        :param loadbalancer_ids: The loadbalancer_ids of this BatchDeleteLoadbalancersResponse.
        :type loadbalancer_ids: list[str]
        """
        self._loadbalancer_ids = loadbalancer_ids

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteLoadbalancersResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteLoadbalancersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
