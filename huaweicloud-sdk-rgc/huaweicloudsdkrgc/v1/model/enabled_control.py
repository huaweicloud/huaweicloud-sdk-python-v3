# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnabledControl:

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
        'name': 'str',
        'description': 'str',
        'control_objective': 'str',
        'behavior': 'str',
        'owner': 'str',
        'regional_preference': 'str'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'control_identifier': 'control_identifier',
        'name': 'name',
        'description': 'description',
        'control_objective': 'control_objective',
        'behavior': 'behavior',
        'owner': 'owner',
        'regional_preference': 'regional_preference'
    }

    def __init__(self, manage_account_id=None, control_identifier=None, name=None, description=None, control_objective=None, behavior=None, owner=None, regional_preference=None):
        r"""EnabledControl

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理员账号ID。
        :type manage_account_id: str
        :param control_identifier: 控制策略标识。
        :type control_identifier: str
        :param name: 控制策略名称。
        :type name: str
        :param description: 控制策略描述。
        :type description: str
        :param control_objective: 控制策略目标。
        :type control_objective: str
        :param behavior: 控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。
        :type behavior: str
        :param owner: 控制策略来源。
        :type owner: str
        :param regional_preference: 区域选项，取值有两种分别是：区域的regional和全局的global。
        :type regional_preference: str
        """
        
        

        self._manage_account_id = None
        self._control_identifier = None
        self._name = None
        self._description = None
        self._control_objective = None
        self._behavior = None
        self._owner = None
        self._regional_preference = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if control_identifier is not None:
            self.control_identifier = control_identifier
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

    @property
    def manage_account_id(self):
        r"""Gets the manage_account_id of this EnabledControl.

        管理员账号ID。

        :return: The manage_account_id of this EnabledControl.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        r"""Sets the manage_account_id of this EnabledControl.

        管理员账号ID。

        :param manage_account_id: The manage_account_id of this EnabledControl.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def control_identifier(self):
        r"""Gets the control_identifier of this EnabledControl.

        控制策略标识。

        :return: The control_identifier of this EnabledControl.
        :rtype: str
        """
        return self._control_identifier

    @control_identifier.setter
    def control_identifier(self, control_identifier):
        r"""Sets the control_identifier of this EnabledControl.

        控制策略标识。

        :param control_identifier: The control_identifier of this EnabledControl.
        :type control_identifier: str
        """
        self._control_identifier = control_identifier

    @property
    def name(self):
        r"""Gets the name of this EnabledControl.

        控制策略名称。

        :return: The name of this EnabledControl.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnabledControl.

        控制策略名称。

        :param name: The name of this EnabledControl.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EnabledControl.

        控制策略描述。

        :return: The description of this EnabledControl.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnabledControl.

        控制策略描述。

        :param description: The description of this EnabledControl.
        :type description: str
        """
        self._description = description

    @property
    def control_objective(self):
        r"""Gets the control_objective of this EnabledControl.

        控制策略目标。

        :return: The control_objective of this EnabledControl.
        :rtype: str
        """
        return self._control_objective

    @control_objective.setter
    def control_objective(self, control_objective):
        r"""Sets the control_objective of this EnabledControl.

        控制策略目标。

        :param control_objective: The control_objective of this EnabledControl.
        :type control_objective: str
        """
        self._control_objective = control_objective

    @property
    def behavior(self):
        r"""Gets the behavior of this EnabledControl.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :return: The behavior of this EnabledControl.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        r"""Sets the behavior of this EnabledControl.

        控制策略类型。包括主动性控制策略Proactive、检测性控制策略Detective、预防性控制策略Preventive。

        :param behavior: The behavior of this EnabledControl.
        :type behavior: str
        """
        self._behavior = behavior

    @property
    def owner(self):
        r"""Gets the owner of this EnabledControl.

        控制策略来源。

        :return: The owner of this EnabledControl.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this EnabledControl.

        控制策略来源。

        :param owner: The owner of this EnabledControl.
        :type owner: str
        """
        self._owner = owner

    @property
    def regional_preference(self):
        r"""Gets the regional_preference of this EnabledControl.

        区域选项，取值有两种分别是：区域的regional和全局的global。

        :return: The regional_preference of this EnabledControl.
        :rtype: str
        """
        return self._regional_preference

    @regional_preference.setter
    def regional_preference(self, regional_preference):
        r"""Sets the regional_preference of this EnabledControl.

        区域选项，取值有两种分别是：区域的regional和全局的global。

        :param regional_preference: The regional_preference of this EnabledControl.
        :type regional_preference: str
        """
        self._regional_preference = regional_preference

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
        if not isinstance(other, EnabledControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
