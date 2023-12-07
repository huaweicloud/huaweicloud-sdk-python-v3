# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigRuleComplianceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'config_rule_compliances': 'list[ConfigRuleCompliance]'
    }

    attribute_map = {
        'account_id': 'account_id',
        'config_rule_compliances': 'config_rule_compliances'
    }

    def __init__(self, account_id=None, config_rule_compliances=None):
        """ListConfigRuleComplianceResponse

        The model defined in huaweicloud sdk

        :param account_id: 账号ID
        :type account_id: str
        :param config_rule_compliances: 
        :type config_rule_compliances: list[:class:`huaweicloudsdkrgc.v1.ConfigRuleCompliance`]
        """
        
        super(ListConfigRuleComplianceResponse, self).__init__()

        self._account_id = None
        self._config_rule_compliances = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if config_rule_compliances is not None:
            self.config_rule_compliances = config_rule_compliances

    @property
    def account_id(self):
        """Gets the account_id of this ListConfigRuleComplianceResponse.

        账号ID

        :return: The account_id of this ListConfigRuleComplianceResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ListConfigRuleComplianceResponse.

        账号ID

        :param account_id: The account_id of this ListConfigRuleComplianceResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def config_rule_compliances(self):
        """Gets the config_rule_compliances of this ListConfigRuleComplianceResponse.

        :return: The config_rule_compliances of this ListConfigRuleComplianceResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.ConfigRuleCompliance`]
        """
        return self._config_rule_compliances

    @config_rule_compliances.setter
    def config_rule_compliances(self, config_rule_compliances):
        """Sets the config_rule_compliances of this ListConfigRuleComplianceResponse.

        :param config_rule_compliances: The config_rule_compliances of this ListConfigRuleComplianceResponse.
        :type config_rule_compliances: list[:class:`huaweicloudsdkrgc.v1.ConfigRuleCompliance`]
        """
        self._config_rule_compliances = config_rule_compliances

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
        if not isinstance(other, ListConfigRuleComplianceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
