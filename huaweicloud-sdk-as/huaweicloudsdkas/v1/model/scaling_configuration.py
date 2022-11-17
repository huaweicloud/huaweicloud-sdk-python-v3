# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_configuration_id': 'str',
        'tenant': 'str',
        'scaling_configuration_name': 'str',
        'instance_config': 'InstanceConfigResult',
        'create_time': 'datetime',
        'scaling_group_id': 'str'
    }

    attribute_map = {
        'scaling_configuration_id': 'scaling_configuration_id',
        'tenant': 'tenant',
        'scaling_configuration_name': 'scaling_configuration_name',
        'instance_config': 'instance_config',
        'create_time': 'create_time',
        'scaling_group_id': 'scaling_group_id'
    }

    def __init__(self, scaling_configuration_id=None, tenant=None, scaling_configuration_name=None, instance_config=None, create_time=None, scaling_group_id=None):
        """ScalingConfiguration

        The model defined in huaweicloud sdk

        :param scaling_configuration_id: 伸缩配置ID，全局唯一。
        :type scaling_configuration_id: str
        :param tenant: 租户ID。
        :type tenant: str
        :param scaling_configuration_name: 伸缩配置名称。
        :type scaling_configuration_name: str
        :param instance_config: 
        :type instance_config: :class:`huaweicloudsdkas.v1.InstanceConfigResult`
        :param create_time: 创建伸缩配置的时间，遵循UTC时间。
        :type create_time: datetime
        :param scaling_group_id: 绑定该伸缩配置的伸缩组ID
        :type scaling_group_id: str
        """
        
        

        self._scaling_configuration_id = None
        self._tenant = None
        self._scaling_configuration_name = None
        self._instance_config = None
        self._create_time = None
        self._scaling_group_id = None
        self.discriminator = None

        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if tenant is not None:
            self.tenant = tenant
        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if instance_config is not None:
            self.instance_config = instance_config
        if create_time is not None:
            self.create_time = create_time
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ScalingConfiguration.

        伸缩配置ID，全局唯一。

        :return: The scaling_configuration_id of this ScalingConfiguration.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ScalingConfiguration.

        伸缩配置ID，全局唯一。

        :param scaling_configuration_id: The scaling_configuration_id of this ScalingConfiguration.
        :type scaling_configuration_id: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def tenant(self):
        """Gets the tenant of this ScalingConfiguration.

        租户ID。

        :return: The tenant of this ScalingConfiguration.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this ScalingConfiguration.

        租户ID。

        :param tenant: The tenant of this ScalingConfiguration.
        :type tenant: str
        """
        self._tenant = tenant

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ScalingConfiguration.

        伸缩配置名称。

        :return: The scaling_configuration_name of this ScalingConfiguration.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ScalingConfiguration.

        伸缩配置名称。

        :param scaling_configuration_name: The scaling_configuration_name of this ScalingConfiguration.
        :type scaling_configuration_name: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def instance_config(self):
        """Gets the instance_config of this ScalingConfiguration.

        :return: The instance_config of this ScalingConfiguration.
        :rtype: :class:`huaweicloudsdkas.v1.InstanceConfigResult`
        """
        return self._instance_config

    @instance_config.setter
    def instance_config(self, instance_config):
        """Sets the instance_config of this ScalingConfiguration.

        :param instance_config: The instance_config of this ScalingConfiguration.
        :type instance_config: :class:`huaweicloudsdkas.v1.InstanceConfigResult`
        """
        self._instance_config = instance_config

    @property
    def create_time(self):
        """Gets the create_time of this ScalingConfiguration.

        创建伸缩配置的时间，遵循UTC时间。

        :return: The create_time of this ScalingConfiguration.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingConfiguration.

        创建伸缩配置的时间，遵循UTC时间。

        :param create_time: The create_time of this ScalingConfiguration.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingConfiguration.

        绑定该伸缩配置的伸缩组ID

        :return: The scaling_group_id of this ScalingConfiguration.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingConfiguration.

        绑定该伸缩配置的伸缩组ID

        :param scaling_group_id: The scaling_group_id of this ScalingConfiguration.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

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
        if not isinstance(other, ScalingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
