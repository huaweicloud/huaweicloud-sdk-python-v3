# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecModelDataVolumesExtendParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing': 'str',
        'volume_group': 'str'
    }

    attribute_map = {
        'billing': 'billing',
        'volume_group': 'volumeGroup'
    }

    def __init__(self, billing=None, volume_group=None):
        r"""PoolSpecModelDataVolumesExtendParams

        The model defined in huaweicloud sdk

        :param billing: **参数解释**：标识存储实例是否计费。为空则表示不计费。该字段用户不可指定或修改。 **取值范围**：不涉及。
        :type billing: str
        :param volume_group: **参数解释**：磁盘分组名称，用于各个存储空间的划分。 **取值范围**：可选项如下： - vgpaas：容器盘。 - default：普通数据盘，以默认方式挂载。 - vguser{num}：普通数据盘，指定挂载路径，不同路径的分组名称不同，如vguser1，vguser2。 - vg-everest-localvolume-persistent：普通数据盘，作为持久存储卷 - vg-everest-localvolume-ephemeral：普通数据盘，作为临时存储卷
        :type volume_group: str
        """
        
        

        self._billing = None
        self._volume_group = None
        self.discriminator = None

        if billing is not None:
            self.billing = billing
        if volume_group is not None:
            self.volume_group = volume_group

    @property
    def billing(self):
        r"""Gets the billing of this PoolSpecModelDataVolumesExtendParams.

        **参数解释**：标识存储实例是否计费。为空则表示不计费。该字段用户不可指定或修改。 **取值范围**：不涉及。

        :return: The billing of this PoolSpecModelDataVolumesExtendParams.
        :rtype: str
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this PoolSpecModelDataVolumesExtendParams.

        **参数解释**：标识存储实例是否计费。为空则表示不计费。该字段用户不可指定或修改。 **取值范围**：不涉及。

        :param billing: The billing of this PoolSpecModelDataVolumesExtendParams.
        :type billing: str
        """
        self._billing = billing

    @property
    def volume_group(self):
        r"""Gets the volume_group of this PoolSpecModelDataVolumesExtendParams.

        **参数解释**：磁盘分组名称，用于各个存储空间的划分。 **取值范围**：可选项如下： - vgpaas：容器盘。 - default：普通数据盘，以默认方式挂载。 - vguser{num}：普通数据盘，指定挂载路径，不同路径的分组名称不同，如vguser1，vguser2。 - vg-everest-localvolume-persistent：普通数据盘，作为持久存储卷 - vg-everest-localvolume-ephemeral：普通数据盘，作为临时存储卷

        :return: The volume_group of this PoolSpecModelDataVolumesExtendParams.
        :rtype: str
        """
        return self._volume_group

    @volume_group.setter
    def volume_group(self, volume_group):
        r"""Sets the volume_group of this PoolSpecModelDataVolumesExtendParams.

        **参数解释**：磁盘分组名称，用于各个存储空间的划分。 **取值范围**：可选项如下： - vgpaas：容器盘。 - default：普通数据盘，以默认方式挂载。 - vguser{num}：普通数据盘，指定挂载路径，不同路径的分组名称不同，如vguser1，vguser2。 - vg-everest-localvolume-persistent：普通数据盘，作为持久存储卷 - vg-everest-localvolume-ephemeral：普通数据盘，作为临时存储卷

        :param volume_group: The volume_group of this PoolSpecModelDataVolumesExtendParams.
        :type volume_group: str
        """
        self._volume_group = volume_group

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
        if not isinstance(other, PoolSpecModelDataVolumesExtendParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
