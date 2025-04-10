# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectStrategyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_set_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'rule_set_id': 'rule_set_id',
        'project_id': 'project_id'
    }

    def __init__(self, rule_set_id=None, project_id=None):
        r"""ShowProjectStrategyRequest

        The model defined in huaweicloud sdk

        :param rule_set_id: 策略ID
        :type rule_set_id: str
        :param project_id: 项目ID
        :type project_id: str
        """
        
        

        self._rule_set_id = None
        self._project_id = None
        self.discriminator = None

        self.rule_set_id = rule_set_id
        self.project_id = project_id

    @property
    def rule_set_id(self):
        r"""Gets the rule_set_id of this ShowProjectStrategyRequest.

        策略ID

        :return: The rule_set_id of this ShowProjectStrategyRequest.
        :rtype: str
        """
        return self._rule_set_id

    @rule_set_id.setter
    def rule_set_id(self, rule_set_id):
        r"""Sets the rule_set_id of this ShowProjectStrategyRequest.

        策略ID

        :param rule_set_id: The rule_set_id of this ShowProjectStrategyRequest.
        :type rule_set_id: str
        """
        self._rule_set_id = rule_set_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowProjectStrategyRequest.

        项目ID

        :return: The project_id of this ShowProjectStrategyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowProjectStrategyRequest.

        项目ID

        :param project_id: The project_id of this ShowProjectStrategyRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ShowProjectStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
