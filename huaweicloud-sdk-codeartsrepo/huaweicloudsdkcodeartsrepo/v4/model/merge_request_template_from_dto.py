# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestTemplateFromDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'type': 'str',
        'repository_id': 'int',
        'group_id': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'path': 'path',
        'type': 'type',
        'repository_id': 'repository_id',
        'group_id': 'group_id',
        'project_id': 'project_id'
    }

    def __init__(self, path=None, type=None, repository_id=None, group_id=None, project_id=None):
        r"""MergeRequestTemplateFromDto

        The model defined in huaweicloud sdk

        :param path: **参数解释：** 设置来源的url链接，点击可跳转到项目、代码组或仓库的和并请求模板设置。
        :type path: str
        :param type: **参数解释：** repository: 设置来自于仓库 group: 设置继承自代码组 project: 设置继承自项目
        :type type: str
        :param repository_id: **参数解释：** 仓库id，不来源于仓库时为null。
        :type repository_id: int
        :param group_id: **参数解释：** 代码组id，不来源于代码组时为null。
        :type group_id: int
        :param project_id: **参数解释：** 项目id，不来源于项目时为null。
        :type project_id: str
        """
        
        

        self._path = None
        self._type = None
        self._repository_id = None
        self._group_id = None
        self._project_id = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if type is not None:
            self.type = type
        if repository_id is not None:
            self.repository_id = repository_id
        if group_id is not None:
            self.group_id = group_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def path(self):
        r"""Gets the path of this MergeRequestTemplateFromDto.

        **参数解释：** 设置来源的url链接，点击可跳转到项目、代码组或仓库的和并请求模板设置。

        :return: The path of this MergeRequestTemplateFromDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this MergeRequestTemplateFromDto.

        **参数解释：** 设置来源的url链接，点击可跳转到项目、代码组或仓库的和并请求模板设置。

        :param path: The path of this MergeRequestTemplateFromDto.
        :type path: str
        """
        self._path = path

    @property
    def type(self):
        r"""Gets the type of this MergeRequestTemplateFromDto.

        **参数解释：** repository: 设置来自于仓库 group: 设置继承自代码组 project: 设置继承自项目

        :return: The type of this MergeRequestTemplateFromDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MergeRequestTemplateFromDto.

        **参数解释：** repository: 设置来自于仓库 group: 设置继承自代码组 project: 设置继承自项目

        :param type: The type of this MergeRequestTemplateFromDto.
        :type type: str
        """
        self._type = type

    @property
    def repository_id(self):
        r"""Gets the repository_id of this MergeRequestTemplateFromDto.

        **参数解释：** 仓库id，不来源于仓库时为null。

        :return: The repository_id of this MergeRequestTemplateFromDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this MergeRequestTemplateFromDto.

        **参数解释：** 仓库id，不来源于仓库时为null。

        :param repository_id: The repository_id of this MergeRequestTemplateFromDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def group_id(self):
        r"""Gets the group_id of this MergeRequestTemplateFromDto.

        **参数解释：** 代码组id，不来源于代码组时为null。

        :return: The group_id of this MergeRequestTemplateFromDto.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this MergeRequestTemplateFromDto.

        **参数解释：** 代码组id，不来源于代码组时为null。

        :param group_id: The group_id of this MergeRequestTemplateFromDto.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def project_id(self):
        r"""Gets the project_id of this MergeRequestTemplateFromDto.

        **参数解释：** 项目id，不来源于项目时为null。

        :return: The project_id of this MergeRequestTemplateFromDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MergeRequestTemplateFromDto.

        **参数解释：** 项目id，不来源于项目时为null。

        :param project_id: The project_id of this MergeRequestTemplateFromDto.
        :type project_id: str
        """
        self._project_id = project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MergeRequestTemplateFromDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
