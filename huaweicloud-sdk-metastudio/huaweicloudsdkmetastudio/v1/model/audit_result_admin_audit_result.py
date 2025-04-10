# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditResultAdminAuditResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'attachment_name': 'str',
        'attachment_url': 'str',
        'audit_time': 'int'
    }

    attribute_map = {
        'message': 'message',
        'attachment_name': 'attachment_name',
        'attachment_url': 'attachment_url',
        'audit_time': 'audit_time'
    }

    def __init__(self, message=None, attachment_name=None, attachment_url=None, audit_time=None):
        r"""AuditResultAdminAuditResult

        The model defined in huaweicloud sdk

        :param message: 审核信息。
        :type message: str
        :param attachment_name: 附件名称。
        :type attachment_name: str
        :param attachment_url: 附件下载地址。
        :type attachment_url: str
        :param audit_time: 操作时间。
        :type audit_time: int
        """
        
        

        self._message = None
        self._attachment_name = None
        self._attachment_url = None
        self._audit_time = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if attachment_name is not None:
            self.attachment_name = attachment_name
        if attachment_url is not None:
            self.attachment_url = attachment_url
        if audit_time is not None:
            self.audit_time = audit_time

    @property
    def message(self):
        r"""Gets the message of this AuditResultAdminAuditResult.

        审核信息。

        :return: The message of this AuditResultAdminAuditResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this AuditResultAdminAuditResult.

        审核信息。

        :param message: The message of this AuditResultAdminAuditResult.
        :type message: str
        """
        self._message = message

    @property
    def attachment_name(self):
        r"""Gets the attachment_name of this AuditResultAdminAuditResult.

        附件名称。

        :return: The attachment_name of this AuditResultAdminAuditResult.
        :rtype: str
        """
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, attachment_name):
        r"""Sets the attachment_name of this AuditResultAdminAuditResult.

        附件名称。

        :param attachment_name: The attachment_name of this AuditResultAdminAuditResult.
        :type attachment_name: str
        """
        self._attachment_name = attachment_name

    @property
    def attachment_url(self):
        r"""Gets the attachment_url of this AuditResultAdminAuditResult.

        附件下载地址。

        :return: The attachment_url of this AuditResultAdminAuditResult.
        :rtype: str
        """
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, attachment_url):
        r"""Sets the attachment_url of this AuditResultAdminAuditResult.

        附件下载地址。

        :param attachment_url: The attachment_url of this AuditResultAdminAuditResult.
        :type attachment_url: str
        """
        self._attachment_url = attachment_url

    @property
    def audit_time(self):
        r"""Gets the audit_time of this AuditResultAdminAuditResult.

        操作时间。

        :return: The audit_time of this AuditResultAdminAuditResult.
        :rtype: int
        """
        return self._audit_time

    @audit_time.setter
    def audit_time(self, audit_time):
        r"""Sets the audit_time of this AuditResultAdminAuditResult.

        操作时间。

        :param audit_time: The audit_time of this AuditResultAdminAuditResult.
        :type audit_time: int
        """
        self._audit_time = audit_time

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
        if not isinstance(other, AuditResultAdminAuditResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
