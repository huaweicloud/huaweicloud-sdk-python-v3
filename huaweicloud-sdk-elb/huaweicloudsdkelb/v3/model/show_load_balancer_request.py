# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoadBalancerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_id': 'str'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, loadbalancer_id=None):
        r"""ShowLoadBalancerRequest

        The model defined in huaweicloud sdk

        :param loadbalancer_id: 负载均衡器ID。
        :type loadbalancer_id: str
        """
        
        

        self._loadbalancer_id = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ShowLoadBalancerRequest.

        负载均衡器ID。

        :return: The loadbalancer_id of this ShowLoadBalancerRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ShowLoadBalancerRequest.

        负载均衡器ID。

        :param loadbalancer_id: The loadbalancer_id of this ShowLoadBalancerRequest.
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
        if not isinstance(other, ShowLoadBalancerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
