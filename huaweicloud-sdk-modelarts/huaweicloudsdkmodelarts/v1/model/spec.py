# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Spec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'SpecResource',
        'volumes': 'list[SpecVolumes]',
        'log_export_path': 'LogExportPath',
        'auto_stop': 'AutoStop',
        'schedule_policy': 'SchedulePolicy',
        'log_export_config': 'LogExportConfig',
        'notification': 'Notification',
        'custom_metrics': 'list[CustomMetrics]',
        'output_model': 'OutputModel',
        'asset_model': 'AssetModel',
        'asset_id': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'volumes': 'volumes',
        'log_export_path': 'log_export_path',
        'auto_stop': 'auto_stop',
        'schedule_policy': 'schedule_policy',
        'log_export_config': 'log_export_config',
        'notification': 'notification',
        'custom_metrics': 'custom_metrics',
        'output_model': 'output_model',
        'asset_model': 'asset_model',
        'asset_id': 'asset_id'
    }

    def __init__(self, resource=None, volumes=None, log_export_path=None, auto_stop=None, schedule_policy=None, log_export_config=None, notification=None, custom_metrics=None, output_model=None, asset_model=None, asset_id=None):
        r"""Spec

        The model defined in huaweicloud sdk

        :param resource: 
        :type resource: :class:`huaweicloudsdkmodelarts.v1.SpecResource`
        :param volumes: **参数解释**：训练作业挂载卷信息。 **约束限制**：不涉及。
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.SpecVolumes`]
        :param log_export_path: 
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.LogExportPath`
        :param auto_stop: 
        :type auto_stop: :class:`huaweicloudsdkmodelarts.v1.AutoStop`
        :param schedule_policy: 
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicy`
        :param log_export_config: 
        :type log_export_config: :class:`huaweicloudsdkmodelarts.v1.LogExportConfig`
        :param notification: 
        :type notification: :class:`huaweicloudsdkmodelarts.v1.Notification`
        :param custom_metrics: **参数解释**：指标采集配置。
        :type custom_metrics: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        :param output_model: 
        :type output_model: :class:`huaweicloudsdkmodelarts.v1.OutputModel`
        :param asset_model: 
        :type asset_model: :class:`huaweicloudsdkmodelarts.v1.AssetModel`
        :param asset_id: **参数解释**：精调训练作业资产模型ID。
        :type asset_id: str
        """
        
        

        self._resource = None
        self._volumes = None
        self._log_export_path = None
        self._auto_stop = None
        self._schedule_policy = None
        self._log_export_config = None
        self._notification = None
        self._custom_metrics = None
        self._output_model = None
        self._asset_model = None
        self._asset_id = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if volumes is not None:
            self.volumes = volumes
        if log_export_path is not None:
            self.log_export_path = log_export_path
        if auto_stop is not None:
            self.auto_stop = auto_stop
        if schedule_policy is not None:
            self.schedule_policy = schedule_policy
        if log_export_config is not None:
            self.log_export_config = log_export_config
        if notification is not None:
            self.notification = notification
        if custom_metrics is not None:
            self.custom_metrics = custom_metrics
        if output_model is not None:
            self.output_model = output_model
        if asset_model is not None:
            self.asset_model = asset_model
        if asset_id is not None:
            self.asset_id = asset_id

    @property
    def resource(self):
        r"""Gets the resource of this Spec.

        :return: The resource of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SpecResource`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this Spec.

        :param resource: The resource of this Spec.
        :type resource: :class:`huaweicloudsdkmodelarts.v1.SpecResource`
        """
        self._resource = resource

    @property
    def volumes(self):
        r"""Gets the volumes of this Spec.

        **参数解释**：训练作业挂载卷信息。 **约束限制**：不涉及。

        :return: The volumes of this Spec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SpecVolumes`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this Spec.

        **参数解释**：训练作业挂载卷信息。 **约束限制**：不涉及。

        :param volumes: The volumes of this Spec.
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.SpecVolumes`]
        """
        self._volumes = volumes

    @property
    def log_export_path(self):
        r"""Gets the log_export_path of this Spec.

        :return: The log_export_path of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LogExportPath`
        """
        return self._log_export_path

    @log_export_path.setter
    def log_export_path(self, log_export_path):
        r"""Sets the log_export_path of this Spec.

        :param log_export_path: The log_export_path of this Spec.
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.LogExportPath`
        """
        self._log_export_path = log_export_path

    @property
    def auto_stop(self):
        r"""Gets the auto_stop of this Spec.

        :return: The auto_stop of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AutoStop`
        """
        return self._auto_stop

    @auto_stop.setter
    def auto_stop(self, auto_stop):
        r"""Sets the auto_stop of this Spec.

        :param auto_stop: The auto_stop of this Spec.
        :type auto_stop: :class:`huaweicloudsdkmodelarts.v1.AutoStop`
        """
        self._auto_stop = auto_stop

    @property
    def schedule_policy(self):
        r"""Gets the schedule_policy of this Spec.

        :return: The schedule_policy of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicy`
        """
        return self._schedule_policy

    @schedule_policy.setter
    def schedule_policy(self, schedule_policy):
        r"""Sets the schedule_policy of this Spec.

        :param schedule_policy: The schedule_policy of this Spec.
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicy`
        """
        self._schedule_policy = schedule_policy

    @property
    def log_export_config(self):
        r"""Gets the log_export_config of this Spec.

        :return: The log_export_config of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LogExportConfig`
        """
        return self._log_export_config

    @log_export_config.setter
    def log_export_config(self, log_export_config):
        r"""Sets the log_export_config of this Spec.

        :param log_export_config: The log_export_config of this Spec.
        :type log_export_config: :class:`huaweicloudsdkmodelarts.v1.LogExportConfig`
        """
        self._log_export_config = log_export_config

    @property
    def notification(self):
        r"""Gets the notification of this Spec.

        :return: The notification of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Notification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        r"""Sets the notification of this Spec.

        :param notification: The notification of this Spec.
        :type notification: :class:`huaweicloudsdkmodelarts.v1.Notification`
        """
        self._notification = notification

    @property
    def custom_metrics(self):
        r"""Gets the custom_metrics of this Spec.

        **参数解释**：指标采集配置。

        :return: The custom_metrics of this Spec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        """
        return self._custom_metrics

    @custom_metrics.setter
    def custom_metrics(self, custom_metrics):
        r"""Sets the custom_metrics of this Spec.

        **参数解释**：指标采集配置。

        :param custom_metrics: The custom_metrics of this Spec.
        :type custom_metrics: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        """
        self._custom_metrics = custom_metrics

    @property
    def output_model(self):
        r"""Gets the output_model of this Spec.

        :return: The output_model of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.OutputModel`
        """
        return self._output_model

    @output_model.setter
    def output_model(self, output_model):
        r"""Sets the output_model of this Spec.

        :param output_model: The output_model of this Spec.
        :type output_model: :class:`huaweicloudsdkmodelarts.v1.OutputModel`
        """
        self._output_model = output_model

    @property
    def asset_model(self):
        r"""Gets the asset_model of this Spec.

        :return: The asset_model of this Spec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AssetModel`
        """
        return self._asset_model

    @asset_model.setter
    def asset_model(self, asset_model):
        r"""Sets the asset_model of this Spec.

        :param asset_model: The asset_model of this Spec.
        :type asset_model: :class:`huaweicloudsdkmodelarts.v1.AssetModel`
        """
        self._asset_model = asset_model

    @property
    def asset_id(self):
        r"""Gets the asset_id of this Spec.

        **参数解释**：精调训练作业资产模型ID。

        :return: The asset_id of this Spec.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this Spec.

        **参数解释**：精调训练作业资产模型ID。

        :param asset_id: The asset_id of this Spec.
        :type asset_id: str
        """
        self._asset_id = asset_id

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
        if not isinstance(other, Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
