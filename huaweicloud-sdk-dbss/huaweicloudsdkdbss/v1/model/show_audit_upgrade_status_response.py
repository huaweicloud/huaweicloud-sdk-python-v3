# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditUpgradeStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_upgrade_infos': 'list[AuditUpgradeStatus]'
    }

    attribute_map = {
        'audit_upgrade_infos': 'audit_upgrade_infos'
    }

    def __init__(self, audit_upgrade_infos=None):
        r"""ShowAuditUpgradeStatusResponse

        The model defined in huaweicloud sdk

        :param audit_upgrade_infos: 实例升级信息
        :type audit_upgrade_infos: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStatus`]
        """
        
        super(ShowAuditUpgradeStatusResponse, self).__init__()

        self._audit_upgrade_infos = None
        self.discriminator = None

        if audit_upgrade_infos is not None:
            self.audit_upgrade_infos = audit_upgrade_infos

    @property
    def audit_upgrade_infos(self):
        r"""Gets the audit_upgrade_infos of this ShowAuditUpgradeStatusResponse.

        实例升级信息

        :return: The audit_upgrade_infos of this ShowAuditUpgradeStatusResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStatus`]
        """
        return self._audit_upgrade_infos

    @audit_upgrade_infos.setter
    def audit_upgrade_infos(self, audit_upgrade_infos):
        r"""Sets the audit_upgrade_infos of this ShowAuditUpgradeStatusResponse.

        实例升级信息

        :param audit_upgrade_infos: The audit_upgrade_infos of this ShowAuditUpgradeStatusResponse.
        :type audit_upgrade_infos: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStatus`]
        """
        self._audit_upgrade_infos = audit_upgrade_infos

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
        if not isinstance(other, ShowAuditUpgradeStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
