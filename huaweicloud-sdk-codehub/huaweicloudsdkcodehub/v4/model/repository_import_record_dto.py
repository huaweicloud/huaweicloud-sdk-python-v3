# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryImportRecordDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'state': 'str',
        'repository': 'RepositorySimpleDto',
        'origin_full_name': 'str',
        'source_url': 'str',
        'source_type': 'str',
        'created_at': 'str',
        'finished_at': 'str',
        'repository_size': 'float',
        'error_message': 'str',
        'target_full_name': 'str',
        'target_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'repository': 'repository',
        'origin_full_name': 'origin_full_name',
        'source_url': 'source_url',
        'source_type': 'source_type',
        'created_at': 'created_at',
        'finished_at': 'finished_at',
        'repository_size': 'repository_size',
        'error_message': 'error_message',
        'target_full_name': 'target_full_name',
        'target_project_id': 'target_project_id'
    }

    def __init__(self, id=None, state=None, repository=None, origin_full_name=None, source_url=None, source_type=None, created_at=None, finished_at=None, repository_size=None, error_message=None, target_full_name=None, target_project_id=None):
        r"""RepositoryImportRecordDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 主键ID。
        :type id: int
        :param state: **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中 **默认取值：** 不涉及。
        :type state: str
        :param repository: 
        :type repository: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        :param origin_full_name: **参数解释：** 源仓库路径。
        :type origin_full_name: str
        :param source_url: **参数解释：** 源仓库地址。
        :type source_url: str
        :param source_type: **参数解释：** 导入来源。 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup
        :type source_type: str
        :param created_at: **参数解释：** 导入时间。
        :type created_at: str
        :param finished_at: **参数解释：** 导入完成时间。
        :type finished_at: str
        :param repository_size: **参数解释：** 源仓库容量。
        :type repository_size: float
        :param error_message: **参数解释：** 失败原因。
        :type error_message: str
        :param target_full_name: **参数解释：** 仓库路径。
        :type target_full_name: str
        :param target_project_id: **参数解释：** 项目ID。
        :type target_project_id: str
        """
        
        

        self._id = None
        self._state = None
        self._repository = None
        self._origin_full_name = None
        self._source_url = None
        self._source_type = None
        self._created_at = None
        self._finished_at = None
        self._repository_size = None
        self._error_message = None
        self._target_full_name = None
        self._target_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if repository is not None:
            self.repository = repository
        if origin_full_name is not None:
            self.origin_full_name = origin_full_name
        if source_url is not None:
            self.source_url = source_url
        if source_type is not None:
            self.source_type = source_type
        if created_at is not None:
            self.created_at = created_at
        if finished_at is not None:
            self.finished_at = finished_at
        if repository_size is not None:
            self.repository_size = repository_size
        if error_message is not None:
            self.error_message = error_message
        if target_full_name is not None:
            self.target_full_name = target_full_name
        if target_project_id is not None:
            self.target_project_id = target_project_id

    @property
    def id(self):
        r"""Gets the id of this RepositoryImportRecordDto.

        **参数解释：** 主键ID。

        :return: The id of this RepositoryImportRecordDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositoryImportRecordDto.

        **参数解释：** 主键ID。

        :param id: The id of this RepositoryImportRecordDto.
        :type id: int
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this RepositoryImportRecordDto.

        **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中 **默认取值：** 不涉及。

        :return: The state of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this RepositoryImportRecordDto.

        **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中 **默认取值：** 不涉及。

        :param state: The state of this RepositoryImportRecordDto.
        :type state: str
        """
        self._state = state

    @property
    def repository(self):
        r"""Gets the repository of this RepositoryImportRecordDto.

        :return: The repository of this RepositoryImportRecordDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this RepositoryImportRecordDto.

        :param repository: The repository of this RepositoryImportRecordDto.
        :type repository: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        """
        self._repository = repository

    @property
    def origin_full_name(self):
        r"""Gets the origin_full_name of this RepositoryImportRecordDto.

        **参数解释：** 源仓库路径。

        :return: The origin_full_name of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._origin_full_name

    @origin_full_name.setter
    def origin_full_name(self, origin_full_name):
        r"""Sets the origin_full_name of this RepositoryImportRecordDto.

        **参数解释：** 源仓库路径。

        :param origin_full_name: The origin_full_name of this RepositoryImportRecordDto.
        :type origin_full_name: str
        """
        self._origin_full_name = origin_full_name

    @property
    def source_url(self):
        r"""Gets the source_url of this RepositoryImportRecordDto.

        **参数解释：** 源仓库地址。

        :return: The source_url of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this RepositoryImportRecordDto.

        **参数解释：** 源仓库地址。

        :param source_url: The source_url of this RepositoryImportRecordDto.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def source_type(self):
        r"""Gets the source_type of this RepositoryImportRecordDto.

        **参数解释：** 导入来源。 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup

        :return: The source_type of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this RepositoryImportRecordDto.

        **参数解释：** 导入来源。 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup

        :param source_type: The source_type of this RepositoryImportRecordDto.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def created_at(self):
        r"""Gets the created_at of this RepositoryImportRecordDto.

        **参数解释：** 导入时间。

        :return: The created_at of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RepositoryImportRecordDto.

        **参数解释：** 导入时间。

        :param created_at: The created_at of this RepositoryImportRecordDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this RepositoryImportRecordDto.

        **参数解释：** 导入完成时间。

        :return: The finished_at of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this RepositoryImportRecordDto.

        **参数解释：** 导入完成时间。

        :param finished_at: The finished_at of this RepositoryImportRecordDto.
        :type finished_at: str
        """
        self._finished_at = finished_at

    @property
    def repository_size(self):
        r"""Gets the repository_size of this RepositoryImportRecordDto.

        **参数解释：** 源仓库容量。

        :return: The repository_size of this RepositoryImportRecordDto.
        :rtype: float
        """
        return self._repository_size

    @repository_size.setter
    def repository_size(self, repository_size):
        r"""Sets the repository_size of this RepositoryImportRecordDto.

        **参数解释：** 源仓库容量。

        :param repository_size: The repository_size of this RepositoryImportRecordDto.
        :type repository_size: float
        """
        self._repository_size = repository_size

    @property
    def error_message(self):
        r"""Gets the error_message of this RepositoryImportRecordDto.

        **参数解释：** 失败原因。

        :return: The error_message of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this RepositoryImportRecordDto.

        **参数解释：** 失败原因。

        :param error_message: The error_message of this RepositoryImportRecordDto.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def target_full_name(self):
        r"""Gets the target_full_name of this RepositoryImportRecordDto.

        **参数解释：** 仓库路径。

        :return: The target_full_name of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._target_full_name

    @target_full_name.setter
    def target_full_name(self, target_full_name):
        r"""Sets the target_full_name of this RepositoryImportRecordDto.

        **参数解释：** 仓库路径。

        :param target_full_name: The target_full_name of this RepositoryImportRecordDto.
        :type target_full_name: str
        """
        self._target_full_name = target_full_name

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this RepositoryImportRecordDto.

        **参数解释：** 项目ID。

        :return: The target_project_id of this RepositoryImportRecordDto.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this RepositoryImportRecordDto.

        **参数解释：** 项目ID。

        :param target_project_id: The target_project_id of this RepositoryImportRecordDto.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

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
        if not isinstance(other, RepositoryImportRecordDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
