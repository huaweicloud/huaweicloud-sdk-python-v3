# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAomMappingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'project_id': 'str',
        'rule_name': 'str',
        'rule_info': 'AomMappingRuleInfo'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'project_id': 'project_id',
        'rule_name': 'rule_name',
        'rule_info': 'rule_info'
    }

    def __init__(self, rule_id=None, project_id=None, rule_name=None, rule_info=None):
        r"""UpdateAomMappingRequest

        The model defined in huaweicloud sdk

        :param rule_id: 接入规则id
        :type rule_id: str
        :param project_id: 项目id
        :type project_id: str
        :param rule_name: 接入规则名称
        :type rule_name: str
        :param rule_info: 
        :type rule_info: :class:`huaweicloudsdklts.v2.AomMappingRuleInfo`
        """
        
        

        self._rule_id = None
        self._project_id = None
        self._rule_name = None
        self._rule_info = None
        self.discriminator = None

        self.rule_id = rule_id
        self.project_id = project_id
        self.rule_name = rule_name
        self.rule_info = rule_info

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateAomMappingRequest.

        接入规则id

        :return: The rule_id of this UpdateAomMappingRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateAomMappingRequest.

        接入规则id

        :param rule_id: The rule_id of this UpdateAomMappingRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateAomMappingRequest.

        项目id

        :return: The project_id of this UpdateAomMappingRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateAomMappingRequest.

        项目id

        :param project_id: The project_id of this UpdateAomMappingRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateAomMappingRequest.

        接入规则名称

        :return: The rule_name of this UpdateAomMappingRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateAomMappingRequest.

        接入规则名称

        :param rule_name: The rule_name of this UpdateAomMappingRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_info(self):
        r"""Gets the rule_info of this UpdateAomMappingRequest.

        :return: The rule_info of this UpdateAomMappingRequest.
        :rtype: :class:`huaweicloudsdklts.v2.AomMappingRuleInfo`
        """
        return self._rule_info

    @rule_info.setter
    def rule_info(self, rule_info):
        r"""Sets the rule_info of this UpdateAomMappingRequest.

        :param rule_info: The rule_info of this UpdateAomMappingRequest.
        :type rule_info: :class:`huaweicloudsdklts.v2.AomMappingRuleInfo`
        """
        self._rule_info = rule_info

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
        if not isinstance(other, UpdateAomMappingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
