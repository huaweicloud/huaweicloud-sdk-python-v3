# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewSettingParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories_and_modules_enabled': 'bool',
        'review_modules': 'list[str]',
        'secondary_category_enabled': 'bool',
        'review_default_categories': 'list[str]',
        'review_customized_categories': 'list[str]',
        'is_assignee_id_required': 'bool',
        'is_review_categories_required': 'bool',
        'is_review_modules_required': 'bool'
    }

    attribute_map = {
        'categories_and_modules_enabled': 'categories_and_modules_enabled',
        'review_modules': 'review_modules',
        'secondary_category_enabled': 'secondary_category_enabled',
        'review_default_categories': 'review_default_categories',
        'review_customized_categories': 'review_customized_categories',
        'is_assignee_id_required': 'is_assignee_id_required',
        'is_review_categories_required': 'is_review_categories_required',
        'is_review_modules_required': 'is_review_modules_required'
    }

    def __init__(self, categories_and_modules_enabled=None, review_modules=None, secondary_category_enabled=None, review_default_categories=None, review_customized_categories=None, is_assignee_id_required=None, is_review_categories_required=None, is_review_modules_required=None):
        r"""ReviewSettingParamDto

        The model defined in huaweicloud sdk

        :param categories_and_modules_enabled: **参数解释：** 是否启用启用检视意见分类与模块。
        :type categories_and_modules_enabled: bool
        :param review_modules: **参数解释：** 检视意见模块。
        :type review_modules: list[str]
        :param secondary_category_enabled: **参数解释：** 是否启用系统预置检视意见分类。
        :type secondary_category_enabled: bool
        :param review_default_categories: **参数解释：** 检视意见分类(已勾选的分类的key列表)。
        :type review_default_categories: list[str]
        :param review_customized_categories: **参数解释：** 自定义分类列表。
        :type review_customized_categories: list[str]
        :param is_assignee_id_required: **参数解释：** 是否勾选指派给。
        :type is_assignee_id_required: bool
        :param is_review_categories_required: **参数解释：** 是否勾选意见分类。
        :type is_review_categories_required: bool
        :param is_review_modules_required: **参数解释：** 是否勾选意见模块。
        :type is_review_modules_required: bool
        """
        
        

        self._categories_and_modules_enabled = None
        self._review_modules = None
        self._secondary_category_enabled = None
        self._review_default_categories = None
        self._review_customized_categories = None
        self._is_assignee_id_required = None
        self._is_review_categories_required = None
        self._is_review_modules_required = None
        self.discriminator = None

        if categories_and_modules_enabled is not None:
            self.categories_and_modules_enabled = categories_and_modules_enabled
        if review_modules is not None:
            self.review_modules = review_modules
        if secondary_category_enabled is not None:
            self.secondary_category_enabled = secondary_category_enabled
        if review_default_categories is not None:
            self.review_default_categories = review_default_categories
        if review_customized_categories is not None:
            self.review_customized_categories = review_customized_categories
        if is_assignee_id_required is not None:
            self.is_assignee_id_required = is_assignee_id_required
        if is_review_categories_required is not None:
            self.is_review_categories_required = is_review_categories_required
        if is_review_modules_required is not None:
            self.is_review_modules_required = is_review_modules_required

    @property
    def categories_and_modules_enabled(self):
        r"""Gets the categories_and_modules_enabled of this ReviewSettingParamDto.

        **参数解释：** 是否启用启用检视意见分类与模块。

        :return: The categories_and_modules_enabled of this ReviewSettingParamDto.
        :rtype: bool
        """
        return self._categories_and_modules_enabled

    @categories_and_modules_enabled.setter
    def categories_and_modules_enabled(self, categories_and_modules_enabled):
        r"""Sets the categories_and_modules_enabled of this ReviewSettingParamDto.

        **参数解释：** 是否启用启用检视意见分类与模块。

        :param categories_and_modules_enabled: The categories_and_modules_enabled of this ReviewSettingParamDto.
        :type categories_and_modules_enabled: bool
        """
        self._categories_and_modules_enabled = categories_and_modules_enabled

    @property
    def review_modules(self):
        r"""Gets the review_modules of this ReviewSettingParamDto.

        **参数解释：** 检视意见模块。

        :return: The review_modules of this ReviewSettingParamDto.
        :rtype: list[str]
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this ReviewSettingParamDto.

        **参数解释：** 检视意见模块。

        :param review_modules: The review_modules of this ReviewSettingParamDto.
        :type review_modules: list[str]
        """
        self._review_modules = review_modules

    @property
    def secondary_category_enabled(self):
        r"""Gets the secondary_category_enabled of this ReviewSettingParamDto.

        **参数解释：** 是否启用系统预置检视意见分类。

        :return: The secondary_category_enabled of this ReviewSettingParamDto.
        :rtype: bool
        """
        return self._secondary_category_enabled

    @secondary_category_enabled.setter
    def secondary_category_enabled(self, secondary_category_enabled):
        r"""Sets the secondary_category_enabled of this ReviewSettingParamDto.

        **参数解释：** 是否启用系统预置检视意见分类。

        :param secondary_category_enabled: The secondary_category_enabled of this ReviewSettingParamDto.
        :type secondary_category_enabled: bool
        """
        self._secondary_category_enabled = secondary_category_enabled

    @property
    def review_default_categories(self):
        r"""Gets the review_default_categories of this ReviewSettingParamDto.

        **参数解释：** 检视意见分类(已勾选的分类的key列表)。

        :return: The review_default_categories of this ReviewSettingParamDto.
        :rtype: list[str]
        """
        return self._review_default_categories

    @review_default_categories.setter
    def review_default_categories(self, review_default_categories):
        r"""Sets the review_default_categories of this ReviewSettingParamDto.

        **参数解释：** 检视意见分类(已勾选的分类的key列表)。

        :param review_default_categories: The review_default_categories of this ReviewSettingParamDto.
        :type review_default_categories: list[str]
        """
        self._review_default_categories = review_default_categories

    @property
    def review_customized_categories(self):
        r"""Gets the review_customized_categories of this ReviewSettingParamDto.

        **参数解释：** 自定义分类列表。

        :return: The review_customized_categories of this ReviewSettingParamDto.
        :rtype: list[str]
        """
        return self._review_customized_categories

    @review_customized_categories.setter
    def review_customized_categories(self, review_customized_categories):
        r"""Sets the review_customized_categories of this ReviewSettingParamDto.

        **参数解释：** 自定义分类列表。

        :param review_customized_categories: The review_customized_categories of this ReviewSettingParamDto.
        :type review_customized_categories: list[str]
        """
        self._review_customized_categories = review_customized_categories

    @property
    def is_assignee_id_required(self):
        r"""Gets the is_assignee_id_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选指派给。

        :return: The is_assignee_id_required of this ReviewSettingParamDto.
        :rtype: bool
        """
        return self._is_assignee_id_required

    @is_assignee_id_required.setter
    def is_assignee_id_required(self, is_assignee_id_required):
        r"""Sets the is_assignee_id_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选指派给。

        :param is_assignee_id_required: The is_assignee_id_required of this ReviewSettingParamDto.
        :type is_assignee_id_required: bool
        """
        self._is_assignee_id_required = is_assignee_id_required

    @property
    def is_review_categories_required(self):
        r"""Gets the is_review_categories_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选意见分类。

        :return: The is_review_categories_required of this ReviewSettingParamDto.
        :rtype: bool
        """
        return self._is_review_categories_required

    @is_review_categories_required.setter
    def is_review_categories_required(self, is_review_categories_required):
        r"""Sets the is_review_categories_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选意见分类。

        :param is_review_categories_required: The is_review_categories_required of this ReviewSettingParamDto.
        :type is_review_categories_required: bool
        """
        self._is_review_categories_required = is_review_categories_required

    @property
    def is_review_modules_required(self):
        r"""Gets the is_review_modules_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选意见模块。

        :return: The is_review_modules_required of this ReviewSettingParamDto.
        :rtype: bool
        """
        return self._is_review_modules_required

    @is_review_modules_required.setter
    def is_review_modules_required(self, is_review_modules_required):
        r"""Sets the is_review_modules_required of this ReviewSettingParamDto.

        **参数解释：** 是否勾选意见模块。

        :param is_review_modules_required: The is_review_modules_required of this ReviewSettingParamDto.
        :type is_review_modules_required: bool
        """
        self._is_review_modules_required = is_review_modules_required

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
        if not isinstance(other, ReviewSettingParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
