# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadbalancerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer': 'LoadbalancerResp',
        'order_id': 'str',
        'loadbalancer_id': 'str'
    }

    attribute_map = {
        'loadbalancer': 'loadbalancer',
        'order_id': 'order_id',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, loadbalancer=None, order_id=None, loadbalancer_id=None):
        r"""CreateLoadbalancerResponse

        The model defined in huaweicloud sdk

        :param loadbalancer: 
        :type loadbalancer: :class:`huaweicloudsdkelb.v2.LoadbalancerResp`
        :param order_id: 订单号[（包周期场景返回该字段）](tag:hws)
        :type order_id: str
        :param loadbalancer_id: 负载均衡器的ID[（包周期场景返回该字段）](tag:hws)
        :type loadbalancer_id: str
        """
        
        super(CreateLoadbalancerResponse, self).__init__()

        self._loadbalancer = None
        self._order_id = None
        self._loadbalancer_id = None
        self.discriminator = None

        if loadbalancer is not None:
            self.loadbalancer = loadbalancer
        if order_id is not None:
            self.order_id = order_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def loadbalancer(self):
        r"""Gets the loadbalancer of this CreateLoadbalancerResponse.

        :return: The loadbalancer of this CreateLoadbalancerResponse.
        :rtype: :class:`huaweicloudsdkelb.v2.LoadbalancerResp`
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        r"""Sets the loadbalancer of this CreateLoadbalancerResponse.

        :param loadbalancer: The loadbalancer of this CreateLoadbalancerResponse.
        :type loadbalancer: :class:`huaweicloudsdkelb.v2.LoadbalancerResp`
        """
        self._loadbalancer = loadbalancer

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateLoadbalancerResponse.

        订单号[（包周期场景返回该字段）](tag:hws)

        :return: The order_id of this CreateLoadbalancerResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateLoadbalancerResponse.

        订单号[（包周期场景返回该字段）](tag:hws)

        :param order_id: The order_id of this CreateLoadbalancerResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CreateLoadbalancerResponse.

        负载均衡器的ID[（包周期场景返回该字段）](tag:hws)

        :return: The loadbalancer_id of this CreateLoadbalancerResponse.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CreateLoadbalancerResponse.

        负载均衡器的ID[（包周期场景返回该字段）](tag:hws)

        :param loadbalancer_id: The loadbalancer_id of this CreateLoadbalancerResponse.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, CreateLoadbalancerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
