# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnSupportAuditInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_infos': 'list[UnSupportAuditInfo]',
        'support_version': 'str'
    }

    attribute_map = {
        'audit_infos': 'audit_infos',
        'support_version': 'support_version'
    }

    def __init__(self, audit_infos=None, support_version=None):
        r"""UnSupportAuditInfoResponse

        The model defined in huaweicloud sdk

        :param audit_infos: 审计信息
        :type audit_infos: list[:class:`huaweicloudsdkdbss.v1.UnSupportAuditInfo`]
        :param support_version: 支持的版本
        :type support_version: str
        """
        
        

        self._audit_infos = None
        self._support_version = None
        self.discriminator = None

        if audit_infos is not None:
            self.audit_infos = audit_infos
        if support_version is not None:
            self.support_version = support_version

    @property
    def audit_infos(self):
        r"""Gets the audit_infos of this UnSupportAuditInfoResponse.

        审计信息

        :return: The audit_infos of this UnSupportAuditInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.UnSupportAuditInfo`]
        """
        return self._audit_infos

    @audit_infos.setter
    def audit_infos(self, audit_infos):
        r"""Sets the audit_infos of this UnSupportAuditInfoResponse.

        审计信息

        :param audit_infos: The audit_infos of this UnSupportAuditInfoResponse.
        :type audit_infos: list[:class:`huaweicloudsdkdbss.v1.UnSupportAuditInfo`]
        """
        self._audit_infos = audit_infos

    @property
    def support_version(self):
        r"""Gets the support_version of this UnSupportAuditInfoResponse.

        支持的版本

        :return: The support_version of this UnSupportAuditInfoResponse.
        :rtype: str
        """
        return self._support_version

    @support_version.setter
    def support_version(self, support_version):
        r"""Sets the support_version of this UnSupportAuditInfoResponse.

        支持的版本

        :param support_version: The support_version of this UnSupportAuditInfoResponse.
        :type support_version: str
        """
        self._support_version = support_version

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
        if not isinstance(other, UnSupportAuditInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
