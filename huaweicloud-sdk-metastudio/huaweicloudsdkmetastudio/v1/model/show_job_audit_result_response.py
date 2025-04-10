# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobAuditResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system_audit_result': 'AuditResultSystemAuditResult',
        'admin_audit_result': 'AuditResultAdminAuditResult'
    }

    attribute_map = {
        'system_audit_result': 'system_audit_result',
        'admin_audit_result': 'admin_audit_result'
    }

    def __init__(self, system_audit_result=None, admin_audit_result=None):
        r"""ShowJobAuditResultResponse

        The model defined in huaweicloud sdk

        :param system_audit_result: 
        :type system_audit_result: :class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResult`
        :param admin_audit_result: 
        :type admin_audit_result: :class:`huaweicloudsdkmetastudio.v1.AuditResultAdminAuditResult`
        """
        
        super(ShowJobAuditResultResponse, self).__init__()

        self._system_audit_result = None
        self._admin_audit_result = None
        self.discriminator = None

        if system_audit_result is not None:
            self.system_audit_result = system_audit_result
        if admin_audit_result is not None:
            self.admin_audit_result = admin_audit_result

    @property
    def system_audit_result(self):
        r"""Gets the system_audit_result of this ShowJobAuditResultResponse.

        :return: The system_audit_result of this ShowJobAuditResultResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResult`
        """
        return self._system_audit_result

    @system_audit_result.setter
    def system_audit_result(self, system_audit_result):
        r"""Sets the system_audit_result of this ShowJobAuditResultResponse.

        :param system_audit_result: The system_audit_result of this ShowJobAuditResultResponse.
        :type system_audit_result: :class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResult`
        """
        self._system_audit_result = system_audit_result

    @property
    def admin_audit_result(self):
        r"""Gets the admin_audit_result of this ShowJobAuditResultResponse.

        :return: The admin_audit_result of this ShowJobAuditResultResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AuditResultAdminAuditResult`
        """
        return self._admin_audit_result

    @admin_audit_result.setter
    def admin_audit_result(self, admin_audit_result):
        r"""Sets the admin_audit_result of this ShowJobAuditResultResponse.

        :param admin_audit_result: The admin_audit_result of this ShowJobAuditResultResponse.
        :type admin_audit_result: :class:`huaweicloudsdkmetastudio.v1.AuditResultAdminAuditResult`
        """
        self._admin_audit_result = admin_audit_result

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
        if not isinstance(other, ShowJobAuditResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
