# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseProjectInfoResult:

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
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, status=None, created_at=None, updated_at=None):
        r"""EnterpriseProjectInfoResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 企业项目ID。 **取值范围**: 不涉及。
        :type id: str
        :param name: **参数解释**: 企业项目名称。 **取值范围**: 不涉及。
        :type name: str
        :param description: **参数解释**: 企业项目描述。 **取值范围**: 不涉及。
        :type description: str
        :param status: **参数解释**: 企业项目状态。 **取值范围**: - 1：启用。 - 2：停用。
        :type status: str
        :param created_at: **参数解释**: 创建时间，格式为UTC格式。如：2018-05-18T06:49:06Z。 **取值范围**: 不涉及。
        :type created_at: str
        :param updated_at: **参数解释**: 修改时间，格式为UTC格式。如：2018-05-28T02:21:36Z。 **取值范围**: 不涉及。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目ID。 **取值范围**: 不涉及。

        :return: The id of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目ID。 **取值范围**: 不涉及。

        :param id: The id of this EnterpriseProjectInfoResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目名称。 **取值范围**: 不涉及。

        :return: The name of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目名称。 **取值范围**: 不涉及。

        :param name: The name of this EnterpriseProjectInfoResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目描述。 **取值范围**: 不涉及。

        :return: The description of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目描述。 **取值范围**: 不涉及。

        :param description: The description of this EnterpriseProjectInfoResult.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目状态。 **取值范围**: - 1：启用。 - 2：停用。

        :return: The status of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EnterpriseProjectInfoResult.

        **参数解释**: 企业项目状态。 **取值范围**: - 1：启用。 - 2：停用。

        :param status: The status of this EnterpriseProjectInfoResult.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this EnterpriseProjectInfoResult.

        **参数解释**: 创建时间，格式为UTC格式。如：2018-05-18T06:49:06Z。 **取值范围**: 不涉及。

        :return: The created_at of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EnterpriseProjectInfoResult.

        **参数解释**: 创建时间，格式为UTC格式。如：2018-05-18T06:49:06Z。 **取值范围**: 不涉及。

        :param created_at: The created_at of this EnterpriseProjectInfoResult.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EnterpriseProjectInfoResult.

        **参数解释**: 修改时间，格式为UTC格式。如：2018-05-28T02:21:36Z。 **取值范围**: 不涉及。

        :return: The updated_at of this EnterpriseProjectInfoResult.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EnterpriseProjectInfoResult.

        **参数解释**: 修改时间，格式为UTC格式。如：2018-05-28T02:21:36Z。 **取值范围**: 不涉及。

        :param updated_at: The updated_at of this EnterpriseProjectInfoResult.
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
        if not isinstance(other, EnterpriseProjectInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
