# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupDeployment:

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
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None):
        r"""GroupDeployment

        The model defined in huaweicloud sdk

        :param id: 应用部署uuid
        :type id: str
        :param name: 应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾
        :type name: str
        :param description: 应用部署描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 应用部署创建时间
        :type created_at: str
        :param updated_at: 应用部署更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this GroupDeployment.

        应用部署uuid

        :return: The id of this GroupDeployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupDeployment.

        应用部署uuid

        :param id: The id of this GroupDeployment.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupDeployment.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :return: The name of this GroupDeployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupDeployment.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :param name: The name of this GroupDeployment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this GroupDeployment.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this GroupDeployment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GroupDeployment.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this GroupDeployment.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this GroupDeployment.

        项目ID

        :return: The project_id of this GroupDeployment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this GroupDeployment.

        项目ID

        :param project_id: The project_id of this GroupDeployment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this GroupDeployment.

        应用部署创建时间

        :return: The created_at of this GroupDeployment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GroupDeployment.

        应用部署创建时间

        :param created_at: The created_at of this GroupDeployment.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GroupDeployment.

        应用部署更新时间

        :return: The updated_at of this GroupDeployment.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GroupDeployment.

        应用部署更新时间

        :param updated_at: The updated_at of this GroupDeployment.
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
        if not isinstance(other, GroupDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
