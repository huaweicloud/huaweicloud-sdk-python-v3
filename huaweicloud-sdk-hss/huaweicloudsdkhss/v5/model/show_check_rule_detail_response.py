# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckRuleDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'reference': 'str',
        'audit': 'str',
        'remediation': 'str',
        'check_info_list': 'list[CheckRuleCheckCaseResponseInfo]'
    }

    attribute_map = {
        'description': 'description',
        'reference': 'reference',
        'audit': 'audit',
        'remediation': 'remediation',
        'check_info_list': 'check_info_list'
    }

    def __init__(self, description=None, reference=None, audit=None, remediation=None, check_info_list=None):
        """ShowCheckRuleDetailResponse

        The model defined in huaweicloud sdk

        :param description: 当前检查项（检测规则）的描述
        :type description: str
        :param reference: 当前检查项（检测规则）的制定依据
        :type reference: str
        :param audit: 当前检查项（检测规则）的审计描述
        :type audit: str
        :param remediation: 当前检查项（检测规则）的修改建议
        :type remediation: str
        :param check_info_list: 检测用例信息
        :type check_info_list: list[:class:`huaweicloudsdkhss.v5.CheckRuleCheckCaseResponseInfo`]
        """
        
        super(ShowCheckRuleDetailResponse, self).__init__()

        self._description = None
        self._reference = None
        self._audit = None
        self._remediation = None
        self._check_info_list = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if reference is not None:
            self.reference = reference
        if audit is not None:
            self.audit = audit
        if remediation is not None:
            self.remediation = remediation
        if check_info_list is not None:
            self.check_info_list = check_info_list

    @property
    def description(self):
        """Gets the description of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的描述

        :return: The description of this ShowCheckRuleDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的描述

        :param description: The description of this ShowCheckRuleDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def reference(self):
        """Gets the reference of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的制定依据

        :return: The reference of this ShowCheckRuleDetailResponse.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的制定依据

        :param reference: The reference of this ShowCheckRuleDetailResponse.
        :type reference: str
        """
        self._reference = reference

    @property
    def audit(self):
        """Gets the audit of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的审计描述

        :return: The audit of this ShowCheckRuleDetailResponse.
        :rtype: str
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        """Sets the audit of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的审计描述

        :param audit: The audit of this ShowCheckRuleDetailResponse.
        :type audit: str
        """
        self._audit = audit

    @property
    def remediation(self):
        """Gets the remediation of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的修改建议

        :return: The remediation of this ShowCheckRuleDetailResponse.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this ShowCheckRuleDetailResponse.

        当前检查项（检测规则）的修改建议

        :param remediation: The remediation of this ShowCheckRuleDetailResponse.
        :type remediation: str
        """
        self._remediation = remediation

    @property
    def check_info_list(self):
        """Gets the check_info_list of this ShowCheckRuleDetailResponse.

        检测用例信息

        :return: The check_info_list of this ShowCheckRuleDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleCheckCaseResponseInfo`]
        """
        return self._check_info_list

    @check_info_list.setter
    def check_info_list(self, check_info_list):
        """Sets the check_info_list of this ShowCheckRuleDetailResponse.

        检测用例信息

        :param check_info_list: The check_info_list of this ShowCheckRuleDetailResponse.
        :type check_info_list: list[:class:`huaweicloudsdkhss.v5.CheckRuleCheckCaseResponseInfo`]
        """
        self._check_info_list = check_info_list

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
        if not isinstance(other, ShowCheckRuleDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
