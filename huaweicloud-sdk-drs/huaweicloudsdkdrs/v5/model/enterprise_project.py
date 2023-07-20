# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseProject:

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
        """EnterpriseProject

        The model defined in huaweicloud sdk

        :param id: 企业项目ID，0表示默认企业项目。
        :type id: str
        :param name: 企业项目名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param status: 企业项目状态。 - 1：启用 - 2：停用
        :type status: str
        :param created_at: 创建时间，例如：2023-01-20T07:18:26Z
        :type created_at: str
        :param updated_at: 更新时间，例如：2023-03-01T09:42:02Z
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
        """Gets the id of this EnterpriseProject.

        企业项目ID，0表示默认企业项目。

        :return: The id of this EnterpriseProject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnterpriseProject.

        企业项目ID，0表示默认企业项目。

        :param id: The id of this EnterpriseProject.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnterpriseProject.

        企业项目名称。

        :return: The name of this EnterpriseProject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterpriseProject.

        企业项目名称。

        :param name: The name of this EnterpriseProject.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EnterpriseProject.

        描述。

        :return: The description of this EnterpriseProject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnterpriseProject.

        描述。

        :param description: The description of this EnterpriseProject.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this EnterpriseProject.

        企业项目状态。 - 1：启用 - 2：停用

        :return: The status of this EnterpriseProject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnterpriseProject.

        企业项目状态。 - 1：启用 - 2：停用

        :param status: The status of this EnterpriseProject.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this EnterpriseProject.

        创建时间，例如：2023-01-20T07:18:26Z

        :return: The created_at of this EnterpriseProject.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EnterpriseProject.

        创建时间，例如：2023-01-20T07:18:26Z

        :param created_at: The created_at of this EnterpriseProject.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EnterpriseProject.

        更新时间，例如：2023-03-01T09:42:02Z

        :return: The updated_at of this EnterpriseProject.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EnterpriseProject.

        更新时间，例如：2023-03-01T09:42:02Z

        :param updated_at: The updated_at of this EnterpriseProject.
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
        if not isinstance(other, EnterpriseProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
