# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowControlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'implementation': 'str',
        'guidance': 'str',
        'resource': 'list[str]',
        'service': 'str',
        'behavior': 'str',
        'control_objective': 'str',
        'framework': 'list[str]',
        'artifacts': 'list[Artifact]',
        'aliases': 'list[str]',
        'owner': 'str',
        'severity': 'str',
        'version': 'str',
        'release_date': 'datetime'
    }

    attribute_map = {
        'identifier': 'identifier',
        'implementation': 'implementation',
        'guidance': 'guidance',
        'resource': 'resource',
        'service': 'service',
        'behavior': 'behavior',
        'control_objective': 'control_objective',
        'framework': 'framework',
        'artifacts': 'artifacts',
        'aliases': 'aliases',
        'owner': 'owner',
        'severity': 'severity',
        'version': 'version',
        'release_date': 'release_date'
    }

    def __init__(self, identifier=None, implementation=None, guidance=None, resource=None, service=None, behavior=None, control_objective=None, framework=None, artifacts=None, aliases=None, owner=None, severity=None, version=None, release_date=None):
        """ShowControlResponse

        The model defined in huaweicloud sdk

        :param identifier: 控制策略ID。
        :type identifier: str
        :param implementation: 业务控制策略（SCP），配置规则。
        :type implementation: str
        :param guidance: 控制策略必须性。
        :type guidance: str
        :param resource: 治理资源。
        :type resource: list[str]
        :param service: 控制策略所属服务。
        :type service: str
        :param behavior: 控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。
        :type behavior: str
        :param control_objective: 控制策略目标。
        :type control_objective: str
        :param framework: 治理策略来自的框架。
        :type framework: list[str]
        :param artifacts: 策略内容。
        :type artifacts: list[:class:`huaweicloudsdkrgc.v1.Artifact`]
        :param aliases: 别名列表。
        :type aliases: list[str]
        :param owner: 账号的创建来源，包括CUSTOM和RGC。
        :type owner: str
        :param severity: 严重性(High)。
        :type severity: str
        :param version: 版本。
        :type version: str
        :param release_date: 发布时间。
        :type release_date: datetime
        """
        
        super(ShowControlResponse, self).__init__()

        self._identifier = None
        self._implementation = None
        self._guidance = None
        self._resource = None
        self._service = None
        self._behavior = None
        self._control_objective = None
        self._framework = None
        self._artifacts = None
        self._aliases = None
        self._owner = None
        self._severity = None
        self._version = None
        self._release_date = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if implementation is not None:
            self.implementation = implementation
        if guidance is not None:
            self.guidance = guidance
        if resource is not None:
            self.resource = resource
        if service is not None:
            self.service = service
        if behavior is not None:
            self.behavior = behavior
        if control_objective is not None:
            self.control_objective = control_objective
        if framework is not None:
            self.framework = framework
        if artifacts is not None:
            self.artifacts = artifacts
        if aliases is not None:
            self.aliases = aliases
        if owner is not None:
            self.owner = owner
        if severity is not None:
            self.severity = severity
        if version is not None:
            self.version = version
        if release_date is not None:
            self.release_date = release_date

    @property
    def identifier(self):
        """Gets the identifier of this ShowControlResponse.

        控制策略ID。

        :return: The identifier of this ShowControlResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ShowControlResponse.

        控制策略ID。

        :param identifier: The identifier of this ShowControlResponse.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def implementation(self):
        """Gets the implementation of this ShowControlResponse.

        业务控制策略（SCP），配置规则。

        :return: The implementation of this ShowControlResponse.
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        """Sets the implementation of this ShowControlResponse.

        业务控制策略（SCP），配置规则。

        :param implementation: The implementation of this ShowControlResponse.
        :type implementation: str
        """
        self._implementation = implementation

    @property
    def guidance(self):
        """Gets the guidance of this ShowControlResponse.

        控制策略必须性。

        :return: The guidance of this ShowControlResponse.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        """Sets the guidance of this ShowControlResponse.

        控制策略必须性。

        :param guidance: The guidance of this ShowControlResponse.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def resource(self):
        """Gets the resource of this ShowControlResponse.

        治理资源。

        :return: The resource of this ShowControlResponse.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ShowControlResponse.

        治理资源。

        :param resource: The resource of this ShowControlResponse.
        :type resource: list[str]
        """
        self._resource = resource

    @property
    def service(self):
        """Gets the service of this ShowControlResponse.

        控制策略所属服务。

        :return: The service of this ShowControlResponse.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ShowControlResponse.

        控制策略所属服务。

        :param service: The service of this ShowControlResponse.
        :type service: str
        """
        self._service = service

    @property
    def behavior(self):
        """Gets the behavior of this ShowControlResponse.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :return: The behavior of this ShowControlResponse.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this ShowControlResponse.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :param behavior: The behavior of this ShowControlResponse.
        :type behavior: str
        """
        self._behavior = behavior

    @property
    def control_objective(self):
        """Gets the control_objective of this ShowControlResponse.

        控制策略目标。

        :return: The control_objective of this ShowControlResponse.
        :rtype: str
        """
        return self._control_objective

    @control_objective.setter
    def control_objective(self, control_objective):
        """Sets the control_objective of this ShowControlResponse.

        控制策略目标。

        :param control_objective: The control_objective of this ShowControlResponse.
        :type control_objective: str
        """
        self._control_objective = control_objective

    @property
    def framework(self):
        """Gets the framework of this ShowControlResponse.

        治理策略来自的框架。

        :return: The framework of this ShowControlResponse.
        :rtype: list[str]
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this ShowControlResponse.

        治理策略来自的框架。

        :param framework: The framework of this ShowControlResponse.
        :type framework: list[str]
        """
        self._framework = framework

    @property
    def artifacts(self):
        """Gets the artifacts of this ShowControlResponse.

        策略内容。

        :return: The artifacts of this ShowControlResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.Artifact`]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this ShowControlResponse.

        策略内容。

        :param artifacts: The artifacts of this ShowControlResponse.
        :type artifacts: list[:class:`huaweicloudsdkrgc.v1.Artifact`]
        """
        self._artifacts = artifacts

    @property
    def aliases(self):
        """Gets the aliases of this ShowControlResponse.

        别名列表。

        :return: The aliases of this ShowControlResponse.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this ShowControlResponse.

        别名列表。

        :param aliases: The aliases of this ShowControlResponse.
        :type aliases: list[str]
        """
        self._aliases = aliases

    @property
    def owner(self):
        """Gets the owner of this ShowControlResponse.

        账号的创建来源，包括CUSTOM和RGC。

        :return: The owner of this ShowControlResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowControlResponse.

        账号的创建来源，包括CUSTOM和RGC。

        :param owner: The owner of this ShowControlResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def severity(self):
        """Gets the severity of this ShowControlResponse.

        严重性(High)。

        :return: The severity of this ShowControlResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ShowControlResponse.

        严重性(High)。

        :param severity: The severity of this ShowControlResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def version(self):
        """Gets the version of this ShowControlResponse.

        版本。

        :return: The version of this ShowControlResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowControlResponse.

        版本。

        :param version: The version of this ShowControlResponse.
        :type version: str
        """
        self._version = version

    @property
    def release_date(self):
        """Gets the release_date of this ShowControlResponse.

        发布时间。

        :return: The release_date of this ShowControlResponse.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ShowControlResponse.

        发布时间。

        :param release_date: The release_date of this ShowControlResponse.
        :type release_date: datetime
        """
        self._release_date = release_date

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
        if not isinstance(other, ShowControlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
