# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrgConformancePackDetailedStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'conformance_pack_id': 'str',
        'conformance_pack_name': 'str',
        'state': 'str',
        'error_message': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'conformance_pack_id': 'conformance_pack_id',
        'conformance_pack_name': 'conformance_pack_name',
        'state': 'state',
        'error_message': 'error_message',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, domain_id=None, conformance_pack_id=None, conformance_pack_name=None, state=None, error_message=None, created_at=None, updated_at=None):
        """OrgConformancePackDetailedStatus

        The model defined in huaweicloud sdk

        :param domain_id: 成员帐号ID。
        :type domain_id: str
        :param conformance_pack_id: 合规规则包ID。
        :type conformance_pack_id: str
        :param conformance_pack_name: 合规规则包名称。
        :type conformance_pack_name: str
        :param state: 合规规则包部署状态
        :type state: str
        :param error_message: 部署或删除组织合规规则包错误时的错误信息
        :type error_message: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._domain_id = None
        self._conformance_pack_id = None
        self._conformance_pack_name = None
        self._state = None
        self._error_message = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if conformance_pack_id is not None:
            self.conformance_pack_id = conformance_pack_id
        if conformance_pack_name is not None:
            self.conformance_pack_name = conformance_pack_name
        if state is not None:
            self.state = state
        if error_message is not None:
            self.error_message = error_message
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this OrgConformancePackDetailedStatus.

        成员帐号ID。

        :return: The domain_id of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this OrgConformancePackDetailedStatus.

        成员帐号ID。

        :param domain_id: The domain_id of this OrgConformancePackDetailedStatus.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def conformance_pack_id(self):
        """Gets the conformance_pack_id of this OrgConformancePackDetailedStatus.

        合规规则包ID。

        :return: The conformance_pack_id of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._conformance_pack_id

    @conformance_pack_id.setter
    def conformance_pack_id(self, conformance_pack_id):
        """Sets the conformance_pack_id of this OrgConformancePackDetailedStatus.

        合规规则包ID。

        :param conformance_pack_id: The conformance_pack_id of this OrgConformancePackDetailedStatus.
        :type conformance_pack_id: str
        """
        self._conformance_pack_id = conformance_pack_id

    @property
    def conformance_pack_name(self):
        """Gets the conformance_pack_name of this OrgConformancePackDetailedStatus.

        合规规则包名称。

        :return: The conformance_pack_name of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._conformance_pack_name

    @conformance_pack_name.setter
    def conformance_pack_name(self, conformance_pack_name):
        """Sets the conformance_pack_name of this OrgConformancePackDetailedStatus.

        合规规则包名称。

        :param conformance_pack_name: The conformance_pack_name of this OrgConformancePackDetailedStatus.
        :type conformance_pack_name: str
        """
        self._conformance_pack_name = conformance_pack_name

    @property
    def state(self):
        """Gets the state of this OrgConformancePackDetailedStatus.

        合规规则包部署状态

        :return: The state of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OrgConformancePackDetailedStatus.

        合规规则包部署状态

        :param state: The state of this OrgConformancePackDetailedStatus.
        :type state: str
        """
        self._state = state

    @property
    def error_message(self):
        """Gets the error_message of this OrgConformancePackDetailedStatus.

        部署或删除组织合规规则包错误时的错误信息

        :return: The error_message of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this OrgConformancePackDetailedStatus.

        部署或删除组织合规规则包错误时的错误信息

        :param error_message: The error_message of this OrgConformancePackDetailedStatus.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def created_at(self):
        """Gets the created_at of this OrgConformancePackDetailedStatus.

        创建时间。

        :return: The created_at of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrgConformancePackDetailedStatus.

        创建时间。

        :param created_at: The created_at of this OrgConformancePackDetailedStatus.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrgConformancePackDetailedStatus.

        更新时间。

        :return: The updated_at of this OrgConformancePackDetailedStatus.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrgConformancePackDetailedStatus.

        更新时间。

        :param updated_at: The updated_at of this OrgConformancePackDetailedStatus.
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
        if not isinstance(other, OrgConformancePackDetailedStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
