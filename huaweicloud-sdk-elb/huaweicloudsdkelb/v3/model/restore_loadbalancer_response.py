# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreLoadbalancerResponse(SdkResponse):

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
        'type': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'type': 'type',
        'job_id': 'job_id'
    }

    def __init__(self, request_id=None, type=None, job_id=None):
        r"""RestoreLoadbalancerResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param type: **参数解释**：ELB实例的类型。  **取值范围**： - v2：共享型ELB。 - v3：独享型ELB。
        :type type: str
        :param job_id: **参数解释**：还原负载均衡器的任务ID。  **取值范围**：不涉及
        :type job_id: str
        """
        
        super(RestoreLoadbalancerResponse, self).__init__()

        self._request_id = None
        self._type = None
        self._job_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if type is not None:
            self.type = type
        if job_id is not None:
            self.job_id = job_id

    @property
    def request_id(self):
        r"""Gets the request_id of this RestoreLoadbalancerResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this RestoreLoadbalancerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this RestoreLoadbalancerResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this RestoreLoadbalancerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def type(self):
        r"""Gets the type of this RestoreLoadbalancerResponse.

        **参数解释**：ELB实例的类型。  **取值范围**： - v2：共享型ELB。 - v3：独享型ELB。

        :return: The type of this RestoreLoadbalancerResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RestoreLoadbalancerResponse.

        **参数解释**：ELB实例的类型。  **取值范围**： - v2：共享型ELB。 - v3：独享型ELB。

        :param type: The type of this RestoreLoadbalancerResponse.
        :type type: str
        """
        self._type = type

    @property
    def job_id(self):
        r"""Gets the job_id of this RestoreLoadbalancerResponse.

        **参数解释**：还原负载均衡器的任务ID。  **取值范围**：不涉及

        :return: The job_id of this RestoreLoadbalancerResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RestoreLoadbalancerResponse.

        **参数解释**：还原负载均衡器的任务ID。  **取值范围**：不涉及

        :param job_id: The job_id of this RestoreLoadbalancerResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, RestoreLoadbalancerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
