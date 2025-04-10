# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityDataClassificationRuleGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'name': 'str',
        'rules': 'list[DataClassificationRuleQueryDTO]',
        'description': 'str',
        'created_by': 'str',
        'created_at': 'int',
        'updated_by': 'str',
        'updated_at': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'rules': 'rules',
        'description': 'description',
        'created_by': 'created_by',
        'created_at': 'created_at',
        'updated_by': 'updated_by',
        'updated_at': 'updated_at',
        'project_id': 'project_id'
    }

    def __init__(self, uuid=None, name=None, rules=None, description=None, created_by=None, created_at=None, updated_by=None, updated_at=None, project_id=None):
        r"""CreateSecurityDataClassificationRuleGroupResponse

        The model defined in huaweicloud sdk

        :param uuid: 规则组ID
        :type uuid: str
        :param name: 规则组名称
        :type name: str
        :param rules: 规则实体
        :type rules: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        :param description: 规则组描述
        :type description: str
        :param created_by: 规则组创建人
        :type created_by: str
        :param created_at: 规则组创建时间
        :type created_at: int
        :param updated_by: 规则组更新人
        :type updated_by: str
        :param updated_at: 规则组更新时间
        :type updated_at: int
        :param project_id: 项目ID
        :type project_id: str
        """
        
        super(CreateSecurityDataClassificationRuleGroupResponse, self).__init__()

        self._uuid = None
        self._name = None
        self._rules = None
        self._description = None
        self._created_by = None
        self._created_at = None
        self._updated_by = None
        self._updated_at = None
        self._project_id = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id

    @property
    def uuid(self):
        r"""Gets the uuid of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组ID

        :return: The uuid of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组ID

        :param uuid: The uuid of this CreateSecurityDataClassificationRuleGroupResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def name(self):
        r"""Gets the name of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组名称

        :return: The name of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组名称

        :param name: The name of this CreateSecurityDataClassificationRuleGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def rules(self):
        r"""Gets the rules of this CreateSecurityDataClassificationRuleGroupResponse.

        规则实体

        :return: The rules of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this CreateSecurityDataClassificationRuleGroupResponse.

        规则实体

        :param rules: The rules of this CreateSecurityDataClassificationRuleGroupResponse.
        :type rules: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        """
        self._rules = rules

    @property
    def description(self):
        r"""Gets the description of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组描述

        :return: The description of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组描述

        :param description: The description of this CreateSecurityDataClassificationRuleGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        r"""Gets the created_by of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组创建人

        :return: The created_by of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组创建人

        :param created_by: The created_by of this CreateSecurityDataClassificationRuleGroupResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组创建时间

        :return: The created_at of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组创建时间

        :param created_at: The created_at of this CreateSecurityDataClassificationRuleGroupResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_by(self):
        r"""Gets the updated_by of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组更新人

        :return: The updated_by of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组更新人

        :param updated_by: The updated_by of this CreateSecurityDataClassificationRuleGroupResponse.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组更新时间

        :return: The updated_at of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateSecurityDataClassificationRuleGroupResponse.

        规则组更新时间

        :param updated_at: The updated_at of this CreateSecurityDataClassificationRuleGroupResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateSecurityDataClassificationRuleGroupResponse.

        项目ID

        :return: The project_id of this CreateSecurityDataClassificationRuleGroupResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateSecurityDataClassificationRuleGroupResponse.

        项目ID

        :param project_id: The project_id of this CreateSecurityDataClassificationRuleGroupResponse.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, CreateSecurityDataClassificationRuleGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
