# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunFlinkJobRequestBody:

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
        'endpoint_name': 'str',
        'job_config': 'FlinkJobArtifact',
        'deployment_id': 'str',
        'job_agency': 'str',
        'flink_config': 'dict(str, str)',
        'autoscaling_policy': 'AutoscalingPolicy',
        'image_config': 'FlinkJobImageConfig',
        'resource_config': 'FlinkResourceConfig',
        'execution_mode': 'FlinkJobExecutionMode',
        'restore_strategy': 'RestoreStrategy',
        'logging_config': 'FlinkLoggingConfig',
        'labels': 'list[FlinkLabel]',
        'description': 'str',
        'alert_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'job_config': 'job_config',
        'deployment_id': 'deployment_id',
        'job_agency': 'job_agency',
        'flink_config': 'flink_config',
        'autoscaling_policy': 'autoscaling_policy',
        'image_config': 'image_config',
        'resource_config': 'resource_config',
        'execution_mode': 'execution_mode',
        'restore_strategy': 'restore_strategy',
        'logging_config': 'logging_config',
        'labels': 'labels',
        'description': 'description',
        'alert_enabled': 'alert_enabled'
    }

    def __init__(self, name=None, endpoint_name=None, job_config=None, deployment_id=None, job_agency=None, flink_config=None, autoscaling_policy=None, image_config=None, resource_config=None, execution_mode=None, restore_strategy=None, logging_config=None, labels=None, description=None, alert_enabled=None):
        r"""RunFlinkJobRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：作业名称，用于标识Flink作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。
        :type name: str
        :param endpoint_name: **参数解释**：作业运行的端点名称，用于指定作业执行环境。可通过[查询端点列表](ListV2Endpoints.xml)或[查询所有端点列表](ListV2AllEndpoints.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.FlinkJobArtifact`
        :param deployment_id: **参数解释**：已部署作业ID，用于关联聚合Flink实例。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。
        :type deployment_id: str
        :param job_agency: **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源。 **约束限制**：须为当前租户下已存在的委托，系统管理委托不可用于提交作业。 **取值范围**：长度为1~64个字符，字符组成不限制。 **默认取值**：不指定时默认使用端点作业委托。
        :type job_agency: str
        :param flink_config: **参数解释**：用户自定义的Flink配置参数，为键值对形式。最多支持100个参数，每个值长度为1~1024个字符。不允许配置execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir等系统保留参数，上述系统保留参数由平台根据端点配置自动填充并在查询响应中返回，无需用户配置。 **约束限制**：不涉及。
        :type flink_config: dict(str, str)
        :param autoscaling_policy: 
        :type autoscaling_policy: :class:`huaweicloudsdkaidatalake.v2.AutoscalingPolicy`
        :param image_config: 
        :type image_config: :class:`huaweicloudsdkaidatalake.v2.FlinkJobImageConfig`
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceConfig`
        :param execution_mode: 
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        :param restore_strategy: 
        :type restore_strategy: :class:`huaweicloudsdkaidatalake.v2.RestoreStrategy`
        :param logging_config: 
        :type logging_config: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggingConfig`
        :param labels: **参数解释**：标签，用于作业分类和筛选。 **约束限制**：标签数量不能超过16条。
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        :param description: **参数解释**：描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。
        :type description: str
        :param alert_enabled: **参数解释**：是否对该作业开启失败告警通知，用于按作业控制是否向客户发送告警消息。 **约束限制**：仅提交作业时指定，作业运行期间不支持修改。 **取值范围**：   - true：开启。作业运行失败或提交失败时，通过消息中心向客户发送告警通知。   - false：关闭。该作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭（不发送该作业的失败告警通知），需要告警时显式指定为 true。
        :type alert_enabled: bool
        """
        
        

        self._name = None
        self._endpoint_name = None
        self._job_config = None
        self._deployment_id = None
        self._job_agency = None
        self._flink_config = None
        self._autoscaling_policy = None
        self._image_config = None
        self._resource_config = None
        self._execution_mode = None
        self._restore_strategy = None
        self._logging_config = None
        self._labels = None
        self._description = None
        self._alert_enabled = None
        self.discriminator = None

        self.name = name
        self.endpoint_name = endpoint_name
        self.job_config = job_config
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if job_agency is not None:
            self.job_agency = job_agency
        if flink_config is not None:
            self.flink_config = flink_config
        if autoscaling_policy is not None:
            self.autoscaling_policy = autoscaling_policy
        if image_config is not None:
            self.image_config = image_config
        if resource_config is not None:
            self.resource_config = resource_config
        if execution_mode is not None:
            self.execution_mode = execution_mode
        if restore_strategy is not None:
            self.restore_strategy = restore_strategy
        if logging_config is not None:
            self.logging_config = logging_config
        if labels is not None:
            self.labels = labels
        if description is not None:
            self.description = description
        if alert_enabled is not None:
            self.alert_enabled = alert_enabled

    @property
    def name(self):
        r"""Gets the name of this RunFlinkJobRequestBody.

        **参数解释**：作业名称，用于标识Flink作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。

        :return: The name of this RunFlinkJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunFlinkJobRequestBody.

        **参数解释**：作业名称，用于标识Flink作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。

        :param name: The name of this RunFlinkJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RunFlinkJobRequestBody.

        **参数解释**：作业运行的端点名称，用于指定作业执行环境。可通过[查询端点列表](ListV2Endpoints.xml)或[查询所有端点列表](ListV2AllEndpoints.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this RunFlinkJobRequestBody.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RunFlinkJobRequestBody.

        **参数解释**：作业运行的端点名称，用于指定作业执行环境。可通过[查询端点列表](ListV2Endpoints.xml)或[查询所有端点列表](ListV2AllEndpoints.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this RunFlinkJobRequestBody.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def job_config(self):
        r"""Gets the job_config of this RunFlinkJobRequestBody.

        :return: The job_config of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobArtifact`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this RunFlinkJobRequestBody.

        :param job_config: The job_config of this RunFlinkJobRequestBody.
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.FlinkJobArtifact`
        """
        self._job_config = job_config

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this RunFlinkJobRequestBody.

        **参数解释**：已部署作业ID，用于关联聚合Flink实例。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。

        :return: The deployment_id of this RunFlinkJobRequestBody.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this RunFlinkJobRequestBody.

        **参数解释**：已部署作业ID，用于关联聚合Flink实例。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。

        :param deployment_id: The deployment_id of this RunFlinkJobRequestBody.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def job_agency(self):
        r"""Gets the job_agency of this RunFlinkJobRequestBody.

        **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源。 **约束限制**：须为当前租户下已存在的委托，系统管理委托不可用于提交作业。 **取值范围**：长度为1~64个字符，字符组成不限制。 **默认取值**：不指定时默认使用端点作业委托。

        :return: The job_agency of this RunFlinkJobRequestBody.
        :rtype: str
        """
        return self._job_agency

    @job_agency.setter
    def job_agency(self, job_agency):
        r"""Sets the job_agency of this RunFlinkJobRequestBody.

        **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源。 **约束限制**：须为当前租户下已存在的委托，系统管理委托不可用于提交作业。 **取值范围**：长度为1~64个字符，字符组成不限制。 **默认取值**：不指定时默认使用端点作业委托。

        :param job_agency: The job_agency of this RunFlinkJobRequestBody.
        :type job_agency: str
        """
        self._job_agency = job_agency

    @property
    def flink_config(self):
        r"""Gets the flink_config of this RunFlinkJobRequestBody.

        **参数解释**：用户自定义的Flink配置参数，为键值对形式。最多支持100个参数，每个值长度为1~1024个字符。不允许配置execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir等系统保留参数，上述系统保留参数由平台根据端点配置自动填充并在查询响应中返回，无需用户配置。 **约束限制**：不涉及。

        :return: The flink_config of this RunFlinkJobRequestBody.
        :rtype: dict(str, str)
        """
        return self._flink_config

    @flink_config.setter
    def flink_config(self, flink_config):
        r"""Sets the flink_config of this RunFlinkJobRequestBody.

        **参数解释**：用户自定义的Flink配置参数，为键值对形式。最多支持100个参数，每个值长度为1~1024个字符。不允许配置execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir等系统保留参数，上述系统保留参数由平台根据端点配置自动填充并在查询响应中返回，无需用户配置。 **约束限制**：不涉及。

        :param flink_config: The flink_config of this RunFlinkJobRequestBody.
        :type flink_config: dict(str, str)
        """
        self._flink_config = flink_config

    @property
    def autoscaling_policy(self):
        r"""Gets the autoscaling_policy of this RunFlinkJobRequestBody.

        :return: The autoscaling_policy of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AutoscalingPolicy`
        """
        return self._autoscaling_policy

    @autoscaling_policy.setter
    def autoscaling_policy(self, autoscaling_policy):
        r"""Sets the autoscaling_policy of this RunFlinkJobRequestBody.

        :param autoscaling_policy: The autoscaling_policy of this RunFlinkJobRequestBody.
        :type autoscaling_policy: :class:`huaweicloudsdkaidatalake.v2.AutoscalingPolicy`
        """
        self._autoscaling_policy = autoscaling_policy

    @property
    def image_config(self):
        r"""Gets the image_config of this RunFlinkJobRequestBody.

        :return: The image_config of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobImageConfig`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        r"""Sets the image_config of this RunFlinkJobRequestBody.

        :param image_config: The image_config of this RunFlinkJobRequestBody.
        :type image_config: :class:`huaweicloudsdkaidatalake.v2.FlinkJobImageConfig`
        """
        self._image_config = image_config

    @property
    def resource_config(self):
        r"""Gets the resource_config of this RunFlinkJobRequestBody.

        :return: The resource_config of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this RunFlinkJobRequestBody.

        :param resource_config: The resource_config of this RunFlinkJobRequestBody.
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceConfig`
        """
        self._resource_config = resource_config

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this RunFlinkJobRequestBody.

        :return: The execution_mode of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this RunFlinkJobRequestBody.

        :param execution_mode: The execution_mode of this RunFlinkJobRequestBody.
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        self._execution_mode = execution_mode

    @property
    def restore_strategy(self):
        r"""Gets the restore_strategy of this RunFlinkJobRequestBody.

        :return: The restore_strategy of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RestoreStrategy`
        """
        return self._restore_strategy

    @restore_strategy.setter
    def restore_strategy(self, restore_strategy):
        r"""Sets the restore_strategy of this RunFlinkJobRequestBody.

        :param restore_strategy: The restore_strategy of this RunFlinkJobRequestBody.
        :type restore_strategy: :class:`huaweicloudsdkaidatalake.v2.RestoreStrategy`
        """
        self._restore_strategy = restore_strategy

    @property
    def logging_config(self):
        r"""Gets the logging_config of this RunFlinkJobRequestBody.

        :return: The logging_config of this RunFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggingConfig`
        """
        return self._logging_config

    @logging_config.setter
    def logging_config(self, logging_config):
        r"""Sets the logging_config of this RunFlinkJobRequestBody.

        :param logging_config: The logging_config of this RunFlinkJobRequestBody.
        :type logging_config: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggingConfig`
        """
        self._logging_config = logging_config

    @property
    def labels(self):
        r"""Gets the labels of this RunFlinkJobRequestBody.

        **参数解释**：标签，用于作业分类和筛选。 **约束限制**：标签数量不能超过16条。

        :return: The labels of this RunFlinkJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this RunFlinkJobRequestBody.

        **参数解释**：标签，用于作业分类和筛选。 **约束限制**：标签数量不能超过16条。

        :param labels: The labels of this RunFlinkJobRequestBody.
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        """
        self._labels = labels

    @property
    def description(self):
        r"""Gets the description of this RunFlinkJobRequestBody.

        **参数解释**：描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :return: The description of this RunFlinkJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunFlinkJobRequestBody.

        **参数解释**：描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :param description: The description of this RunFlinkJobRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def alert_enabled(self):
        r"""Gets the alert_enabled of this RunFlinkJobRequestBody.

        **参数解释**：是否对该作业开启失败告警通知，用于按作业控制是否向客户发送告警消息。 **约束限制**：仅提交作业时指定，作业运行期间不支持修改。 **取值范围**：   - true：开启。作业运行失败或提交失败时，通过消息中心向客户发送告警通知。   - false：关闭。该作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭（不发送该作业的失败告警通知），需要告警时显式指定为 true。

        :return: The alert_enabled of this RunFlinkJobRequestBody.
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        r"""Sets the alert_enabled of this RunFlinkJobRequestBody.

        **参数解释**：是否对该作业开启失败告警通知，用于按作业控制是否向客户发送告警消息。 **约束限制**：仅提交作业时指定，作业运行期间不支持修改。 **取值范围**：   - true：开启。作业运行失败或提交失败时，通过消息中心向客户发送告警通知。   - false：关闭。该作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭（不发送该作业的失败告警通知），需要告警时显式指定为 true。

        :param alert_enabled: The alert_enabled of this RunFlinkJobRequestBody.
        :type alert_enabled: bool
        """
        self._alert_enabled = alert_enabled

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
        if not isinstance(other, RunFlinkJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
