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
        'extend_param': 'ResizeClusterRequestExtendParam'
    }

    attribute_map = {
        'flavor_resize': 'flavorResize',
        'extend_param': 'extendParam'
    }

    def __init__(self, flavor_resize=None, extend_param=None):
        """ResizeClusterRequestBody

        The model defined in huaweicloud sdk

        :param flavor_resize: 要变更的目标规格  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  &gt;    - s1：单控制节点CCE集群。 &gt;    - s2：多控制节点CCE集群。 &gt;    - dec：专属CCE集群规格。如cce.dec.s1.small为小规模单控制节点专属CCE集群（最大50节点）。 &gt;    - 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 &gt;    - 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 &gt;    - 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。 
        :type flavor_resize: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestExtendParam`
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

        要变更的目标规格  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    - s1：单控制节点CCE集群。 >    - s2：多控制节点CCE集群。 >    - dec：专属CCE集群规格。如cce.dec.s1.small为小规模单控制节点专属CCE集群（最大50节点）。 >    - 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >    - 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。 

        :return: The flavor_resize of this ResizeClusterRequestBody.
        :rtype: str
        """
        return self._flavor_resize

    @flavor_resize.setter
    def flavor_resize(self, flavor_resize):
        """Sets the flavor_resize of this ResizeClusterRequestBody.

        要变更的目标规格  - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    - s1：单控制节点CCE集群。 >    - s2：多控制节点CCE集群。 >    - dec：专属CCE集群规格。如cce.dec.s1.small为小规模单控制节点专属CCE集群（最大50节点）。 >    - 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >    - 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。 

        :param flavor_resize: The flavor_resize of this ResizeClusterRequestBody.
        :type flavor_resize: str
        """
        self._flavor_resize = flavor_resize

    @property
    def extend_param(self):
        """Gets the extend_param of this ResizeClusterRequestBody.

        :return: The extend_param of this ResizeClusterRequestBody.
        :rtype: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this ResizeClusterRequestBody.

        :param extend_param: The extend_param of this ResizeClusterRequestBody.
        :type extend_param: :class:`huaweicloudsdkcce.v3.ResizeClusterRequestExtendParam`
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
