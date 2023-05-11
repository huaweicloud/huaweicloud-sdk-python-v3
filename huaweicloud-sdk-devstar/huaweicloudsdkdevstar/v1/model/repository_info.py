# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'gitignore': 'str',
        'member_permission': 'int',
        'readme_permission': 'int',
        'visibility_level': 'int',
        'license_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'gitignore': 'gitignore',
        'member_permission': 'member_permission',
        'readme_permission': 'readme_permission',
        'visibility_level': 'visibility_level',
        'license_id': 'license_id'
    }

    def __init__(self, name=None, description=None, project_id=None, region_id=None, gitignore=None, member_permission=None, readme_permission=None, visibility_level=None, license_id=None):
        """RepositoryInfo

        The model defined in huaweicloud sdk

        :param name: 代码仓的名称。
        :type name: str
        :param description: 代码仓描述。
        :type description: str
        :param project_id: 项目id。
        :type project_id: str
        :param region_id: 区域id。
        :type region_id: str
        :param gitignore: 根据编程语言生成gitignore文件。
        :type gitignore: str
        :param member_permission: 是否允许项目内成员访问仓库： - 0：不允许 - 1：允许 
        :type member_permission: int
        :param readme_permission: 是否允许生成README文件： - 0：不允许 - 1：允许 
        :type readme_permission: int
        :param visibility_level: 是否公开： - 0：私有 - 20：公开只读 
        :type visibility_level: int
        :param license_id:  开源许可证id （0:默认）。
        :type license_id: int
        """
        
        

        self._name = None
        self._description = None
        self._project_id = None
        self._region_id = None
        self._gitignore = None
        self._member_permission = None
        self._readme_permission = None
        self._visibility_level = None
        self._license_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if gitignore is not None:
            self.gitignore = gitignore
        if member_permission is not None:
            self.member_permission = member_permission
        if readme_permission is not None:
            self.readme_permission = readme_permission
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if license_id is not None:
            self.license_id = license_id

    @property
    def name(self):
        """Gets the name of this RepositoryInfo.

        代码仓的名称。

        :return: The name of this RepositoryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryInfo.

        代码仓的名称。

        :param name: The name of this RepositoryInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this RepositoryInfo.

        代码仓描述。

        :return: The description of this RepositoryInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepositoryInfo.

        代码仓描述。

        :param description: The description of this RepositoryInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this RepositoryInfo.

        项目id。

        :return: The project_id of this RepositoryInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepositoryInfo.

        项目id。

        :param project_id: The project_id of this RepositoryInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this RepositoryInfo.

        区域id。

        :return: The region_id of this RepositoryInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this RepositoryInfo.

        区域id。

        :param region_id: The region_id of this RepositoryInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def gitignore(self):
        """Gets the gitignore of this RepositoryInfo.

        根据编程语言生成gitignore文件。

        :return: The gitignore of this RepositoryInfo.
        :rtype: str
        """
        return self._gitignore

    @gitignore.setter
    def gitignore(self, gitignore):
        """Sets the gitignore of this RepositoryInfo.

        根据编程语言生成gitignore文件。

        :param gitignore: The gitignore of this RepositoryInfo.
        :type gitignore: str
        """
        self._gitignore = gitignore

    @property
    def member_permission(self):
        """Gets the member_permission of this RepositoryInfo.

        是否允许项目内成员访问仓库： - 0：不允许 - 1：允许 

        :return: The member_permission of this RepositoryInfo.
        :rtype: int
        """
        return self._member_permission

    @member_permission.setter
    def member_permission(self, member_permission):
        """Sets the member_permission of this RepositoryInfo.

        是否允许项目内成员访问仓库： - 0：不允许 - 1：允许 

        :param member_permission: The member_permission of this RepositoryInfo.
        :type member_permission: int
        """
        self._member_permission = member_permission

    @property
    def readme_permission(self):
        """Gets the readme_permission of this RepositoryInfo.

        是否允许生成README文件： - 0：不允许 - 1：允许 

        :return: The readme_permission of this RepositoryInfo.
        :rtype: int
        """
        return self._readme_permission

    @readme_permission.setter
    def readme_permission(self, readme_permission):
        """Sets the readme_permission of this RepositoryInfo.

        是否允许生成README文件： - 0：不允许 - 1：允许 

        :param readme_permission: The readme_permission of this RepositoryInfo.
        :type readme_permission: int
        """
        self._readme_permission = readme_permission

    @property
    def visibility_level(self):
        """Gets the visibility_level of this RepositoryInfo.

        是否公开： - 0：私有 - 20：公开只读 

        :return: The visibility_level of this RepositoryInfo.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        """Sets the visibility_level of this RepositoryInfo.

        是否公开： - 0：私有 - 20：公开只读 

        :param visibility_level: The visibility_level of this RepositoryInfo.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def license_id(self):
        """Gets the license_id of this RepositoryInfo.

         开源许可证id （0:默认）。

        :return: The license_id of this RepositoryInfo.
        :rtype: int
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this RepositoryInfo.

         开源许可证id （0:默认）。

        :param license_id: The license_id of this RepositoryInfo.
        :type license_id: int
        """
        self._license_id = license_id

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
        if not isinstance(other, RepositoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
