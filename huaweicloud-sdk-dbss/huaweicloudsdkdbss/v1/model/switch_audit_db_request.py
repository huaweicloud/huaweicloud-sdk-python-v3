# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchAuditDbRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'lts_audit_switch': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'lts_audit_switch': 'lts_audit_switch'
    }

    def __init__(self, id=None, status=None, lts_audit_switch=None):
        r"""SwitchAuditDbRequest

        The model defined in huaweicloud sdk

        :param id: 数据库ID,可在查询数据库列表接口的ID字段获取。
        :type id: str
        :param status: 开关状态 - ON:开启 - OFF:关闭
        :type status: str
        :param lts_audit_switch: 是否关闭LTS审计,DWS数据库场景使用。若用户未选择关闭LTS审计,则不做操作。 - 1 :是 - 0 或 其它:保持原状
        :type lts_audit_switch: int
        """
        
        

        self._id = None
        self._status = None
        self._lts_audit_switch = None
        self.discriminator = None

        self.id = id
        self.status = status
        if lts_audit_switch is not None:
            self.lts_audit_switch = lts_audit_switch

    @property
    def id(self):
        r"""Gets the id of this SwitchAuditDbRequest.

        数据库ID,可在查询数据库列表接口的ID字段获取。

        :return: The id of this SwitchAuditDbRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SwitchAuditDbRequest.

        数据库ID,可在查询数据库列表接口的ID字段获取。

        :param id: The id of this SwitchAuditDbRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this SwitchAuditDbRequest.

        开关状态 - ON:开启 - OFF:关闭

        :return: The status of this SwitchAuditDbRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SwitchAuditDbRequest.

        开关状态 - ON:开启 - OFF:关闭

        :param status: The status of this SwitchAuditDbRequest.
        :type status: str
        """
        self._status = status

    @property
    def lts_audit_switch(self):
        r"""Gets the lts_audit_switch of this SwitchAuditDbRequest.

        是否关闭LTS审计,DWS数据库场景使用。若用户未选择关闭LTS审计,则不做操作。 - 1 :是 - 0 或 其它:保持原状

        :return: The lts_audit_switch of this SwitchAuditDbRequest.
        :rtype: int
        """
        return self._lts_audit_switch

    @lts_audit_switch.setter
    def lts_audit_switch(self, lts_audit_switch):
        r"""Sets the lts_audit_switch of this SwitchAuditDbRequest.

        是否关闭LTS审计,DWS数据库场景使用。若用户未选择关闭LTS审计,则不做操作。 - 1 :是 - 0 或 其它:保持原状

        :param lts_audit_switch: The lts_audit_switch of this SwitchAuditDbRequest.
        :type lts_audit_switch: int
        """
        self._lts_audit_switch = lts_audit_switch

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
        if not isinstance(other, SwitchAuditDbRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
