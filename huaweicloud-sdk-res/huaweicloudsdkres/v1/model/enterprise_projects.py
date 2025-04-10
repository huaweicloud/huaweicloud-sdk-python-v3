# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseProjects:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'int',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, description=None, id=None, name=None, status=None, updated_at=None):
        r"""EnterpriseProjects

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: str
        :param description: 描述。
        :type description: str
        :param id: 企业项目id。
        :type id: str
        :param name: 企业项目名称。
        :type name: str
        :param status: 状态。
        :type status: int
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._created_at = None
        self._description = None
        self._id = None
        self._name = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        r"""Gets the created_at of this EnterpriseProjects.

        创建时间。

        :return: The created_at of this EnterpriseProjects.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EnterpriseProjects.

        创建时间。

        :param created_at: The created_at of this EnterpriseProjects.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this EnterpriseProjects.

        描述。

        :return: The description of this EnterpriseProjects.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnterpriseProjects.

        描述。

        :param description: The description of this EnterpriseProjects.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this EnterpriseProjects.

        企业项目id。

        :return: The id of this EnterpriseProjects.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EnterpriseProjects.

        企业项目id。

        :param id: The id of this EnterpriseProjects.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EnterpriseProjects.

        企业项目名称。

        :return: The name of this EnterpriseProjects.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnterpriseProjects.

        企业项目名称。

        :param name: The name of this EnterpriseProjects.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this EnterpriseProjects.

        状态。

        :return: The status of this EnterpriseProjects.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EnterpriseProjects.

        状态。

        :param status: The status of this EnterpriseProjects.
        :type status: int
        """
        self._status = status

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EnterpriseProjects.

        更新时间。

        :return: The updated_at of this EnterpriseProjects.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EnterpriseProjects.

        更新时间。

        :param updated_at: The updated_at of this EnterpriseProjects.
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
        if not isinstance(other, EnterpriseProjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
