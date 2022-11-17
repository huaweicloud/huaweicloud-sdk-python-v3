# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingGroupInstance:

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
        'instance_name': 'str',
        'scaling_group_id': 'str',
        'scaling_group_name': 'str',
        'life_cycle_state': 'str',
        'health_status': 'str',
        'scaling_configuration_name': 'str',
        'scaling_configuration_id': 'str',
        'create_time': 'datetime',
        'protect_from_scaling_down': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'scaling_group_id': 'scaling_group_id',
        'scaling_group_name': 'scaling_group_name',
        'life_cycle_state': 'life_cycle_state',
        'health_status': 'health_status',
        'scaling_configuration_name': 'scaling_configuration_name',
        'scaling_configuration_id': 'scaling_configuration_id',
        'create_time': 'create_time',
        'protect_from_scaling_down': 'protect_from_scaling_down'
    }

    def __init__(self, instance_id=None, instance_name=None, scaling_group_id=None, scaling_group_name=None, life_cycle_state=None, health_status=None, scaling_configuration_name=None, scaling_configuration_id=None, create_time=None, protect_from_scaling_down=None):
        """ScalingGroupInstance

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param scaling_group_id: 实例所在伸缩组ID。
        :type scaling_group_id: str
        :param scaling_group_name: 实例所在伸缩组名称。
        :type scaling_group_name: str
        :param life_cycle_state: 实例在伸缩组中的生命周期状态：  - INSERVICE：已启用 - PENDING：正在加入伸缩组 - PENDING_WAIT：等待（正在加入伸缩组） - REMOVING：正在移出伸缩组 - REMOVING_WAIT：等待（正在移出伸缩组） - STANDBY：已备用 - ENTERING_STANDBY：进入备用状态
        :type life_cycle_state: str
        :param health_status: 实例健康状态:INITAILIZING:初始化；NORMAL：正常；ERROR：错误。
        :type health_status: str
        :param scaling_configuration_name: 伸缩配置名称。如果返回为空，表示伸缩配置已经被删除。如果返回MANNUAL_ADD，表示实例为手动加入。
        :type scaling_configuration_name: str
        :param scaling_configuration_id: 伸缩配置ID。
        :type scaling_configuration_id: str
        :param create_time: 实例加入伸缩组的时间，遵循UTC时间。
        :type create_time: datetime
        :param protect_from_scaling_down: 实例的实例保护属性。
        :type protect_from_scaling_down: bool
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._scaling_group_id = None
        self._scaling_group_name = None
        self._life_cycle_state = None
        self._health_status = None
        self._scaling_configuration_name = None
        self._scaling_configuration_id = None
        self._create_time = None
        self._protect_from_scaling_down = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if life_cycle_state is not None:
            self.life_cycle_state = life_cycle_state
        if health_status is not None:
            self.health_status = health_status
        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if create_time is not None:
            self.create_time = create_time
        if protect_from_scaling_down is not None:
            self.protect_from_scaling_down = protect_from_scaling_down

    @property
    def instance_id(self):
        """Gets the instance_id of this ScalingGroupInstance.

        实例ID。

        :return: The instance_id of this ScalingGroupInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ScalingGroupInstance.

        实例ID。

        :param instance_id: The instance_id of this ScalingGroupInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ScalingGroupInstance.

        实例名称。

        :return: The instance_name of this ScalingGroupInstance.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ScalingGroupInstance.

        实例名称。

        :param instance_name: The instance_name of this ScalingGroupInstance.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingGroupInstance.

        实例所在伸缩组ID。

        :return: The scaling_group_id of this ScalingGroupInstance.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingGroupInstance.

        实例所在伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ScalingGroupInstance.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ScalingGroupInstance.

        实例所在伸缩组名称。

        :return: The scaling_group_name of this ScalingGroupInstance.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ScalingGroupInstance.

        实例所在伸缩组名称。

        :param scaling_group_name: The scaling_group_name of this ScalingGroupInstance.
        :type scaling_group_name: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def life_cycle_state(self):
        """Gets the life_cycle_state of this ScalingGroupInstance.

        实例在伸缩组中的生命周期状态：  - INSERVICE：已启用 - PENDING：正在加入伸缩组 - PENDING_WAIT：等待（正在加入伸缩组） - REMOVING：正在移出伸缩组 - REMOVING_WAIT：等待（正在移出伸缩组） - STANDBY：已备用 - ENTERING_STANDBY：进入备用状态

        :return: The life_cycle_state of this ScalingGroupInstance.
        :rtype: str
        """
        return self._life_cycle_state

    @life_cycle_state.setter
    def life_cycle_state(self, life_cycle_state):
        """Sets the life_cycle_state of this ScalingGroupInstance.

        实例在伸缩组中的生命周期状态：  - INSERVICE：已启用 - PENDING：正在加入伸缩组 - PENDING_WAIT：等待（正在加入伸缩组） - REMOVING：正在移出伸缩组 - REMOVING_WAIT：等待（正在移出伸缩组） - STANDBY：已备用 - ENTERING_STANDBY：进入备用状态

        :param life_cycle_state: The life_cycle_state of this ScalingGroupInstance.
        :type life_cycle_state: str
        """
        self._life_cycle_state = life_cycle_state

    @property
    def health_status(self):
        """Gets the health_status of this ScalingGroupInstance.

        实例健康状态:INITAILIZING:初始化；NORMAL：正常；ERROR：错误。

        :return: The health_status of this ScalingGroupInstance.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this ScalingGroupInstance.

        实例健康状态:INITAILIZING:初始化；NORMAL：正常；ERROR：错误。

        :param health_status: The health_status of this ScalingGroupInstance.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ScalingGroupInstance.

        伸缩配置名称。如果返回为空，表示伸缩配置已经被删除。如果返回MANNUAL_ADD，表示实例为手动加入。

        :return: The scaling_configuration_name of this ScalingGroupInstance.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ScalingGroupInstance.

        伸缩配置名称。如果返回为空，表示伸缩配置已经被删除。如果返回MANNUAL_ADD，表示实例为手动加入。

        :param scaling_configuration_name: The scaling_configuration_name of this ScalingGroupInstance.
        :type scaling_configuration_name: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ScalingGroupInstance.

        伸缩配置ID。

        :return: The scaling_configuration_id of this ScalingGroupInstance.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ScalingGroupInstance.

        伸缩配置ID。

        :param scaling_configuration_id: The scaling_configuration_id of this ScalingGroupInstance.
        :type scaling_configuration_id: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def create_time(self):
        """Gets the create_time of this ScalingGroupInstance.

        实例加入伸缩组的时间，遵循UTC时间。

        :return: The create_time of this ScalingGroupInstance.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingGroupInstance.

        实例加入伸缩组的时间，遵循UTC时间。

        :param create_time: The create_time of this ScalingGroupInstance.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def protect_from_scaling_down(self):
        """Gets the protect_from_scaling_down of this ScalingGroupInstance.

        实例的实例保护属性。

        :return: The protect_from_scaling_down of this ScalingGroupInstance.
        :rtype: bool
        """
        return self._protect_from_scaling_down

    @protect_from_scaling_down.setter
    def protect_from_scaling_down(self, protect_from_scaling_down):
        """Sets the protect_from_scaling_down of this ScalingGroupInstance.

        实例的实例保护属性。

        :param protect_from_scaling_down: The protect_from_scaling_down of this ScalingGroupInstance.
        :type protect_from_scaling_down: bool
        """
        self._protect_from_scaling_down = protect_from_scaling_down

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
        if not isinstance(other, ScalingGroupInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
