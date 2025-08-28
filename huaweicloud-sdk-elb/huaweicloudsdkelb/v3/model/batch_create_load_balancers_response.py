# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateLoadBalancersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_ids': 'list[str]',
        'job_id': 'str',
        'order_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'loadbalancer_ids': 'loadbalancer_ids',
        'job_id': 'job_id',
        'order_id': 'order_id',
        'request_id': 'request_id'
    }

    def __init__(self, loadbalancer_ids=None, job_id=None, order_id=None, request_id=None):
        r"""BatchCreateLoadBalancersResponse

        The model defined in huaweicloud sdk

        :param loadbalancer_ids: **参数解释**：批创负载均衡器ID（UUID）的列表。  **取值范围**：不涉及
        :type loadbalancer_ids: list[str]
        :param job_id: **参数解释**：批量创建负载均衡器的job ID。  **取值范围**：不涉及
        :type job_id: str
        :param order_id: **参数解释**：订单号[（只有批量创建包周期实例的场景返回该字段）](tag:hws)  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)
        :type order_id: str
        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        """
        
        super(BatchCreateLoadBalancersResponse, self).__init__()

        self._loadbalancer_ids = None
        self._job_id = None
        self._order_id = None
        self._request_id = None
        self.discriminator = None

        if loadbalancer_ids is not None:
            self.loadbalancer_ids = loadbalancer_ids
        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def loadbalancer_ids(self):
        r"""Gets the loadbalancer_ids of this BatchCreateLoadBalancersResponse.

        **参数解释**：批创负载均衡器ID（UUID）的列表。  **取值范围**：不涉及

        :return: The loadbalancer_ids of this BatchCreateLoadBalancersResponse.
        :rtype: list[str]
        """
        return self._loadbalancer_ids

    @loadbalancer_ids.setter
    def loadbalancer_ids(self, loadbalancer_ids):
        r"""Sets the loadbalancer_ids of this BatchCreateLoadBalancersResponse.

        **参数解释**：批创负载均衡器ID（UUID）的列表。  **取值范围**：不涉及

        :param loadbalancer_ids: The loadbalancer_ids of this BatchCreateLoadBalancersResponse.
        :type loadbalancer_ids: list[str]
        """
        self._loadbalancer_ids = loadbalancer_ids

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：批量创建负载均衡器的job ID。  **取值范围**：不涉及

        :return: The job_id of this BatchCreateLoadBalancersResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：批量创建负载均衡器的job ID。  **取值范围**：不涉及

        :param job_id: The job_id of this BatchCreateLoadBalancersResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：订单号[（只有批量创建包周期实例的场景返回该字段）](tag:hws)  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :return: The order_id of this BatchCreateLoadBalancersResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：订单号[（只有批量创建包周期实例的场景返回该字段）](tag:hws)  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :param order_id: The order_id of this BatchCreateLoadBalancersResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this BatchCreateLoadBalancersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchCreateLoadBalancersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this BatchCreateLoadBalancersResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, BatchCreateLoadBalancersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
