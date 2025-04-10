# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSkillOrderInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expiration_stop_flag': 'int',
        'package_order_id': 'str',
        'icon': 'str',
        'commission_flag': 'int',
        'product_info': 'list[str]',
        'package_id': 'str',
        'measure_type': 'str',
        'update_time': 'int',
        'channel_limit': 'int',
        'resource_step_size': 'int',
        'cloud_service_type': 'str',
        'developer_id': 'str',
        'amount': 'int',
        'format': 'str',
        'resource_type': 'str',
        'expire_time': 'int',
        'measure_unit': 'str',
        'skill_chip': 'str',
        'versions': 'list[str]',
        'skill_name': 'str',
        'skill_type': 'str',
        'used_amount': 'int',
        'charge_model': 'int',
        'resource_spec_code': 'str',
        'skill_id': 'str',
        'skill_platform': 'str',
        'order_limit': 'int',
        'order_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'expiration_stop_flag': 'expiration_stop_flag',
        'package_order_id': 'package_order_id',
        'icon': 'icon',
        'commission_flag': 'commission_flag',
        'product_info': 'product_info',
        'package_id': 'package_id',
        'measure_type': 'measure_type',
        'update_time': 'update_time',
        'channel_limit': 'channel_limit',
        'resource_step_size': 'resource_step_size',
        'cloud_service_type': 'cloud_service_type',
        'developer_id': 'developer_id',
        'amount': 'amount',
        'format': 'format',
        'resource_type': 'resource_type',
        'expire_time': 'expire_time',
        'measure_unit': 'measure_unit',
        'skill_chip': 'skill_chip',
        'versions': 'versions',
        'skill_name': 'skill_name',
        'skill_type': 'skill_type',
        'used_amount': 'used_amount',
        'charge_model': 'charge_model',
        'resource_spec_code': 'resource_spec_code',
        'skill_id': 'skill_id',
        'skill_platform': 'skill_platform',
        'order_limit': 'order_limit',
        'order_id': 'order_id',
        'status': 'status'
    }

    def __init__(self, expiration_stop_flag=None, package_order_id=None, icon=None, commission_flag=None, product_info=None, package_id=None, measure_type=None, update_time=None, channel_limit=None, resource_step_size=None, cloud_service_type=None, developer_id=None, amount=None, format=None, resource_type=None, expire_time=None, measure_unit=None, skill_chip=None, versions=None, skill_name=None, skill_type=None, used_amount=None, charge_model=None, resource_spec_code=None, skill_id=None, skill_platform=None, order_limit=None, order_id=None, status=None):
        r"""ShowSkillOrderInfoResponse

        The model defined in huaweicloud sdk

        :param expiration_stop_flag: 技能是否支持永久使用标识。1标识支持，0为不支持
        :type expiration_stop_flag: int
        :param package_order_id: 技能套餐包订单ID
        :type package_order_id: str
        :param icon: 技能图标
        :type icon: str
        :param commission_flag: 定制技能标识
        :type commission_flag: int
        :param product_info: 产品收费编码信息
        :type product_info: list[str]
        :param package_id: 套餐包ID
        :type package_id: str
        :param measure_type: 计费类型，physical_src表示按物理量纲收费，比如包周期 ，src表示一次性收费
        :type measure_type: str
        :param update_time: 更新时间
        :type update_time: int
        :param channel_limit: 通道数限制
        :type channel_limit: int
        :param resource_step_size: 步长
        :type resource_step_size: int
        :param cloud_service_type: 云服务编码
        :type cloud_service_type: str
        :param developer_id: 开发者ID
        :type developer_id: str
        :param amount: 订单数量
        :type amount: int
        :param format: 技能类型，文件类型file，镜像类型iamge
        :type format: str
        :param resource_type: 资源类别
        :type resource_type: str
        :param expire_time: 到期时间
        :type expire_time: int
        :param measure_unit: 计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费
        :type measure_unit: str
        :param skill_chip: 芯片类别
        :type skill_chip: str
        :param versions: 技能版本列表
        :type versions: list[str]
        :param skill_name: 技能名字
        :type skill_name: str
        :param skill_type: 技能类别
        :type skill_type: str
        :param used_amount: 订单使用份数
        :type used_amount: int
        :param charge_model: 计费模式
        :type charge_model: int
        :param resource_spec_code: 资源编码
        :type resource_spec_code: str
        :param skill_id: 技能ID
        :type skill_id: str
        :param skill_platform: 技能支持的平台
        :type skill_platform: str
        :param order_limit: 订单购买限制
        :type order_limit: int
        :param order_id: 订单ID
        :type order_id: str
        :param status: 订单状态，0表示正常状态，1表示冻结状态，2表示受限状态
        :type status: int
        """
        
        super(ShowSkillOrderInfoResponse, self).__init__()

        self._expiration_stop_flag = None
        self._package_order_id = None
        self._icon = None
        self._commission_flag = None
        self._product_info = None
        self._package_id = None
        self._measure_type = None
        self._update_time = None
        self._channel_limit = None
        self._resource_step_size = None
        self._cloud_service_type = None
        self._developer_id = None
        self._amount = None
        self._format = None
        self._resource_type = None
        self._expire_time = None
        self._measure_unit = None
        self._skill_chip = None
        self._versions = None
        self._skill_name = None
        self._skill_type = None
        self._used_amount = None
        self._charge_model = None
        self._resource_spec_code = None
        self._skill_id = None
        self._skill_platform = None
        self._order_limit = None
        self._order_id = None
        self._status = None
        self.discriminator = None

        if expiration_stop_flag is not None:
            self.expiration_stop_flag = expiration_stop_flag
        if package_order_id is not None:
            self.package_order_id = package_order_id
        if icon is not None:
            self.icon = icon
        if commission_flag is not None:
            self.commission_flag = commission_flag
        if product_info is not None:
            self.product_info = product_info
        if package_id is not None:
            self.package_id = package_id
        if measure_type is not None:
            self.measure_type = measure_type
        if update_time is not None:
            self.update_time = update_time
        if channel_limit is not None:
            self.channel_limit = channel_limit
        if resource_step_size is not None:
            self.resource_step_size = resource_step_size
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if developer_id is not None:
            self.developer_id = developer_id
        if amount is not None:
            self.amount = amount
        if format is not None:
            self.format = format
        if resource_type is not None:
            self.resource_type = resource_type
        if expire_time is not None:
            self.expire_time = expire_time
        if measure_unit is not None:
            self.measure_unit = measure_unit
        if skill_chip is not None:
            self.skill_chip = skill_chip
        if versions is not None:
            self.versions = versions
        if skill_name is not None:
            self.skill_name = skill_name
        if skill_type is not None:
            self.skill_type = skill_type
        if used_amount is not None:
            self.used_amount = used_amount
        if charge_model is not None:
            self.charge_model = charge_model
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if skill_id is not None:
            self.skill_id = skill_id
        if skill_platform is not None:
            self.skill_platform = skill_platform
        if order_limit is not None:
            self.order_limit = order_limit
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status

    @property
    def expiration_stop_flag(self):
        r"""Gets the expiration_stop_flag of this ShowSkillOrderInfoResponse.

        技能是否支持永久使用标识。1标识支持，0为不支持

        :return: The expiration_stop_flag of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._expiration_stop_flag

    @expiration_stop_flag.setter
    def expiration_stop_flag(self, expiration_stop_flag):
        r"""Sets the expiration_stop_flag of this ShowSkillOrderInfoResponse.

        技能是否支持永久使用标识。1标识支持，0为不支持

        :param expiration_stop_flag: The expiration_stop_flag of this ShowSkillOrderInfoResponse.
        :type expiration_stop_flag: int
        """
        self._expiration_stop_flag = expiration_stop_flag

    @property
    def package_order_id(self):
        r"""Gets the package_order_id of this ShowSkillOrderInfoResponse.

        技能套餐包订单ID

        :return: The package_order_id of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._package_order_id

    @package_order_id.setter
    def package_order_id(self, package_order_id):
        r"""Sets the package_order_id of this ShowSkillOrderInfoResponse.

        技能套餐包订单ID

        :param package_order_id: The package_order_id of this ShowSkillOrderInfoResponse.
        :type package_order_id: str
        """
        self._package_order_id = package_order_id

    @property
    def icon(self):
        r"""Gets the icon of this ShowSkillOrderInfoResponse.

        技能图标

        :return: The icon of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this ShowSkillOrderInfoResponse.

        技能图标

        :param icon: The icon of this ShowSkillOrderInfoResponse.
        :type icon: str
        """
        self._icon = icon

    @property
    def commission_flag(self):
        r"""Gets the commission_flag of this ShowSkillOrderInfoResponse.

        定制技能标识

        :return: The commission_flag of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._commission_flag

    @commission_flag.setter
    def commission_flag(self, commission_flag):
        r"""Sets the commission_flag of this ShowSkillOrderInfoResponse.

        定制技能标识

        :param commission_flag: The commission_flag of this ShowSkillOrderInfoResponse.
        :type commission_flag: int
        """
        self._commission_flag = commission_flag

    @property
    def product_info(self):
        r"""Gets the product_info of this ShowSkillOrderInfoResponse.

        产品收费编码信息

        :return: The product_info of this ShowSkillOrderInfoResponse.
        :rtype: list[str]
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this ShowSkillOrderInfoResponse.

        产品收费编码信息

        :param product_info: The product_info of this ShowSkillOrderInfoResponse.
        :type product_info: list[str]
        """
        self._product_info = product_info

    @property
    def package_id(self):
        r"""Gets the package_id of this ShowSkillOrderInfoResponse.

        套餐包ID

        :return: The package_id of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this ShowSkillOrderInfoResponse.

        套餐包ID

        :param package_id: The package_id of this ShowSkillOrderInfoResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def measure_type(self):
        r"""Gets the measure_type of this ShowSkillOrderInfoResponse.

        计费类型，physical_src表示按物理量纲收费，比如包周期 ，src表示一次性收费

        :return: The measure_type of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        r"""Sets the measure_type of this ShowSkillOrderInfoResponse.

        计费类型，physical_src表示按物理量纲收费，比如包周期 ，src表示一次性收费

        :param measure_type: The measure_type of this ShowSkillOrderInfoResponse.
        :type measure_type: str
        """
        self._measure_type = measure_type

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSkillOrderInfoResponse.

        更新时间

        :return: The update_time of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSkillOrderInfoResponse.

        更新时间

        :param update_time: The update_time of this ShowSkillOrderInfoResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def channel_limit(self):
        r"""Gets the channel_limit of this ShowSkillOrderInfoResponse.

        通道数限制

        :return: The channel_limit of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._channel_limit

    @channel_limit.setter
    def channel_limit(self, channel_limit):
        r"""Sets the channel_limit of this ShowSkillOrderInfoResponse.

        通道数限制

        :param channel_limit: The channel_limit of this ShowSkillOrderInfoResponse.
        :type channel_limit: int
        """
        self._channel_limit = channel_limit

    @property
    def resource_step_size(self):
        r"""Gets the resource_step_size of this ShowSkillOrderInfoResponse.

        步长

        :return: The resource_step_size of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._resource_step_size

    @resource_step_size.setter
    def resource_step_size(self, resource_step_size):
        r"""Sets the resource_step_size of this ShowSkillOrderInfoResponse.

        步长

        :param resource_step_size: The resource_step_size of this ShowSkillOrderInfoResponse.
        :type resource_step_size: int
        """
        self._resource_step_size = resource_step_size

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ShowSkillOrderInfoResponse.

        云服务编码

        :return: The cloud_service_type of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ShowSkillOrderInfoResponse.

        云服务编码

        :param cloud_service_type: The cloud_service_type of this ShowSkillOrderInfoResponse.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def developer_id(self):
        r"""Gets the developer_id of this ShowSkillOrderInfoResponse.

        开发者ID

        :return: The developer_id of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        r"""Sets the developer_id of this ShowSkillOrderInfoResponse.

        开发者ID

        :param developer_id: The developer_id of this ShowSkillOrderInfoResponse.
        :type developer_id: str
        """
        self._developer_id = developer_id

    @property
    def amount(self):
        r"""Gets the amount of this ShowSkillOrderInfoResponse.

        订单数量

        :return: The amount of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this ShowSkillOrderInfoResponse.

        订单数量

        :param amount: The amount of this ShowSkillOrderInfoResponse.
        :type amount: int
        """
        self._amount = amount

    @property
    def format(self):
        r"""Gets the format of this ShowSkillOrderInfoResponse.

        技能类型，文件类型file，镜像类型iamge

        :return: The format of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ShowSkillOrderInfoResponse.

        技能类型，文件类型file，镜像类型iamge

        :param format: The format of this ShowSkillOrderInfoResponse.
        :type format: str
        """
        self._format = format

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowSkillOrderInfoResponse.

        资源类别

        :return: The resource_type of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowSkillOrderInfoResponse.

        资源类别

        :param resource_type: The resource_type of this ShowSkillOrderInfoResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowSkillOrderInfoResponse.

        到期时间

        :return: The expire_time of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowSkillOrderInfoResponse.

        到期时间

        :param expire_time: The expire_time of this ShowSkillOrderInfoResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def measure_unit(self):
        r"""Gets the measure_unit of this ShowSkillOrderInfoResponse.

        计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费

        :return: The measure_unit of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        r"""Sets the measure_unit of this ShowSkillOrderInfoResponse.

        计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费

        :param measure_unit: The measure_unit of this ShowSkillOrderInfoResponse.
        :type measure_unit: str
        """
        self._measure_unit = measure_unit

    @property
    def skill_chip(self):
        r"""Gets the skill_chip of this ShowSkillOrderInfoResponse.

        芯片类别

        :return: The skill_chip of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._skill_chip

    @skill_chip.setter
    def skill_chip(self, skill_chip):
        r"""Sets the skill_chip of this ShowSkillOrderInfoResponse.

        芯片类别

        :param skill_chip: The skill_chip of this ShowSkillOrderInfoResponse.
        :type skill_chip: str
        """
        self._skill_chip = skill_chip

    @property
    def versions(self):
        r"""Gets the versions of this ShowSkillOrderInfoResponse.

        技能版本列表

        :return: The versions of this ShowSkillOrderInfoResponse.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ShowSkillOrderInfoResponse.

        技能版本列表

        :param versions: The versions of this ShowSkillOrderInfoResponse.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def skill_name(self):
        r"""Gets the skill_name of this ShowSkillOrderInfoResponse.

        技能名字

        :return: The skill_name of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._skill_name

    @skill_name.setter
    def skill_name(self, skill_name):
        r"""Sets the skill_name of this ShowSkillOrderInfoResponse.

        技能名字

        :param skill_name: The skill_name of this ShowSkillOrderInfoResponse.
        :type skill_name: str
        """
        self._skill_name = skill_name

    @property
    def skill_type(self):
        r"""Gets the skill_type of this ShowSkillOrderInfoResponse.

        技能类别

        :return: The skill_type of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._skill_type

    @skill_type.setter
    def skill_type(self, skill_type):
        r"""Sets the skill_type of this ShowSkillOrderInfoResponse.

        技能类别

        :param skill_type: The skill_type of this ShowSkillOrderInfoResponse.
        :type skill_type: str
        """
        self._skill_type = skill_type

    @property
    def used_amount(self):
        r"""Gets the used_amount of this ShowSkillOrderInfoResponse.

        订单使用份数

        :return: The used_amount of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        r"""Sets the used_amount of this ShowSkillOrderInfoResponse.

        订单使用份数

        :param used_amount: The used_amount of this ShowSkillOrderInfoResponse.
        :type used_amount: int
        """
        self._used_amount = used_amount

    @property
    def charge_model(self):
        r"""Gets the charge_model of this ShowSkillOrderInfoResponse.

        计费模式

        :return: The charge_model of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        r"""Sets the charge_model of this ShowSkillOrderInfoResponse.

        计费模式

        :param charge_model: The charge_model of this ShowSkillOrderInfoResponse.
        :type charge_model: int
        """
        self._charge_model = charge_model

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ShowSkillOrderInfoResponse.

        资源编码

        :return: The resource_spec_code of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ShowSkillOrderInfoResponse.

        资源编码

        :param resource_spec_code: The resource_spec_code of this ShowSkillOrderInfoResponse.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def skill_id(self):
        r"""Gets the skill_id of this ShowSkillOrderInfoResponse.

        技能ID

        :return: The skill_id of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this ShowSkillOrderInfoResponse.

        技能ID

        :param skill_id: The skill_id of this ShowSkillOrderInfoResponse.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def skill_platform(self):
        r"""Gets the skill_platform of this ShowSkillOrderInfoResponse.

        技能支持的平台

        :return: The skill_platform of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._skill_platform

    @skill_platform.setter
    def skill_platform(self, skill_platform):
        r"""Sets the skill_platform of this ShowSkillOrderInfoResponse.

        技能支持的平台

        :param skill_platform: The skill_platform of this ShowSkillOrderInfoResponse.
        :type skill_platform: str
        """
        self._skill_platform = skill_platform

    @property
    def order_limit(self):
        r"""Gets the order_limit of this ShowSkillOrderInfoResponse.

        订单购买限制

        :return: The order_limit of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._order_limit

    @order_limit.setter
    def order_limit(self, order_limit):
        r"""Sets the order_limit of this ShowSkillOrderInfoResponse.

        订单购买限制

        :param order_limit: The order_limit of this ShowSkillOrderInfoResponse.
        :type order_limit: int
        """
        self._order_limit = order_limit

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowSkillOrderInfoResponse.

        订单ID

        :return: The order_id of this ShowSkillOrderInfoResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowSkillOrderInfoResponse.

        订单ID

        :param order_id: The order_id of this ShowSkillOrderInfoResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        r"""Gets the status of this ShowSkillOrderInfoResponse.

        订单状态，0表示正常状态，1表示冻结状态，2表示受限状态

        :return: The status of this ShowSkillOrderInfoResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSkillOrderInfoResponse.

        订单状态，0表示正常状态，1表示冻结状态，2表示受限状态

        :param status: The status of this ShowSkillOrderInfoResponse.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ShowSkillOrderInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
