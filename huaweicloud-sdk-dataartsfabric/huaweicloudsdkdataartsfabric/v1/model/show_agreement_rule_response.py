# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgreementRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_rules': 'list[AgreementRule]'
    }

    attribute_map = {
        'agreement_rules': 'agreement_rules'
    }

    def __init__(self, agreement_rules=None):
        r"""ShowAgreementRuleResponse

        The model defined in huaweicloud sdk

        :param agreement_rules: 系统协议列表
        :type agreement_rules: list[:class:`huaweicloudsdkdataartsfabric.v1.AgreementRule`]
        """
        
        super(ShowAgreementRuleResponse, self).__init__()

        self._agreement_rules = None
        self.discriminator = None

        if agreement_rules is not None:
            self.agreement_rules = agreement_rules

    @property
    def agreement_rules(self):
        r"""Gets the agreement_rules of this ShowAgreementRuleResponse.

        系统协议列表

        :return: The agreement_rules of this ShowAgreementRuleResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.AgreementRule`]
        """
        return self._agreement_rules

    @agreement_rules.setter
    def agreement_rules(self, agreement_rules):
        r"""Sets the agreement_rules of this ShowAgreementRuleResponse.

        系统协议列表

        :param agreement_rules: The agreement_rules of this ShowAgreementRuleResponse.
        :type agreement_rules: list[:class:`huaweicloudsdkdataartsfabric.v1.AgreementRule`]
        """
        self._agreement_rules = agreement_rules

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
        if not isinstance(other, ShowAgreementRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
