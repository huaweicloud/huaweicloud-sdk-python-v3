# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetProjectInfoV4ResultProject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_num_id': 'int',
        'project_id': 'str',
        'name': 'str',
        'created_on': 'int',
        'updated_on': 'int',
        'project_type': 'str',
        'archive': 'int',
        'enterprise_id': 'str',
        'project_code': 'str',
        'creator': 'GetProjectInfoV4ResultProjectCreator'
    }

    attribute_map = {
        'project_num_id': 'project_num_id',
        'project_id': 'project_id',
        'name': 'name',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'project_type': 'project_type',
        'archive': 'archive',
        'enterprise_id': 'enterprise_id',
        'project_code': 'project_code',
        'creator': 'creator'
    }

    def __init__(self, project_num_id=None, project_id=None, name=None, created_on=None, updated_on=None, project_type=None, archive=None, enterprise_id=None, project_code=None, creator=None):
        r"""GetProjectInfoV4ResultProject

        The model defined in huaweicloud sdk

        :param project_num_id: 项目numId
        :type project_num_id: int
        :param project_id: 项目uuid
        :type project_id: str
        :param name: 项目名称
        :type name: str
        :param created_on: 项目创建时间
        :type created_on: int
        :param updated_on: 项目更新时间
        :type updated_on: int
        :param project_type: 项目类型
        :type project_type: str
        :param archive: 是否归档
        :type archive: int
        :param enterprise_id: 企业项目id
        :type enterprise_id: str
        :param project_code: 项目代号
        :type project_code: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.GetProjectInfoV4ResultProjectCreator`
        """
        
        

        self._project_num_id = None
        self._project_id = None
        self._name = None
        self._created_on = None
        self._updated_on = None
        self._project_type = None
        self._archive = None
        self._enterprise_id = None
        self._project_code = None
        self._creator = None
        self.discriminator = None

        if project_num_id is not None:
            self.project_num_id = project_num_id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if project_type is not None:
            self.project_type = project_type
        if archive is not None:
            self.archive = archive
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if project_code is not None:
            self.project_code = project_code
        if creator is not None:
            self.creator = creator

    @property
    def project_num_id(self):
        r"""Gets the project_num_id of this GetProjectInfoV4ResultProject.

        项目numId

        :return: The project_num_id of this GetProjectInfoV4ResultProject.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        r"""Sets the project_num_id of this GetProjectInfoV4ResultProject.

        项目numId

        :param project_num_id: The project_num_id of this GetProjectInfoV4ResultProject.
        :type project_num_id: int
        """
        self._project_num_id = project_num_id

    @property
    def project_id(self):
        r"""Gets the project_id of this GetProjectInfoV4ResultProject.

        项目uuid

        :return: The project_id of this GetProjectInfoV4ResultProject.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this GetProjectInfoV4ResultProject.

        项目uuid

        :param project_id: The project_id of this GetProjectInfoV4ResultProject.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this GetProjectInfoV4ResultProject.

        项目名称

        :return: The name of this GetProjectInfoV4ResultProject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetProjectInfoV4ResultProject.

        项目名称

        :param name: The name of this GetProjectInfoV4ResultProject.
        :type name: str
        """
        self._name = name

    @property
    def created_on(self):
        r"""Gets the created_on of this GetProjectInfoV4ResultProject.

        项目创建时间

        :return: The created_on of this GetProjectInfoV4ResultProject.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this GetProjectInfoV4ResultProject.

        项目创建时间

        :param created_on: The created_on of this GetProjectInfoV4ResultProject.
        :type created_on: int
        """
        self._created_on = created_on

    @property
    def updated_on(self):
        r"""Gets the updated_on of this GetProjectInfoV4ResultProject.

        项目更新时间

        :return: The updated_on of this GetProjectInfoV4ResultProject.
        :rtype: int
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        r"""Sets the updated_on of this GetProjectInfoV4ResultProject.

        项目更新时间

        :param updated_on: The updated_on of this GetProjectInfoV4ResultProject.
        :type updated_on: int
        """
        self._updated_on = updated_on

    @property
    def project_type(self):
        r"""Gets the project_type of this GetProjectInfoV4ResultProject.

        项目类型

        :return: The project_type of this GetProjectInfoV4ResultProject.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this GetProjectInfoV4ResultProject.

        项目类型

        :param project_type: The project_type of this GetProjectInfoV4ResultProject.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def archive(self):
        r"""Gets the archive of this GetProjectInfoV4ResultProject.

        是否归档

        :return: The archive of this GetProjectInfoV4ResultProject.
        :rtype: int
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        r"""Sets the archive of this GetProjectInfoV4ResultProject.

        是否归档

        :param archive: The archive of this GetProjectInfoV4ResultProject.
        :type archive: int
        """
        self._archive = archive

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this GetProjectInfoV4ResultProject.

        企业项目id

        :return: The enterprise_id of this GetProjectInfoV4ResultProject.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this GetProjectInfoV4ResultProject.

        企业项目id

        :param enterprise_id: The enterprise_id of this GetProjectInfoV4ResultProject.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def project_code(self):
        r"""Gets the project_code of this GetProjectInfoV4ResultProject.

        项目代号

        :return: The project_code of this GetProjectInfoV4ResultProject.
        :rtype: str
        """
        return self._project_code

    @project_code.setter
    def project_code(self, project_code):
        r"""Sets the project_code of this GetProjectInfoV4ResultProject.

        项目代号

        :param project_code: The project_code of this GetProjectInfoV4ResultProject.
        :type project_code: str
        """
        self._project_code = project_code

    @property
    def creator(self):
        r"""Gets the creator of this GetProjectInfoV4ResultProject.

        :return: The creator of this GetProjectInfoV4ResultProject.
        :rtype: :class:`huaweicloudsdkprojectman.v4.GetProjectInfoV4ResultProjectCreator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this GetProjectInfoV4ResultProject.

        :param creator: The creator of this GetProjectInfoV4ResultProject.
        :type creator: :class:`huaweicloudsdkprojectman.v4.GetProjectInfoV4ResultProjectCreator`
        """
        self._creator = creator

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
        if not isinstance(other, GetProjectInfoV4ResultProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
