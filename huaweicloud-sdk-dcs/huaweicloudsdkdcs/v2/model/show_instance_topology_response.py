# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redis_server': 'list[TopologyInfo]',
        'cluster_lvs': 'list[TopologyInfo]',
        'cluster_admin': 'list[TopologyInfo]',
        'cluster_proxy': 'list[TopologyInfo]',
        'master': 'list[TopologyInfo]',
        'vpcendpoint': 'list[TopologyInfo]',
        'elb': 'list[TopologyInfo]'
    }

    attribute_map = {
        'redis_server': 'redis_server',
        'cluster_lvs': 'cluster_lvs',
        'cluster_admin': 'cluster_admin',
        'cluster_proxy': 'cluster_proxy',
        'master': 'master',
        'vpcendpoint': 'vpcendpoint',
        'elb': 'elb'
    }

    def __init__(self, redis_server=None, cluster_lvs=None, cluster_admin=None, cluster_proxy=None, master=None, vpcendpoint=None, elb=None):
        r"""ShowInstanceTopologyResponse

        The model defined in huaweicloud sdk

        :param redis_server: **参数解释**： 集群角色：redis-server实例拓朴图。 
        :type redis_server: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param cluster_lvs: **参数解释**： 集群角色：lvs实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 
        :type cluster_lvs: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param cluster_admin: **参数解释**： 集群角色：admin实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 
        :type cluster_admin: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param cluster_proxy: **参数解释**： 集群角色：proxy实例拓朴图。 
        :type cluster_proxy: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param master: **参数解释**： Redis的角色master实例拓朴图，只适用于Redis 3.0版本实例。 
        :type master: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param vpcendpoint: **参数解释**： 集群角色：VPC Endpoint服务实例拓朴图，适用于4.0及以上版本实例。 
        :type vpcendpoint: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        :param elb: **参数解释**： 集群角色：ELB服务实例拓朴图，适用于Redis 4.0及以上版本实例。 
        :type elb: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        
        super(ShowInstanceTopologyResponse, self).__init__()

        self._redis_server = None
        self._cluster_lvs = None
        self._cluster_admin = None
        self._cluster_proxy = None
        self._master = None
        self._vpcendpoint = None
        self._elb = None
        self.discriminator = None

        if redis_server is not None:
            self.redis_server = redis_server
        if cluster_lvs is not None:
            self.cluster_lvs = cluster_lvs
        if cluster_admin is not None:
            self.cluster_admin = cluster_admin
        if cluster_proxy is not None:
            self.cluster_proxy = cluster_proxy
        if master is not None:
            self.master = master
        if vpcendpoint is not None:
            self.vpcendpoint = vpcendpoint
        if elb is not None:
            self.elb = elb

    @property
    def redis_server(self):
        r"""Gets the redis_server of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：redis-server实例拓朴图。 

        :return: The redis_server of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._redis_server

    @redis_server.setter
    def redis_server(self, redis_server):
        r"""Sets the redis_server of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：redis-server实例拓朴图。 

        :param redis_server: The redis_server of this ShowInstanceTopologyResponse.
        :type redis_server: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._redis_server = redis_server

    @property
    def cluster_lvs(self):
        r"""Gets the cluster_lvs of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：lvs实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 

        :return: The cluster_lvs of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._cluster_lvs

    @cluster_lvs.setter
    def cluster_lvs(self, cluster_lvs):
        r"""Sets the cluster_lvs of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：lvs实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 

        :param cluster_lvs: The cluster_lvs of this ShowInstanceTopologyResponse.
        :type cluster_lvs: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._cluster_lvs = cluster_lvs

    @property
    def cluster_admin(self):
        r"""Gets the cluster_admin of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：admin实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 

        :return: The cluster_admin of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._cluster_admin

    @cluster_admin.setter
    def cluster_admin(self, cluster_admin):
        r"""Sets the cluster_admin of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：admin实例拓朴图（当前已下线），只适用于Redis 3.0版本实例。 

        :param cluster_admin: The cluster_admin of this ShowInstanceTopologyResponse.
        :type cluster_admin: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._cluster_admin = cluster_admin

    @property
    def cluster_proxy(self):
        r"""Gets the cluster_proxy of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：proxy实例拓朴图。 

        :return: The cluster_proxy of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._cluster_proxy

    @cluster_proxy.setter
    def cluster_proxy(self, cluster_proxy):
        r"""Sets the cluster_proxy of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：proxy实例拓朴图。 

        :param cluster_proxy: The cluster_proxy of this ShowInstanceTopologyResponse.
        :type cluster_proxy: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._cluster_proxy = cluster_proxy

    @property
    def master(self):
        r"""Gets the master of this ShowInstanceTopologyResponse.

        **参数解释**： Redis的角色master实例拓朴图，只适用于Redis 3.0版本实例。 

        :return: The master of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this ShowInstanceTopologyResponse.

        **参数解释**： Redis的角色master实例拓朴图，只适用于Redis 3.0版本实例。 

        :param master: The master of this ShowInstanceTopologyResponse.
        :type master: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._master = master

    @property
    def vpcendpoint(self):
        r"""Gets the vpcendpoint of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：VPC Endpoint服务实例拓朴图，适用于4.0及以上版本实例。 

        :return: The vpcendpoint of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._vpcendpoint

    @vpcendpoint.setter
    def vpcendpoint(self, vpcendpoint):
        r"""Sets the vpcendpoint of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：VPC Endpoint服务实例拓朴图，适用于4.0及以上版本实例。 

        :param vpcendpoint: The vpcendpoint of this ShowInstanceTopologyResponse.
        :type vpcendpoint: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._vpcendpoint = vpcendpoint

    @property
    def elb(self):
        r"""Gets the elb of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：ELB服务实例拓朴图，适用于Redis 4.0及以上版本实例。 

        :return: The elb of this ShowInstanceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        return self._elb

    @elb.setter
    def elb(self, elb):
        r"""Sets the elb of this ShowInstanceTopologyResponse.

        **参数解释**： 集群角色：ELB服务实例拓朴图，适用于Redis 4.0及以上版本实例。 

        :param elb: The elb of this ShowInstanceTopologyResponse.
        :type elb: list[:class:`huaweicloudsdkdcs.v2.TopologyInfo`]
        """
        self._elb = elb

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
        if not isinstance(other, ShowInstanceTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
