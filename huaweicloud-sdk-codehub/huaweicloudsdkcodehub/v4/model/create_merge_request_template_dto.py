# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMergeRequestTemplateDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'merge_request_title': 'str',
        'description': 'str',
        'auto_extract_mr_title': 'int',
        'is_wip': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'template_name': 'template_name',
        'merge_request_title': 'merge_request_title',
        'description': 'description',
        'auto_extract_mr_title': 'auto_extract_mr_title',
        'is_wip': 'is_wip',
        'is_default': 'is_default'
    }

    def __init__(self, template_name=None, merge_request_title=None, description=None, auto_extract_mr_title=None, is_wip=None, is_default=None):
        r"""CreateMergeRequestTemplateDto

        The model defined in huaweicloud sdk

        :param template_name: **参数解释：** 模板名称
        :type template_name: str
        :param merge_request_title: **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）
        :type merge_request_title: str
        :param description: **参数解释：** 描述
        :type description: str
        :param auto_extract_mr_title: **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题
        :type auto_extract_mr_title: int
        :param is_wip: **参数解释：** 是否在标题中添加[WIP]
        :type is_wip: bool
        :param is_default: **参数解释：** 是否设置为默认模板
        :type is_default: bool
        """
        
        

        self._template_name = None
        self._merge_request_title = None
        self._description = None
        self._auto_extract_mr_title = None
        self._is_wip = None
        self._is_default = None
        self.discriminator = None

        self.template_name = template_name
        if merge_request_title is not None:
            self.merge_request_title = merge_request_title
        if description is not None:
            self.description = description
        if auto_extract_mr_title is not None:
            self.auto_extract_mr_title = auto_extract_mr_title
        if is_wip is not None:
            self.is_wip = is_wip
        if is_default is not None:
            self.is_default = is_default

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateMergeRequestTemplateDto.

        **参数解释：** 模板名称

        :return: The template_name of this CreateMergeRequestTemplateDto.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateMergeRequestTemplateDto.

        **参数解释：** 模板名称

        :param template_name: The template_name of this CreateMergeRequestTemplateDto.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def merge_request_title(self):
        r"""Gets the merge_request_title of this CreateMergeRequestTemplateDto.

        **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）

        :return: The merge_request_title of this CreateMergeRequestTemplateDto.
        :rtype: str
        """
        return self._merge_request_title

    @merge_request_title.setter
    def merge_request_title(self, merge_request_title):
        r"""Sets the merge_request_title of this CreateMergeRequestTemplateDto.

        **参数解释：** 合并请求标题（不自动提取合并请求标题时生效）

        :param merge_request_title: The merge_request_title of this CreateMergeRequestTemplateDto.
        :type merge_request_title: str
        """
        self._merge_request_title = merge_request_title

    @property
    def description(self):
        r"""Gets the description of this CreateMergeRequestTemplateDto.

        **参数解释：** 描述

        :return: The description of this CreateMergeRequestTemplateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateMergeRequestTemplateDto.

        **参数解释：** 描述

        :param description: The description of this CreateMergeRequestTemplateDto.
        :type description: str
        """
        self._description = description

    @property
    def auto_extract_mr_title(self):
        r"""Gets the auto_extract_mr_title of this CreateMergeRequestTemplateDto.

        **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题

        :return: The auto_extract_mr_title of this CreateMergeRequestTemplateDto.
        :rtype: int
        """
        return self._auto_extract_mr_title

    @auto_extract_mr_title.setter
    def auto_extract_mr_title(self, auto_extract_mr_title):
        r"""Sets the auto_extract_mr_title of this CreateMergeRequestTemplateDto.

        **参数解释：** 自动提取合并请求标题 0：不提取 1：提取提交信息 2：提取e2e单标题

        :param auto_extract_mr_title: The auto_extract_mr_title of this CreateMergeRequestTemplateDto.
        :type auto_extract_mr_title: int
        """
        self._auto_extract_mr_title = auto_extract_mr_title

    @property
    def is_wip(self):
        r"""Gets the is_wip of this CreateMergeRequestTemplateDto.

        **参数解释：** 是否在标题中添加[WIP]

        :return: The is_wip of this CreateMergeRequestTemplateDto.
        :rtype: bool
        """
        return self._is_wip

    @is_wip.setter
    def is_wip(self, is_wip):
        r"""Sets the is_wip of this CreateMergeRequestTemplateDto.

        **参数解释：** 是否在标题中添加[WIP]

        :param is_wip: The is_wip of this CreateMergeRequestTemplateDto.
        :type is_wip: bool
        """
        self._is_wip = is_wip

    @property
    def is_default(self):
        r"""Gets the is_default of this CreateMergeRequestTemplateDto.

        **参数解释：** 是否设置为默认模板

        :return: The is_default of this CreateMergeRequestTemplateDto.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this CreateMergeRequestTemplateDto.

        **参数解释：** 是否设置为默认模板

        :param is_default: The is_default of this CreateMergeRequestTemplateDto.
        :type is_default: bool
        """
        self._is_default = is_default

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
        if not isinstance(other, CreateMergeRequestTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
