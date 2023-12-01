# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_resize': 'str',
        'extend_param': 'ResizeClusterRequestBodyExtendParam'
    }

    attribute_map = {
        'flavor_resize': 'flavorResize',
        'extend_param': 'extendParam'
    }

    def __init__(self, flavor_resize=None, extend_param=None):
        """ResizeClusterRequestBody

        The model defined in huaweicloud sdk

        :param flavor_resize: 要变更的目标规格。仅支持变更集群最大节点规模，不支持变更控制节点数，且不支持降低集群规格。例如原集群规格为cce.s2.medium，仅支持变更至cce.s2.large及以上规格，不支持变更至cce.s2.small或cce.s1.medium。  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  &gt;    关于规格参数中的字段说明如下： &gt;    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 &gt;    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 &gt;    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) &gt;    - small：表示集群支持管理的最大节点规模为50节点。 &gt;    - medium：表示集群支持管理的最大节点规模为200节点。 &gt;    - large：表示集群支持管理的最大节点规模为1000节点。 &gt;    - xlarge：表示集群支持管理的最大节点规模为2000节点。。 
        :type flavor_resize: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestBodyExtendParam`
        """
        
        

        self._flavor_resize = None
        self._extend_param = None
        self.discriminator = None

        self.flavor_resize = flavor_resize
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def flavor_resize(self):
        """Gets the flavor_resize of this ResizeClusterRequestBody.

        要变更的目标规格。仅支持变更集群最大节点规模，不支持变更控制节点数，且不支持降低集群规格。例如原集群规格为cce.s2.medium，仅支持变更至cce.s2.large及以上规格，不支持变更至cce.s2.small或cce.s1.medium。  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    关于规格参数中的字段说明如下： >    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 >    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) >    - small：表示集群支持管理的最大节点规模为50节点。 >    - medium：表示集群支持管理的最大节点规模为200节点。 >    - large：表示集群支持管理的最大节点规模为1000节点。 >    - xlarge：表示集群支持管理的最大节点规模为2000节点。。 

        :return: The flavor_resize of this ResizeClusterRequestBody.
        :rtype: str
        """
        return self._flavor_resize

    @flavor_resize.setter
    def flavor_resize(self, flavor_resize):
        """Sets the flavor_resize of this ResizeClusterRequestBody.

        要变更的目标规格。仅支持变更集群最大节点规模，不支持变更控制节点数，且不支持降低集群规格。例如原集群规格为cce.s2.medium，仅支持变更至cce.s2.large及以上规格，不支持变更至cce.s2.small或cce.s1.medium。  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    关于规格参数中的字段说明如下： >    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 >    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) >    - small：表示集群支持管理的最大节点规模为50节点。 >    - medium：表示集群支持管理的最大节点规模为200节点。 >    - large：表示集群支持管理的最大节点规模为1000节点。 >    - xlarge：表示集群支持管理的最大节点规模为2000节点。。 

        :param flavor_resize: The flavor_resize of this ResizeClusterRequestBody.
        :type flavor_resize: str
        """
        self._flavor_resize = flavor_resize

    @property
    def extend_param(self):
        """Gets the extend_param of this ResizeClusterRequestBody.

        :return: The extend_param of this ResizeClusterRequestBody.
        :rtype: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestBodyExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this ResizeClusterRequestBody.

        :param extend_param: The extend_param of this ResizeClusterRequestBody.
        :type extend_param: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestBodyExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, ResizeClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
