# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLakeFormationInstanceResponse(SdkResponse):

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
        'in_recycle_bin': 'bool'
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
        'in_recycle_bin': 'in_recycle_bin'
    }

    def __init__(self, instance_id=None, name=None, description=None, enterprise_project_id=None, shared=None, default_instance=None, create_time=None, update_time=None, status=None, in_recycle_bin=None):
        r"""UpdateLakeFormationInstanceResponse

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
        :param in_recycle_bin: 是否在回收站
        :type in_recycle_bin: bool
        """
        
        super(UpdateLakeFormationInstanceResponse, self).__init__()

        self._instance_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._shared = None
        self._default_instance = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._in_recycle_bin = None
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
        if in_recycle_bin is not None:
            self.in_recycle_bin = in_recycle_bin

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateLakeFormationInstanceResponse.

        LakeFormation实例ID。

        :return: The instance_id of this UpdateLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateLakeFormationInstanceResponse.

        LakeFormation实例ID。

        :param instance_id: The instance_id of this UpdateLakeFormationInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this UpdateLakeFormationInstanceResponse.

        实例名称。

        :return: The name of this UpdateLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLakeFormationInstanceResponse.

        实例名称。

        :param name: The name of this UpdateLakeFormationInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateLakeFormationInstanceResponse.

        描述。

        :return: The description of this UpdateLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLakeFormationInstanceResponse.

        描述。

        :param description: The description of this UpdateLakeFormationInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateLakeFormationInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this UpdateLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateLakeFormationInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this UpdateLakeFormationInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def shared(self):
        r"""Gets the shared of this UpdateLakeFormationInstanceResponse.

        逻辑多租和物理多租的判断。false为物理多租；true为逻辑多租。

        :return: The shared of this UpdateLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        r"""Sets the shared of this UpdateLakeFormationInstanceResponse.

        逻辑多租和物理多租的判断。false为物理多租；true为逻辑多租。

        :param shared: The shared of this UpdateLakeFormationInstanceResponse.
        :type shared: bool
        """
        self._shared = shared

    @property
    def default_instance(self):
        r"""Gets the default_instance of this UpdateLakeFormationInstanceResponse.

        是否为默认实例

        :return: The default_instance of this UpdateLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._default_instance

    @default_instance.setter
    def default_instance(self, default_instance):
        r"""Sets the default_instance of this UpdateLakeFormationInstanceResponse.

        是否为默认实例

        :param default_instance: The default_instance of this UpdateLakeFormationInstanceResponse.
        :type default_instance: bool
        """
        self._default_instance = default_instance

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateLakeFormationInstanceResponse.

        实例创建时间戳

        :return: The create_time of this UpdateLakeFormationInstanceResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateLakeFormationInstanceResponse.

        实例创建时间戳

        :param create_time: The create_time of this UpdateLakeFormationInstanceResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateLakeFormationInstanceResponse.

        实例更新时间戳

        :return: The update_time of this UpdateLakeFormationInstanceResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateLakeFormationInstanceResponse.

        实例更新时间戳

        :param update_time: The update_time of this UpdateLakeFormationInstanceResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def status(self):
        r"""Gets the status of this UpdateLakeFormationInstanceResponse.

        实例状态,RESOURCE_PREPARATION-实例资源准备中,RUNNING-实例运行中,RESOURCE_RELEASE-实例资源释放中,DELETED-实例已释放,RESOURCE_PREPARATION_FAIL-实例资源准备失败,FROZEN_RELEASABLE-可恢复冻结,FROZEN_UNRELEASABLE-不可恢复冻结,RECOVERING-恢复中,DELETING-删除中,SCALING-扩容中,SCALE_FAIL-扩容失败

        :return: The status of this UpdateLakeFormationInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateLakeFormationInstanceResponse.

        实例状态,RESOURCE_PREPARATION-实例资源准备中,RUNNING-实例运行中,RESOURCE_RELEASE-实例资源释放中,DELETED-实例已释放,RESOURCE_PREPARATION_FAIL-实例资源准备失败,FROZEN_RELEASABLE-可恢复冻结,FROZEN_UNRELEASABLE-不可恢复冻结,RECOVERING-恢复中,DELETING-删除中,SCALING-扩容中,SCALE_FAIL-扩容失败

        :param status: The status of this UpdateLakeFormationInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def in_recycle_bin(self):
        r"""Gets the in_recycle_bin of this UpdateLakeFormationInstanceResponse.

        是否在回收站

        :return: The in_recycle_bin of this UpdateLakeFormationInstanceResponse.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        r"""Sets the in_recycle_bin of this UpdateLakeFormationInstanceResponse.

        是否在回收站

        :param in_recycle_bin: The in_recycle_bin of this UpdateLakeFormationInstanceResponse.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

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
        if not isinstance(other, UpdateLakeFormationInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
