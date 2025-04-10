# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'environment_id': 'str',
        'flavor_id': 'FlavorId',
        'replica': 'int',
        'artifacts': 'dict(str, object)',
        'version': 'str',
        'configuration': 'InstanceConfiguration',
        'description': 'str',
        'external_accesses': 'list[ExternalAccessesCreate]',
        'refer_resources': 'list[ReferResourceCreate]'
    }

    attribute_map = {
        'name': 'name',
        'environment_id': 'environment_id',
        'flavor_id': 'flavor_id',
        'replica': 'replica',
        'artifacts': 'artifacts',
        'version': 'version',
        'configuration': 'configuration',
        'description': 'description',
        'external_accesses': 'external_accesses',
        'refer_resources': 'refer_resources'
    }

    def __init__(self, name=None, environment_id=None, flavor_id=None, replica=None, artifacts=None, version=None, configuration=None, description=None, external_accesses=None, refer_resources=None):
        r"""InstanceCreate

        The model defined in huaweicloud sdk

        :param name: 应用组件实例名称。
        :type name: str
        :param environment_id: 环境ID。
        :type environment_id: str
        :param flavor_id: 
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        :param replica: 实例副本数。
        :type replica: int
        :param artifacts: 组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。
        :type artifacts: dict(str, object)
        :param version: 应用组件版本号，满足版本语义，如1.0.0。。
        :type version: str
        :param configuration: 
        :type configuration: :class:`huaweicloudsdkservicestage.v2.InstanceConfiguration`
        :param description: 描述。
        :type description: str
        :param external_accesses: 访问方式。
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccessesCreate`]
        :param refer_resources: 部署资源。
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResourceCreate`]
        """
        
        

        self._name = None
        self._environment_id = None
        self._flavor_id = None
        self._replica = None
        self._artifacts = None
        self._version = None
        self._configuration = None
        self._description = None
        self._external_accesses = None
        self._refer_resources = None
        self.discriminator = None

        self.name = name
        self.environment_id = environment_id
        self.flavor_id = flavor_id
        self.replica = replica
        self.artifacts = artifacts
        self.version = version
        if configuration is not None:
            self.configuration = configuration
        if description is not None:
            self.description = description
        if external_accesses is not None:
            self.external_accesses = external_accesses
        self.refer_resources = refer_resources

    @property
    def name(self):
        r"""Gets the name of this InstanceCreate.

        应用组件实例名称。

        :return: The name of this InstanceCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceCreate.

        应用组件实例名称。

        :param name: The name of this InstanceCreate.
        :type name: str
        """
        self._name = name

    @property
    def environment_id(self):
        r"""Gets the environment_id of this InstanceCreate.

        环境ID。

        :return: The environment_id of this InstanceCreate.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this InstanceCreate.

        环境ID。

        :param environment_id: The environment_id of this InstanceCreate.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this InstanceCreate.

        :return: The flavor_id of this InstanceCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this InstanceCreate.

        :param flavor_id: The flavor_id of this InstanceCreate.
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        self._flavor_id = flavor_id

    @property
    def replica(self):
        r"""Gets the replica of this InstanceCreate.

        实例副本数。

        :return: The replica of this InstanceCreate.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this InstanceCreate.

        实例副本数。

        :param replica: The replica of this InstanceCreate.
        :type replica: int
        """
        self._replica = replica

    @property
    def artifacts(self):
        r"""Gets the artifacts of this InstanceCreate.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :return: The artifacts of this InstanceCreate.
        :rtype: dict(str, object)
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        r"""Sets the artifacts of this InstanceCreate.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :param artifacts: The artifacts of this InstanceCreate.
        :type artifacts: dict(str, object)
        """
        self._artifacts = artifacts

    @property
    def version(self):
        r"""Gets the version of this InstanceCreate.

        应用组件版本号，满足版本语义，如1.0.0。。

        :return: The version of this InstanceCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstanceCreate.

        应用组件版本号，满足版本语义，如1.0.0。。

        :param version: The version of this InstanceCreate.
        :type version: str
        """
        self._version = version

    @property
    def configuration(self):
        r"""Gets the configuration of this InstanceCreate.

        :return: The configuration of this InstanceCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceConfiguration`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this InstanceCreate.

        :param configuration: The configuration of this InstanceCreate.
        :type configuration: :class:`huaweicloudsdkservicestage.v2.InstanceConfiguration`
        """
        self._configuration = configuration

    @property
    def description(self):
        r"""Gets the description of this InstanceCreate.

        描述。

        :return: The description of this InstanceCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstanceCreate.

        描述。

        :param description: The description of this InstanceCreate.
        :type description: str
        """
        self._description = description

    @property
    def external_accesses(self):
        r"""Gets the external_accesses of this InstanceCreate.

        访问方式。

        :return: The external_accesses of this InstanceCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccessesCreate`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        r"""Sets the external_accesses of this InstanceCreate.

        访问方式。

        :param external_accesses: The external_accesses of this InstanceCreate.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccessesCreate`]
        """
        self._external_accesses = external_accesses

    @property
    def refer_resources(self):
        r"""Gets the refer_resources of this InstanceCreate.

        部署资源。

        :return: The refer_resources of this InstanceCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ReferResourceCreate`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        r"""Sets the refer_resources of this InstanceCreate.

        部署资源。

        :param refer_resources: The refer_resources of this InstanceCreate.
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResourceCreate`]
        """
        self._refer_resources = refer_resources

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
        if not isinstance(other, InstanceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
