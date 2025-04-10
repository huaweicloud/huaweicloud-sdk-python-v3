# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForkProjectRepoRequest:

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
        'project_name': 'str',
        'repo_name': 'str',
        'template_id': 'str',
        'type': 'str',
        'visibility_level': 'int',
        'external_project_info': 'ExternalKeyMessage'
    }

    attribute_map = {
        'import_members': 'import_members',
        'project_name': 'project_name',
        'repo_name': 'repo_name',
        'template_id': 'template_id',
        'type': 'type',
        'visibility_level': 'visibility_level',
        'external_project_info': 'external_project_info'
    }

    def __init__(self, import_members=None, project_name=None, repo_name=None, template_id=None, type=None, visibility_level=None, external_project_info=None):
        r"""ForkProjectRepoRequest

        The model defined in huaweicloud sdk

        :param import_members: 是否导入项目成员，取值范围：0-&gt;不导入项目成员，1-&gt;导入项目成员
        :type import_members: int
        :param project_name: 项目名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头
        :type project_name: str
        :param repo_name: 仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头
        :type repo_name: str
        :param template_id: 复制模板的ID
        :type template_id: str
        :param type: 项目类型，scrum
        :type type: str
        :param visibility_level: 仓库可见性：  *私有仓库：仓库仅对仓库成员可见，仓库成员可读写和访问仓库，取值范围为0  *公开仓库：   1.项目内成员只读仓库：仓库对项目内成员公开只读，并项目内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   2.租户内成员只读仓库：仓库对租户内成员公开只读，并租户内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   3.所有访客只读仓库：仓库对所有访客公开只读，并所有访客可在项目下和代码组下的仓库列表中查看和搜索，取值范围为20
        :type visibility_level: int
        :param external_project_info: 
        :type external_project_info: :class:`huaweicloudsdkcodehub.v3.ExternalKeyMessage`
        """
        
        

        self._import_members = None
        self._project_name = None
        self._repo_name = None
        self._template_id = None
        self._type = None
        self._visibility_level = None
        self._external_project_info = None
        self.discriminator = None

        if import_members is not None:
            self.import_members = import_members
        self.project_name = project_name
        self.repo_name = repo_name
        self.template_id = template_id
        if type is not None:
            self.type = type
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if external_project_info is not None:
            self.external_project_info = external_project_info

    @property
    def import_members(self):
        r"""Gets the import_members of this ForkProjectRepoRequest.

        是否导入项目成员，取值范围：0->不导入项目成员，1->导入项目成员

        :return: The import_members of this ForkProjectRepoRequest.
        :rtype: int
        """
        return self._import_members

    @import_members.setter
    def import_members(self, import_members):
        r"""Sets the import_members of this ForkProjectRepoRequest.

        是否导入项目成员，取值范围：0->不导入项目成员，1->导入项目成员

        :param import_members: The import_members of this ForkProjectRepoRequest.
        :type import_members: int
        """
        self._import_members = import_members

    @property
    def project_name(self):
        r"""Gets the project_name of this ForkProjectRepoRequest.

        项目名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :return: The project_name of this ForkProjectRepoRequest.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ForkProjectRepoRequest.

        项目名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :param project_name: The project_name of this ForkProjectRepoRequest.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ForkProjectRepoRequest.

        仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :return: The repo_name of this ForkProjectRepoRequest.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ForkProjectRepoRequest.

        仓库名称，取值范围：可以输入英文大小写字母、数字、连字符、下划线，且必须以字母开头

        :param repo_name: The repo_name of this ForkProjectRepoRequest.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def template_id(self):
        r"""Gets the template_id of this ForkProjectRepoRequest.

        复制模板的ID

        :return: The template_id of this ForkProjectRepoRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ForkProjectRepoRequest.

        复制模板的ID

        :param template_id: The template_id of this ForkProjectRepoRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def type(self):
        r"""Gets the type of this ForkProjectRepoRequest.

        项目类型，scrum

        :return: The type of this ForkProjectRepoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ForkProjectRepoRequest.

        项目类型，scrum

        :param type: The type of this ForkProjectRepoRequest.
        :type type: str
        """
        self._type = type

    @property
    def visibility_level(self):
        r"""Gets the visibility_level of this ForkProjectRepoRequest.

        仓库可见性：  *私有仓库：仓库仅对仓库成员可见，仓库成员可读写和访问仓库，取值范围为0  *公开仓库：   1.项目内成员只读仓库：仓库对项目内成员公开只读，并项目内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   2.租户内成员只读仓库：仓库对租户内成员公开只读，并租户内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   3.所有访客只读仓库：仓库对所有访客公开只读，并所有访客可在项目下和代码组下的仓库列表中查看和搜索，取值范围为20

        :return: The visibility_level of this ForkProjectRepoRequest.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        r"""Sets the visibility_level of this ForkProjectRepoRequest.

        仓库可见性：  *私有仓库：仓库仅对仓库成员可见，仓库成员可读写和访问仓库，取值范围为0  *公开仓库：   1.项目内成员只读仓库：仓库对项目内成员公开只读，并项目内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   2.租户内成员只读仓库：仓库对租户内成员公开只读，并租户内成员可在项目下和代码组下的仓库列表中查看和搜索，取值范围为10   3.所有访客只读仓库：仓库对所有访客公开只读，并所有访客可在项目下和代码组下的仓库列表中查看和搜索，取值范围为20

        :param visibility_level: The visibility_level of this ForkProjectRepoRequest.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def external_project_info(self):
        r"""Gets the external_project_info of this ForkProjectRepoRequest.

        :return: The external_project_info of this ForkProjectRepoRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.ExternalKeyMessage`
        """
        return self._external_project_info

    @external_project_info.setter
    def external_project_info(self, external_project_info):
        r"""Sets the external_project_info of this ForkProjectRepoRequest.

        :param external_project_info: The external_project_info of this ForkProjectRepoRequest.
        :type external_project_info: :class:`huaweicloudsdkcodehub.v3.ExternalKeyMessage`
        """
        self._external_project_info = external_project_info

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
        if not isinstance(other, ForkProjectRepoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
