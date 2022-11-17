# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeLoadbalancerChargeModeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_id_list': 'list[str]',
        'loadbalancer_id_list': 'list[str]',
        'order_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'eip_id_list': 'eip_id_list',
        'loadbalancer_id_list': 'loadbalancer_id_list',
        'order_id': 'order_id',
        'request_id': 'request_id'
    }

    def __init__(self, eip_id_list=None, loadbalancer_id_list=None, order_id=None, request_id=None):
        """ChangeLoadbalancerChargeModeResponse

        The model defined in huaweicloud sdk

        :param eip_id_list: 转包周期下单成功的EIP ID列表
        :type eip_id_list: list[str]
        :param loadbalancer_id_list: 转包周期下单成功的LB ID列表
        :type loadbalancer_id_list: list[str]
        :param order_id: 转包周期订单号
        :type order_id: str
        :param request_id: 请求的UUIID
        :type request_id: str
        """
        
        super(ChangeLoadbalancerChargeModeResponse, self).__init__()

        self._eip_id_list = None
        self._loadbalancer_id_list = None
        self._order_id = None
        self._request_id = None
        self.discriminator = None

        if eip_id_list is not None:
            self.eip_id_list = eip_id_list
        if loadbalancer_id_list is not None:
            self.loadbalancer_id_list = loadbalancer_id_list
        if order_id is not None:
            self.order_id = order_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def eip_id_list(self):
        """Gets the eip_id_list of this ChangeLoadbalancerChargeModeResponse.

        转包周期下单成功的EIP ID列表

        :return: The eip_id_list of this ChangeLoadbalancerChargeModeResponse.
        :rtype: list[str]
        """
        return self._eip_id_list

    @eip_id_list.setter
    def eip_id_list(self, eip_id_list):
        """Sets the eip_id_list of this ChangeLoadbalancerChargeModeResponse.

        转包周期下单成功的EIP ID列表

        :param eip_id_list: The eip_id_list of this ChangeLoadbalancerChargeModeResponse.
        :type eip_id_list: list[str]
        """
        self._eip_id_list = eip_id_list

    @property
    def loadbalancer_id_list(self):
        """Gets the loadbalancer_id_list of this ChangeLoadbalancerChargeModeResponse.

        转包周期下单成功的LB ID列表

        :return: The loadbalancer_id_list of this ChangeLoadbalancerChargeModeResponse.
        :rtype: list[str]
        """
        return self._loadbalancer_id_list

    @loadbalancer_id_list.setter
    def loadbalancer_id_list(self, loadbalancer_id_list):
        """Sets the loadbalancer_id_list of this ChangeLoadbalancerChargeModeResponse.

        转包周期下单成功的LB ID列表

        :param loadbalancer_id_list: The loadbalancer_id_list of this ChangeLoadbalancerChargeModeResponse.
        :type loadbalancer_id_list: list[str]
        """
        self._loadbalancer_id_list = loadbalancer_id_list

    @property
    def order_id(self):
        """Gets the order_id of this ChangeLoadbalancerChargeModeResponse.

        转包周期订单号

        :return: The order_id of this ChangeLoadbalancerChargeModeResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ChangeLoadbalancerChargeModeResponse.

        转包周期订单号

        :param order_id: The order_id of this ChangeLoadbalancerChargeModeResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def request_id(self):
        """Gets the request_id of this ChangeLoadbalancerChargeModeResponse.

        请求的UUIID

        :return: The request_id of this ChangeLoadbalancerChargeModeResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ChangeLoadbalancerChargeModeResponse.

        请求的UUIID

        :param request_id: The request_id of this ChangeLoadbalancerChargeModeResponse.
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
        if not isinstance(other, ChangeLoadbalancerChargeModeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
