# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscussionTemplateDto:

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
        'template_name': 'str',
        'description': 'str',
        'assignee_id': 'int',
        'categories': 'str',
        'categories_en': 'str',
        'categories_cn': 'str',
        'modules': 'list[str]',
        'review_severity': 'str',
        'is_default': 'bool',
        'creator_id': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'creator': 'UserBasicDto',
        'assignee': 'UserBasicDto'
    }

    attribute_map = {
        'id': 'id',
        'template_name': 'template_name',
        'description': 'description',
        'assignee_id': 'assignee_id',
        'categories': 'categories',
        'categories_en': 'categories_en',
        'categories_cn': 'categories_cn',
        'modules': 'modules',
        'review_severity': 'review_severity',
        'is_default': 'is_default',
        'creator_id': 'creator_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'creator': 'creator',
        'assignee': 'assignee'
    }

    def __init__(self, id=None, template_name=None, description=None, assignee_id=None, categories=None, categories_en=None, categories_cn=None, modules=None, review_severity=None, is_default=None, creator_id=None, created_at=None, updated_at=None, creator=None, assignee=None):
        r"""DiscussionTemplateDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 检视意见模板主键id。
        :type id: int
        :param template_name: **参数解释：** 模板名称。
        :type template_name: str
        :param description: **参数解释：** 描述。
        :type description: str
        :param assignee_id: **参数解释：** 默认指派人。
        :type assignee_id: int
        :param categories: **参数解释：** 意见分类key。
        :type categories: str
        :param categories_en: **参数解释：** 意见分类英文。
        :type categories_en: str
        :param categories_cn: **参数解释：** 意见分类中文。
        :type categories_cn: str
        :param modules: **参数解释：** 检视意见模块。
        :type modules: list[str]
        :param review_severity: **参数解释：** 严重程度key。
        :type review_severity: str
        :param is_default: **参数解释：** 是否设置为默认模板。
        :type is_default: bool
        :param creator_id: **参数解释：** 模板作者id。
        :type creator_id: int
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        
        

        self._id = None
        self._template_name = None
        self._description = None
        self._assignee_id = None
        self._categories = None
        self._categories_en = None
        self._categories_cn = None
        self._modules = None
        self._review_severity = None
        self._is_default = None
        self._creator_id = None
        self._created_at = None
        self._updated_at = None
        self._creator = None
        self._assignee = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_name is not None:
            self.template_name = template_name
        if description is not None:
            self.description = description
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if categories is not None:
            self.categories = categories
        if categories_en is not None:
            self.categories_en = categories_en
        if categories_cn is not None:
            self.categories_cn = categories_cn
        if modules is not None:
            self.modules = modules
        if review_severity is not None:
            self.review_severity = review_severity
        if is_default is not None:
            self.is_default = is_default
        if creator_id is not None:
            self.creator_id = creator_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if creator is not None:
            self.creator = creator
        if assignee is not None:
            self.assignee = assignee

    @property
    def id(self):
        r"""Gets the id of this DiscussionTemplateDto.

        **参数解释：** 检视意见模板主键id。

        :return: The id of this DiscussionTemplateDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiscussionTemplateDto.

        **参数解释：** 检视意见模板主键id。

        :param id: The id of this DiscussionTemplateDto.
        :type id: int
        """
        self._id = id

    @property
    def template_name(self):
        r"""Gets the template_name of this DiscussionTemplateDto.

        **参数解释：** 模板名称。

        :return: The template_name of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this DiscussionTemplateDto.

        **参数解释：** 模板名称。

        :param template_name: The template_name of this DiscussionTemplateDto.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        r"""Gets the description of this DiscussionTemplateDto.

        **参数解释：** 描述。

        :return: The description of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DiscussionTemplateDto.

        **参数解释：** 描述。

        :param description: The description of this DiscussionTemplateDto.
        :type description: str
        """
        self._description = description

    @property
    def assignee_id(self):
        r"""Gets the assignee_id of this DiscussionTemplateDto.

        **参数解释：** 默认指派人。

        :return: The assignee_id of this DiscussionTemplateDto.
        :rtype: int
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        r"""Sets the assignee_id of this DiscussionTemplateDto.

        **参数解释：** 默认指派人。

        :param assignee_id: The assignee_id of this DiscussionTemplateDto.
        :type assignee_id: int
        """
        self._assignee_id = assignee_id

    @property
    def categories(self):
        r"""Gets the categories of this DiscussionTemplateDto.

        **参数解释：** 意见分类key。

        :return: The categories of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this DiscussionTemplateDto.

        **参数解释：** 意见分类key。

        :param categories: The categories of this DiscussionTemplateDto.
        :type categories: str
        """
        self._categories = categories

    @property
    def categories_en(self):
        r"""Gets the categories_en of this DiscussionTemplateDto.

        **参数解释：** 意见分类英文。

        :return: The categories_en of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._categories_en

    @categories_en.setter
    def categories_en(self, categories_en):
        r"""Sets the categories_en of this DiscussionTemplateDto.

        **参数解释：** 意见分类英文。

        :param categories_en: The categories_en of this DiscussionTemplateDto.
        :type categories_en: str
        """
        self._categories_en = categories_en

    @property
    def categories_cn(self):
        r"""Gets the categories_cn of this DiscussionTemplateDto.

        **参数解释：** 意见分类中文。

        :return: The categories_cn of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._categories_cn

    @categories_cn.setter
    def categories_cn(self, categories_cn):
        r"""Sets the categories_cn of this DiscussionTemplateDto.

        **参数解释：** 意见分类中文。

        :param categories_cn: The categories_cn of this DiscussionTemplateDto.
        :type categories_cn: str
        """
        self._categories_cn = categories_cn

    @property
    def modules(self):
        r"""Gets the modules of this DiscussionTemplateDto.

        **参数解释：** 检视意见模块。

        :return: The modules of this DiscussionTemplateDto.
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this DiscussionTemplateDto.

        **参数解释：** 检视意见模块。

        :param modules: The modules of this DiscussionTemplateDto.
        :type modules: list[str]
        """
        self._modules = modules

    @property
    def review_severity(self):
        r"""Gets the review_severity of this DiscussionTemplateDto.

        **参数解释：** 严重程度key。

        :return: The review_severity of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._review_severity

    @review_severity.setter
    def review_severity(self, review_severity):
        r"""Sets the review_severity of this DiscussionTemplateDto.

        **参数解释：** 严重程度key。

        :param review_severity: The review_severity of this DiscussionTemplateDto.
        :type review_severity: str
        """
        self._review_severity = review_severity

    @property
    def is_default(self):
        r"""Gets the is_default of this DiscussionTemplateDto.

        **参数解释：** 是否设置为默认模板。

        :return: The is_default of this DiscussionTemplateDto.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this DiscussionTemplateDto.

        **参数解释：** 是否设置为默认模板。

        :param is_default: The is_default of this DiscussionTemplateDto.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def creator_id(self):
        r"""Gets the creator_id of this DiscussionTemplateDto.

        **参数解释：** 模板作者id。

        :return: The creator_id of this DiscussionTemplateDto.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this DiscussionTemplateDto.

        **参数解释：** 模板作者id。

        :param creator_id: The creator_id of this DiscussionTemplateDto.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def created_at(self):
        r"""Gets the created_at of this DiscussionTemplateDto.

        **参数解释：** 创建时间。

        :return: The created_at of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DiscussionTemplateDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this DiscussionTemplateDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DiscussionTemplateDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this DiscussionTemplateDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DiscussionTemplateDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this DiscussionTemplateDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def creator(self):
        r"""Gets the creator of this DiscussionTemplateDto.

        :return: The creator of this DiscussionTemplateDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this DiscussionTemplateDto.

        :param creator: The creator of this DiscussionTemplateDto.
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._creator = creator

    @property
    def assignee(self):
        r"""Gets the assignee of this DiscussionTemplateDto.

        :return: The assignee of this DiscussionTemplateDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this DiscussionTemplateDto.

        :param assignee: The assignee of this DiscussionTemplateDto.
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._assignee = assignee

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
        if not isinstance(other, DiscussionTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
