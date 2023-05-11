# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkillInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_scenes': 'str',
        'app_template_id': 'str',
        'icon': 'str',
        'version_num': 'int',
        'description': 'str',
        'product_info': 'list[str]',
        'type': 'str',
        'platform': 'str',
        'self_dev_flag': 'int',
        'measure_type': 'str',
        'approval_result': 'str',
        'update_time': 'str',
        'channel_limit': 'int',
        'publish_time': 'str',
        'resource_step_size': 'int',
        'approval_time': 'str',
        'cloud_service_type': 'str',
        'summary': 'str',
        'test_status': 'int',
        'chip': 'str',
        'is_verify_model': 'bool',
        'format': 'str',
        'resource_type': 'str',
        'version': 'str',
        'measure_unit': 'str',
        'tags': 'list[str]',
        'size': 'int',
        'test_result': 'str',
        'install_times': 'int',
        'privacy_policy': 'list[str]',
        'name': 'str',
        'scenes': 'list[str]',
        'charge_model': 'int',
        'resource_spec_code': 'str',
        'skill_id': 'str',
        'developer': 'str',
        'main_scenes': 'str',
        'device_types': 'list[str]',
        'status': 'int'
    }

    attribute_map = {
        'sub_scenes': 'sub_scenes',
        'app_template_id': 'app_template_id',
        'icon': 'icon',
        'version_num': 'version_num',
        'description': 'description',
        'product_info': 'product_info',
        'type': 'type',
        'platform': 'platform',
        'self_dev_flag': 'self_dev_flag',
        'measure_type': 'measure_type',
        'approval_result': 'approval_result',
        'update_time': 'update_time',
        'channel_limit': 'channel_limit',
        'publish_time': 'publish_time',
        'resource_step_size': 'resource_step_size',
        'approval_time': 'approval_time',
        'cloud_service_type': 'cloud_service_type',
        'summary': 'summary',
        'test_status': 'test_status',
        'chip': 'chip',
        'is_verify_model': 'is_verify_model',
        'format': 'format',
        'resource_type': 'resource_type',
        'version': 'version',
        'measure_unit': 'measure_unit',
        'tags': 'tags',
        'size': 'size',
        'test_result': 'test_result',
        'install_times': 'install_times',
        'privacy_policy': 'privacy_policy',
        'name': 'name',
        'scenes': 'scenes',
        'charge_model': 'charge_model',
        'resource_spec_code': 'resource_spec_code',
        'skill_id': 'skill_id',
        'developer': 'developer',
        'main_scenes': 'main_scenes',
        'device_types': 'device_types',
        'status': 'status'
    }

    def __init__(self, sub_scenes=None, app_template_id=None, icon=None, version_num=None, description=None, product_info=None, type=None, platform=None, self_dev_flag=None, measure_type=None, approval_result=None, update_time=None, channel_limit=None, publish_time=None, resource_step_size=None, approval_time=None, cloud_service_type=None, summary=None, test_status=None, chip=None, is_verify_model=None, format=None, resource_type=None, version=None, measure_unit=None, tags=None, size=None, test_result=None, install_times=None, privacy_policy=None, name=None, scenes=None, charge_model=None, resource_spec_code=None, skill_id=None, developer=None, main_scenes=None, device_types=None, status=None):
        """SkillInfo

        The model defined in huaweicloud sdk

        :param sub_scenes: 技能应用场景
        :type sub_scenes: str
        :param app_template_id: 应用模板ID
        :type app_template_id: str
        :param icon: 技能图标
        :type icon: str
        :param version_num: 技能版本数量
        :type version_num: int
        :param description: 技能描述
        :type description: str
        :param product_info: 计费编码信息
        :type product_info: list[str]
        :param type: 技能类别，分为standard和lite
        :type type: str
        :param platform: 技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows
        :type platform: str
        :param self_dev_flag: 自研标识，1表示是HiLens自研算法。
        :type self_dev_flag: int
        :param measure_type: 计费类型，physical_src表示物理量标，如按周期收费。 src表示一次性
        :type measure_type: str
        :param approval_result: 技能审核结果
        :type approval_result: str
        :param update_time: 更新时间，形如2022-06-30 17:22:48 GMT+08:00
        :type update_time: str
        :param channel_limit: 通道数
        :type channel_limit: int
        :param publish_time: 发布时间
        :type publish_time: str
        :param resource_step_size: 步长
        :type resource_step_size: int
        :param approval_time: 审批时间
        :type approval_time: str
        :param cloud_service_type: 云服务编码
        :type cloud_service_type: str
        :param summary: 摘要
        :type summary: str
        :param test_status: 测试状态
        :type test_status: int
        :param chip: 芯片
        :type chip: str
        :param is_verify_model: 是否校验模型
        :type is_verify_model: bool
        :param format: 技能类型，文件类型file，镜像类型iamge
        :type format: str
        :param resource_type: 资源类别
        :type resource_type: str
        :param version: 技能版本
        :type version: str
        :param measure_unit: 计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费
        :type measure_unit: str
        :param tags: 标签
        :type tags: list[str]
        :param size: 技能大小
        :type size: int
        :param test_result: 测试结果
        :type test_result: str
        :param install_times: 安装次数
        :type install_times: int
        :param privacy_policy: 隐私条款
        :type privacy_policy: list[str]
        :param name: 技能名字
        :type name: str
        :param scenes: 技能场景
        :type scenes: list[str]
        :param charge_model: 计费模式
        :type charge_model: int
        :param resource_spec_code: 云服务资源编码
        :type resource_spec_code: str
        :param skill_id: 技能ID
        :type skill_id: str
        :param developer: 开发者名字
        :type developer: str
        :param main_scenes: 主场景
        :type main_scenes: str
        :param device_types: 所支持的设备类别
        :type device_types: list[str]
        :param status: 技能状态
        :type status: int
        """
        
        

        self._sub_scenes = None
        self._app_template_id = None
        self._icon = None
        self._version_num = None
        self._description = None
        self._product_info = None
        self._type = None
        self._platform = None
        self._self_dev_flag = None
        self._measure_type = None
        self._approval_result = None
        self._update_time = None
        self._channel_limit = None
        self._publish_time = None
        self._resource_step_size = None
        self._approval_time = None
        self._cloud_service_type = None
        self._summary = None
        self._test_status = None
        self._chip = None
        self._is_verify_model = None
        self._format = None
        self._resource_type = None
        self._version = None
        self._measure_unit = None
        self._tags = None
        self._size = None
        self._test_result = None
        self._install_times = None
        self._privacy_policy = None
        self._name = None
        self._scenes = None
        self._charge_model = None
        self._resource_spec_code = None
        self._skill_id = None
        self._developer = None
        self._main_scenes = None
        self._device_types = None
        self._status = None
        self.discriminator = None

        self.sub_scenes = sub_scenes
        self.app_template_id = app_template_id
        self.icon = icon
        self.version_num = version_num
        self.description = description
        self.product_info = product_info
        self.type = type
        self.platform = platform
        self.self_dev_flag = self_dev_flag
        self.measure_type = measure_type
        self.approval_result = approval_result
        self.update_time = update_time
        self.channel_limit = channel_limit
        self.publish_time = publish_time
        self.resource_step_size = resource_step_size
        self.approval_time = approval_time
        self.cloud_service_type = cloud_service_type
        self.summary = summary
        self.test_status = test_status
        self.chip = chip
        self.is_verify_model = is_verify_model
        self.format = format
        self.resource_type = resource_type
        self.version = version
        self.measure_unit = measure_unit
        self.tags = tags
        self.size = size
        self.test_result = test_result
        self.install_times = install_times
        self.privacy_policy = privacy_policy
        self.name = name
        self.scenes = scenes
        self.charge_model = charge_model
        self.resource_spec_code = resource_spec_code
        self.skill_id = skill_id
        self.developer = developer
        self.main_scenes = main_scenes
        self.device_types = device_types
        self.status = status

    @property
    def sub_scenes(self):
        """Gets the sub_scenes of this SkillInfo.

        技能应用场景

        :return: The sub_scenes of this SkillInfo.
        :rtype: str
        """
        return self._sub_scenes

    @sub_scenes.setter
    def sub_scenes(self, sub_scenes):
        """Sets the sub_scenes of this SkillInfo.

        技能应用场景

        :param sub_scenes: The sub_scenes of this SkillInfo.
        :type sub_scenes: str
        """
        self._sub_scenes = sub_scenes

    @property
    def app_template_id(self):
        """Gets the app_template_id of this SkillInfo.

        应用模板ID

        :return: The app_template_id of this SkillInfo.
        :rtype: str
        """
        return self._app_template_id

    @app_template_id.setter
    def app_template_id(self, app_template_id):
        """Sets the app_template_id of this SkillInfo.

        应用模板ID

        :param app_template_id: The app_template_id of this SkillInfo.
        :type app_template_id: str
        """
        self._app_template_id = app_template_id

    @property
    def icon(self):
        """Gets the icon of this SkillInfo.

        技能图标

        :return: The icon of this SkillInfo.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this SkillInfo.

        技能图标

        :param icon: The icon of this SkillInfo.
        :type icon: str
        """
        self._icon = icon

    @property
    def version_num(self):
        """Gets the version_num of this SkillInfo.

        技能版本数量

        :return: The version_num of this SkillInfo.
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        """Sets the version_num of this SkillInfo.

        技能版本数量

        :param version_num: The version_num of this SkillInfo.
        :type version_num: int
        """
        self._version_num = version_num

    @property
    def description(self):
        """Gets the description of this SkillInfo.

        技能描述

        :return: The description of this SkillInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SkillInfo.

        技能描述

        :param description: The description of this SkillInfo.
        :type description: str
        """
        self._description = description

    @property
    def product_info(self):
        """Gets the product_info of this SkillInfo.

        计费编码信息

        :return: The product_info of this SkillInfo.
        :rtype: list[str]
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this SkillInfo.

        计费编码信息

        :param product_info: The product_info of this SkillInfo.
        :type product_info: list[str]
        """
        self._product_info = product_info

    @property
    def type(self):
        """Gets the type of this SkillInfo.

        技能类别，分为standard和lite

        :return: The type of this SkillInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SkillInfo.

        技能类别，分为standard和lite

        :param type: The type of this SkillInfo.
        :type type: str
        """
        self._type = type

    @property
    def platform(self):
        """Gets the platform of this SkillInfo.

        技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows

        :return: The platform of this SkillInfo.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this SkillInfo.

        技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows

        :param platform: The platform of this SkillInfo.
        :type platform: str
        """
        self._platform = platform

    @property
    def self_dev_flag(self):
        """Gets the self_dev_flag of this SkillInfo.

        自研标识，1表示是HiLens自研算法。

        :return: The self_dev_flag of this SkillInfo.
        :rtype: int
        """
        return self._self_dev_flag

    @self_dev_flag.setter
    def self_dev_flag(self, self_dev_flag):
        """Sets the self_dev_flag of this SkillInfo.

        自研标识，1表示是HiLens自研算法。

        :param self_dev_flag: The self_dev_flag of this SkillInfo.
        :type self_dev_flag: int
        """
        self._self_dev_flag = self_dev_flag

    @property
    def measure_type(self):
        """Gets the measure_type of this SkillInfo.

        计费类型，physical_src表示物理量标，如按周期收费。 src表示一次性

        :return: The measure_type of this SkillInfo.
        :rtype: str
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this SkillInfo.

        计费类型，physical_src表示物理量标，如按周期收费。 src表示一次性

        :param measure_type: The measure_type of this SkillInfo.
        :type measure_type: str
        """
        self._measure_type = measure_type

    @property
    def approval_result(self):
        """Gets the approval_result of this SkillInfo.

        技能审核结果

        :return: The approval_result of this SkillInfo.
        :rtype: str
        """
        return self._approval_result

    @approval_result.setter
    def approval_result(self, approval_result):
        """Sets the approval_result of this SkillInfo.

        技能审核结果

        :param approval_result: The approval_result of this SkillInfo.
        :type approval_result: str
        """
        self._approval_result = approval_result

    @property
    def update_time(self):
        """Gets the update_time of this SkillInfo.

        更新时间，形如2022-06-30 17:22:48 GMT+08:00

        :return: The update_time of this SkillInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SkillInfo.

        更新时间，形如2022-06-30 17:22:48 GMT+08:00

        :param update_time: The update_time of this SkillInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def channel_limit(self):
        """Gets the channel_limit of this SkillInfo.

        通道数

        :return: The channel_limit of this SkillInfo.
        :rtype: int
        """
        return self._channel_limit

    @channel_limit.setter
    def channel_limit(self, channel_limit):
        """Sets the channel_limit of this SkillInfo.

        通道数

        :param channel_limit: The channel_limit of this SkillInfo.
        :type channel_limit: int
        """
        self._channel_limit = channel_limit

    @property
    def publish_time(self):
        """Gets the publish_time of this SkillInfo.

        发布时间

        :return: The publish_time of this SkillInfo.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this SkillInfo.

        发布时间

        :param publish_time: The publish_time of this SkillInfo.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def resource_step_size(self):
        """Gets the resource_step_size of this SkillInfo.

        步长

        :return: The resource_step_size of this SkillInfo.
        :rtype: int
        """
        return self._resource_step_size

    @resource_step_size.setter
    def resource_step_size(self, resource_step_size):
        """Sets the resource_step_size of this SkillInfo.

        步长

        :param resource_step_size: The resource_step_size of this SkillInfo.
        :type resource_step_size: int
        """
        self._resource_step_size = resource_step_size

    @property
    def approval_time(self):
        """Gets the approval_time of this SkillInfo.

        审批时间

        :return: The approval_time of this SkillInfo.
        :rtype: str
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        """Sets the approval_time of this SkillInfo.

        审批时间

        :param approval_time: The approval_time of this SkillInfo.
        :type approval_time: str
        """
        self._approval_time = approval_time

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this SkillInfo.

        云服务编码

        :return: The cloud_service_type of this SkillInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this SkillInfo.

        云服务编码

        :param cloud_service_type: The cloud_service_type of this SkillInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def summary(self):
        """Gets the summary of this SkillInfo.

        摘要

        :return: The summary of this SkillInfo.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this SkillInfo.

        摘要

        :param summary: The summary of this SkillInfo.
        :type summary: str
        """
        self._summary = summary

    @property
    def test_status(self):
        """Gets the test_status of this SkillInfo.

        测试状态

        :return: The test_status of this SkillInfo.
        :rtype: int
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status):
        """Sets the test_status of this SkillInfo.

        测试状态

        :param test_status: The test_status of this SkillInfo.
        :type test_status: int
        """
        self._test_status = test_status

    @property
    def chip(self):
        """Gets the chip of this SkillInfo.

        芯片

        :return: The chip of this SkillInfo.
        :rtype: str
        """
        return self._chip

    @chip.setter
    def chip(self, chip):
        """Sets the chip of this SkillInfo.

        芯片

        :param chip: The chip of this SkillInfo.
        :type chip: str
        """
        self._chip = chip

    @property
    def is_verify_model(self):
        """Gets the is_verify_model of this SkillInfo.

        是否校验模型

        :return: The is_verify_model of this SkillInfo.
        :rtype: bool
        """
        return self._is_verify_model

    @is_verify_model.setter
    def is_verify_model(self, is_verify_model):
        """Sets the is_verify_model of this SkillInfo.

        是否校验模型

        :param is_verify_model: The is_verify_model of this SkillInfo.
        :type is_verify_model: bool
        """
        self._is_verify_model = is_verify_model

    @property
    def format(self):
        """Gets the format of this SkillInfo.

        技能类型，文件类型file，镜像类型iamge

        :return: The format of this SkillInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SkillInfo.

        技能类型，文件类型file，镜像类型iamge

        :param format: The format of this SkillInfo.
        :type format: str
        """
        self._format = format

    @property
    def resource_type(self):
        """Gets the resource_type of this SkillInfo.

        资源类别

        :return: The resource_type of this SkillInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SkillInfo.

        资源类别

        :param resource_type: The resource_type of this SkillInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def version(self):
        """Gets the version of this SkillInfo.

        技能版本

        :return: The version of this SkillInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SkillInfo.

        技能版本

        :param version: The version of this SkillInfo.
        :type version: str
        """
        self._version = version

    @property
    def measure_unit(self):
        """Gets the measure_unit of this SkillInfo.

        计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费

        :return: The measure_unit of this SkillInfo.
        :rtype: str
        """
        return self._measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        """Sets the measure_unit of this SkillInfo.

        计费单位 qps 表示按qps收费，road表示技能路数instance 表示按实例收费

        :param measure_unit: The measure_unit of this SkillInfo.
        :type measure_unit: str
        """
        self._measure_unit = measure_unit

    @property
    def tags(self):
        """Gets the tags of this SkillInfo.

        标签

        :return: The tags of this SkillInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SkillInfo.

        标签

        :param tags: The tags of this SkillInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def size(self):
        """Gets the size of this SkillInfo.

        技能大小

        :return: The size of this SkillInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SkillInfo.

        技能大小

        :param size: The size of this SkillInfo.
        :type size: int
        """
        self._size = size

    @property
    def test_result(self):
        """Gets the test_result of this SkillInfo.

        测试结果

        :return: The test_result of this SkillInfo.
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this SkillInfo.

        测试结果

        :param test_result: The test_result of this SkillInfo.
        :type test_result: str
        """
        self._test_result = test_result

    @property
    def install_times(self):
        """Gets the install_times of this SkillInfo.

        安装次数

        :return: The install_times of this SkillInfo.
        :rtype: int
        """
        return self._install_times

    @install_times.setter
    def install_times(self, install_times):
        """Sets the install_times of this SkillInfo.

        安装次数

        :param install_times: The install_times of this SkillInfo.
        :type install_times: int
        """
        self._install_times = install_times

    @property
    def privacy_policy(self):
        """Gets the privacy_policy of this SkillInfo.

        隐私条款

        :return: The privacy_policy of this SkillInfo.
        :rtype: list[str]
        """
        return self._privacy_policy

    @privacy_policy.setter
    def privacy_policy(self, privacy_policy):
        """Sets the privacy_policy of this SkillInfo.

        隐私条款

        :param privacy_policy: The privacy_policy of this SkillInfo.
        :type privacy_policy: list[str]
        """
        self._privacy_policy = privacy_policy

    @property
    def name(self):
        """Gets the name of this SkillInfo.

        技能名字

        :return: The name of this SkillInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SkillInfo.

        技能名字

        :param name: The name of this SkillInfo.
        :type name: str
        """
        self._name = name

    @property
    def scenes(self):
        """Gets the scenes of this SkillInfo.

        技能场景

        :return: The scenes of this SkillInfo.
        :rtype: list[str]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        """Sets the scenes of this SkillInfo.

        技能场景

        :param scenes: The scenes of this SkillInfo.
        :type scenes: list[str]
        """
        self._scenes = scenes

    @property
    def charge_model(self):
        """Gets the charge_model of this SkillInfo.

        计费模式

        :return: The charge_model of this SkillInfo.
        :rtype: int
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        """Sets the charge_model of this SkillInfo.

        计费模式

        :param charge_model: The charge_model of this SkillInfo.
        :type charge_model: int
        """
        self._charge_model = charge_model

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this SkillInfo.

        云服务资源编码

        :return: The resource_spec_code of this SkillInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this SkillInfo.

        云服务资源编码

        :param resource_spec_code: The resource_spec_code of this SkillInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def skill_id(self):
        """Gets the skill_id of this SkillInfo.

        技能ID

        :return: The skill_id of this SkillInfo.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this SkillInfo.

        技能ID

        :param skill_id: The skill_id of this SkillInfo.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def developer(self):
        """Gets the developer of this SkillInfo.

        开发者名字

        :return: The developer of this SkillInfo.
        :rtype: str
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this SkillInfo.

        开发者名字

        :param developer: The developer of this SkillInfo.
        :type developer: str
        """
        self._developer = developer

    @property
    def main_scenes(self):
        """Gets the main_scenes of this SkillInfo.

        主场景

        :return: The main_scenes of this SkillInfo.
        :rtype: str
        """
        return self._main_scenes

    @main_scenes.setter
    def main_scenes(self, main_scenes):
        """Sets the main_scenes of this SkillInfo.

        主场景

        :param main_scenes: The main_scenes of this SkillInfo.
        :type main_scenes: str
        """
        self._main_scenes = main_scenes

    @property
    def device_types(self):
        """Gets the device_types of this SkillInfo.

        所支持的设备类别

        :return: The device_types of this SkillInfo.
        :rtype: list[str]
        """
        return self._device_types

    @device_types.setter
    def device_types(self, device_types):
        """Sets the device_types of this SkillInfo.

        所支持的设备类别

        :param device_types: The device_types of this SkillInfo.
        :type device_types: list[str]
        """
        self._device_types = device_types

    @property
    def status(self):
        """Gets the status of this SkillInfo.

        技能状态

        :return: The status of this SkillInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SkillInfo.

        技能状态

        :param status: The status of this SkillInfo.
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
        if not isinstance(other, SkillInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
