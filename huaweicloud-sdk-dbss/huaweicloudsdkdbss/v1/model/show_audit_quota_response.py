# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'audit_quota': 'int',
        'cpu': 'int',
        'ram': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'audit_quota': 'audit_quota',
        'cpu': 'cpu',
        'ram': 'ram'
    }

    def __init__(self, project_id=None, audit_quota=None, cpu=None, ram=None):
        r"""ShowAuditQuotaResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。
        :type project_id: str
        :param audit_quota: 审计实例剩余配额。
        :type audit_quota: int
        :param cpu: CPU剩余配额。
        :type cpu: int
        :param ram: 内存剩余配额。
        :type ram: int
        """
        
        super(ShowAuditQuotaResponse, self).__init__()

        self._project_id = None
        self._audit_quota = None
        self._cpu = None
        self._ram = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if audit_quota is not None:
            self.audit_quota = audit_quota
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAuditQuotaResponse.

        项目ID。

        :return: The project_id of this ShowAuditQuotaResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAuditQuotaResponse.

        项目ID。

        :param project_id: The project_id of this ShowAuditQuotaResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def audit_quota(self):
        r"""Gets the audit_quota of this ShowAuditQuotaResponse.

        审计实例剩余配额。

        :return: The audit_quota of this ShowAuditQuotaResponse.
        :rtype: int
        """
        return self._audit_quota

    @audit_quota.setter
    def audit_quota(self, audit_quota):
        r"""Sets the audit_quota of this ShowAuditQuotaResponse.

        审计实例剩余配额。

        :param audit_quota: The audit_quota of this ShowAuditQuotaResponse.
        :type audit_quota: int
        """
        self._audit_quota = audit_quota

    @property
    def cpu(self):
        r"""Gets the cpu of this ShowAuditQuotaResponse.

        CPU剩余配额。

        :return: The cpu of this ShowAuditQuotaResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ShowAuditQuotaResponse.

        CPU剩余配额。

        :param cpu: The cpu of this ShowAuditQuotaResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        r"""Gets the ram of this ShowAuditQuotaResponse.

        内存剩余配额。

        :return: The ram of this ShowAuditQuotaResponse.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ShowAuditQuotaResponse.

        内存剩余配额。

        :param ram: The ram of this ShowAuditQuotaResponse.
        :type ram: int
        """
        self._ram = ram

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
        if not isinstance(other, ShowAuditQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
