# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneLoadbalancerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_list': 'list[CloneLoadbalancerResponseBodyLoadbalancerList]',
        'request_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'loadbalancer_list': 'loadbalancer_list',
        'request_id': 'request_id',
        'job_id': 'job_id'
    }

    def __init__(self, loadbalancer_list=None, request_id=None, job_id=None):
        r"""CloneLoadbalancerResponse

        The model defined in huaweicloud sdk

        :param loadbalancer_list: 
        :type loadbalancer_list: list[:class:`huaweicloudsdkelb.v3.CloneLoadbalancerResponseBodyLoadbalancerList`]
        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param job_id: **参数解释**：实例复制任务ID。  **取值范围**：不涉及
        :type job_id: str
        """
        
        super(CloneLoadbalancerResponse, self).__init__()

        self._loadbalancer_list = None
        self._request_id = None
        self._job_id = None
        self.discriminator = None

        if loadbalancer_list is not None:
            self.loadbalancer_list = loadbalancer_list
        if request_id is not None:
            self.request_id = request_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def loadbalancer_list(self):
        r"""Gets the loadbalancer_list of this CloneLoadbalancerResponse.

        :return: The loadbalancer_list of this CloneLoadbalancerResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CloneLoadbalancerResponseBodyLoadbalancerList`]
        """
        return self._loadbalancer_list

    @loadbalancer_list.setter
    def loadbalancer_list(self, loadbalancer_list):
        r"""Sets the loadbalancer_list of this CloneLoadbalancerResponse.

        :param loadbalancer_list: The loadbalancer_list of this CloneLoadbalancerResponse.
        :type loadbalancer_list: list[:class:`huaweicloudsdkelb.v3.CloneLoadbalancerResponseBodyLoadbalancerList`]
        """
        self._loadbalancer_list = loadbalancer_list

    @property
    def request_id(self):
        r"""Gets the request_id of this CloneLoadbalancerResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this CloneLoadbalancerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CloneLoadbalancerResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this CloneLoadbalancerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this CloneLoadbalancerResponse.

        **参数解释**：实例复制任务ID。  **取值范围**：不涉及

        :return: The job_id of this CloneLoadbalancerResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CloneLoadbalancerResponse.

        **参数解释**：实例复制任务ID。  **取值范围**：不涉及

        :param job_id: The job_id of this CloneLoadbalancerResponse.
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
        if not isinstance(other, CloneLoadbalancerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
