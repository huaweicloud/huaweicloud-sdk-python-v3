# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInstanceOverView:

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
        'description': 'str',
        'environment_id': 'str',
        'platform_type': 'InstancePlatformType',
        'flavor_id': 'FlavorId',
        'artifacts': 'dict(str, object)',
        'version': 'str',
        'configuration': 'object',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'external_accesses': 'list[ExternalAccesses]',
        'refer_resources': 'list[ReferResources]',
        'status_detail': 'InstanceStatusView'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'description': 'description',
        'environment_id': 'environment_id',
        'platform_type': 'platform_type',
        'flavor_id': 'flavor_id',
        'artifacts': 'artifacts',
        'version': 'version',
        'configuration': 'configuration',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'external_accesses': 'external_accesses',
        'refer_resources': 'refer_resources',
        'status_detail': 'status_detail'
    }

    def __init__(self, instance_id=None, instance_name=None, description=None, environment_id=None, platform_type=None, flavor_id=None, artifacts=None, version=None, configuration=None, creator=None, create_time=None, update_time=None, external_accesses=None, refer_resources=None, status_detail=None):
        r"""ComponentInstanceOverView

        The model defined in huaweicloud sdk

        :param instance_id: 应用组件实例ID。
        :type instance_id: str
        :param instance_name: 应用组件实例名称。
        :type instance_name: str
        :param description: 实例描述。
        :type description: str
        :param environment_id: 应用组件环境ID。
        :type environment_id: str
        :param platform_type: 
        :type platform_type: :class:`huaweicloudsdkservicestage.v2.InstancePlatformType`
        :param flavor_id: 
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        :param artifacts: 组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。
        :type artifacts: dict(str, object)
        :param version: 应用组件版本号。
        :type version: str
        :param configuration: 应用组件配置，如环境变量。
        :type configuration: object
        :param creator: 创建人。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param external_accesses: 访问方式列表。
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        :param refer_resources: 部署资源列表。
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResources`]
        :param status_detail: 
        :type status_detail: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._description = None
        self._environment_id = None
        self._platform_type = None
        self._flavor_id = None
        self._artifacts = None
        self._version = None
        self._configuration = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._external_accesses = None
        self._refer_resources = None
        self._status_detail = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if description is not None:
            self.description = description
        if environment_id is not None:
            self.environment_id = environment_id
        if platform_type is not None:
            self.platform_type = platform_type
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if artifacts is not None:
            self.artifacts = artifacts
        if version is not None:
            self.version = version
        if configuration is not None:
            self.configuration = configuration
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if external_accesses is not None:
            self.external_accesses = external_accesses
        if refer_resources is not None:
            self.refer_resources = refer_resources
        if status_detail is not None:
            self.status_detail = status_detail

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ComponentInstanceOverView.

        应用组件实例ID。

        :return: The instance_id of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ComponentInstanceOverView.

        应用组件实例ID。

        :param instance_id: The instance_id of this ComponentInstanceOverView.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ComponentInstanceOverView.

        应用组件实例名称。

        :return: The instance_name of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ComponentInstanceOverView.

        应用组件实例名称。

        :param instance_name: The instance_name of this ComponentInstanceOverView.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def description(self):
        r"""Gets the description of this ComponentInstanceOverView.

        实例描述。

        :return: The description of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentInstanceOverView.

        实例描述。

        :param description: The description of this ComponentInstanceOverView.
        :type description: str
        """
        self._description = description

    @property
    def environment_id(self):
        r"""Gets the environment_id of this ComponentInstanceOverView.

        应用组件环境ID。

        :return: The environment_id of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this ComponentInstanceOverView.

        应用组件环境ID。

        :param environment_id: The environment_id of this ComponentInstanceOverView.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def platform_type(self):
        r"""Gets the platform_type of this ComponentInstanceOverView.

        :return: The platform_type of this ComponentInstanceOverView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstancePlatformType`
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this ComponentInstanceOverView.

        :param platform_type: The platform_type of this ComponentInstanceOverView.
        :type platform_type: :class:`huaweicloudsdkservicestage.v2.InstancePlatformType`
        """
        self._platform_type = platform_type

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ComponentInstanceOverView.

        :return: The flavor_id of this ComponentInstanceOverView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ComponentInstanceOverView.

        :param flavor_id: The flavor_id of this ComponentInstanceOverView.
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        self._flavor_id = flavor_id

    @property
    def artifacts(self):
        r"""Gets the artifacts of this ComponentInstanceOverView.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :return: The artifacts of this ComponentInstanceOverView.
        :rtype: dict(str, object)
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        r"""Sets the artifacts of this ComponentInstanceOverView.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :param artifacts: The artifacts of this ComponentInstanceOverView.
        :type artifacts: dict(str, object)
        """
        self._artifacts = artifacts

    @property
    def version(self):
        r"""Gets the version of this ComponentInstanceOverView.

        应用组件版本号。

        :return: The version of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentInstanceOverView.

        应用组件版本号。

        :param version: The version of this ComponentInstanceOverView.
        :type version: str
        """
        self._version = version

    @property
    def configuration(self):
        r"""Gets the configuration of this ComponentInstanceOverView.

        应用组件配置，如环境变量。

        :return: The configuration of this ComponentInstanceOverView.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this ComponentInstanceOverView.

        应用组件配置，如环境变量。

        :param configuration: The configuration of this ComponentInstanceOverView.
        :type configuration: object
        """
        self._configuration = configuration

    @property
    def creator(self):
        r"""Gets the creator of this ComponentInstanceOverView.

        创建人。

        :return: The creator of this ComponentInstanceOverView.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ComponentInstanceOverView.

        创建人。

        :param creator: The creator of this ComponentInstanceOverView.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentInstanceOverView.

        创建时间。

        :return: The create_time of this ComponentInstanceOverView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentInstanceOverView.

        创建时间。

        :param create_time: The create_time of this ComponentInstanceOverView.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentInstanceOverView.

        修改时间。

        :return: The update_time of this ComponentInstanceOverView.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentInstanceOverView.

        修改时间。

        :param update_time: The update_time of this ComponentInstanceOverView.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def external_accesses(self):
        r"""Gets the external_accesses of this ComponentInstanceOverView.

        访问方式列表。

        :return: The external_accesses of this ComponentInstanceOverView.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        r"""Sets the external_accesses of this ComponentInstanceOverView.

        访问方式列表。

        :param external_accesses: The external_accesses of this ComponentInstanceOverView.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

    @property
    def refer_resources(self):
        r"""Gets the refer_resources of this ComponentInstanceOverView.

        部署资源列表。

        :return: The refer_resources of this ComponentInstanceOverView.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ReferResources`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        r"""Sets the refer_resources of this ComponentInstanceOverView.

        部署资源列表。

        :param refer_resources: The refer_resources of this ComponentInstanceOverView.
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResources`]
        """
        self._refer_resources = refer_resources

    @property
    def status_detail(self):
        r"""Gets the status_detail of this ComponentInstanceOverView.

        :return: The status_detail of this ComponentInstanceOverView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        r"""Sets the status_detail of this ComponentInstanceOverView.

        :param status_detail: The status_detail of this ComponentInstanceOverView.
        :type status_detail: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        self._status_detail = status_detail

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
        if not isinstance(other, ComponentInstanceOverView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
