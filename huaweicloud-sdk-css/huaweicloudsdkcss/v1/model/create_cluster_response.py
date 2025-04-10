# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'CreateClusterClusterResponse',
        'order_id': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'order_id': 'orderId'
    }

    def __init__(self, cluster=None, order_id=None):
        r"""CreateClusterResponse

        The model defined in huaweicloud sdk

        :param cluster: 
        :type cluster: :class:`huaweicloudsdkcss.v1.CreateClusterClusterResponse`
        :param order_id: 订单号。若创建的是包周期集群，则只返回ordeld参数。
        :type order_id: str
        """
        
        super(CreateClusterResponse, self).__init__()

        self._cluster = None
        self._order_id = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if order_id is not None:
            self.order_id = order_id

    @property
    def cluster(self):
        r"""Gets the cluster of this CreateClusterResponse.

        :return: The cluster of this CreateClusterResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterClusterResponse`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        r"""Sets the cluster of this CreateClusterResponse.

        :param cluster: The cluster of this CreateClusterResponse.
        :type cluster: :class:`huaweicloudsdkcss.v1.CreateClusterClusterResponse`
        """
        self._cluster = cluster

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateClusterResponse.

        订单号。若创建的是包周期集群，则只返回ordeld参数。

        :return: The order_id of this CreateClusterResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateClusterResponse.

        订单号。若创建的是包周期集群，则只返回ordeld参数。

        :param order_id: The order_id of this CreateClusterResponse.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
