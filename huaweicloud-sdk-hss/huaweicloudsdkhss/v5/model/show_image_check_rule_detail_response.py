# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageCheckRuleDetailResponse(SdkResponse):

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
        'check_info_list': 'list[ImageCheckRuleCheckCaseResponseInfo]'
    }

    attribute_map = {
        'description': 'description',
        'reference': 'reference',
        'audit': 'audit',
        'remediation': 'remediation',
        'check_info_list': 'check_info_list'
    }

    def __init__(self, description=None, reference=None, audit=None, remediation=None, check_info_list=None):
        r"""ShowImageCheckRuleDetailResponse

        The model defined in huaweicloud sdk

        :param description: 检查项描述
        :type description: str
        :param reference: 参考
        :type reference: str
        :param audit: 审计描述
        :type audit: str
        :param remediation: 修改建议
        :type remediation: str
        :param check_info_list: 检测用例信息
        :type check_info_list: list[:class:`huaweicloudsdkhss.v5.ImageCheckRuleCheckCaseResponseInfo`]
        """
        
        super(ShowImageCheckRuleDetailResponse, self).__init__()

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
        r"""Gets the description of this ShowImageCheckRuleDetailResponse.

        检查项描述

        :return: The description of this ShowImageCheckRuleDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowImageCheckRuleDetailResponse.

        检查项描述

        :param description: The description of this ShowImageCheckRuleDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def reference(self):
        r"""Gets the reference of this ShowImageCheckRuleDetailResponse.

        参考

        :return: The reference of this ShowImageCheckRuleDetailResponse.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this ShowImageCheckRuleDetailResponse.

        参考

        :param reference: The reference of this ShowImageCheckRuleDetailResponse.
        :type reference: str
        """
        self._reference = reference

    @property
    def audit(self):
        r"""Gets the audit of this ShowImageCheckRuleDetailResponse.

        审计描述

        :return: The audit of this ShowImageCheckRuleDetailResponse.
        :rtype: str
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        r"""Sets the audit of this ShowImageCheckRuleDetailResponse.

        审计描述

        :param audit: The audit of this ShowImageCheckRuleDetailResponse.
        :type audit: str
        """
        self._audit = audit

    @property
    def remediation(self):
        r"""Gets the remediation of this ShowImageCheckRuleDetailResponse.

        修改建议

        :return: The remediation of this ShowImageCheckRuleDetailResponse.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        r"""Sets the remediation of this ShowImageCheckRuleDetailResponse.

        修改建议

        :param remediation: The remediation of this ShowImageCheckRuleDetailResponse.
        :type remediation: str
        """
        self._remediation = remediation

    @property
    def check_info_list(self):
        r"""Gets the check_info_list of this ShowImageCheckRuleDetailResponse.

        检测用例信息

        :return: The check_info_list of this ShowImageCheckRuleDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageCheckRuleCheckCaseResponseInfo`]
        """
        return self._check_info_list

    @check_info_list.setter
    def check_info_list(self, check_info_list):
        r"""Sets the check_info_list of this ShowImageCheckRuleDetailResponse.

        检测用例信息

        :param check_info_list: The check_info_list of this ShowImageCheckRuleDetailResponse.
        :type check_info_list: list[:class:`huaweicloudsdkhss.v5.ImageCheckRuleCheckCaseResponseInfo`]
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
        if not isinstance(other, ShowImageCheckRuleDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
