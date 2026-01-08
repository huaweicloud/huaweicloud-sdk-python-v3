# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteLoadbalancersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unbounded_pool': 'bool',
        'public_ip': 'bool',
        'loadbalancer_ids': 'list[str]'
    }

    attribute_map = {
        'unbounded_pool': 'unbounded_pool',
        'public_ip': 'public_ip',
        'loadbalancer_ids': 'loadbalancer_ids'
    }

    def __init__(self, unbounded_pool=None, public_ip=None, loadbalancer_ids=None):
        r"""BatchDeleteLoadbalancersRequestBody

        The model defined in huaweicloud sdk

        :param unbounded_pool: 解绑后的游离pool是否被删除
        :type unbounded_pool: bool
        :param public_ip: 是否删除公网IP
        :type public_ip: bool
        :param loadbalancer_ids: 待删除的负载均衡器id列表。
        :type loadbalancer_ids: list[str]
        """
        
        

        self._unbounded_pool = None
        self._public_ip = None
        self._loadbalancer_ids = None
        self.discriminator = None

        if unbounded_pool is not None:
            self.unbounded_pool = unbounded_pool
        if public_ip is not None:
            self.public_ip = public_ip
        self.loadbalancer_ids = loadbalancer_ids

    @property
    def unbounded_pool(self):
        r"""Gets the unbounded_pool of this BatchDeleteLoadbalancersRequestBody.

        解绑后的游离pool是否被删除

        :return: The unbounded_pool of this BatchDeleteLoadbalancersRequestBody.
        :rtype: bool
        """
        return self._unbounded_pool

    @unbounded_pool.setter
    def unbounded_pool(self, unbounded_pool):
        r"""Sets the unbounded_pool of this BatchDeleteLoadbalancersRequestBody.

        解绑后的游离pool是否被删除

        :param unbounded_pool: The unbounded_pool of this BatchDeleteLoadbalancersRequestBody.
        :type unbounded_pool: bool
        """
        self._unbounded_pool = unbounded_pool

    @property
    def public_ip(self):
        r"""Gets the public_ip of this BatchDeleteLoadbalancersRequestBody.

        是否删除公网IP

        :return: The public_ip of this BatchDeleteLoadbalancersRequestBody.
        :rtype: bool
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this BatchDeleteLoadbalancersRequestBody.

        是否删除公网IP

        :param public_ip: The public_ip of this BatchDeleteLoadbalancersRequestBody.
        :type public_ip: bool
        """
        self._public_ip = public_ip

    @property
    def loadbalancer_ids(self):
        r"""Gets the loadbalancer_ids of this BatchDeleteLoadbalancersRequestBody.

        待删除的负载均衡器id列表。

        :return: The loadbalancer_ids of this BatchDeleteLoadbalancersRequestBody.
        :rtype: list[str]
        """
        return self._loadbalancer_ids

    @loadbalancer_ids.setter
    def loadbalancer_ids(self, loadbalancer_ids):
        r"""Sets the loadbalancer_ids of this BatchDeleteLoadbalancersRequestBody.

        待删除的负载均衡器id列表。

        :param loadbalancer_ids: The loadbalancer_ids of this BatchDeleteLoadbalancersRequestBody.
        :type loadbalancer_ids: list[str]
        """
        self._loadbalancer_ids = loadbalancer_ids

    def to_dict(self):
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
        if not isinstance(other, BatchDeleteLoadbalancersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
