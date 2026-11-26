# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReplicationPolicyRequestBody:

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
        'description': 'str',
        'src_registry': 'ReplicationRegistry',
        'dest_registry': 'ReplicationRegistry',
        'dest_namespace': 'str',
        'dest_namespace_replace_count': 'int',
        'filters': 'list[Filter]',
        'repo_scope_mode': 'str',
        'trigger': 'TriggerConfig',
        'override': 'bool',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'src_registry': 'src_registry',
        'dest_registry': 'dest_registry',
        'dest_namespace': 'dest_namespace',
        'dest_namespace_replace_count': 'dest_namespace_replace_count',
        'filters': 'filters',
        'repo_scope_mode': 'repo_scope_mode',
        'trigger': 'trigger',
        'override': 'override',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, src_registry=None, dest_registry=None, dest_namespace=None, dest_namespace_replace_count=None, filters=None, repo_scope_mode=None, trigger=None, override=None, enabled=None):
        r"""CreateReplicationPolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 策略名称, 1-256字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。
        :type name: str
        :param description: 策略描述
        :type description: str
        :param src_registry: 
        :type src_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        :param dest_registry: 
        :type dest_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        :param dest_namespace: 目标命名空间名，默认值为空值
        :type dest_namespace: str
        :param dest_namespace_replace_count: 在镜像复制过程中，针对多路径镜像名称，可通过设置替换层级来优化仓库目录结构。支持的值为-1,0,1,2,3。dest_namespace_replace_count不传值，则默认为-1。假设原始镜像路径为 a/b/c/d/img，其中a为原始镜像的命名空间名称，目标命名空间为 ns，不同替换级别的效果如下： -1：替换所有级：&#39;a/b/c/d/img&#39; -&gt; &#39;ns/img&#39; 0：无替换：&#39;a/b/c/d/img&#39; -&gt; &#39;ns/a/b/c/d/img&#39; 1：替换1级：&#39;a/b/c/d/img&#39; -&gt; &#39;ns/b/c/d/img&#39; 2：替换2级：&#39;a/b/c/d/img&#39; -&gt; &#39;ns/c/d/img&#39; 3：替换3级：&#39;a/b/c/d/img&#39; -&gt; &#39;ns/d/img&#39;
        :type dest_namespace_replace_count: int
        :param filters: 过滤器（目前只支持harbor类型的仓库）
        :type filters: list[:class:`huaweicloudsdkswr.v2.Filter`]
        :param repo_scope_mode: repo的选择方式，regular，selection
        :type repo_scope_mode: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param override: 是否覆盖，默认为false
        :type override: bool
        :param enabled: 是否启用，默认为false
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._src_registry = None
        self._dest_registry = None
        self._dest_namespace = None
        self._dest_namespace_replace_count = None
        self._filters = None
        self._repo_scope_mode = None
        self._trigger = None
        self._override = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if src_registry is not None:
            self.src_registry = src_registry
        if dest_registry is not None:
            self.dest_registry = dest_registry
        if dest_namespace is not None:
            self.dest_namespace = dest_namespace
        if dest_namespace_replace_count is not None:
            self.dest_namespace_replace_count = dest_namespace_replace_count
        self.filters = filters
        self.repo_scope_mode = repo_scope_mode
        self.trigger = trigger
        if override is not None:
            self.override = override
        self.enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this CreateReplicationPolicyRequestBody.

        策略名称, 1-256字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。

        :return: The name of this CreateReplicationPolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateReplicationPolicyRequestBody.

        策略名称, 1-256字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。

        :param name: The name of this CreateReplicationPolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateReplicationPolicyRequestBody.

        策略描述

        :return: The description of this CreateReplicationPolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateReplicationPolicyRequestBody.

        策略描述

        :param description: The description of this CreateReplicationPolicyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def src_registry(self):
        r"""Gets the src_registry of this CreateReplicationPolicyRequestBody.

        :return: The src_registry of this CreateReplicationPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        return self._src_registry

    @src_registry.setter
    def src_registry(self, src_registry):
        r"""Sets the src_registry of this CreateReplicationPolicyRequestBody.

        :param src_registry: The src_registry of this CreateReplicationPolicyRequestBody.
        :type src_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        self._src_registry = src_registry

    @property
    def dest_registry(self):
        r"""Gets the dest_registry of this CreateReplicationPolicyRequestBody.

        :return: The dest_registry of this CreateReplicationPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        return self._dest_registry

    @dest_registry.setter
    def dest_registry(self, dest_registry):
        r"""Sets the dest_registry of this CreateReplicationPolicyRequestBody.

        :param dest_registry: The dest_registry of this CreateReplicationPolicyRequestBody.
        :type dest_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        self._dest_registry = dest_registry

    @property
    def dest_namespace(self):
        r"""Gets the dest_namespace of this CreateReplicationPolicyRequestBody.

        目标命名空间名，默认值为空值

        :return: The dest_namespace of this CreateReplicationPolicyRequestBody.
        :rtype: str
        """
        return self._dest_namespace

    @dest_namespace.setter
    def dest_namespace(self, dest_namespace):
        r"""Sets the dest_namespace of this CreateReplicationPolicyRequestBody.

        目标命名空间名，默认值为空值

        :param dest_namespace: The dest_namespace of this CreateReplicationPolicyRequestBody.
        :type dest_namespace: str
        """
        self._dest_namespace = dest_namespace

    @property
    def dest_namespace_replace_count(self):
        r"""Gets the dest_namespace_replace_count of this CreateReplicationPolicyRequestBody.

        在镜像复制过程中，针对多路径镜像名称，可通过设置替换层级来优化仓库目录结构。支持的值为-1,0,1,2,3。dest_namespace_replace_count不传值，则默认为-1。假设原始镜像路径为 a/b/c/d/img，其中a为原始镜像的命名空间名称，目标命名空间为 ns，不同替换级别的效果如下： -1：替换所有级：'a/b/c/d/img' -> 'ns/img' 0：无替换：'a/b/c/d/img' -> 'ns/a/b/c/d/img' 1：替换1级：'a/b/c/d/img' -> 'ns/b/c/d/img' 2：替换2级：'a/b/c/d/img' -> 'ns/c/d/img' 3：替换3级：'a/b/c/d/img' -> 'ns/d/img'

        :return: The dest_namespace_replace_count of this CreateReplicationPolicyRequestBody.
        :rtype: int
        """
        return self._dest_namespace_replace_count

    @dest_namespace_replace_count.setter
    def dest_namespace_replace_count(self, dest_namespace_replace_count):
        r"""Sets the dest_namespace_replace_count of this CreateReplicationPolicyRequestBody.

        在镜像复制过程中，针对多路径镜像名称，可通过设置替换层级来优化仓库目录结构。支持的值为-1,0,1,2,3。dest_namespace_replace_count不传值，则默认为-1。假设原始镜像路径为 a/b/c/d/img，其中a为原始镜像的命名空间名称，目标命名空间为 ns，不同替换级别的效果如下： -1：替换所有级：'a/b/c/d/img' -> 'ns/img' 0：无替换：'a/b/c/d/img' -> 'ns/a/b/c/d/img' 1：替换1级：'a/b/c/d/img' -> 'ns/b/c/d/img' 2：替换2级：'a/b/c/d/img' -> 'ns/c/d/img' 3：替换3级：'a/b/c/d/img' -> 'ns/d/img'

        :param dest_namespace_replace_count: The dest_namespace_replace_count of this CreateReplicationPolicyRequestBody.
        :type dest_namespace_replace_count: int
        """
        self._dest_namespace_replace_count = dest_namespace_replace_count

    @property
    def filters(self):
        r"""Gets the filters of this CreateReplicationPolicyRequestBody.

        过滤器（目前只支持harbor类型的仓库）

        :return: The filters of this CreateReplicationPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Filter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this CreateReplicationPolicyRequestBody.

        过滤器（目前只支持harbor类型的仓库）

        :param filters: The filters of this CreateReplicationPolicyRequestBody.
        :type filters: list[:class:`huaweicloudsdkswr.v2.Filter`]
        """
        self._filters = filters

    @property
    def repo_scope_mode(self):
        r"""Gets the repo_scope_mode of this CreateReplicationPolicyRequestBody.

        repo的选择方式，regular，selection

        :return: The repo_scope_mode of this CreateReplicationPolicyRequestBody.
        :rtype: str
        """
        return self._repo_scope_mode

    @repo_scope_mode.setter
    def repo_scope_mode(self, repo_scope_mode):
        r"""Sets the repo_scope_mode of this CreateReplicationPolicyRequestBody.

        repo的选择方式，regular，selection

        :param repo_scope_mode: The repo_scope_mode of this CreateReplicationPolicyRequestBody.
        :type repo_scope_mode: str
        """
        self._repo_scope_mode = repo_scope_mode

    @property
    def trigger(self):
        r"""Gets the trigger of this CreateReplicationPolicyRequestBody.

        :return: The trigger of this CreateReplicationPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this CreateReplicationPolicyRequestBody.

        :param trigger: The trigger of this CreateReplicationPolicyRequestBody.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def override(self):
        r"""Gets the override of this CreateReplicationPolicyRequestBody.

        是否覆盖，默认为false

        :return: The override of this CreateReplicationPolicyRequestBody.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this CreateReplicationPolicyRequestBody.

        是否覆盖，默认为false

        :param override: The override of this CreateReplicationPolicyRequestBody.
        :type override: bool
        """
        self._override = override

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateReplicationPolicyRequestBody.

        是否启用，默认为false

        :return: The enabled of this CreateReplicationPolicyRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateReplicationPolicyRequestBody.

        是否启用，默认为false

        :param enabled: The enabled of this CreateReplicationPolicyRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, CreateReplicationPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
