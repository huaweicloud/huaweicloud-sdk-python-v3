# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'Resource',
        'volumes': 'list[JobVolumeResp]',
        'log_export_path': 'LogExportPathResp',
        'schedule_policy': 'SchedulePolicyResp',
        'custom_metrics': 'list[CustomMetrics]',
        'output_model': 'OutputModelResp',
        'asset_model': 'AssetModelResp'
    }

    attribute_map = {
        'resource': 'resource',
        'volumes': 'volumes',
        'log_export_path': 'log_export_path',
        'schedule_policy': 'schedule_policy',
        'custom_metrics': 'custom_metrics',
        'output_model': 'output_model',
        'asset_model': 'asset_model'
    }

    def __init__(self, resource=None, volumes=None, log_export_path=None, schedule_policy=None, custom_metrics=None, output_model=None, asset_model=None):
        r"""SpecResponse

        The model defined in huaweicloud sdk

        :param resource: 
        :type resource: :class:`huaweicloudsdkmodelarts.v1.Resource`
        :param volumes: **参数解释**：训练作业挂载卷信息。
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.JobVolumeResp`]
        :param log_export_path: 
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.LogExportPathResp`
        :param schedule_policy: 
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicyResp`
        :param custom_metrics: **参数解释**：指标采集配置。
        :type custom_metrics: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        :param output_model: 
        :type output_model: :class:`huaweicloudsdkmodelarts.v1.OutputModelResp`
        :param asset_model: 
        :type asset_model: :class:`huaweicloudsdkmodelarts.v1.AssetModelResp`
        """
        
        

        self._resource = None
        self._volumes = None
        self._log_export_path = None
        self._schedule_policy = None
        self._custom_metrics = None
        self._output_model = None
        self._asset_model = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if volumes is not None:
            self.volumes = volumes
        if log_export_path is not None:
            self.log_export_path = log_export_path
        if schedule_policy is not None:
            self.schedule_policy = schedule_policy
        if custom_metrics is not None:
            self.custom_metrics = custom_metrics
        if output_model is not None:
            self.output_model = output_model
        if asset_model is not None:
            self.asset_model = asset_model

    @property
    def resource(self):
        r"""Gets the resource of this SpecResponse.

        :return: The resource of this SpecResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Resource`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this SpecResponse.

        :param resource: The resource of this SpecResponse.
        :type resource: :class:`huaweicloudsdkmodelarts.v1.Resource`
        """
        self._resource = resource

    @property
    def volumes(self):
        r"""Gets the volumes of this SpecResponse.

        **参数解释**：训练作业挂载卷信息。

        :return: The volumes of this SpecResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobVolumeResp`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this SpecResponse.

        **参数解释**：训练作业挂载卷信息。

        :param volumes: The volumes of this SpecResponse.
        :type volumes: list[:class:`huaweicloudsdkmodelarts.v1.JobVolumeResp`]
        """
        self._volumes = volumes

    @property
    def log_export_path(self):
        r"""Gets the log_export_path of this SpecResponse.

        :return: The log_export_path of this SpecResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LogExportPathResp`
        """
        return self._log_export_path

    @log_export_path.setter
    def log_export_path(self, log_export_path):
        r"""Sets the log_export_path of this SpecResponse.

        :param log_export_path: The log_export_path of this SpecResponse.
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.LogExportPathResp`
        """
        self._log_export_path = log_export_path

    @property
    def schedule_policy(self):
        r"""Gets the schedule_policy of this SpecResponse.

        :return: The schedule_policy of this SpecResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicyResp`
        """
        return self._schedule_policy

    @schedule_policy.setter
    def schedule_policy(self, schedule_policy):
        r"""Sets the schedule_policy of this SpecResponse.

        :param schedule_policy: The schedule_policy of this SpecResponse.
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.SchedulePolicyResp`
        """
        self._schedule_policy = schedule_policy

    @property
    def custom_metrics(self):
        r"""Gets the custom_metrics of this SpecResponse.

        **参数解释**：指标采集配置。

        :return: The custom_metrics of this SpecResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        """
        return self._custom_metrics

    @custom_metrics.setter
    def custom_metrics(self, custom_metrics):
        r"""Sets the custom_metrics of this SpecResponse.

        **参数解释**：指标采集配置。

        :param custom_metrics: The custom_metrics of this SpecResponse.
        :type custom_metrics: list[:class:`huaweicloudsdkmodelarts.v1.CustomMetrics`]
        """
        self._custom_metrics = custom_metrics

    @property
    def output_model(self):
        r"""Gets the output_model of this SpecResponse.

        :return: The output_model of this SpecResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.OutputModelResp`
        """
        return self._output_model

    @output_model.setter
    def output_model(self, output_model):
        r"""Sets the output_model of this SpecResponse.

        :param output_model: The output_model of this SpecResponse.
        :type output_model: :class:`huaweicloudsdkmodelarts.v1.OutputModelResp`
        """
        self._output_model = output_model

    @property
    def asset_model(self):
        r"""Gets the asset_model of this SpecResponse.

        :return: The asset_model of this SpecResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AssetModelResp`
        """
        return self._asset_model

    @asset_model.setter
    def asset_model(self, asset_model):
        r"""Sets the asset_model of this SpecResponse.

        :param asset_model: The asset_model of this SpecResponse.
        :type asset_model: :class:`huaweicloudsdkmodelarts.v1.AssetModelResp`
        """
        self._asset_model = asset_model

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
        if not isinstance(other, SpecResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
