# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLakeFormationInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'shared': 'bool',
        'default_instance': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'status': 'str',
        'resource_progress': 'int',
        'resource_expected_duration': 'int',
        'scale_progress': 'int',
        'scale_expected_duration': 'int',
        'in_recycle_bin': 'bool',
        'tags': 'list[ResourceTag]',
        'specs': 'list[CreateSpec]',
        'charge_mode': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'shared': 'shared',
        'default_instance': 'default_instance',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'resource_progress': 'resource_progress',
        'resource_expected_duration': 'resource_expected_duration',
        'scale_progress': 'scale_progress',
        'scale_expected_duration': 'scale_expected_duration',
        'in_recycle_bin': 'in_recycle_bin',
        'tags': 'tags',
        'specs': 'specs',
        'charge_mode': 'charge_mode',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, instance_id=None, name=None, description=None, enterprise_project_id=None, shared=None, default_instance=None, create_time=None, update_time=None, status=None, resource_progress=None, resource_expected_duration=None, scale_progress=None, scale_expected_duration=None, in_recycle_bin=None, tags=None, specs=None, charge_mode=None, x_request_id=None):
        """ShowLakeFormationInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。
        :type instance_id: str
        :param name: 实例名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param shared: 逻辑多租和物理多租的判断。false为物理多租；true为逻辑多租。
        :type shared: bool
        :param default_instance: 是否为默认实例
        :type default_instance: bool
        :param create_time: 实例创建时间戳
        :type create_time: datetime
        :param update_time: 实例更新时间戳
        :type update_time: datetime
        :param status: 实例状态,RESOURCE_PREPARATION-实例资源准备中,RUNNING-实例运行中,RESOURCE_RELEASE-实例资源释放中,DELETED-实例已释放,RESOURCE_PREPARATION_FAIL-实例资源准备失败,FROZEN_RELEASABLE-可恢复冻结,FROZEN_UNRELEASABLE-不可恢复冻结,RECOVERING-恢复中,DELETING-删除中,SCALING-扩容中,SCALE_FAIL-扩容失败
        :type status: str
        :param resource_progress: 资源准备进度百分比，只有当实例处于资源准备中状态时才会计算并返回该值
        :type resource_progress: int
        :param resource_expected_duration: 资源准备预计时长，单位分钟
        :type resource_expected_duration: int
        :param scale_progress: 规格变更进度百分比，只有当实例处于规格变更中状态时才会计算并返回该值
        :type scale_progress: int
        :param scale_expected_duration: 规格变更预计时长，单位分钟
        :type scale_expected_duration: int
        :param in_recycle_bin: 是否在回收站
        :type in_recycle_bin: bool
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        :param specs: 规格信息
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        :param charge_mode: 计费模式,postPaid&#x3D;按需计费,prePaid&#x3D;包周期计费
        :type charge_mode: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowLakeFormationInstanceResponse, self).__init__()

        self._instance_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._shared = None
        self._default_instance = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._resource_progress = None
        self._resource_expected_duration = None
        self._scale_progress = None
        self._scale_expected_duration = None
        self._in_recycle_bin = None
        self._tags = None
        self._specs = None
        self._charge_mode = None
        self._x_request_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if shared is not None:
            self.shared = shared
        if default_instance is not None:
            self.default_instance = default_instance
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if status is not None:
            self.status = status
        if resource_progress is not None:
            self.resource_progress = resource_progress
        if resource_expected_duration is not None:
            self.resource_expected_duration = resource_expected_duration
        if scale_progress is not None:
            self.scale_progress = scale_progress
        if scale_expected_duration is not None:
            self.scale_expected_duration = scale_expected_duration
        if in_recycle_bin is not None:
            self.in_recycle_bin = in_recycle_bin
        if tags is not None:
            self.tags = tags
        if specs is not None:
            self.specs = specs
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowLakeFormationInstanceResponse.

        LakeFormation实例ID。

        :return: The instance_id of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowLakeFormationInstanceResponse.

        LakeFormation实例ID。

        :param instance_id: The instance_id of this ShowLakeFormationInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this ShowLakeFormationInstanceResponse.

        实例名称。

        :return: The name of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowLakeFormationInstanceResponse.

        实例名称。

        :param name: The name of this ShowLakeFormationInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowLakeFormationInstanceResponse.

        描述。

        :return: The description of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowLakeFormationInstanceResponse.

        描述。

        :param description: The description of this ShowLakeFormationInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowLakeFormationInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowLakeFormationInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowLakeFormationInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def shared(self):
        """Gets the shared of this ShowLakeFormationInstanceResponse.

        逻辑多租和物理多租的判断。false为物理多租；true为逻辑多租。

        :return: The shared of this ShowLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this ShowLakeFormationInstanceResponse.

        逻辑多租和物理多租的判断。false为物理多租；true为逻辑多租。

        :param shared: The shared of this ShowLakeFormationInstanceResponse.
        :type shared: bool
        """
        self._shared = shared

    @property
    def default_instance(self):
        """Gets the default_instance of this ShowLakeFormationInstanceResponse.

        是否为默认实例

        :return: The default_instance of this ShowLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._default_instance

    @default_instance.setter
    def default_instance(self, default_instance):
        """Sets the default_instance of this ShowLakeFormationInstanceResponse.

        是否为默认实例

        :param default_instance: The default_instance of this ShowLakeFormationInstanceResponse.
        :type default_instance: bool
        """
        self._default_instance = default_instance

    @property
    def create_time(self):
        """Gets the create_time of this ShowLakeFormationInstanceResponse.

        实例创建时间戳

        :return: The create_time of this ShowLakeFormationInstanceResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowLakeFormationInstanceResponse.

        实例创建时间戳

        :param create_time: The create_time of this ShowLakeFormationInstanceResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowLakeFormationInstanceResponse.

        实例更新时间戳

        :return: The update_time of this ShowLakeFormationInstanceResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowLakeFormationInstanceResponse.

        实例更新时间戳

        :param update_time: The update_time of this ShowLakeFormationInstanceResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def status(self):
        """Gets the status of this ShowLakeFormationInstanceResponse.

        实例状态,RESOURCE_PREPARATION-实例资源准备中,RUNNING-实例运行中,RESOURCE_RELEASE-实例资源释放中,DELETED-实例已释放,RESOURCE_PREPARATION_FAIL-实例资源准备失败,FROZEN_RELEASABLE-可恢复冻结,FROZEN_UNRELEASABLE-不可恢复冻结,RECOVERING-恢复中,DELETING-删除中,SCALING-扩容中,SCALE_FAIL-扩容失败

        :return: The status of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowLakeFormationInstanceResponse.

        实例状态,RESOURCE_PREPARATION-实例资源准备中,RUNNING-实例运行中,RESOURCE_RELEASE-实例资源释放中,DELETED-实例已释放,RESOURCE_PREPARATION_FAIL-实例资源准备失败,FROZEN_RELEASABLE-可恢复冻结,FROZEN_UNRELEASABLE-不可恢复冻结,RECOVERING-恢复中,DELETING-删除中,SCALING-扩容中,SCALE_FAIL-扩容失败

        :param status: The status of this ShowLakeFormationInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def resource_progress(self):
        """Gets the resource_progress of this ShowLakeFormationInstanceResponse.

        资源准备进度百分比，只有当实例处于资源准备中状态时才会计算并返回该值

        :return: The resource_progress of this ShowLakeFormationInstanceResponse.
        :rtype: int
        """
        return self._resource_progress

    @resource_progress.setter
    def resource_progress(self, resource_progress):
        """Sets the resource_progress of this ShowLakeFormationInstanceResponse.

        资源准备进度百分比，只有当实例处于资源准备中状态时才会计算并返回该值

        :param resource_progress: The resource_progress of this ShowLakeFormationInstanceResponse.
        :type resource_progress: int
        """
        self._resource_progress = resource_progress

    @property
    def resource_expected_duration(self):
        """Gets the resource_expected_duration of this ShowLakeFormationInstanceResponse.

        资源准备预计时长，单位分钟

        :return: The resource_expected_duration of this ShowLakeFormationInstanceResponse.
        :rtype: int
        """
        return self._resource_expected_duration

    @resource_expected_duration.setter
    def resource_expected_duration(self, resource_expected_duration):
        """Sets the resource_expected_duration of this ShowLakeFormationInstanceResponse.

        资源准备预计时长，单位分钟

        :param resource_expected_duration: The resource_expected_duration of this ShowLakeFormationInstanceResponse.
        :type resource_expected_duration: int
        """
        self._resource_expected_duration = resource_expected_duration

    @property
    def scale_progress(self):
        """Gets the scale_progress of this ShowLakeFormationInstanceResponse.

        规格变更进度百分比，只有当实例处于规格变更中状态时才会计算并返回该值

        :return: The scale_progress of this ShowLakeFormationInstanceResponse.
        :rtype: int
        """
        return self._scale_progress

    @scale_progress.setter
    def scale_progress(self, scale_progress):
        """Sets the scale_progress of this ShowLakeFormationInstanceResponse.

        规格变更进度百分比，只有当实例处于规格变更中状态时才会计算并返回该值

        :param scale_progress: The scale_progress of this ShowLakeFormationInstanceResponse.
        :type scale_progress: int
        """
        self._scale_progress = scale_progress

    @property
    def scale_expected_duration(self):
        """Gets the scale_expected_duration of this ShowLakeFormationInstanceResponse.

        规格变更预计时长，单位分钟

        :return: The scale_expected_duration of this ShowLakeFormationInstanceResponse.
        :rtype: int
        """
        return self._scale_expected_duration

    @scale_expected_duration.setter
    def scale_expected_duration(self, scale_expected_duration):
        """Sets the scale_expected_duration of this ShowLakeFormationInstanceResponse.

        规格变更预计时长，单位分钟

        :param scale_expected_duration: The scale_expected_duration of this ShowLakeFormationInstanceResponse.
        :type scale_expected_duration: int
        """
        self._scale_expected_duration = scale_expected_duration

    @property
    def in_recycle_bin(self):
        """Gets the in_recycle_bin of this ShowLakeFormationInstanceResponse.

        是否在回收站

        :return: The in_recycle_bin of this ShowLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        """Sets the in_recycle_bin of this ShowLakeFormationInstanceResponse.

        是否在回收站

        :param in_recycle_bin: The in_recycle_bin of this ShowLakeFormationInstanceResponse.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

    @property
    def tags(self):
        """Gets the tags of this ShowLakeFormationInstanceResponse.

        标签列表

        :return: The tags of this ShowLakeFormationInstanceResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowLakeFormationInstanceResponse.

        标签列表

        :param tags: The tags of this ShowLakeFormationInstanceResponse.
        :type tags: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def specs(self):
        """Gets the specs of this ShowLakeFormationInstanceResponse.

        规格信息

        :return: The specs of this ShowLakeFormationInstanceResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this ShowLakeFormationInstanceResponse.

        规格信息

        :param specs: The specs of this ShowLakeFormationInstanceResponse.
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        self._specs = specs

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ShowLakeFormationInstanceResponse.

        计费模式,postPaid=按需计费,prePaid=包周期计费

        :return: The charge_mode of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ShowLakeFormationInstanceResponse.

        计费模式,postPaid=按需计费,prePaid=包周期计费

        :param charge_mode: The charge_mode of this ShowLakeFormationInstanceResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowLakeFormationInstanceResponse.

        :return: The x_request_id of this ShowLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowLakeFormationInstanceResponse.

        :param x_request_id: The x_request_id of this ShowLakeFormationInstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowLakeFormationInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
