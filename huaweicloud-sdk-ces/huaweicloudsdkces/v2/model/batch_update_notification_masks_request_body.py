# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateNotificationMasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mask_name': 'str',
        'relation_type': 'str',
        'relation_ids': 'list[str]',
        'resources': 'list[Resource]',
        'metric_names': 'list[str]',
        'product_metrics': 'list[ProductMetric]',
        'resource_level': 'str',
        'product_name': 'str',
        'mask_type': 'str',
        'start_date': 'date',
        'start_time': 'str',
        'end_date': 'date',
        'end_time': 'str',
        'effective_timezone': 'str'
    }

    attribute_map = {
        'mask_name': 'mask_name',
        'relation_type': 'relation_type',
        'relation_ids': 'relation_ids',
        'resources': 'resources',
        'metric_names': 'metric_names',
        'product_metrics': 'product_metrics',
        'resource_level': 'resource_level',
        'product_name': 'product_name',
        'mask_type': 'mask_type',
        'start_date': 'start_date',
        'start_time': 'start_time',
        'end_date': 'end_date',
        'end_time': 'end_time',
        'effective_timezone': 'effective_timezone'
    }

    def __init__(self, mask_name=None, relation_type=None, relation_ids=None, resources=None, metric_names=None, product_metrics=None, resource_level=None, product_name=None, mask_type=None, start_date=None, start_time=None, end_date=None, end_time=None, effective_timezone=None):
        r"""BatchUpdateNotificationMasksRequestBody

        The model defined in huaweicloud sdk

        :param mask_name: **参数解释**： 屏蔽规则名称。    **约束限制**： 不涉及。 **取值范围**： 只能为字母、数字、汉字、-、_，长度为[1,64]个字符。      **默认取值**： 不涉及。 
        :type mask_name: str
        :param relation_type: **参数解释**： 屏蔽告警通知的实现方式。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为 RESOURCE、RESOURCE_POLICY_NOTIFICATION、EVENT.SYS 长度为[1,32]个字符。 - ALARM_RULE：通过告警规则屏蔽告警通知。 - RESOURCE：通过资源屏蔽告警通知。 - RESOURCE_POLICY_NOTIFICATION：通过告警策略屏蔽告警通知。 - RESOURCE_POLICY_ALARM：（已废弃，不推荐使用）通过屏蔽告警计算来屏蔽告警通知。 - EVENT.SYS 通过事件来屏蔽告警 **默认取值**： 不涉及。 
        :type relation_type: str
        :param relation_ids: **参数解释**： 关联ID列表。        **约束限制**： relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION时填屏蔽的告警策略ID。包含的关联ID数量为[1,100] 
        :type relation_ids: list[str]
        :param resources: **参数解释**： 必填。关联的资源列表   **约束限制**： relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION 时填屏蔽的资源信息。包含的资源数量为[1,100] 
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        :param metric_names: **参数解释**： 关联的指标名称 **约束限制**： relation_type为RESOURCE可选填，不填视为对资源所有指标进行告警屏蔽。包含的指标数量为[0,50] 
        :type metric_names: list[str]
        :param product_metrics: **参数解释**： 按云产品维度屏蔽时的指标信息 **约束限制**： 包含的指标数量为[0,50] 
        :type product_metrics: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        :param resource_level: **参数解释**： 资源层级。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：资源层级为云产品 - dimension：资源层级为子维度 **默认取值**： 不涉及。 
        :type resource_level: str
        :param product_name: **参数解释**： 资源层级为云产品时的云产品名称 **约束限制**： 不涉及 **取值范围**： 长度为[0,128]个字符。 **默认取值**： 不涉及。 
        :type product_name: str
        :param mask_type: **参数解释**： 屏蔽类型。          **约束限制**： 不涉及。 **取值范围**： 只能为START_END_TIME、FOREVER_TIME、CYCLE_TIME - START_END_TIME：按起止时间屏蔽。 - FOREVER_TIME：永久时间屏蔽。 - CYCLE_TIME：按周期时间屏蔽。           **默认取值**： 不涉及。 
        :type mask_type: str
        :param start_date: **参数解释**： 屏蔽起始日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 
        :type start_date: date
        :param start_time: **参数解释**： 屏蔽起始时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 
        :type start_time: str
        :param end_date: **参数解释**： 屏蔽截止日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 
        :type end_date: date
        :param end_time: **参数解释**： 屏蔽截止时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 
        :type end_time: str
        :param effective_timezone: **参数解释**： 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 
        :type effective_timezone: str
        """
        
        

        self._mask_name = None
        self._relation_type = None
        self._relation_ids = None
        self._resources = None
        self._metric_names = None
        self._product_metrics = None
        self._resource_level = None
        self._product_name = None
        self._mask_type = None
        self._start_date = None
        self._start_time = None
        self._end_date = None
        self._end_time = None
        self._effective_timezone = None
        self.discriminator = None

        if mask_name is not None:
            self.mask_name = mask_name
        self.relation_type = relation_type
        self.relation_ids = relation_ids
        if resources is not None:
            self.resources = resources
        if metric_names is not None:
            self.metric_names = metric_names
        if product_metrics is not None:
            self.product_metrics = product_metrics
        if resource_level is not None:
            self.resource_level = resource_level
        if product_name is not None:
            self.product_name = product_name
        self.mask_type = mask_type
        if start_date is not None:
            self.start_date = start_date
        if start_time is not None:
            self.start_time = start_time
        if end_date is not None:
            self.end_date = end_date
        if end_time is not None:
            self.end_time = end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone

    @property
    def mask_name(self):
        r"""Gets the mask_name of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽规则名称。    **约束限制**： 不涉及。 **取值范围**： 只能为字母、数字、汉字、-、_，长度为[1,64]个字符。      **默认取值**： 不涉及。 

        :return: The mask_name of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._mask_name

    @mask_name.setter
    def mask_name(self, mask_name):
        r"""Sets the mask_name of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽规则名称。    **约束限制**： 不涉及。 **取值范围**： 只能为字母、数字、汉字、-、_，长度为[1,64]个字符。      **默认取值**： 不涉及。 

        :param mask_name: The mask_name of this BatchUpdateNotificationMasksRequestBody.
        :type mask_name: str
        """
        self._mask_name = mask_name

    @property
    def relation_type(self):
        r"""Gets the relation_type of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽告警通知的实现方式。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为 RESOURCE、RESOURCE_POLICY_NOTIFICATION、EVENT.SYS 长度为[1,32]个字符。 - ALARM_RULE：通过告警规则屏蔽告警通知。 - RESOURCE：通过资源屏蔽告警通知。 - RESOURCE_POLICY_NOTIFICATION：通过告警策略屏蔽告警通知。 - RESOURCE_POLICY_ALARM：（已废弃，不推荐使用）通过屏蔽告警计算来屏蔽告警通知。 - EVENT.SYS 通过事件来屏蔽告警 **默认取值**： 不涉及。 

        :return: The relation_type of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        r"""Sets the relation_type of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽告警通知的实现方式。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为 RESOURCE、RESOURCE_POLICY_NOTIFICATION、EVENT.SYS 长度为[1,32]个字符。 - ALARM_RULE：通过告警规则屏蔽告警通知。 - RESOURCE：通过资源屏蔽告警通知。 - RESOURCE_POLICY_NOTIFICATION：通过告警策略屏蔽告警通知。 - RESOURCE_POLICY_ALARM：（已废弃，不推荐使用）通过屏蔽告警计算来屏蔽告警通知。 - EVENT.SYS 通过事件来屏蔽告警 **默认取值**： 不涉及。 

        :param relation_type: The relation_type of this BatchUpdateNotificationMasksRequestBody.
        :type relation_type: str
        """
        self._relation_type = relation_type

    @property
    def relation_ids(self):
        r"""Gets the relation_ids of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 关联ID列表。        **约束限制**： relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION时填屏蔽的告警策略ID。包含的关联ID数量为[1,100] 

        :return: The relation_ids of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        r"""Sets the relation_ids of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 关联ID列表。        **约束限制**： relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION时填屏蔽的告警策略ID。包含的关联ID数量为[1,100] 

        :param relation_ids: The relation_ids of this BatchUpdateNotificationMasksRequestBody.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def resources(self):
        r"""Gets the resources of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 必填。关联的资源列表   **约束限制**： relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION 时填屏蔽的资源信息。包含的资源数量为[1,100] 

        :return: The resources of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 必填。关联的资源列表   **约束限制**： relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION 时填屏蔽的资源信息。包含的资源数量为[1,100] 

        :param resources: The resources of this BatchUpdateNotificationMasksRequestBody.
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        self._resources = resources

    @property
    def metric_names(self):
        r"""Gets the metric_names of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 关联的指标名称 **约束限制**： relation_type为RESOURCE可选填，不填视为对资源所有指标进行告警屏蔽。包含的指标数量为[0,50] 

        :return: The metric_names of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 关联的指标名称 **约束限制**： relation_type为RESOURCE可选填，不填视为对资源所有指标进行告警屏蔽。包含的指标数量为[0,50] 

        :param metric_names: The metric_names of this BatchUpdateNotificationMasksRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def product_metrics(self):
        r"""Gets the product_metrics of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 按云产品维度屏蔽时的指标信息 **约束限制**： 包含的指标数量为[0,50] 

        :return: The product_metrics of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        """
        return self._product_metrics

    @product_metrics.setter
    def product_metrics(self, product_metrics):
        r"""Sets the product_metrics of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 按云产品维度屏蔽时的指标信息 **约束限制**： 包含的指标数量为[0,50] 

        :param product_metrics: The product_metrics of this BatchUpdateNotificationMasksRequestBody.
        :type product_metrics: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        """
        self._product_metrics = product_metrics

    @property
    def resource_level(self):
        r"""Gets the resource_level of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 资源层级。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：资源层级为云产品 - dimension：资源层级为子维度 **默认取值**： 不涉及。 

        :return: The resource_level of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 资源层级。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：资源层级为云产品 - dimension：资源层级为子维度 **默认取值**： 不涉及。 

        :param resource_level: The resource_level of this BatchUpdateNotificationMasksRequestBody.
        :type resource_level: str
        """
        self._resource_level = resource_level

    @property
    def product_name(self):
        r"""Gets the product_name of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 资源层级为云产品时的云产品名称 **约束限制**： 不涉及 **取值范围**： 长度为[0,128]个字符。 **默认取值**： 不涉及。 

        :return: The product_name of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 资源层级为云产品时的云产品名称 **约束限制**： 不涉及 **取值范围**： 长度为[0,128]个字符。 **默认取值**： 不涉及。 

        :param product_name: The product_name of this BatchUpdateNotificationMasksRequestBody.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def mask_type(self):
        r"""Gets the mask_type of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽类型。          **约束限制**： 不涉及。 **取值范围**： 只能为START_END_TIME、FOREVER_TIME、CYCLE_TIME - START_END_TIME：按起止时间屏蔽。 - FOREVER_TIME：永久时间屏蔽。 - CYCLE_TIME：按周期时间屏蔽。           **默认取值**： 不涉及。 

        :return: The mask_type of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._mask_type

    @mask_type.setter
    def mask_type(self, mask_type):
        r"""Sets the mask_type of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽类型。          **约束限制**： 不涉及。 **取值范围**： 只能为START_END_TIME、FOREVER_TIME、CYCLE_TIME - START_END_TIME：按起止时间屏蔽。 - FOREVER_TIME：永久时间屏蔽。 - CYCLE_TIME：按周期时间屏蔽。           **默认取值**： 不涉及。 

        :param mask_type: The mask_type of this BatchUpdateNotificationMasksRequestBody.
        :type mask_type: str
        """
        self._mask_type = mask_type

    @property
    def start_date(self):
        r"""Gets the start_date of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽起始日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 

        :return: The start_date of this BatchUpdateNotificationMasksRequestBody.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽起始日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 

        :param start_date: The start_date of this BatchUpdateNotificationMasksRequestBody.
        :type start_date: date
        """
        self._start_date = start_date

    @property
    def start_time(self):
        r"""Gets the start_time of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽起始时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 

        :return: The start_time of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽起始时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 

        :param start_time: The start_time of this BatchUpdateNotificationMasksRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_date(self):
        r"""Gets the end_date of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽截止日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 

        :return: The end_date of this BatchUpdateNotificationMasksRequestBody.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽截止日期。           **约束限制**： 不涉及。 **取值范围**： 字符长度为10，格式为：yyyy-MM-dd           **默认取值**： 不涉及。 

        :param end_date: The end_date of this BatchUpdateNotificationMasksRequestBody.
        :type end_date: date
        """
        self._end_date = end_date

    @property
    def end_time(self):
        r"""Gets the end_time of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽截止时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 

        :return: The end_time of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 屏蔽截止时间。          **约束限制**： 不涉及。 **取值范围**： 字符长度为8，格式为：HH:mm:ss         **默认取值**： 不涉及。 

        :param end_time: The end_time of this BatchUpdateNotificationMasksRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 

        :return: The effective_timezone of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this BatchUpdateNotificationMasksRequestBody.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 

        :param effective_timezone: The effective_timezone of this BatchUpdateNotificationMasksRequestBody.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

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
        if not isinstance(other, BatchUpdateNotificationMasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
