# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrgConformancePackStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_conformance_pack_id': 'str',
        'org_conformance_pack_name': 'str',
        'state': 'str',
        'error_message': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'org_conformance_pack_id': 'org_conformance_pack_id',
        'org_conformance_pack_name': 'org_conformance_pack_name',
        'state': 'state',
        'error_message': 'error_message',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, org_conformance_pack_id=None, org_conformance_pack_name=None, state=None, error_message=None, created_at=None, updated_at=None):
        r"""OrgConformancePackStatus

        The model defined in huaweicloud sdk

        :param org_conformance_pack_id: 组织合规规则包ID。
        :type org_conformance_pack_id: str
        :param org_conformance_pack_name: 组织合规规则包名称。
        :type org_conformance_pack_name: str
        :param state: 合规规则包部署状态
        :type state: str
        :param error_message: 部署或删除组织合规规则包错误时的错误信息
        :type error_message: str
        :param created_at: 组织合规规则包创建时间。
        :type created_at: str
        :param updated_at: 组织合规规则包更新时间。
        :type updated_at: str
        """
        
        

        self._org_conformance_pack_id = None
        self._org_conformance_pack_name = None
        self._state = None
        self._error_message = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if org_conformance_pack_id is not None:
            self.org_conformance_pack_id = org_conformance_pack_id
        if org_conformance_pack_name is not None:
            self.org_conformance_pack_name = org_conformance_pack_name
        if state is not None:
            self.state = state
        if error_message is not None:
            self.error_message = error_message
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def org_conformance_pack_id(self):
        r"""Gets the org_conformance_pack_id of this OrgConformancePackStatus.

        组织合规规则包ID。

        :return: The org_conformance_pack_id of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._org_conformance_pack_id

    @org_conformance_pack_id.setter
    def org_conformance_pack_id(self, org_conformance_pack_id):
        r"""Sets the org_conformance_pack_id of this OrgConformancePackStatus.

        组织合规规则包ID。

        :param org_conformance_pack_id: The org_conformance_pack_id of this OrgConformancePackStatus.
        :type org_conformance_pack_id: str
        """
        self._org_conformance_pack_id = org_conformance_pack_id

    @property
    def org_conformance_pack_name(self):
        r"""Gets the org_conformance_pack_name of this OrgConformancePackStatus.

        组织合规规则包名称。

        :return: The org_conformance_pack_name of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._org_conformance_pack_name

    @org_conformance_pack_name.setter
    def org_conformance_pack_name(self, org_conformance_pack_name):
        r"""Sets the org_conformance_pack_name of this OrgConformancePackStatus.

        组织合规规则包名称。

        :param org_conformance_pack_name: The org_conformance_pack_name of this OrgConformancePackStatus.
        :type org_conformance_pack_name: str
        """
        self._org_conformance_pack_name = org_conformance_pack_name

    @property
    def state(self):
        r"""Gets the state of this OrgConformancePackStatus.

        合规规则包部署状态

        :return: The state of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this OrgConformancePackStatus.

        合规规则包部署状态

        :param state: The state of this OrgConformancePackStatus.
        :type state: str
        """
        self._state = state

    @property
    def error_message(self):
        r"""Gets the error_message of this OrgConformancePackStatus.

        部署或删除组织合规规则包错误时的错误信息

        :return: The error_message of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this OrgConformancePackStatus.

        部署或删除组织合规规则包错误时的错误信息

        :param error_message: The error_message of this OrgConformancePackStatus.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def created_at(self):
        r"""Gets the created_at of this OrgConformancePackStatus.

        组织合规规则包创建时间。

        :return: The created_at of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OrgConformancePackStatus.

        组织合规规则包创建时间。

        :param created_at: The created_at of this OrgConformancePackStatus.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this OrgConformancePackStatus.

        组织合规规则包更新时间。

        :return: The updated_at of this OrgConformancePackStatus.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this OrgConformancePackStatus.

        组织合规规则包更新时间。

        :param updated_at: The updated_at of this OrgConformancePackStatus.
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
        if not isinstance(other, OrgConformancePackStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
