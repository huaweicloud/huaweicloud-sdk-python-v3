# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetControl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_account_id': 'str',
        'control_identifier': 'str',
        'state': 'str',
        'version': 'str',
        'name': 'str',
        'description': 'str',
        'control_objective': 'str',
        'behavior': 'str',
        'owner': 'str',
        'regional_preference': 'str',
        'guidance': 'str',
        'service': 'str',
        'implementation': 'str'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'control_identifier': 'control_identifier',
        'state': 'state',
        'version': 'version',
        'name': 'name',
        'description': 'description',
        'control_objective': 'control_objective',
        'behavior': 'behavior',
        'owner': 'owner',
        'regional_preference': 'regional_preference',
        'guidance': 'guidance',
        'service': 'service',
        'implementation': 'implementation'
    }

    def __init__(self, manage_account_id=None, control_identifier=None, state=None, version=None, name=None, description=None, control_objective=None, behavior=None, owner=None, regional_preference=None, guidance=None, service=None, implementation=None):
        r"""TargetControl

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理员账号ID。
        :type manage_account_id: str
        :param control_identifier: 控制策略标识。
        :type control_identifier: str
        :param state: 控制策略启用状态。
        :type state: str
        :param version: 控制策略当前版本号。
        :type version: str
        :param name: 控制策略名称。
        :type name: str
        :param description: 控制策略描述信息。
        :type description: str
        :param control_objective: 控制策略目标。
        :type control_objective: str
        :param behavior: 控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。
        :type behavior: str
        :param owner: 控制策略来源。
        :type owner: str
        :param regional_preference: 区域选项，取值有两种分别是：区域的regional和全局的global。
        :type regional_preference: str
        :param guidance: 控制策略必须性。
        :type guidance: str
        :param service: 控制策略所属服务。
        :type service: str
        :param implementation: 策略类别。
        :type implementation: str
        """
        
        

        self._manage_account_id = None
        self._control_identifier = None
        self._state = None
        self._version = None
        self._name = None
        self._description = None
        self._control_objective = None
        self._behavior = None
        self._owner = None
        self._regional_preference = None
        self._guidance = None
        self._service = None
        self._implementation = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if control_identifier is not None:
            self.control_identifier = control_identifier
        if state is not None:
            self.state = state
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if control_objective is not None:
            self.control_objective = control_objective
        if behavior is not None:
            self.behavior = behavior
        if owner is not None:
            self.owner = owner
        if regional_preference is not None:
            self.regional_preference = regional_preference
        if guidance is not None:
            self.guidance = guidance
        if service is not None:
            self.service = service
        if implementation is not None:
            self.implementation = implementation

    @property
    def manage_account_id(self):
        r"""Gets the manage_account_id of this TargetControl.

        管理员账号ID。

        :return: The manage_account_id of this TargetControl.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        r"""Sets the manage_account_id of this TargetControl.

        管理员账号ID。

        :param manage_account_id: The manage_account_id of this TargetControl.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def control_identifier(self):
        r"""Gets the control_identifier of this TargetControl.

        控制策略标识。

        :return: The control_identifier of this TargetControl.
        :rtype: str
        """
        return self._control_identifier

    @control_identifier.setter
    def control_identifier(self, control_identifier):
        r"""Sets the control_identifier of this TargetControl.

        控制策略标识。

        :param control_identifier: The control_identifier of this TargetControl.
        :type control_identifier: str
        """
        self._control_identifier = control_identifier

    @property
    def state(self):
        r"""Gets the state of this TargetControl.

        控制策略启用状态。

        :return: The state of this TargetControl.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TargetControl.

        控制策略启用状态。

        :param state: The state of this TargetControl.
        :type state: str
        """
        self._state = state

    @property
    def version(self):
        r"""Gets the version of this TargetControl.

        控制策略当前版本号。

        :return: The version of this TargetControl.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this TargetControl.

        控制策略当前版本号。

        :param version: The version of this TargetControl.
        :type version: str
        """
        self._version = version

    @property
    def name(self):
        r"""Gets the name of this TargetControl.

        控制策略名称。

        :return: The name of this TargetControl.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TargetControl.

        控制策略名称。

        :param name: The name of this TargetControl.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TargetControl.

        控制策略描述信息。

        :return: The description of this TargetControl.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TargetControl.

        控制策略描述信息。

        :param description: The description of this TargetControl.
        :type description: str
        """
        self._description = description

    @property
    def control_objective(self):
        r"""Gets the control_objective of this TargetControl.

        控制策略目标。

        :return: The control_objective of this TargetControl.
        :rtype: str
        """
        return self._control_objective

    @control_objective.setter
    def control_objective(self, control_objective):
        r"""Sets the control_objective of this TargetControl.

        控制策略目标。

        :param control_objective: The control_objective of this TargetControl.
        :type control_objective: str
        """
        self._control_objective = control_objective

    @property
    def behavior(self):
        r"""Gets the behavior of this TargetControl.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :return: The behavior of this TargetControl.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        r"""Sets the behavior of this TargetControl.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :param behavior: The behavior of this TargetControl.
        :type behavior: str
        """
        self._behavior = behavior

    @property
    def owner(self):
        r"""Gets the owner of this TargetControl.

        控制策略来源。

        :return: The owner of this TargetControl.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TargetControl.

        控制策略来源。

        :param owner: The owner of this TargetControl.
        :type owner: str
        """
        self._owner = owner

    @property
    def regional_preference(self):
        r"""Gets the regional_preference of this TargetControl.

        区域选项，取值有两种分别是：区域的regional和全局的global。

        :return: The regional_preference of this TargetControl.
        :rtype: str
        """
        return self._regional_preference

    @regional_preference.setter
    def regional_preference(self, regional_preference):
        r"""Sets the regional_preference of this TargetControl.

        区域选项，取值有两种分别是：区域的regional和全局的global。

        :param regional_preference: The regional_preference of this TargetControl.
        :type regional_preference: str
        """
        self._regional_preference = regional_preference

    @property
    def guidance(self):
        r"""Gets the guidance of this TargetControl.

        控制策略必须性。

        :return: The guidance of this TargetControl.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        r"""Sets the guidance of this TargetControl.

        控制策略必须性。

        :param guidance: The guidance of this TargetControl.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def service(self):
        r"""Gets the service of this TargetControl.

        控制策略所属服务。

        :return: The service of this TargetControl.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this TargetControl.

        控制策略所属服务。

        :param service: The service of this TargetControl.
        :type service: str
        """
        self._service = service

    @property
    def implementation(self):
        r"""Gets the implementation of this TargetControl.

        策略类别。

        :return: The implementation of this TargetControl.
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        r"""Sets the implementation of this TargetControl.

        策略类别。

        :param implementation: The implementation of this TargetControl.
        :type implementation: str
        """
        self._implementation = implementation

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
        if not isinstance(other, TargetControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
