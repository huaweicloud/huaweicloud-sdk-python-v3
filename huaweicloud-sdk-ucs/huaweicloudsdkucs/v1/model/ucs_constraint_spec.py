# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSConstraintSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'constraint': 'Constraint',
        'constraint_template_id': 'str',
        'domain_id': 'str',
        'target_scope': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'constraint': 'constraint',
        'constraint_template_id': 'constraintTemplateID',
        'domain_id': 'domainID',
        'target_scope': 'targetScope',
        'target_id': 'targetID'
    }

    def __init__(self, constraint=None, constraint_template_id=None, domain_id=None, target_scope=None, target_id=None):
        r"""UCSConstraintSpec

        The model defined in huaweicloud sdk

        :param constraint: 
        :type constraint: :class:`huaweicloudsdkucs.v1.Constraint`
        :param constraint_template_id: 约束模板ID
        :type constraint_template_id: str
        :param domain_id: 用户的domainID
        :type domain_id: str
        :param target_scope: 策略实例下发范围，当前cluster和fleet二选一
        :type target_scope: str
        :param target_id: 策略实例下发对象，当前为clusterID或clustergroupID
        :type target_id: str
        """
        
        

        self._constraint = None
        self._constraint_template_id = None
        self._domain_id = None
        self._target_scope = None
        self._target_id = None
        self.discriminator = None

        if constraint is not None:
            self.constraint = constraint
        if constraint_template_id is not None:
            self.constraint_template_id = constraint_template_id
        if domain_id is not None:
            self.domain_id = domain_id
        if target_scope is not None:
            self.target_scope = target_scope
        if target_id is not None:
            self.target_id = target_id

    @property
    def constraint(self):
        r"""Gets the constraint of this UCSConstraintSpec.

        :return: The constraint of this UCSConstraintSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.Constraint`
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        r"""Sets the constraint of this UCSConstraintSpec.

        :param constraint: The constraint of this UCSConstraintSpec.
        :type constraint: :class:`huaweicloudsdkucs.v1.Constraint`
        """
        self._constraint = constraint

    @property
    def constraint_template_id(self):
        r"""Gets the constraint_template_id of this UCSConstraintSpec.

        约束模板ID

        :return: The constraint_template_id of this UCSConstraintSpec.
        :rtype: str
        """
        return self._constraint_template_id

    @constraint_template_id.setter
    def constraint_template_id(self, constraint_template_id):
        r"""Sets the constraint_template_id of this UCSConstraintSpec.

        约束模板ID

        :param constraint_template_id: The constraint_template_id of this UCSConstraintSpec.
        :type constraint_template_id: str
        """
        self._constraint_template_id = constraint_template_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UCSConstraintSpec.

        用户的domainID

        :return: The domain_id of this UCSConstraintSpec.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UCSConstraintSpec.

        用户的domainID

        :param domain_id: The domain_id of this UCSConstraintSpec.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def target_scope(self):
        r"""Gets the target_scope of this UCSConstraintSpec.

        策略实例下发范围，当前cluster和fleet二选一

        :return: The target_scope of this UCSConstraintSpec.
        :rtype: str
        """
        return self._target_scope

    @target_scope.setter
    def target_scope(self, target_scope):
        r"""Sets the target_scope of this UCSConstraintSpec.

        策略实例下发范围，当前cluster和fleet二选一

        :param target_scope: The target_scope of this UCSConstraintSpec.
        :type target_scope: str
        """
        self._target_scope = target_scope

    @property
    def target_id(self):
        r"""Gets the target_id of this UCSConstraintSpec.

        策略实例下发对象，当前为clusterID或clustergroupID

        :return: The target_id of this UCSConstraintSpec.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this UCSConstraintSpec.

        策略实例下发对象，当前为clusterID或clustergroupID

        :param target_id: The target_id of this UCSConstraintSpec.
        :type target_id: str
        """
        self._target_id = target_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UCSConstraintSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
