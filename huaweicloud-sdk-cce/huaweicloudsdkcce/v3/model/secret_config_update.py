# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretConfigUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable_default_addon_cred_secret': 'bool',
        'disable_node_agency_cred_secret': 'bool',
        'disable_default_image_pull_secret': 'bool'
    }

    attribute_map = {
        'disable_default_addon_cred_secret': 'disableDefaultAddonCredSecret',
        'disable_node_agency_cred_secret': 'disableNodeAgencyCredSecret',
        'disable_default_image_pull_secret': 'disableDefaultImagePullSecret'
    }

    def __init__(self, disable_default_addon_cred_secret=None, disable_node_agency_cred_secret=None, disable_default_image_pull_secret=None):
        r"""SecretConfigUpdate

        The model defined in huaweicloud sdk

        :param disable_default_addon_cred_secret: **参数解释：** 是否在集群中禁用默认插件凭证（paas.elb、paas.aksk secret）。该Secret的data内容是临时AK/SK数据，部分插件在未配置自定义委托时会使用它作为IAM凭证访问其他云服务。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 仅当集群中所有需要访问云服务的插件均已配置自定义委托后，才能禁用该Secret。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** 不涉及，未指定则不更新此参数。 
        :type disable_default_addon_cred_secret: bool
        :param disable_node_agency_cred_secret: **参数解释：** 是否在集群中禁用节点凭证（node-agency-cred secret）。该Secret的data内容是临时AK/SK数据，节点上安装的系统组件默认使用该凭证。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保已为每个节点/节点池配置委托，且委托至少具备cce:node:get、cce::assumeAgencyForPodIdentity权限，否则禁用该Secret会导致节点安装、运行异常。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 
        :type disable_node_agency_cred_secret: bool
        :param disable_default_image_pull_secret: **参数解释：** 是否在集群中禁用默认镜像访问凭证（default-secret secret）。该Secret的data内容是SWR临时登录指令，用于SWR的私有镜像拉取。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保集群中的工作负载不使用default-secret作为镜像拉取凭证（配置了镜像免密下载或者使用自定义镜像拉取凭证），否则禁用该Secret后可能会导致镜像拉取失败。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 
        :type disable_default_image_pull_secret: bool
        """
        
        

        self._disable_default_addon_cred_secret = None
        self._disable_node_agency_cred_secret = None
        self._disable_default_image_pull_secret = None
        self.discriminator = None

        if disable_default_addon_cred_secret is not None:
            self.disable_default_addon_cred_secret = disable_default_addon_cred_secret
        if disable_node_agency_cred_secret is not None:
            self.disable_node_agency_cred_secret = disable_node_agency_cred_secret
        if disable_default_image_pull_secret is not None:
            self.disable_default_image_pull_secret = disable_default_image_pull_secret

    @property
    def disable_default_addon_cred_secret(self):
        r"""Gets the disable_default_addon_cred_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用默认插件凭证（paas.elb、paas.aksk secret）。该Secret的data内容是临时AK/SK数据，部分插件在未配置自定义委托时会使用它作为IAM凭证访问其他云服务。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 仅当集群中所有需要访问云服务的插件均已配置自定义委托后，才能禁用该Secret。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** 不涉及，未指定则不更新此参数。 

        :return: The disable_default_addon_cred_secret of this SecretConfigUpdate.
        :rtype: bool
        """
        return self._disable_default_addon_cred_secret

    @disable_default_addon_cred_secret.setter
    def disable_default_addon_cred_secret(self, disable_default_addon_cred_secret):
        r"""Sets the disable_default_addon_cred_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用默认插件凭证（paas.elb、paas.aksk secret）。该Secret的data内容是临时AK/SK数据，部分插件在未配置自定义委托时会使用它作为IAM凭证访问其他云服务。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 仅当集群中所有需要访问云服务的插件均已配置自定义委托后，才能禁用该Secret。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** 不涉及，未指定则不更新此参数。 

        :param disable_default_addon_cred_secret: The disable_default_addon_cred_secret of this SecretConfigUpdate.
        :type disable_default_addon_cred_secret: bool
        """
        self._disable_default_addon_cred_secret = disable_default_addon_cred_secret

    @property
    def disable_node_agency_cred_secret(self):
        r"""Gets the disable_node_agency_cred_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用节点凭证（node-agency-cred secret）。该Secret的data内容是临时AK/SK数据，节点上安装的系统组件默认使用该凭证。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保已为每个节点/节点池配置委托，且委托至少具备cce:node:get、cce::assumeAgencyForPodIdentity权限，否则禁用该Secret会导致节点安装、运行异常。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 

        :return: The disable_node_agency_cred_secret of this SecretConfigUpdate.
        :rtype: bool
        """
        return self._disable_node_agency_cred_secret

    @disable_node_agency_cred_secret.setter
    def disable_node_agency_cred_secret(self, disable_node_agency_cred_secret):
        r"""Sets the disable_node_agency_cred_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用节点凭证（node-agency-cred secret）。该Secret的data内容是临时AK/SK数据，节点上安装的系统组件默认使用该凭证。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保已为每个节点/节点池配置委托，且委托至少具备cce:node:get、cce::assumeAgencyForPodIdentity权限，否则禁用该Secret会导致节点安装、运行异常。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 

        :param disable_node_agency_cred_secret: The disable_node_agency_cred_secret of this SecretConfigUpdate.
        :type disable_node_agency_cred_secret: bool
        """
        self._disable_node_agency_cred_secret = disable_node_agency_cred_secret

    @property
    def disable_default_image_pull_secret(self):
        r"""Gets the disable_default_image_pull_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用默认镜像访问凭证（default-secret secret）。该Secret的data内容是SWR临时登录指令，用于SWR的私有镜像拉取。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保集群中的工作负载不使用default-secret作为镜像拉取凭证（配置了镜像免密下载或者使用自定义镜像拉取凭证），否则禁用该Secret后可能会导致镜像拉取失败。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 

        :return: The disable_default_image_pull_secret of this SecretConfigUpdate.
        :rtype: bool
        """
        return self._disable_default_image_pull_secret

    @disable_default_image_pull_secret.setter
    def disable_default_image_pull_secret(self, disable_default_image_pull_secret):
        r"""Sets the disable_default_image_pull_secret of this SecretConfigUpdate.

        **参数解释：** 是否在集群中禁用默认镜像访问凭证（default-secret secret）。该Secret的data内容是SWR临时登录指令，用于SWR的私有镜像拉取。 [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/usermanual-cce/cce_10_1111.html)。](tag:hws) [更多信息请参见[禁用集群中静态存储的临时凭据说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_1111.html)。](tag:hws_hk) **约束限制：** 需确保集群中的工作负载不使用default-secret作为镜像拉取凭证（配置了镜像免密下载或者使用自定义镜像拉取凭证），否则禁用该Secret后可能会导致镜像拉取失败。 **取值范围：** - true: 禁用 - false: 启用  **默认取值：** false 

        :param disable_default_image_pull_secret: The disable_default_image_pull_secret of this SecretConfigUpdate.
        :type disable_default_image_pull_secret: bool
        """
        self._disable_default_image_pull_secret = disable_default_image_pull_secret

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
        if not isinstance(other, SecretConfigUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
