# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMergeRequestTemplateResponse(SdkResponse):

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
        'repository_id': 'int',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'template_name': 'str',
        'merge_request_title': 'str',
        'is_default': 'bool',
        'is_wip': 'bool',
        'auto_extract_mr_title': 'int',
        'creator': 'UserBasicDto'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'template_name': 'template_name',
        'merge_request_title': 'merge_request_title',
        'is_default': 'is_default',
        'is_wip': 'is_wip',
        'auto_extract_mr_title': 'auto_extract_mr_title',
        'creator': 'creator'
    }

    def __init__(self, id=None, repository_id=None, description=None, created_at=None, updated_at=None, template_name=None, merge_request_title=None, is_default=None, is_wip=None, auto_extract_mr_title=None, creator=None):
        r"""ShowMergeRequestTemplateResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合并请求模板主键id
        :type id: int
        :param repository_id: **参数解释：** 仓库id
        :type repository_id: int
        :param description: **参数解释：** 描述
        :type description: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param template_name: **参数解释：** 模板名称
        :type template_name: str
        :param merge_request_title: **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）
        :type merge_request_title: str
        :param is_default: **参数解释：** 是否设置为默认模板
        :type is_default: bool
        :param is_wip: **参数解释：** 是否在标题中添加[WIP]
        :type is_wip: bool
        :param auto_extract_mr_title: **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题
        :type auto_extract_mr_title: int
        :param creator: 
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        
        super(ShowMergeRequestTemplateResponse, self).__init__()

        self._id = None
        self._repository_id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._template_name = None
        self._merge_request_title = None
        self._is_default = None
        self._is_wip = None
        self._auto_extract_mr_title = None
        self._creator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if template_name is not None:
            self.template_name = template_name
        if merge_request_title is not None:
            self.merge_request_title = merge_request_title
        if is_default is not None:
            self.is_default = is_default
        if is_wip is not None:
            self.is_wip = is_wip
        if auto_extract_mr_title is not None:
            self.auto_extract_mr_title = auto_extract_mr_title
        if creator is not None:
            self.creator = creator

    @property
    def id(self):
        r"""Gets the id of this ShowMergeRequestTemplateResponse.

        **参数解释：** 合并请求模板主键id

        :return: The id of this ShowMergeRequestTemplateResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowMergeRequestTemplateResponse.

        **参数解释：** 合并请求模板主键id

        :param id: The id of this ShowMergeRequestTemplateResponse.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowMergeRequestTemplateResponse.

        **参数解释：** 仓库id

        :return: The repository_id of this ShowMergeRequestTemplateResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowMergeRequestTemplateResponse.

        **参数解释：** 仓库id

        :param repository_id: The repository_id of this ShowMergeRequestTemplateResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def description(self):
        r"""Gets the description of this ShowMergeRequestTemplateResponse.

        **参数解释：** 描述

        :return: The description of this ShowMergeRequestTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowMergeRequestTemplateResponse.

        **参数解释：** 描述

        :param description: The description of this ShowMergeRequestTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowMergeRequestTemplateResponse.

        **参数解释：** 创建时间。

        :return: The created_at of this ShowMergeRequestTemplateResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowMergeRequestTemplateResponse.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this ShowMergeRequestTemplateResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowMergeRequestTemplateResponse.

        **参数解释：** 更新时间。

        :return: The updated_at of this ShowMergeRequestTemplateResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowMergeRequestTemplateResponse.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this ShowMergeRequestTemplateResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowMergeRequestTemplateResponse.

        **参数解释：** 模板名称

        :return: The template_name of this ShowMergeRequestTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowMergeRequestTemplateResponse.

        **参数解释：** 模板名称

        :param template_name: The template_name of this ShowMergeRequestTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def merge_request_title(self):
        r"""Gets the merge_request_title of this ShowMergeRequestTemplateResponse.

        **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）

        :return: The merge_request_title of this ShowMergeRequestTemplateResponse.
        :rtype: str
        """
        return self._merge_request_title

    @merge_request_title.setter
    def merge_request_title(self, merge_request_title):
        r"""Sets the merge_request_title of this ShowMergeRequestTemplateResponse.

        **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）

        :param merge_request_title: The merge_request_title of this ShowMergeRequestTemplateResponse.
        :type merge_request_title: str
        """
        self._merge_request_title = merge_request_title

    @property
    def is_default(self):
        r"""Gets the is_default of this ShowMergeRequestTemplateResponse.

        **参数解释：** 是否设置为默认模板

        :return: The is_default of this ShowMergeRequestTemplateResponse.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this ShowMergeRequestTemplateResponse.

        **参数解释：** 是否设置为默认模板

        :param is_default: The is_default of this ShowMergeRequestTemplateResponse.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def is_wip(self):
        r"""Gets the is_wip of this ShowMergeRequestTemplateResponse.

        **参数解释：** 是否在标题中添加[WIP]

        :return: The is_wip of this ShowMergeRequestTemplateResponse.
        :rtype: bool
        """
        return self._is_wip

    @is_wip.setter
    def is_wip(self, is_wip):
        r"""Sets the is_wip of this ShowMergeRequestTemplateResponse.

        **参数解释：** 是否在标题中添加[WIP]

        :param is_wip: The is_wip of this ShowMergeRequestTemplateResponse.
        :type is_wip: bool
        """
        self._is_wip = is_wip

    @property
    def auto_extract_mr_title(self):
        r"""Gets the auto_extract_mr_title of this ShowMergeRequestTemplateResponse.

        **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题

        :return: The auto_extract_mr_title of this ShowMergeRequestTemplateResponse.
        :rtype: int
        """
        return self._auto_extract_mr_title

    @auto_extract_mr_title.setter
    def auto_extract_mr_title(self, auto_extract_mr_title):
        r"""Sets the auto_extract_mr_title of this ShowMergeRequestTemplateResponse.

        **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题

        :param auto_extract_mr_title: The auto_extract_mr_title of this ShowMergeRequestTemplateResponse.
        :type auto_extract_mr_title: int
        """
        self._auto_extract_mr_title = auto_extract_mr_title

    @property
    def creator(self):
        r"""Gets the creator of this ShowMergeRequestTemplateResponse.

        :return: The creator of this ShowMergeRequestTemplateResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowMergeRequestTemplateResponse.

        :param creator: The creator of this ShowMergeRequestTemplateResponse.
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
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
        if not isinstance(other, ShowMergeRequestTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
