# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'flavor_id': 'FlavorId',
        'artifacts': 'dict(str, object)',
        'configuration': 'dict(str, object)',
        'description': 'str',
        'external_accesses': 'list[ExternalAccesses]',
        'refer_resources': 'list[ReferResourceCreate]'
    }

    attribute_map = {
        'version': 'version',
        'flavor_id': 'flavor_id',
        'artifacts': 'artifacts',
        'configuration': 'configuration',
        'description': 'description',
        'external_accesses': 'external_accesses',
        'refer_resources': 'refer_resources'
    }

    def __init__(self, version=None, flavor_id=None, artifacts=None, configuration=None, description=None, external_accesses=None, refer_resources=None):
        """InstanceModify

        The model defined in huaweicloud sdk

        :param version: 应用组件版本号，满足版本语义，如1.0.1。
        :type version: str
        :param flavor_id: 
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        :param artifacts: 组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。
        :type artifacts: dict(str, object)
        :param configuration: 应用配置，如环境变量。
        :type configuration: dict(str, object)
        :param description: 描述。
        :type description: str
        :param external_accesses: 访问方式列表。
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        :param refer_resources: 部署资源列表。
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v2.ReferResourceCreate`]
        """
        
        

        self._version = None
        self._flavor_id = None
        self._artifacts = None
        self._configuration = None
        self._description = None
        self._external_accesses = None
        self._refer_resources = None
        self.discriminator = None

        self.version = version
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if artifacts is not None:
            self.artifacts = artifacts
        if configuration is not None:
            self.configuration = configuration
        if description is not None:
            self.description = description
        if external_accesses is not None:
            self.external_accesses = external_accesses
        if refer_resources is not None:
            self.refer_resources = refer_resources

    @property
    def version(self):
        """Gets the version of this InstanceModify.

        应用组件版本号，满足版本语义，如1.0.1。

        :return: The version of this InstanceModify.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceModify.

        应用组件版本号，满足版本语义，如1.0.1。

        :param version: The version of this InstanceModify.
        :type version: str
        """
        self._version = version

    @property
    def flavor_id(self):
        """Gets the flavor_id of this InstanceModify.


        :return: The flavor_id of this InstanceModify.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this InstanceModify.


        :param flavor_id: The flavor_id of this InstanceModify.
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        self._flavor_id = flavor_id

    @property
    def artifacts(self):
        """Gets the artifacts of this InstanceModify.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :return: The artifacts of this InstanceModify.
        :rtype: dict(str, object)
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this InstanceModify.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :param artifacts: The artifacts of this InstanceModify.
        :type artifacts: dict(str, object)
        """
        self._artifacts = artifacts

    @property
    def configuration(self):
        """Gets the configuration of this InstanceModify.

        应用配置，如环境变量。

        :return: The configuration of this InstanceModify.
        :rtype: dict(str, object)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this InstanceModify.

        应用配置，如环境变量。

        :param configuration: The configuration of this InstanceModify.
        :type configuration: dict(str, object)
        """
        self._configuration = configuration

    @property
    def description(self):
        """Gets the description of this InstanceModify.

        描述。

        :return: The description of this InstanceModify.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceModify.

        描述。

        :param description: The description of this InstanceModify.
        :type description: str
        """
        self._description = description

    @property
    def external_accesses(self):
        """Gets the external_accesses of this InstanceModify.

        访问方式列表。

        :return: The external_accesses of this InstanceModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        """Sets the external_accesses of this InstanceModify.

        访问方式列表。

        :param external_accesses: The external_accesses of this InstanceModify.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

    @property
    def refer_resources(self):
        """Gets the refer_resources of this InstanceModify.

        部署资源列表。

        :return: The refer_resources of this InstanceModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ReferResourceCreate`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        """Sets the refer_resources of this InstanceModify.

        部署资源列表。

        :param refer_resources: The refer_resources of this InstanceModify.
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
        if not isinstance(other, InstanceModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
