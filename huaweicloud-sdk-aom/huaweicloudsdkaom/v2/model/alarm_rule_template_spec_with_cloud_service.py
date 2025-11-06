# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRuleTemplateSpecWithCloudService:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_cloud_service': 'str',
        'related_cce_clusters': 'list[str]',
        'related_prometheus_instances': 'list[str]',
        'alarm_notification': 'AlarmNotification',
        'alarm_template_spec_items': 'list[AlarmTemplateSpecItem]'
    }

    attribute_map = {
        'related_cloud_service': 'related_cloud_service',
        'related_cce_clusters': 'related_cce_clusters',
        'related_prometheus_instances': 'related_prometheus_instances',
        'alarm_notification': 'alarm_notification',
        'alarm_template_spec_items': 'alarm_template_spec_items'
    }

    def __init__(self, related_cloud_service=None, related_cce_clusters=None, related_prometheus_instances=None, alarm_notification=None, alarm_template_spec_items=None):
        r"""AlarmRuleTemplateSpecWithCloudService

        The model defined in huaweicloud sdk

        :param related_cloud_service: 关联的云服务。
        :type related_cloud_service: str
        :param related_cce_clusters: 关联的CCE集群。
        :type related_cce_clusters: list[str]
        :param related_prometheus_instances: 关联的Prom实例。
        :type related_prometheus_instances: list[str]
        :param alarm_notification: 
        :type alarm_notification: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        :param alarm_template_spec_items: 告警模板列表。
        :type alarm_template_spec_items: list[:class:`huaweicloudsdkaom.v2.AlarmTemplateSpecItem`]
        """
        
        

        self._related_cloud_service = None
        self._related_cce_clusters = None
        self._related_prometheus_instances = None
        self._alarm_notification = None
        self._alarm_template_spec_items = None
        self.discriminator = None

        if related_cloud_service is not None:
            self.related_cloud_service = related_cloud_service
        if related_cce_clusters is not None:
            self.related_cce_clusters = related_cce_clusters
        if related_prometheus_instances is not None:
            self.related_prometheus_instances = related_prometheus_instances
        if alarm_notification is not None:
            self.alarm_notification = alarm_notification
        if alarm_template_spec_items is not None:
            self.alarm_template_spec_items = alarm_template_spec_items

    @property
    def related_cloud_service(self):
        r"""Gets the related_cloud_service of this AlarmRuleTemplateSpecWithCloudService.

        关联的云服务。

        :return: The related_cloud_service of this AlarmRuleTemplateSpecWithCloudService.
        :rtype: str
        """
        return self._related_cloud_service

    @related_cloud_service.setter
    def related_cloud_service(self, related_cloud_service):
        r"""Sets the related_cloud_service of this AlarmRuleTemplateSpecWithCloudService.

        关联的云服务。

        :param related_cloud_service: The related_cloud_service of this AlarmRuleTemplateSpecWithCloudService.
        :type related_cloud_service: str
        """
        self._related_cloud_service = related_cloud_service

    @property
    def related_cce_clusters(self):
        r"""Gets the related_cce_clusters of this AlarmRuleTemplateSpecWithCloudService.

        关联的CCE集群。

        :return: The related_cce_clusters of this AlarmRuleTemplateSpecWithCloudService.
        :rtype: list[str]
        """
        return self._related_cce_clusters

    @related_cce_clusters.setter
    def related_cce_clusters(self, related_cce_clusters):
        r"""Sets the related_cce_clusters of this AlarmRuleTemplateSpecWithCloudService.

        关联的CCE集群。

        :param related_cce_clusters: The related_cce_clusters of this AlarmRuleTemplateSpecWithCloudService.
        :type related_cce_clusters: list[str]
        """
        self._related_cce_clusters = related_cce_clusters

    @property
    def related_prometheus_instances(self):
        r"""Gets the related_prometheus_instances of this AlarmRuleTemplateSpecWithCloudService.

        关联的Prom实例。

        :return: The related_prometheus_instances of this AlarmRuleTemplateSpecWithCloudService.
        :rtype: list[str]
        """
        return self._related_prometheus_instances

    @related_prometheus_instances.setter
    def related_prometheus_instances(self, related_prometheus_instances):
        r"""Sets the related_prometheus_instances of this AlarmRuleTemplateSpecWithCloudService.

        关联的Prom实例。

        :param related_prometheus_instances: The related_prometheus_instances of this AlarmRuleTemplateSpecWithCloudService.
        :type related_prometheus_instances: list[str]
        """
        self._related_prometheus_instances = related_prometheus_instances

    @property
    def alarm_notification(self):
        r"""Gets the alarm_notification of this AlarmRuleTemplateSpecWithCloudService.

        :return: The alarm_notification of this AlarmRuleTemplateSpecWithCloudService.
        :rtype: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        return self._alarm_notification

    @alarm_notification.setter
    def alarm_notification(self, alarm_notification):
        r"""Sets the alarm_notification of this AlarmRuleTemplateSpecWithCloudService.

        :param alarm_notification: The alarm_notification of this AlarmRuleTemplateSpecWithCloudService.
        :type alarm_notification: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        self._alarm_notification = alarm_notification

    @property
    def alarm_template_spec_items(self):
        r"""Gets the alarm_template_spec_items of this AlarmRuleTemplateSpecWithCloudService.

        告警模板列表。

        :return: The alarm_template_spec_items of this AlarmRuleTemplateSpecWithCloudService.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmTemplateSpecItem`]
        """
        return self._alarm_template_spec_items

    @alarm_template_spec_items.setter
    def alarm_template_spec_items(self, alarm_template_spec_items):
        r"""Sets the alarm_template_spec_items of this AlarmRuleTemplateSpecWithCloudService.

        告警模板列表。

        :param alarm_template_spec_items: The alarm_template_spec_items of this AlarmRuleTemplateSpecWithCloudService.
        :type alarm_template_spec_items: list[:class:`huaweicloudsdkaom.v2.AlarmTemplateSpecItem`]
        """
        self._alarm_template_spec_items = alarm_template_spec_items

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
        if not isinstance(other, AlarmRuleTemplateSpecWithCloudService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
