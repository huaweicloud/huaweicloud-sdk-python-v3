# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Control:

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
        'name': 'str',
        'description': 'str',
        'guidance': 'str',
        'resource': 'list[str]',
        'framework': 'list[str]',
        'service': 'str',
        'implementation': 'str',
        'behavior': 'str',
        'owner': 'str',
        'severity': 'str',
        'control_objective': 'str',
        'version': 'str',
        'release_date': 'datetime'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'description': 'description',
        'guidance': 'guidance',
        'resource': 'resource',
        'framework': 'framework',
        'service': 'service',
        'implementation': 'implementation',
        'behavior': 'behavior',
        'owner': 'owner',
        'severity': 'severity',
        'control_objective': 'control_objective',
        'version': 'version',
        'release_date': 'release_date'
    }

    def __init__(self, identifier=None, name=None, description=None, guidance=None, resource=None, framework=None, service=None, implementation=None, behavior=None, owner=None, severity=None, control_objective=None, version=None, release_date=None):
        r"""Control

        The model defined in huaweicloud sdk

        :param identifier: 控制策略ID。
        :type identifier: str
        :param name: 控制策略名称。
        :type name: str
        :param description: 控制策略描述。
        :type description: str
        :param guidance: 控制策略必须性。
        :type guidance: str
        :param resource: 治理资源。
        :type resource: list[str]
        :param framework: 治理策略来自的框架。
        :type framework: list[str]
        :param service: 控制策略所属服务。
        :type service: str
        :param implementation: 策略类别。
        :type implementation: str
        :param behavior: 控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。
        :type behavior: str
        :param owner: 控制策略来源。
        :type owner: str
        :param severity: 控制策略严重性。
        :type severity: str
        :param control_objective: 控制策略目标。
        :type control_objective: str
        :param version: 控制策略版本。
        :type version: str
        :param release_date: 控制策略发布时间。
        :type release_date: datetime
        """
        
        

        self._identifier = None
        self._name = None
        self._description = None
        self._guidance = None
        self._resource = None
        self._framework = None
        self._service = None
        self._implementation = None
        self._behavior = None
        self._owner = None
        self._severity = None
        self._control_objective = None
        self._version = None
        self._release_date = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if guidance is not None:
            self.guidance = guidance
        if resource is not None:
            self.resource = resource
        if framework is not None:
            self.framework = framework
        if service is not None:
            self.service = service
        if implementation is not None:
            self.implementation = implementation
        if behavior is not None:
            self.behavior = behavior
        if owner is not None:
            self.owner = owner
        if severity is not None:
            self.severity = severity
        if control_objective is not None:
            self.control_objective = control_objective
        if version is not None:
            self.version = version
        if release_date is not None:
            self.release_date = release_date

    @property
    def identifier(self):
        r"""Gets the identifier of this Control.

        控制策略ID。

        :return: The identifier of this Control.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this Control.

        控制策略ID。

        :param identifier: The identifier of this Control.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def name(self):
        r"""Gets the name of this Control.

        控制策略名称。

        :return: The name of this Control.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Control.

        控制策略名称。

        :param name: The name of this Control.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Control.

        控制策略描述。

        :return: The description of this Control.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Control.

        控制策略描述。

        :param description: The description of this Control.
        :type description: str
        """
        self._description = description

    @property
    def guidance(self):
        r"""Gets the guidance of this Control.

        控制策略必须性。

        :return: The guidance of this Control.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        r"""Sets the guidance of this Control.

        控制策略必须性。

        :param guidance: The guidance of this Control.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def resource(self):
        r"""Gets the resource of this Control.

        治理资源。

        :return: The resource of this Control.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this Control.

        治理资源。

        :param resource: The resource of this Control.
        :type resource: list[str]
        """
        self._resource = resource

    @property
    def framework(self):
        r"""Gets the framework of this Control.

        治理策略来自的框架。

        :return: The framework of this Control.
        :rtype: list[str]
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this Control.

        治理策略来自的框架。

        :param framework: The framework of this Control.
        :type framework: list[str]
        """
        self._framework = framework

    @property
    def service(self):
        r"""Gets the service of this Control.

        控制策略所属服务。

        :return: The service of this Control.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this Control.

        控制策略所属服务。

        :param service: The service of this Control.
        :type service: str
        """
        self._service = service

    @property
    def implementation(self):
        r"""Gets the implementation of this Control.

        策略类别。

        :return: The implementation of this Control.
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        r"""Sets the implementation of this Control.

        策略类别。

        :param implementation: The implementation of this Control.
        :type implementation: str
        """
        self._implementation = implementation

    @property
    def behavior(self):
        r"""Gets the behavior of this Control.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :return: The behavior of this Control.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        r"""Sets the behavior of this Control.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :param behavior: The behavior of this Control.
        :type behavior: str
        """
        self._behavior = behavior

    @property
    def owner(self):
        r"""Gets the owner of this Control.

        控制策略来源。

        :return: The owner of this Control.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this Control.

        控制策略来源。

        :param owner: The owner of this Control.
        :type owner: str
        """
        self._owner = owner

    @property
    def severity(self):
        r"""Gets the severity of this Control.

        控制策略严重性。

        :return: The severity of this Control.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this Control.

        控制策略严重性。

        :param severity: The severity of this Control.
        :type severity: str
        """
        self._severity = severity

    @property
    def control_objective(self):
        r"""Gets the control_objective of this Control.

        控制策略目标。

        :return: The control_objective of this Control.
        :rtype: str
        """
        return self._control_objective

    @control_objective.setter
    def control_objective(self, control_objective):
        r"""Sets the control_objective of this Control.

        控制策略目标。

        :param control_objective: The control_objective of this Control.
        :type control_objective: str
        """
        self._control_objective = control_objective

    @property
    def version(self):
        r"""Gets the version of this Control.

        控制策略版本。

        :return: The version of this Control.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Control.

        控制策略版本。

        :param version: The version of this Control.
        :type version: str
        """
        self._version = version

    @property
    def release_date(self):
        r"""Gets the release_date of this Control.

        控制策略发布时间。

        :return: The release_date of this Control.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        r"""Sets the release_date of this Control.

        控制策略发布时间。

        :param release_date: The release_date of this Control.
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
        if not isinstance(other, Control):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
