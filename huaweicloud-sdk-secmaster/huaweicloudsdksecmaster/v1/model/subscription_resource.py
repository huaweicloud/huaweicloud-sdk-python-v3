# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type_name': 'str',
        'resource_size': 'int',
        'cloud_service': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'to_period': 'bool',
        'create_time': 'int',
        'update_time': 'int',
        'expire_time': 'int',
        'resource_status': 'int',
        'order_id': 'str',
        'charging_mode': 'str',
        'tag_list': 'list[SubscriptionTagInfo]',
        'usages': 'list[ResourceUsage]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type_name': 'resource_type_name',
        'resource_size': 'resource_size',
        'cloud_service': 'cloud_service',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'to_period': 'to_period',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'expire_time': 'expire_time',
        'resource_status': 'resource_status',
        'order_id': 'order_id',
        'charging_mode': 'charging_mode',
        'tag_list': 'tag_list',
        'usages': 'usages'
    }

    def __init__(self, resource_id=None, resource_type_name=None, resource_size=None, cloud_service=None, resource_type=None, resource_spec_code=None, to_period=None, create_time=None, update_time=None, expire_time=None, resource_status=None, order_id=None, charging_mode=None, tag_list=None, usages=None):
        r"""SubscriptionResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源Id
        :type resource_id: str
        :param resource_type_name: 资源名称
        :type resource_type_name: str
        :param resource_size: 资源规格
        :type resource_size: int
        :param cloud_service: 订单来源，默认数据为SecMaster
        :type cloud_service: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param to_period: 当前资源是否能进行按需转包周期操作
        :type to_period: bool
        :param create_time: 创建时间戳
        :type create_time: int
        :param update_time: 更新时间戳
        :type update_time: int
        :param expire_time: 到期时间戳，只有包年包月资源才有该字段
        :type expire_time: int
        :param resource_status: 资源状态，目前返回正常运行的资源，其状态值为0
        :type resource_status: int
        :param order_id: 订单Id，包周期资源有该字段
        :type order_id: str
        :param charging_mode: 计费模式，目前有包周期（包年包月）PREPAID、按需POSTPAID，大小写不敏感
        :type charging_mode: str
        :param tag_list: 资源列表
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTagInfo`]
        :param usages: 资源使用量，当usage&#x3D;true时返回该字段
        :type usages: list[:class:`huaweicloudsdksecmaster.v1.ResourceUsage`]
        """
        
        

        self._resource_id = None
        self._resource_type_name = None
        self._resource_size = None
        self._cloud_service = None
        self._resource_type = None
        self._resource_spec_code = None
        self._to_period = None
        self._create_time = None
        self._update_time = None
        self._expire_time = None
        self._resource_status = None
        self._order_id = None
        self._charging_mode = None
        self._tag_list = None
        self._usages = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_size is not None:
            self.resource_size = resource_size
        if cloud_service is not None:
            self.cloud_service = cloud_service
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if to_period is not None:
            self.to_period = to_period
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if expire_time is not None:
            self.expire_time = expire_time
        if resource_status is not None:
            self.resource_status = resource_status
        if order_id is not None:
            self.order_id = order_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if tag_list is not None:
            self.tag_list = tag_list
        if usages is not None:
            self.usages = usages

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SubscriptionResource.

        资源Id

        :return: The resource_id of this SubscriptionResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SubscriptionResource.

        资源Id

        :param resource_id: The resource_id of this SubscriptionResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this SubscriptionResource.

        资源名称

        :return: The resource_type_name of this SubscriptionResource.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this SubscriptionResource.

        资源名称

        :param resource_type_name: The resource_type_name of this SubscriptionResource.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_size(self):
        r"""Gets the resource_size of this SubscriptionResource.

        资源规格

        :return: The resource_size of this SubscriptionResource.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this SubscriptionResource.

        资源规格

        :param resource_size: The resource_size of this SubscriptionResource.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def cloud_service(self):
        r"""Gets the cloud_service of this SubscriptionResource.

        订单来源，默认数据为SecMaster

        :return: The cloud_service of this SubscriptionResource.
        :rtype: str
        """
        return self._cloud_service

    @cloud_service.setter
    def cloud_service(self, cloud_service):
        r"""Sets the cloud_service of this SubscriptionResource.

        订单来源，默认数据为SecMaster

        :param cloud_service: The cloud_service of this SubscriptionResource.
        :type cloud_service: str
        """
        self._cloud_service = cloud_service

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SubscriptionResource.

        资源类型

        :return: The resource_type of this SubscriptionResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SubscriptionResource.

        资源类型

        :param resource_type: The resource_type of this SubscriptionResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this SubscriptionResource.

        资源规格编码

        :return: The resource_spec_code of this SubscriptionResource.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this SubscriptionResource.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this SubscriptionResource.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def to_period(self):
        r"""Gets the to_period of this SubscriptionResource.

        当前资源是否能进行按需转包周期操作

        :return: The to_period of this SubscriptionResource.
        :rtype: bool
        """
        return self._to_period

    @to_period.setter
    def to_period(self, to_period):
        r"""Sets the to_period of this SubscriptionResource.

        当前资源是否能进行按需转包周期操作

        :param to_period: The to_period of this SubscriptionResource.
        :type to_period: bool
        """
        self._to_period = to_period

    @property
    def create_time(self):
        r"""Gets the create_time of this SubscriptionResource.

        创建时间戳

        :return: The create_time of this SubscriptionResource.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SubscriptionResource.

        创建时间戳

        :param create_time: The create_time of this SubscriptionResource.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SubscriptionResource.

        更新时间戳

        :return: The update_time of this SubscriptionResource.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SubscriptionResource.

        更新时间戳

        :param update_time: The update_time of this SubscriptionResource.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this SubscriptionResource.

        到期时间戳，只有包年包月资源才有该字段

        :return: The expire_time of this SubscriptionResource.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this SubscriptionResource.

        到期时间戳，只有包年包月资源才有该字段

        :param expire_time: The expire_time of this SubscriptionResource.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def resource_status(self):
        r"""Gets the resource_status of this SubscriptionResource.

        资源状态，目前返回正常运行的资源，其状态值为0

        :return: The resource_status of this SubscriptionResource.
        :rtype: int
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        r"""Sets the resource_status of this SubscriptionResource.

        资源状态，目前返回正常运行的资源，其状态值为0

        :param resource_status: The resource_status of this SubscriptionResource.
        :type resource_status: int
        """
        self._resource_status = resource_status

    @property
    def order_id(self):
        r"""Gets the order_id of this SubscriptionResource.

        订单Id，包周期资源有该字段

        :return: The order_id of this SubscriptionResource.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this SubscriptionResource.

        订单Id，包周期资源有该字段

        :param order_id: The order_id of this SubscriptionResource.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SubscriptionResource.

        计费模式，目前有包周期（包年包月）PREPAID、按需POSTPAID，大小写不敏感

        :return: The charging_mode of this SubscriptionResource.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SubscriptionResource.

        计费模式，目前有包周期（包年包月）PREPAID、按需POSTPAID，大小写不敏感

        :param charging_mode: The charging_mode of this SubscriptionResource.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def tag_list(self):
        r"""Gets the tag_list of this SubscriptionResource.

        资源列表

        :return: The tag_list of this SubscriptionResource.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTagInfo`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this SubscriptionResource.

        资源列表

        :param tag_list: The tag_list of this SubscriptionResource.
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTagInfo`]
        """
        self._tag_list = tag_list

    @property
    def usages(self):
        r"""Gets the usages of this SubscriptionResource.

        资源使用量，当usage=true时返回该字段

        :return: The usages of this SubscriptionResource.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ResourceUsage`]
        """
        return self._usages

    @usages.setter
    def usages(self, usages):
        r"""Sets the usages of this SubscriptionResource.

        资源使用量，当usage=true时返回该字段

        :param usages: The usages of this SubscriptionResource.
        :type usages: list[:class:`huaweicloudsdksecmaster.v1.ResourceUsage`]
        """
        self._usages = usages

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
        if not isinstance(other, SubscriptionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
