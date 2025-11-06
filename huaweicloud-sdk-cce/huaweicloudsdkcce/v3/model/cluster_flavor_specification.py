# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterFlavorSpecification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'node_capacity': 'int',
        'available_master_flavors': 'list[MasterFlavorSpec]',
        'is_sold_out': 'bool',
        'is_support_multi_az': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'node_capacity': 'nodeCapacity',
        'available_master_flavors': 'availableMasterFlavors',
        'is_sold_out': 'isSoldOut',
        'is_support_multi_az': 'isSupportMultiAZ'
    }

    def __init__(self, name=None, node_capacity=None, available_master_flavors=None, is_sold_out=None, is_support_multi_az=None):
        r"""ClusterFlavorSpecification

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 规格名称 **取值范围**： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模三控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模三控制节点CCE集群（最大200节点） - cce.s2.large: 大规模三控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模三控制节点CCE集群（最大2000节点） [- cce.s3.small: 小规模五控制节点CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.s3.medium: 中等规模五控制节点CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.s3.large: 大规模五控制节点CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.s3.xlarge: 超大规模五控制节点CCE集群（最大2000节点）](tag:hcs,hcs_sm)  [专属云特殊规格如下：](tag:hws,hws_hk,hcs,hcs_sm) [- cce.dec.s1.small: 小规模单控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s1.medium: 中等规模单控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s1.large: 大规模单控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s1.xlarge: 超大规模单控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s2.small: 小规模三控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s2.medium: 中等规模三控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s2.large: 大规模三控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s2.xlarge: 超大规模三控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s3.small: 小规模五控制节点的专属云CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.dec.s3.medium: 中等规模五控制节点的专属云CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.dec.s3.large: 大规模五控制节点的专属云CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.dec.s3.xlarge: 超大规模五控制节点的专属云CCE集群（最大2000节点）](tag:hcs,hcs_sm)
        :type name: str
        :param node_capacity: **参数解释**： 集群节点规模 **取值范围**： - 50: 最大支持50节点 - 200: 最大支持200节点 - 100: 最大支持1000节点 - 2000: 最大支持2000节点
        :type node_capacity: int
        :param available_master_flavors: **参数解释**： 控制节点详情
        :type available_master_flavors: list[:class:`huaweicloudsdkcce.v3.MasterFlavorSpec`]
        :param is_sold_out: **参数解释**： 集群规格是否售罄 **取值范围**： 不涉及
        :type is_sold_out: bool
        :param is_support_multi_az: **参数解释**： 是否支持控制节点多可用区分布 **取值范围**： 不涉及
        :type is_support_multi_az: bool
        """
        
        

        self._name = None
        self._node_capacity = None
        self._available_master_flavors = None
        self._is_sold_out = None
        self._is_support_multi_az = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_capacity is not None:
            self.node_capacity = node_capacity
        if available_master_flavors is not None:
            self.available_master_flavors = available_master_flavors
        if is_sold_out is not None:
            self.is_sold_out = is_sold_out
        if is_support_multi_az is not None:
            self.is_support_multi_az = is_support_multi_az

    @property
    def name(self):
        r"""Gets the name of this ClusterFlavorSpecification.

        **参数解释**： 规格名称 **取值范围**： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模三控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模三控制节点CCE集群（最大200节点） - cce.s2.large: 大规模三控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模三控制节点CCE集群（最大2000节点） [- cce.s3.small: 小规模五控制节点CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.s3.medium: 中等规模五控制节点CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.s3.large: 大规模五控制节点CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.s3.xlarge: 超大规模五控制节点CCE集群（最大2000节点）](tag:hcs,hcs_sm)  [专属云特殊规格如下：](tag:hws,hws_hk,hcs,hcs_sm) [- cce.dec.s1.small: 小规模单控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s1.medium: 中等规模单控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s1.large: 大规模单控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s1.xlarge: 超大规模单控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s2.small: 小规模三控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s2.medium: 中等规模三控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s2.large: 大规模三控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s2.xlarge: 超大规模三控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s3.small: 小规模五控制节点的专属云CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.dec.s3.medium: 中等规模五控制节点的专属云CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.dec.s3.large: 大规模五控制节点的专属云CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.dec.s3.xlarge: 超大规模五控制节点的专属云CCE集群（最大2000节点）](tag:hcs,hcs_sm)

        :return: The name of this ClusterFlavorSpecification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterFlavorSpecification.

        **参数解释**： 规格名称 **取值范围**： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模三控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模三控制节点CCE集群（最大200节点） - cce.s2.large: 大规模三控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模三控制节点CCE集群（最大2000节点） [- cce.s3.small: 小规模五控制节点CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.s3.medium: 中等规模五控制节点CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.s3.large: 大规模五控制节点CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.s3.xlarge: 超大规模五控制节点CCE集群（最大2000节点）](tag:hcs,hcs_sm)  [专属云特殊规格如下：](tag:hws,hws_hk,hcs,hcs_sm) [- cce.dec.s1.small: 小规模单控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s1.medium: 中等规模单控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s1.large: 大规模单控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s1.xlarge: 超大规模单控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s2.small: 小规模三控制节点的专属云CCE集群（最大50节点）](tag:hws,hws_hk) [- cce.dec.s2.medium: 中等规模三控制节点的专属云CCE集群（最大200节点）](tag:hws,hws_hk) [- cce.dec.s2.large: 大规模三控制节点的专属云CCE集群（最大1000节点）](tag:hws,hws_hk) [- cce.dec.s2.xlarge: 超大规模三控制节点的专属云CCE集群（最大2000节点）](tag:hws,hws_hk) [- cce.dec.s3.small: 小规模五控制节点的专属云CCE集群（最大50节点）](tag:hcs,hcs_sm) [- cce.dec.s3.medium: 中等规模五控制节点的专属云CCE集群（最大200节点）](tag:hcs,hcs_sm) [- cce.dec.s3.large: 大规模五控制节点的专属云CCE集群（最大1000节点）](tag:hcs,hcs_sm) [- cce.dec.s3.xlarge: 超大规模五控制节点的专属云CCE集群（最大2000节点）](tag:hcs,hcs_sm)

        :param name: The name of this ClusterFlavorSpecification.
        :type name: str
        """
        self._name = name

    @property
    def node_capacity(self):
        r"""Gets the node_capacity of this ClusterFlavorSpecification.

        **参数解释**： 集群节点规模 **取值范围**： - 50: 最大支持50节点 - 200: 最大支持200节点 - 100: 最大支持1000节点 - 2000: 最大支持2000节点

        :return: The node_capacity of this ClusterFlavorSpecification.
        :rtype: int
        """
        return self._node_capacity

    @node_capacity.setter
    def node_capacity(self, node_capacity):
        r"""Sets the node_capacity of this ClusterFlavorSpecification.

        **参数解释**： 集群节点规模 **取值范围**： - 50: 最大支持50节点 - 200: 最大支持200节点 - 100: 最大支持1000节点 - 2000: 最大支持2000节点

        :param node_capacity: The node_capacity of this ClusterFlavorSpecification.
        :type node_capacity: int
        """
        self._node_capacity = node_capacity

    @property
    def available_master_flavors(self):
        r"""Gets the available_master_flavors of this ClusterFlavorSpecification.

        **参数解释**： 控制节点详情

        :return: The available_master_flavors of this ClusterFlavorSpecification.
        :rtype: list[:class:`huaweicloudsdkcce.v3.MasterFlavorSpec`]
        """
        return self._available_master_flavors

    @available_master_flavors.setter
    def available_master_flavors(self, available_master_flavors):
        r"""Sets the available_master_flavors of this ClusterFlavorSpecification.

        **参数解释**： 控制节点详情

        :param available_master_flavors: The available_master_flavors of this ClusterFlavorSpecification.
        :type available_master_flavors: list[:class:`huaweicloudsdkcce.v3.MasterFlavorSpec`]
        """
        self._available_master_flavors = available_master_flavors

    @property
    def is_sold_out(self):
        r"""Gets the is_sold_out of this ClusterFlavorSpecification.

        **参数解释**： 集群规格是否售罄 **取值范围**： 不涉及

        :return: The is_sold_out of this ClusterFlavorSpecification.
        :rtype: bool
        """
        return self._is_sold_out

    @is_sold_out.setter
    def is_sold_out(self, is_sold_out):
        r"""Sets the is_sold_out of this ClusterFlavorSpecification.

        **参数解释**： 集群规格是否售罄 **取值范围**： 不涉及

        :param is_sold_out: The is_sold_out of this ClusterFlavorSpecification.
        :type is_sold_out: bool
        """
        self._is_sold_out = is_sold_out

    @property
    def is_support_multi_az(self):
        r"""Gets the is_support_multi_az of this ClusterFlavorSpecification.

        **参数解释**： 是否支持控制节点多可用区分布 **取值范围**： 不涉及

        :return: The is_support_multi_az of this ClusterFlavorSpecification.
        :rtype: bool
        """
        return self._is_support_multi_az

    @is_support_multi_az.setter
    def is_support_multi_az(self, is_support_multi_az):
        r"""Sets the is_support_multi_az of this ClusterFlavorSpecification.

        **参数解释**： 是否支持控制节点多可用区分布 **取值范围**： 不涉及

        :param is_support_multi_az: The is_support_multi_az of this ClusterFlavorSpecification.
        :type is_support_multi_az: bool
        """
        self._is_support_multi_az = is_support_multi_az

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
        if not isinstance(other, ClusterFlavorSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
