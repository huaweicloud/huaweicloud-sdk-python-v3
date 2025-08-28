# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listener_id': 'str',
        'operating_status': 'str',
        'reason': 'MemberHealthCheckFailedReason',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'operating_status': 'operating_status',
        'reason': 'reason',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, listener_id=None, operating_status=None, reason=None, created_at=None, updated_at=None):
        r"""MemberStatus

        The model defined in huaweicloud sdk

        :param listener_id: **参数解释**：监听器ID  **取值范围**：不涉及
        :type listener_id: str
        :param operating_status: **参数解释**：后端服务器的健康状态。  **取值范围**： - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。
        :type operating_status: str
        :param reason: 
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        :param created_at: **参数解释**：创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及
        :type updated_at: str
        """
        
        

        self._listener_id = None
        self._operating_status = None
        self._reason = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.listener_id = listener_id
        self.operating_status = operating_status
        if reason is not None:
            self.reason = reason
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def listener_id(self):
        r"""Gets the listener_id of this MemberStatus.

        **参数解释**：监听器ID  **取值范围**：不涉及

        :return: The listener_id of this MemberStatus.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this MemberStatus.

        **参数解释**：监听器ID  **取值范围**：不涉及

        :param listener_id: The listener_id of this MemberStatus.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def operating_status(self):
        r"""Gets the operating_status of this MemberStatus.

        **参数解释**：后端服务器的健康状态。  **取值范围**： - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。

        :return: The operating_status of this MemberStatus.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this MemberStatus.

        **参数解释**：后端服务器的健康状态。  **取值范围**： - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。

        :param operating_status: The operating_status of this MemberStatus.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def reason(self):
        r"""Gets the reason of this MemberStatus.

        :return: The reason of this MemberStatus.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this MemberStatus.

        :param reason: The reason of this MemberStatus.
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        self._reason = reason

    @property
    def created_at(self):
        r"""Gets the created_at of this MemberStatus.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及

        :return: The created_at of this MemberStatus.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MemberStatus.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及

        :param created_at: The created_at of this MemberStatus.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MemberStatus.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及

        :return: The updated_at of this MemberStatus.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MemberStatus.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及

        :param updated_at: The updated_at of this MemberStatus.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, MemberStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
