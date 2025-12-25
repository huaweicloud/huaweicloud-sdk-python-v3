# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerNetworkUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidrs': 'list[ContainerCIDR]',
        'containercidrs': 'list[str]'
    }

    attribute_map = {
        'cidrs': 'cidrs',
        'containercidrs': 'containercidrs'
    }

    def __init__(self, cidrs=None, containercidrs=None):
        r"""ContainerNetworkUpdate

        The model defined in huaweicloud sdk

        :param cidrs: 容器网络网段列表。1.21及新版本集群，当集群网络类型为vpc-router时，支持增量添加容器网段，最多配置20个。  此参数在集群更新后不可更改，请谨慎选择。
        :type cidrs: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        :param containercidrs: **参数解释：** 容器网络网段列表。当集群网络类型为vpc-router时，支持添加或删除容器网段。支持的集群版本如下： - v1.28.15-r60及以上版本 - v1.29.15-r20及以上版本 - v1.30.14-r20及以上版本 - v1.31.10-r20及以上版本 - v1.32.6-r20及以上版本 - v1.33.5-r10及以上版本  支持修改集群容器网段的顺序，顺序在前的容器网段优先被使用。 **约束限制：** - 最多支持配置20个子网。 - 填写为空时，该字段不生效。  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type containercidrs: list[str]
        """
        
        

        self._cidrs = None
        self._containercidrs = None
        self.discriminator = None

        if cidrs is not None:
            self.cidrs = cidrs
        if containercidrs is not None:
            self.containercidrs = containercidrs

    @property
    def cidrs(self):
        r"""Gets the cidrs of this ContainerNetworkUpdate.

        容器网络网段列表。1.21及新版本集群，当集群网络类型为vpc-router时，支持增量添加容器网段，最多配置20个。  此参数在集群更新后不可更改，请谨慎选择。

        :return: The cidrs of this ContainerNetworkUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        r"""Sets the cidrs of this ContainerNetworkUpdate.

        容器网络网段列表。1.21及新版本集群，当集群网络类型为vpc-router时，支持增量添加容器网段，最多配置20个。  此参数在集群更新后不可更改，请谨慎选择。

        :param cidrs: The cidrs of this ContainerNetworkUpdate.
        :type cidrs: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        """
        self._cidrs = cidrs

    @property
    def containercidrs(self):
        r"""Gets the containercidrs of this ContainerNetworkUpdate.

        **参数解释：** 容器网络网段列表。当集群网络类型为vpc-router时，支持添加或删除容器网段。支持的集群版本如下： - v1.28.15-r60及以上版本 - v1.29.15-r20及以上版本 - v1.30.14-r20及以上版本 - v1.31.10-r20及以上版本 - v1.32.6-r20及以上版本 - v1.33.5-r10及以上版本  支持修改集群容器网段的顺序，顺序在前的容器网段优先被使用。 **约束限制：** - 最多支持配置20个子网。 - 填写为空时，该字段不生效。  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The containercidrs of this ContainerNetworkUpdate.
        :rtype: list[str]
        """
        return self._containercidrs

    @containercidrs.setter
    def containercidrs(self, containercidrs):
        r"""Sets the containercidrs of this ContainerNetworkUpdate.

        **参数解释：** 容器网络网段列表。当集群网络类型为vpc-router时，支持添加或删除容器网段。支持的集群版本如下： - v1.28.15-r60及以上版本 - v1.29.15-r20及以上版本 - v1.30.14-r20及以上版本 - v1.31.10-r20及以上版本 - v1.32.6-r20及以上版本 - v1.33.5-r10及以上版本  支持修改集群容器网段的顺序，顺序在前的容器网段优先被使用。 **约束限制：** - 最多支持配置20个子网。 - 填写为空时，该字段不生效。  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param containercidrs: The containercidrs of this ContainerNetworkUpdate.
        :type containercidrs: list[str]
        """
        self._containercidrs = containercidrs

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
        if not isinstance(other, ContainerNetworkUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
