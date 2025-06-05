# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMaskRespNotificationMasks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_mask_id': 'str',
        'mask_name': 'str',
        'relation_type': 'RelationType',
        'relation_id': 'str',
        'resource_type': 'MaskResourceType',
        'metric_names': 'list[str]',
        'product_metrics': 'list[ProductMetric]',
        'resource_level': 'str',
        'product_name': 'str',
        'resources': 'list[ResourceCategory]',
        'mask_status': 'MaskStatus',
        'mask_type': 'MaskType',
        'create_time': 'int',
        'update_time': 'int',
        'start_date': 'date',
        'start_time': 'str',
        'end_date': 'date',
        'end_time': 'str',
        'effective_timezone': 'str',
        'policies': 'list[PoliciesInListResp]'
    }

    attribute_map = {
        'notification_mask_id': 'notification_mask_id',
        'mask_name': 'mask_name',
        'relation_type': 'relation_type',
        'relation_id': 'relation_id',
        'resource_type': 'resource_type',
        'metric_names': 'metric_names',
        'product_metrics': 'product_metrics',
        'resource_level': 'resource_level',
        'product_name': 'product_name',
        'resources': 'resources',
        'mask_status': 'mask_status',
        'mask_type': 'mask_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'start_date': 'start_date',
        'start_time': 'start_time',
        'end_date': 'end_date',
        'end_time': 'end_time',
        'effective_timezone': 'effective_timezone',
        'policies': 'policies'
    }

    def __init__(self, notification_mask_id=None, mask_name=None, relation_type=None, relation_id=None, resource_type=None, metric_names=None, product_metrics=None, resource_level=None, product_name=None, resources=None, mask_status=None, mask_type=None, create_time=None, update_time=None, start_date=None, start_time=None, end_date=None, end_time=None, effective_timezone=None, policies=None):
        r"""ListNotificationMaskRespNotificationMasks

        The model defined in huaweicloud sdk

        :param notification_mask_id: 屏蔽规则ID
        :type notification_mask_id: str
        :param mask_name: 屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64
        :type mask_name: str
        :param relation_type: 
        :type relation_type: :class:`huaweicloudsdkces.v2.RelationType`
        :param relation_id: 关联编号
        :type relation_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkces.v2.MaskResourceType`
        :param metric_names: 关联指标名称，relation_type为RESOURCE时存在该字段
        :type metric_names: list[str]
        :param product_metrics: 按云产品维度屏蔽时的指标信息
        :type product_metrics: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        :param resource_level: dimension: 子维度,product: 云产品
        :type resource_level: str
        :param product_name: 资源为云产品时的云产品名称
        :type product_name: str
        :param resources: 关联资源类型，relation_type为RESOURCE时存在该字段,只需要查询出资源的namespace+维度名即可
        :type resources: list[:class:`huaweicloudsdkces.v2.ResourceCategory`]
        :param mask_status: 
        :type mask_status: :class:`huaweicloudsdkces.v2.MaskStatus`
        :param mask_type: 
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        :param create_time: 告警屏蔽的创建时间，UNIX时间戳，单位毫秒。
        :type create_time: int
        :param update_time: 告警屏蔽的更新时间，UNIX时间戳，单位毫秒。
        :type update_time: int
        :param start_date: 屏蔽起始日期，yyyy-MM-dd。
        :type start_date: date
        :param start_time: 屏蔽起始时间，HH:mm:ss。
        :type start_time: str
        :param end_date: 屏蔽截止日期，yyyy-MM-dd。
        :type end_date: date
        :param end_time: 屏蔽截止时间，HH:mm:ss。
        :type end_time: str
        :param effective_timezone: 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;
        :type effective_timezone: str
        :param policies: 告警策略列表。
        :type policies: list[:class:`huaweicloudsdkces.v2.PoliciesInListResp`]
        """
        
        

        self._notification_mask_id = None
        self._mask_name = None
        self._relation_type = None
        self._relation_id = None
        self._resource_type = None
        self._metric_names = None
        self._product_metrics = None
        self._resource_level = None
        self._product_name = None
        self._resources = None
        self._mask_status = None
        self._mask_type = None
        self._create_time = None
        self._update_time = None
        self._start_date = None
        self._start_time = None
        self._end_date = None
        self._end_time = None
        self._effective_timezone = None
        self._policies = None
        self.discriminator = None

        self.notification_mask_id = notification_mask_id
        if mask_name is not None:
            self.mask_name = mask_name
        self.relation_type = relation_type
        if relation_id is not None:
            self.relation_id = relation_id
        if resource_type is not None:
            self.resource_type = resource_type
        if metric_names is not None:
            self.metric_names = metric_names
        if product_metrics is not None:
            self.product_metrics = product_metrics
        if resource_level is not None:
            self.resource_level = resource_level
        if product_name is not None:
            self.product_name = product_name
        if resources is not None:
            self.resources = resources
        self.mask_status = mask_status
        self.mask_type = mask_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
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
        if policies is not None:
            self.policies = policies

    @property
    def notification_mask_id(self):
        r"""Gets the notification_mask_id of this ListNotificationMaskRespNotificationMasks.

        屏蔽规则ID

        :return: The notification_mask_id of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._notification_mask_id

    @notification_mask_id.setter
    def notification_mask_id(self, notification_mask_id):
        r"""Sets the notification_mask_id of this ListNotificationMaskRespNotificationMasks.

        屏蔽规则ID

        :param notification_mask_id: The notification_mask_id of this ListNotificationMaskRespNotificationMasks.
        :type notification_mask_id: str
        """
        self._notification_mask_id = notification_mask_id

    @property
    def mask_name(self):
        r"""Gets the mask_name of this ListNotificationMaskRespNotificationMasks.

        屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64

        :return: The mask_name of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._mask_name

    @mask_name.setter
    def mask_name(self, mask_name):
        r"""Sets the mask_name of this ListNotificationMaskRespNotificationMasks.

        屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64

        :param mask_name: The mask_name of this ListNotificationMaskRespNotificationMasks.
        :type mask_name: str
        """
        self._mask_name = mask_name

    @property
    def relation_type(self):
        r"""Gets the relation_type of this ListNotificationMaskRespNotificationMasks.

        :return: The relation_type of this ListNotificationMaskRespNotificationMasks.
        :rtype: :class:`huaweicloudsdkces.v2.RelationType`
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        r"""Sets the relation_type of this ListNotificationMaskRespNotificationMasks.

        :param relation_type: The relation_type of this ListNotificationMaskRespNotificationMasks.
        :type relation_type: :class:`huaweicloudsdkces.v2.RelationType`
        """
        self._relation_type = relation_type

    @property
    def relation_id(self):
        r"""Gets the relation_id of this ListNotificationMaskRespNotificationMasks.

        关联编号

        :return: The relation_id of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this ListNotificationMaskRespNotificationMasks.

        关联编号

        :param relation_id: The relation_id of this ListNotificationMaskRespNotificationMasks.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListNotificationMaskRespNotificationMasks.

        :return: The resource_type of this ListNotificationMaskRespNotificationMasks.
        :rtype: :class:`huaweicloudsdkces.v2.MaskResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListNotificationMaskRespNotificationMasks.

        :param resource_type: The resource_type of this ListNotificationMaskRespNotificationMasks.
        :type resource_type: :class:`huaweicloudsdkces.v2.MaskResourceType`
        """
        self._resource_type = resource_type

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ListNotificationMaskRespNotificationMasks.

        关联指标名称，relation_type为RESOURCE时存在该字段

        :return: The metric_names of this ListNotificationMaskRespNotificationMasks.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ListNotificationMaskRespNotificationMasks.

        关联指标名称，relation_type为RESOURCE时存在该字段

        :param metric_names: The metric_names of this ListNotificationMaskRespNotificationMasks.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def product_metrics(self):
        r"""Gets the product_metrics of this ListNotificationMaskRespNotificationMasks.

        按云产品维度屏蔽时的指标信息

        :return: The product_metrics of this ListNotificationMaskRespNotificationMasks.
        :rtype: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        """
        return self._product_metrics

    @product_metrics.setter
    def product_metrics(self, product_metrics):
        r"""Sets the product_metrics of this ListNotificationMaskRespNotificationMasks.

        按云产品维度屏蔽时的指标信息

        :param product_metrics: The product_metrics of this ListNotificationMaskRespNotificationMasks.
        :type product_metrics: list[:class:`huaweicloudsdkces.v2.ProductMetric`]
        """
        self._product_metrics = product_metrics

    @property
    def resource_level(self):
        r"""Gets the resource_level of this ListNotificationMaskRespNotificationMasks.

        dimension: 子维度,product: 云产品

        :return: The resource_level of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this ListNotificationMaskRespNotificationMasks.

        dimension: 子维度,product: 云产品

        :param resource_level: The resource_level of this ListNotificationMaskRespNotificationMasks.
        :type resource_level: str
        """
        self._resource_level = resource_level

    @property
    def product_name(self):
        r"""Gets the product_name of this ListNotificationMaskRespNotificationMasks.

        资源为云产品时的云产品名称

        :return: The product_name of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ListNotificationMaskRespNotificationMasks.

        资源为云产品时的云产品名称

        :param product_name: The product_name of this ListNotificationMaskRespNotificationMasks.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def resources(self):
        r"""Gets the resources of this ListNotificationMaskRespNotificationMasks.

        关联资源类型，relation_type为RESOURCE时存在该字段,只需要查询出资源的namespace+维度名即可

        :return: The resources of this ListNotificationMaskRespNotificationMasks.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceCategory`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListNotificationMaskRespNotificationMasks.

        关联资源类型，relation_type为RESOURCE时存在该字段,只需要查询出资源的namespace+维度名即可

        :param resources: The resources of this ListNotificationMaskRespNotificationMasks.
        :type resources: list[:class:`huaweicloudsdkces.v2.ResourceCategory`]
        """
        self._resources = resources

    @property
    def mask_status(self):
        r"""Gets the mask_status of this ListNotificationMaskRespNotificationMasks.

        :return: The mask_status of this ListNotificationMaskRespNotificationMasks.
        :rtype: :class:`huaweicloudsdkces.v2.MaskStatus`
        """
        return self._mask_status

    @mask_status.setter
    def mask_status(self, mask_status):
        r"""Sets the mask_status of this ListNotificationMaskRespNotificationMasks.

        :param mask_status: The mask_status of this ListNotificationMaskRespNotificationMasks.
        :type mask_status: :class:`huaweicloudsdkces.v2.MaskStatus`
        """
        self._mask_status = mask_status

    @property
    def mask_type(self):
        r"""Gets the mask_type of this ListNotificationMaskRespNotificationMasks.

        :return: The mask_type of this ListNotificationMaskRespNotificationMasks.
        :rtype: :class:`huaweicloudsdkces.v2.MaskType`
        """
        return self._mask_type

    @mask_type.setter
    def mask_type(self, mask_type):
        r"""Sets the mask_type of this ListNotificationMaskRespNotificationMasks.

        :param mask_type: The mask_type of this ListNotificationMaskRespNotificationMasks.
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        """
        self._mask_type = mask_type

    @property
    def create_time(self):
        r"""Gets the create_time of this ListNotificationMaskRespNotificationMasks.

        告警屏蔽的创建时间，UNIX时间戳，单位毫秒。

        :return: The create_time of this ListNotificationMaskRespNotificationMasks.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListNotificationMaskRespNotificationMasks.

        告警屏蔽的创建时间，UNIX时间戳，单位毫秒。

        :param create_time: The create_time of this ListNotificationMaskRespNotificationMasks.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListNotificationMaskRespNotificationMasks.

        告警屏蔽的更新时间，UNIX时间戳，单位毫秒。

        :return: The update_time of this ListNotificationMaskRespNotificationMasks.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListNotificationMaskRespNotificationMasks.

        告警屏蔽的更新时间，UNIX时间戳，单位毫秒。

        :param update_time: The update_time of this ListNotificationMaskRespNotificationMasks.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def start_date(self):
        r"""Gets the start_date of this ListNotificationMaskRespNotificationMasks.

        屏蔽起始日期，yyyy-MM-dd。

        :return: The start_date of this ListNotificationMaskRespNotificationMasks.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ListNotificationMaskRespNotificationMasks.

        屏蔽起始日期，yyyy-MM-dd。

        :param start_date: The start_date of this ListNotificationMaskRespNotificationMasks.
        :type start_date: date
        """
        self._start_date = start_date

    @property
    def start_time(self):
        r"""Gets the start_time of this ListNotificationMaskRespNotificationMasks.

        屏蔽起始时间，HH:mm:ss。

        :return: The start_time of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListNotificationMaskRespNotificationMasks.

        屏蔽起始时间，HH:mm:ss。

        :param start_time: The start_time of this ListNotificationMaskRespNotificationMasks.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_date(self):
        r"""Gets the end_date of this ListNotificationMaskRespNotificationMasks.

        屏蔽截止日期，yyyy-MM-dd。

        :return: The end_date of this ListNotificationMaskRespNotificationMasks.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this ListNotificationMaskRespNotificationMasks.

        屏蔽截止日期，yyyy-MM-dd。

        :param end_date: The end_date of this ListNotificationMaskRespNotificationMasks.
        :type end_date: date
        """
        self._end_date = end_date

    @property
    def end_time(self):
        r"""Gets the end_time of this ListNotificationMaskRespNotificationMasks.

        屏蔽截止时间，HH:mm:ss。

        :return: The end_time of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListNotificationMaskRespNotificationMasks.

        屏蔽截止时间，HH:mm:ss。

        :param end_time: The end_time of this ListNotificationMaskRespNotificationMasks.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this ListNotificationMaskRespNotificationMasks.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :return: The effective_timezone of this ListNotificationMaskRespNotificationMasks.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this ListNotificationMaskRespNotificationMasks.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :param effective_timezone: The effective_timezone of this ListNotificationMaskRespNotificationMasks.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def policies(self):
        r"""Gets the policies of this ListNotificationMaskRespNotificationMasks.

        告警策略列表。

        :return: The policies of this ListNotificationMaskRespNotificationMasks.
        :rtype: list[:class:`huaweicloudsdkces.v2.PoliciesInListResp`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListNotificationMaskRespNotificationMasks.

        告警策略列表。

        :param policies: The policies of this ListNotificationMaskRespNotificationMasks.
        :type policies: list[:class:`huaweicloudsdkces.v2.PoliciesInListResp`]
        """
        self._policies = policies

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNotificationMaskRespNotificationMasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
