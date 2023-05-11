# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
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
        'id': 'id',
        'name': 'name',
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

    def __init__(self, id=None, name=None, description=None, environment_id=None, platform_type=None, flavor_id=None, artifacts=None, version=None, configuration=None, creator=None, create_time=None, update_time=None, external_accesses=None, refer_resources=None, status_detail=None):
        """ShowInstanceDetailResponse

        The model defined in huaweicloud sdk

        :param id: 应用组件实例ID。
        :type id: str
        :param name: 应用组件实例名称。
        :type name: str
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
        
        super(ShowInstanceDetailResponse, self).__init__()

        self._id = None
        self._name = None
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

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
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
    def id(self):
        """Gets the id of this ShowInstanceDetailResponse.

        应用组件实例ID。

        :return: The id of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowInstanceDetailResponse.

        应用组件实例ID。

        :param id: The id of this ShowInstanceDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowInstanceDetailResponse.

        应用组件实例名称。

        :return: The name of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceDetailResponse.

        应用组件实例名称。

        :param name: The name of this ShowInstanceDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowInstanceDetailResponse.

        实例描述。

        :return: The description of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowInstanceDetailResponse.

        实例描述。

        :param description: The description of this ShowInstanceDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def environment_id(self):
        """Gets the environment_id of this ShowInstanceDetailResponse.

        应用组件环境ID。

        :return: The environment_id of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ShowInstanceDetailResponse.

        应用组件环境ID。

        :param environment_id: The environment_id of this ShowInstanceDetailResponse.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def platform_type(self):
        """Gets the platform_type of this ShowInstanceDetailResponse.

        :return: The platform_type of this ShowInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstancePlatformType`
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this ShowInstanceDetailResponse.

        :param platform_type: The platform_type of this ShowInstanceDetailResponse.
        :type platform_type: :class:`huaweicloudsdkservicestage.v2.InstancePlatformType`
        """
        self._platform_type = platform_type

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ShowInstanceDetailResponse.

        :return: The flavor_id of this ShowInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ShowInstanceDetailResponse.

        :param flavor_id: The flavor_id of this ShowInstanceDetailResponse.
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        self._flavor_id = flavor_id

    @property
    def artifacts(self):
        """Gets the artifacts of this ShowInstanceDetailResponse.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :return: The artifacts of this ShowInstanceDetailResponse.
        :rtype: dict(str, object)
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this ShowInstanceDetailResponse.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :param artifacts: The artifacts of this ShowInstanceDetailResponse.
        :type artifacts: dict(str, object)
        """
        self._artifacts = artifacts

    @property
    def version(self):
        """Gets the version of this ShowInstanceDetailResponse.

        应用组件版本号。

        :return: The version of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowInstanceDetailResponse.

        应用组件版本号。

        :param version: The version of this ShowInstanceDetailResponse.
        :type version: str
        """
        self._version = version

    @property
    def configuration(self):
        """Gets the configuration of this ShowInstanceDetailResponse.

        应用组件配置，如环境变量。

        :return: The configuration of this ShowInstanceDetailResponse.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ShowInstanceDetailResponse.

        应用组件配置，如环境变量。

        :param configuration: The configuration of this ShowInstanceDetailResponse.
        :type configuration: object
        """
        self._configuration = configuration

    @property
    def creator(self):
        """Gets the creator of this ShowInstanceDetailResponse.

        创建人。

        :return: The creator of this ShowInstanceDetailResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowInstanceDetailResponse.

        创建人。

        :param creator: The creator of this ShowInstanceDetailResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ShowInstanceDetailResponse.

        创建时间。

        :return: The create_time of this ShowInstanceDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowInstanceDetailResponse.

        创建时间。

        :param create_time: The create_time of this ShowInstanceDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowInstanceDetailResponse.

        修改时间。

        :return: The update_time of this ShowInstanceDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowInstanceDetailResponse.

        修改时间。

        :param update_time: The update_time of this ShowInstanceDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def external_accesses(self):
        """Gets the external_accesses of this ShowInstanceDetailResponse.

        访问方式列表。

        :return: The external_accesses of this ShowInstanceDetailResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        """Sets the external_accesses of this ShowInstanceDetailResponse.

        访问方式列表。

        :param external_accesses: The external_accesses of this ShowInstanceDetailResponse.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

    @property
    def refer_resources(self):
        """Gets the refer_resources of this ShowInstanceDetailResponse.

        部署资源列表。

        :return: The refer_resources of this ShowInstanceDetailResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ReferResources`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        """Sets the refer_resources of this ShowInstanceDetailResponse.

        部署资源列表。

        :param refer_resources: The refer_resources of this ShowInstanceDetailResponse.
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResources`]
        """
        self._refer_resources = refer_resources

    @property
    def status_detail(self):
        """Gets the status_detail of this ShowInstanceDetailResponse.

        :return: The status_detail of this ShowInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this ShowInstanceDetailResponse.

        :param status_detail: The status_detail of this ShowInstanceDetailResponse.
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
        if not isinstance(other, ShowInstanceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
