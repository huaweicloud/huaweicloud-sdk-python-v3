# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewSettingDto:

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
        'secondary_category_enabled': 'bool',
        'forbidden_add_to_issue': 'bool',
        'primary_categories': 'list[CategoryDto]',
        'review_default_categories': 'list[str]',
        'review_customized_categories': 'list[str]',
        'review_modules': 'list[str]',
        'source_id': 'int',
        'source_type': 'str',
        'source_path': 'str',
        'secondary_category_type': 'str',
        'secondary_categories': 'list[CategoryDto]'
    }

    attribute_map = {
        'categories_and_modules_enabled': 'categories_and_modules_enabled',
        'secondary_category_enabled': 'secondary_category_enabled',
        'forbidden_add_to_issue': 'forbidden_add_to_issue',
        'primary_categories': 'primary_categories',
        'review_default_categories': 'review_default_categories',
        'review_customized_categories': 'review_customized_categories',
        'review_modules': 'review_modules',
        'source_id': 'source_id',
        'source_type': 'source_type',
        'source_path': 'source_path',
        'secondary_category_type': 'secondary_category_type',
        'secondary_categories': 'secondary_categories'
    }

    def __init__(self, categories_and_modules_enabled=None, secondary_category_enabled=None, forbidden_add_to_issue=None, primary_categories=None, review_default_categories=None, review_customized_categories=None, review_modules=None, source_id=None, source_type=None, source_path=None, secondary_category_type=None, secondary_categories=None):
        r"""ReviewSettingDto

        The model defined in huaweicloud sdk

        :param categories_and_modules_enabled: 是否开启检视意见分类和模块
        :type categories_and_modules_enabled: bool
        :param secondary_category_enabled: 是否开启二级分类
        :type secondary_category_enabled: bool
        :param forbidden_add_to_issue: 是否禁止关联issue
        :type forbidden_add_to_issue: bool
        :param primary_categories: 一级分类
        :type primary_categories: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        :param review_default_categories: 默认分类
        :type review_default_categories: list[str]
        :param review_customized_categories: 自定义分类
        :type review_customized_categories: list[str]
        :param review_modules: 检视意见模块
        :type review_modules: list[str]
        :param source_id: 目标id
        :type source_id: int
        :param source_type: 目标类型
        :type source_type: str
        :param source_path: 目标路径
        :type source_path: str
        :param secondary_category_type: 二级分类类型
        :type secondary_category_type: str
        :param secondary_categories: 二级分类
        :type secondary_categories: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        """
        
        

        self._categories_and_modules_enabled = None
        self._secondary_category_enabled = None
        self._forbidden_add_to_issue = None
        self._primary_categories = None
        self._review_default_categories = None
        self._review_customized_categories = None
        self._review_modules = None
        self._source_id = None
        self._source_type = None
        self._source_path = None
        self._secondary_category_type = None
        self._secondary_categories = None
        self.discriminator = None

        if categories_and_modules_enabled is not None:
            self.categories_and_modules_enabled = categories_and_modules_enabled
        if secondary_category_enabled is not None:
            self.secondary_category_enabled = secondary_category_enabled
        if forbidden_add_to_issue is not None:
            self.forbidden_add_to_issue = forbidden_add_to_issue
        if primary_categories is not None:
            self.primary_categories = primary_categories
        if review_default_categories is not None:
            self.review_default_categories = review_default_categories
        if review_customized_categories is not None:
            self.review_customized_categories = review_customized_categories
        if review_modules is not None:
            self.review_modules = review_modules
        if source_id is not None:
            self.source_id = source_id
        if source_type is not None:
            self.source_type = source_type
        if source_path is not None:
            self.source_path = source_path
        if secondary_category_type is not None:
            self.secondary_category_type = secondary_category_type
        if secondary_categories is not None:
            self.secondary_categories = secondary_categories

    @property
    def categories_and_modules_enabled(self):
        r"""Gets the categories_and_modules_enabled of this ReviewSettingDto.

        是否开启检视意见分类和模块

        :return: The categories_and_modules_enabled of this ReviewSettingDto.
        :rtype: bool
        """
        return self._categories_and_modules_enabled

    @categories_and_modules_enabled.setter
    def categories_and_modules_enabled(self, categories_and_modules_enabled):
        r"""Sets the categories_and_modules_enabled of this ReviewSettingDto.

        是否开启检视意见分类和模块

        :param categories_and_modules_enabled: The categories_and_modules_enabled of this ReviewSettingDto.
        :type categories_and_modules_enabled: bool
        """
        self._categories_and_modules_enabled = categories_and_modules_enabled

    @property
    def secondary_category_enabled(self):
        r"""Gets the secondary_category_enabled of this ReviewSettingDto.

        是否开启二级分类

        :return: The secondary_category_enabled of this ReviewSettingDto.
        :rtype: bool
        """
        return self._secondary_category_enabled

    @secondary_category_enabled.setter
    def secondary_category_enabled(self, secondary_category_enabled):
        r"""Sets the secondary_category_enabled of this ReviewSettingDto.

        是否开启二级分类

        :param secondary_category_enabled: The secondary_category_enabled of this ReviewSettingDto.
        :type secondary_category_enabled: bool
        """
        self._secondary_category_enabled = secondary_category_enabled

    @property
    def forbidden_add_to_issue(self):
        r"""Gets the forbidden_add_to_issue of this ReviewSettingDto.

        是否禁止关联issue

        :return: The forbidden_add_to_issue of this ReviewSettingDto.
        :rtype: bool
        """
        return self._forbidden_add_to_issue

    @forbidden_add_to_issue.setter
    def forbidden_add_to_issue(self, forbidden_add_to_issue):
        r"""Sets the forbidden_add_to_issue of this ReviewSettingDto.

        是否禁止关联issue

        :param forbidden_add_to_issue: The forbidden_add_to_issue of this ReviewSettingDto.
        :type forbidden_add_to_issue: bool
        """
        self._forbidden_add_to_issue = forbidden_add_to_issue

    @property
    def primary_categories(self):
        r"""Gets the primary_categories of this ReviewSettingDto.

        一级分类

        :return: The primary_categories of this ReviewSettingDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        """
        return self._primary_categories

    @primary_categories.setter
    def primary_categories(self, primary_categories):
        r"""Sets the primary_categories of this ReviewSettingDto.

        一级分类

        :param primary_categories: The primary_categories of this ReviewSettingDto.
        :type primary_categories: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        """
        self._primary_categories = primary_categories

    @property
    def review_default_categories(self):
        r"""Gets the review_default_categories of this ReviewSettingDto.

        默认分类

        :return: The review_default_categories of this ReviewSettingDto.
        :rtype: list[str]
        """
        return self._review_default_categories

    @review_default_categories.setter
    def review_default_categories(self, review_default_categories):
        r"""Sets the review_default_categories of this ReviewSettingDto.

        默认分类

        :param review_default_categories: The review_default_categories of this ReviewSettingDto.
        :type review_default_categories: list[str]
        """
        self._review_default_categories = review_default_categories

    @property
    def review_customized_categories(self):
        r"""Gets the review_customized_categories of this ReviewSettingDto.

        自定义分类

        :return: The review_customized_categories of this ReviewSettingDto.
        :rtype: list[str]
        """
        return self._review_customized_categories

    @review_customized_categories.setter
    def review_customized_categories(self, review_customized_categories):
        r"""Sets the review_customized_categories of this ReviewSettingDto.

        自定义分类

        :param review_customized_categories: The review_customized_categories of this ReviewSettingDto.
        :type review_customized_categories: list[str]
        """
        self._review_customized_categories = review_customized_categories

    @property
    def review_modules(self):
        r"""Gets the review_modules of this ReviewSettingDto.

        检视意见模块

        :return: The review_modules of this ReviewSettingDto.
        :rtype: list[str]
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this ReviewSettingDto.

        检视意见模块

        :param review_modules: The review_modules of this ReviewSettingDto.
        :type review_modules: list[str]
        """
        self._review_modules = review_modules

    @property
    def source_id(self):
        r"""Gets the source_id of this ReviewSettingDto.

        目标id

        :return: The source_id of this ReviewSettingDto.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ReviewSettingDto.

        目标id

        :param source_id: The source_id of this ReviewSettingDto.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def source_type(self):
        r"""Gets the source_type of this ReviewSettingDto.

        目标类型

        :return: The source_type of this ReviewSettingDto.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ReviewSettingDto.

        目标类型

        :param source_type: The source_type of this ReviewSettingDto.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_path(self):
        r"""Gets the source_path of this ReviewSettingDto.

        目标路径

        :return: The source_path of this ReviewSettingDto.
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        r"""Sets the source_path of this ReviewSettingDto.

        目标路径

        :param source_path: The source_path of this ReviewSettingDto.
        :type source_path: str
        """
        self._source_path = source_path

    @property
    def secondary_category_type(self):
        r"""Gets the secondary_category_type of this ReviewSettingDto.

        二级分类类型

        :return: The secondary_category_type of this ReviewSettingDto.
        :rtype: str
        """
        return self._secondary_category_type

    @secondary_category_type.setter
    def secondary_category_type(self, secondary_category_type):
        r"""Sets the secondary_category_type of this ReviewSettingDto.

        二级分类类型

        :param secondary_category_type: The secondary_category_type of this ReviewSettingDto.
        :type secondary_category_type: str
        """
        self._secondary_category_type = secondary_category_type

    @property
    def secondary_categories(self):
        r"""Gets the secondary_categories of this ReviewSettingDto.

        二级分类

        :return: The secondary_categories of this ReviewSettingDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        """
        return self._secondary_categories

    @secondary_categories.setter
    def secondary_categories(self, secondary_categories):
        r"""Sets the secondary_categories of this ReviewSettingDto.

        二级分类

        :param secondary_categories: The secondary_categories of this ReviewSettingDto.
        :type secondary_categories: list[:class:`huaweicloudsdkcodehub.v3.CategoryDto`]
        """
        self._secondary_categories = secondary_categories

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
        if not isinstance(other, ReviewSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
