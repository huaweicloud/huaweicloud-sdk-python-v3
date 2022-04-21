# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'import_members': 'int',
        'name': 'str',
        'project_uuid': 'str',
        'template_id': 'str',
        'visibility_level': 'int',
        'import_url': 'str',
        'description': 'str',
        'gitignore_id': 'str',
        'license_id': 'int',
        'enable_readme': 'int',
        'caller': 'str'
    }

    attribute_map = {
        'import_members': 'import_members',
        'name': 'name',
        'project_uuid': 'project_uuid',
        'template_id': 'template_id',
        'visibility_level': 'visibility_level',
        'import_url': 'import_url',
        'description': 'description',
        'gitignore_id': 'gitignore_id',
        'license_id': 'license_id',
        'enable_readme': 'enable_readme',
        'caller': 'caller'
    }

    def __init__(self, import_members=None, name=None, project_uuid=None, template_id=None, visibility_level=None, import_url=None, description=None, gitignore_id=None, license_id=None, enable_readme=None, caller=None):
        """CreateRepoRequest

        The model defined in huaweicloud sdk

        :param import_members: 是否导入项目成员，取值范围：0-&gt;不导入项目成员，1-&gt;导入项目成员
        :type import_members: int
        :param name: 仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头
        :type name: str
        :param project_uuid: 指定项目的UUID
        :type project_uuid: str
        :param template_id: 复制模板的ID
        :type template_id: str
        :param visibility_level: 仓库状态，取值范围：0-&gt;私有，20-&gt;公开只读
        :type visibility_level: int
        :param import_url: 模板仓库的https地址的base64加密
        :type import_url: str
        :param description: 仓库描述信息
        :type description: str
        :param gitignore_id: 根据编程语言生成.gitignore文件
        :type gitignore_id: str
        :param license_id: 许可证id
        :type license_id: int
        :param enable_readme: 是否允许生成README文件
        :type enable_readme: int
        :param caller: 调用者
        :type caller: str
        """
        
        

        self._import_members = None
        self._name = None
        self._project_uuid = None
        self._template_id = None
        self._visibility_level = None
        self._import_url = None
        self._description = None
        self._gitignore_id = None
        self._license_id = None
        self._enable_readme = None
        self._caller = None
        self.discriminator = None

        if import_members is not None:
            self.import_members = import_members
        self.name = name
        self.project_uuid = project_uuid
        if template_id is not None:
            self.template_id = template_id
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if import_url is not None:
            self.import_url = import_url
        if description is not None:
            self.description = description
        if gitignore_id is not None:
            self.gitignore_id = gitignore_id
        if license_id is not None:
            self.license_id = license_id
        if enable_readme is not None:
            self.enable_readme = enable_readme
        if caller is not None:
            self.caller = caller

    @property
    def import_members(self):
        """Gets the import_members of this CreateRepoRequest.

        是否导入项目成员，取值范围：0->不导入项目成员，1->导入项目成员

        :return: The import_members of this CreateRepoRequest.
        :rtype: int
        """
        return self._import_members

    @import_members.setter
    def import_members(self, import_members):
        """Sets the import_members of this CreateRepoRequest.

        是否导入项目成员，取值范围：0->不导入项目成员，1->导入项目成员

        :param import_members: The import_members of this CreateRepoRequest.
        :type import_members: int
        """
        self._import_members = import_members

    @property
    def name(self):
        """Gets the name of this CreateRepoRequest.

        仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :return: The name of this CreateRepoRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRepoRequest.

        仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :param name: The name of this CreateRepoRequest.
        :type name: str
        """
        self._name = name

    @property
    def project_uuid(self):
        """Gets the project_uuid of this CreateRepoRequest.

        指定项目的UUID

        :return: The project_uuid of this CreateRepoRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this CreateRepoRequest.

        指定项目的UUID

        :param project_uuid: The project_uuid of this CreateRepoRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def template_id(self):
        """Gets the template_id of this CreateRepoRequest.

        复制模板的ID

        :return: The template_id of this CreateRepoRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateRepoRequest.

        复制模板的ID

        :param template_id: The template_id of this CreateRepoRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def visibility_level(self):
        """Gets the visibility_level of this CreateRepoRequest.

        仓库状态，取值范围：0->私有，20->公开只读

        :return: The visibility_level of this CreateRepoRequest.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        """Sets the visibility_level of this CreateRepoRequest.

        仓库状态，取值范围：0->私有，20->公开只读

        :param visibility_level: The visibility_level of this CreateRepoRequest.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def import_url(self):
        """Gets the import_url of this CreateRepoRequest.

        模板仓库的https地址的base64加密

        :return: The import_url of this CreateRepoRequest.
        :rtype: str
        """
        return self._import_url

    @import_url.setter
    def import_url(self, import_url):
        """Sets the import_url of this CreateRepoRequest.

        模板仓库的https地址的base64加密

        :param import_url: The import_url of this CreateRepoRequest.
        :type import_url: str
        """
        self._import_url = import_url

    @property
    def description(self):
        """Gets the description of this CreateRepoRequest.

        仓库描述信息

        :return: The description of this CreateRepoRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRepoRequest.

        仓库描述信息

        :param description: The description of this CreateRepoRequest.
        :type description: str
        """
        self._description = description

    @property
    def gitignore_id(self):
        """Gets the gitignore_id of this CreateRepoRequest.

        根据编程语言生成.gitignore文件

        :return: The gitignore_id of this CreateRepoRequest.
        :rtype: str
        """
        return self._gitignore_id

    @gitignore_id.setter
    def gitignore_id(self, gitignore_id):
        """Sets the gitignore_id of this CreateRepoRequest.

        根据编程语言生成.gitignore文件

        :param gitignore_id: The gitignore_id of this CreateRepoRequest.
        :type gitignore_id: str
        """
        self._gitignore_id = gitignore_id

    @property
    def license_id(self):
        """Gets the license_id of this CreateRepoRequest.

        许可证id

        :return: The license_id of this CreateRepoRequest.
        :rtype: int
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this CreateRepoRequest.

        许可证id

        :param license_id: The license_id of this CreateRepoRequest.
        :type license_id: int
        """
        self._license_id = license_id

    @property
    def enable_readme(self):
        """Gets the enable_readme of this CreateRepoRequest.

        是否允许生成README文件

        :return: The enable_readme of this CreateRepoRequest.
        :rtype: int
        """
        return self._enable_readme

    @enable_readme.setter
    def enable_readme(self, enable_readme):
        """Sets the enable_readme of this CreateRepoRequest.

        是否允许生成README文件

        :param enable_readme: The enable_readme of this CreateRepoRequest.
        :type enable_readme: int
        """
        self._enable_readme = enable_readme

    @property
    def caller(self):
        """Gets the caller of this CreateRepoRequest.

        调用者

        :return: The caller of this CreateRepoRequest.
        :rtype: str
        """
        return self._caller

    @caller.setter
    def caller(self, caller):
        """Sets the caller of this CreateRepoRequest.

        调用者

        :param caller: The caller of this CreateRepoRequest.
        :type caller: str
        """
        self._caller = caller

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
        if not isinstance(other, CreateRepoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
