# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonCheckSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'addon_list': 'list[AddonInfo]'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'addon_list': 'addonList'
    }

    def __init__(self, cluster_id=None, addon_list=None):
        r"""AddonCheckSpec

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释：** 集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type cluster_id: str
        :param addon_list: **参数解释：** 插件检查信息列表，包含了需要检查的插件模板名称，插件实例ID，插件升级配置等。 **约束限制：** 不涉及 
        :type addon_list: list[:class:`huaweicloudsdkcce.v3.AddonInfo`]
        """
        
        

        self._cluster_id = None
        self._addon_list = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.addon_list = addon_list

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this AddonCheckSpec.

        **参数解释：** 集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The cluster_id of this AddonCheckSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this AddonCheckSpec.

        **参数解释：** 集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param cluster_id: The cluster_id of this AddonCheckSpec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def addon_list(self):
        r"""Gets the addon_list of this AddonCheckSpec.

        **参数解释：** 插件检查信息列表，包含了需要检查的插件模板名称，插件实例ID，插件升级配置等。 **约束限制：** 不涉及 

        :return: The addon_list of this AddonCheckSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AddonInfo`]
        """
        return self._addon_list

    @addon_list.setter
    def addon_list(self, addon_list):
        r"""Sets the addon_list of this AddonCheckSpec.

        **参数解释：** 插件检查信息列表，包含了需要检查的插件模板名称，插件实例ID，插件升级配置等。 **约束限制：** 不涉及 

        :param addon_list: The addon_list of this AddonCheckSpec.
        :type addon_list: list[:class:`huaweicloudsdkcce.v3.AddonInfo`]
        """
        self._addon_list = addon_list

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
        if not isinstance(other, AddonCheckSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
