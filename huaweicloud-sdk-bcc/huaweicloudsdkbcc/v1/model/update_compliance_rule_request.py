# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComplianceRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'compliance_id': 'str',
        'body': 'UpdateComplianceRuleRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'compliance_id': 'compliance_id',
        'body': 'body'
    }

    def __init__(self, domain_id=None, compliance_id=None, body=None):
        r"""UpdateComplianceRuleRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param compliance_id: 合规id
        :type compliance_id: str
        :param body: Body of the UpdateComplianceRuleRequest
        :type body: :class:`huaweicloudsdkbcc.v1.UpdateComplianceRuleRequestBody`
        """
        
        

        self._domain_id = None
        self._compliance_id = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        self.compliance_id = compliance_id
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateComplianceRuleRequest.

        账号ID

        :return: The domain_id of this UpdateComplianceRuleRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateComplianceRuleRequest.

        账号ID

        :param domain_id: The domain_id of this UpdateComplianceRuleRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def compliance_id(self):
        r"""Gets the compliance_id of this UpdateComplianceRuleRequest.

        合规id

        :return: The compliance_id of this UpdateComplianceRuleRequest.
        :rtype: str
        """
        return self._compliance_id

    @compliance_id.setter
    def compliance_id(self, compliance_id):
        r"""Sets the compliance_id of this UpdateComplianceRuleRequest.

        合规id

        :param compliance_id: The compliance_id of this UpdateComplianceRuleRequest.
        :type compliance_id: str
        """
        self._compliance_id = compliance_id

    @property
    def body(self):
        r"""Gets the body of this UpdateComplianceRuleRequest.

        :return: The body of this UpdateComplianceRuleRequest.
        :rtype: :class:`huaweicloudsdkbcc.v1.UpdateComplianceRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateComplianceRuleRequest.

        :param body: The body of this UpdateComplianceRuleRequest.
        :type body: :class:`huaweicloudsdkbcc.v1.UpdateComplianceRuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateComplianceRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
