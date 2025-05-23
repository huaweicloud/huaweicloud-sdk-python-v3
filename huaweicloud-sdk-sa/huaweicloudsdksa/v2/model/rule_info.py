# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleInfo:

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
        'project_id': 'str',
        'rule': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'rule': 'rule'
    }

    def __init__(self, id=None, project_id=None, rule=None):
        r"""RuleInfo

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param project_id: Project id value
        :type project_id: str
        :param rule: Project id value
        :type rule: str
        """
        
        

        self._id = None
        self._project_id = None
        self._rule = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if rule is not None:
            self.rule = rule

    @property
    def id(self):
        r"""Gets the id of this RuleInfo.

        Id value

        :return: The id of this RuleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleInfo.

        Id value

        :param id: The id of this RuleInfo.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this RuleInfo.

        Project id value

        :return: The project_id of this RuleInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RuleInfo.

        Project id value

        :param project_id: The project_id of this RuleInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rule(self):
        r"""Gets the rule of this RuleInfo.

        Project id value

        :return: The rule of this RuleInfo.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this RuleInfo.

        Project id value

        :param rule: The rule of this RuleInfo.
        :type rule: str
        """
        self._rule = rule

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
        if not isinstance(other, RuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
