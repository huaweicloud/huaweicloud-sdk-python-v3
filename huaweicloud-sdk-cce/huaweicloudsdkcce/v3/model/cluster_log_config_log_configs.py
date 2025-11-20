# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterLogConfigLogConfigs:

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
        'enable': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable',
        'type': 'type'
    }

    def __init__(self, name=None, enable=None, type=None):
        r"""ClusterLogConfigLogConfigs

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 日志类型 **约束限制**： 必须为 **kube-apiserver**、**kube-controller-manager**、**kube-scheduler**、**audit** 或者系统插件名称 **取值范围**： - kube-apiserver：采集kube-apiserver组件日志 - kube-controller-manager：采集kube-controller-manager日志 - kube-scheduler：采集kube-scheduler日志 - audit：采集审计日志 - 系统插件名称：采集插件日志  **默认取值**： 不涉及
        :type name: str
        :param enable: **参数解释**： 是否采集 **约束限制**： 不涉及 **取值范围**： - true：开启日志采集 - false：关闭采集日志  **默认取值**： 不涉及 
        :type enable: bool
        :param type: **参数解释**： 组件类型 , 合法取值为control，audit，system-addon。 **约束限制**： - 仅组件类型为系统插件类型时返回该参数 - 作为**配置集群日志**接口更新参数时，如果要采集系统插件日志则必须声明为**system-addon**  **取值范围**： - control: 控制面组件日志。 - audit: 控制面审计日志。 - system-addon: 系统插件日志。  **默认取值**： 不涉及
        :type type: str
        """
        
        

        self._name = None
        self._enable = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this ClusterLogConfigLogConfigs.

        **参数解释**： 日志类型 **约束限制**： 必须为 **kube-apiserver**、**kube-controller-manager**、**kube-scheduler**、**audit** 或者系统插件名称 **取值范围**： - kube-apiserver：采集kube-apiserver组件日志 - kube-controller-manager：采集kube-controller-manager日志 - kube-scheduler：采集kube-scheduler日志 - audit：采集审计日志 - 系统插件名称：采集插件日志  **默认取值**： 不涉及

        :return: The name of this ClusterLogConfigLogConfigs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterLogConfigLogConfigs.

        **参数解释**： 日志类型 **约束限制**： 必须为 **kube-apiserver**、**kube-controller-manager**、**kube-scheduler**、**audit** 或者系统插件名称 **取值范围**： - kube-apiserver：采集kube-apiserver组件日志 - kube-controller-manager：采集kube-controller-manager日志 - kube-scheduler：采集kube-scheduler日志 - audit：采集审计日志 - 系统插件名称：采集插件日志  **默认取值**： 不涉及

        :param name: The name of this ClusterLogConfigLogConfigs.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this ClusterLogConfigLogConfigs.

        **参数解释**： 是否采集 **约束限制**： 不涉及 **取值范围**： - true：开启日志采集 - false：关闭采集日志  **默认取值**： 不涉及 

        :return: The enable of this ClusterLogConfigLogConfigs.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ClusterLogConfigLogConfigs.

        **参数解释**： 是否采集 **约束限制**： 不涉及 **取值范围**： - true：开启日志采集 - false：关闭采集日志  **默认取值**： 不涉及 

        :param enable: The enable of this ClusterLogConfigLogConfigs.
        :type enable: bool
        """
        self._enable = enable

    @property
    def type(self):
        r"""Gets the type of this ClusterLogConfigLogConfigs.

        **参数解释**： 组件类型 , 合法取值为control，audit，system-addon。 **约束限制**： - 仅组件类型为系统插件类型时返回该参数 - 作为**配置集群日志**接口更新参数时，如果要采集系统插件日志则必须声明为**system-addon**  **取值范围**： - control: 控制面组件日志。 - audit: 控制面审计日志。 - system-addon: 系统插件日志。  **默认取值**： 不涉及

        :return: The type of this ClusterLogConfigLogConfigs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterLogConfigLogConfigs.

        **参数解释**： 组件类型 , 合法取值为control，audit，system-addon。 **约束限制**： - 仅组件类型为系统插件类型时返回该参数 - 作为**配置集群日志**接口更新参数时，如果要采集系统插件日志则必须声明为**system-addon**  **取值范围**： - control: 控制面组件日志。 - audit: 控制面审计日志。 - system-addon: 系统插件日志。  **默认取值**： 不涉及

        :param type: The type of this ClusterLogConfigLogConfigs.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ClusterLogConfigLogConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
