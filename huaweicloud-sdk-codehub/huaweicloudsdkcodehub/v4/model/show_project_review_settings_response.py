# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectReviewSettingsResponse(SdkResponse):

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
        'primary_categories': 'list[CategoryDto]',
        'review_default_categories': 'list[str]',
        'review_customized_categories': 'list[str]',
        'review_modules': 'list[str]',
        'repository_id': 'int',
        'note_required_attributes': 'list[RequiredAttributeDto]',
        'codehub_default_categories': 'list[CategoryDto]',
        'hicode_default_categories': 'list[CategoryDto]'
    }

    attribute_map = {
        'categories_and_modules_enabled': 'categories_and_modules_enabled',
        'secondary_category_enabled': 'secondary_category_enabled',
        'primary_categories': 'primary_categories',
        'review_default_categories': 'review_default_categories',
        'review_customized_categories': 'review_customized_categories',
        'review_modules': 'review_modules',
        'repository_id': 'repository_id',
        'note_required_attributes': 'note_required_attributes',
        'codehub_default_categories': 'codehub_default_categories',
        'hicode_default_categories': 'hicode_default_categories'
    }

    def __init__(self, categories_and_modules_enabled=None, secondary_category_enabled=None, primary_categories=None, review_default_categories=None, review_customized_categories=None, review_modules=None, repository_id=None, note_required_attributes=None, codehub_default_categories=None, hicode_default_categories=None):
        r"""ShowProjectReviewSettingsResponse

        The model defined in huaweicloud sdk

        :param categories_and_modules_enabled: **参数解释：** 是否启用启用检视意见分类与模块。
        :type categories_and_modules_enabled: bool
        :param secondary_category_enabled: **参数解释：** 是否启用系统预置检视意见分类。
        :type secondary_category_enabled: bool
        :param primary_categories: **参数解释：** 检视意见分类(已勾选)。
        :type primary_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        :param review_default_categories: **参数解释：** 检视意见分类的key(已勾选)。
        :type review_default_categories: list[str]
        :param review_customized_categories: **参数解释：** 自定义分类。
        :type review_customized_categories: list[str]
        :param review_modules: **参数解释：** 检视意见模块。
        :type review_modules: list[str]
        :param repository_id: **参数解释：** 仓库id。
        :type repository_id: int
        :param note_required_attributes: **参数解释：** 检视意见必填项。
        :type note_required_attributes: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        :param codehub_default_categories: **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。
        :type codehub_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        :param hicode_default_categories: **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。
        :type hicode_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        
        super(ShowProjectReviewSettingsResponse, self).__init__()

        self._categories_and_modules_enabled = None
        self._secondary_category_enabled = None
        self._primary_categories = None
        self._review_default_categories = None
        self._review_customized_categories = None
        self._review_modules = None
        self._repository_id = None
        self._note_required_attributes = None
        self._codehub_default_categories = None
        self._hicode_default_categories = None
        self.discriminator = None

        if categories_and_modules_enabled is not None:
            self.categories_and_modules_enabled = categories_and_modules_enabled
        if secondary_category_enabled is not None:
            self.secondary_category_enabled = secondary_category_enabled
        if primary_categories is not None:
            self.primary_categories = primary_categories
        if review_default_categories is not None:
            self.review_default_categories = review_default_categories
        if review_customized_categories is not None:
            self.review_customized_categories = review_customized_categories
        if review_modules is not None:
            self.review_modules = review_modules
        if repository_id is not None:
            self.repository_id = repository_id
        if note_required_attributes is not None:
            self.note_required_attributes = note_required_attributes
        if codehub_default_categories is not None:
            self.codehub_default_categories = codehub_default_categories
        if hicode_default_categories is not None:
            self.hicode_default_categories = hicode_default_categories

    @property
    def categories_and_modules_enabled(self):
        r"""Gets the categories_and_modules_enabled of this ShowProjectReviewSettingsResponse.

        **参数解释：** 是否启用启用检视意见分类与模块。

        :return: The categories_and_modules_enabled of this ShowProjectReviewSettingsResponse.
        :rtype: bool
        """
        return self._categories_and_modules_enabled

    @categories_and_modules_enabled.setter
    def categories_and_modules_enabled(self, categories_and_modules_enabled):
        r"""Sets the categories_and_modules_enabled of this ShowProjectReviewSettingsResponse.

        **参数解释：** 是否启用启用检视意见分类与模块。

        :param categories_and_modules_enabled: The categories_and_modules_enabled of this ShowProjectReviewSettingsResponse.
        :type categories_and_modules_enabled: bool
        """
        self._categories_and_modules_enabled = categories_and_modules_enabled

    @property
    def secondary_category_enabled(self):
        r"""Gets the secondary_category_enabled of this ShowProjectReviewSettingsResponse.

        **参数解释：** 是否启用系统预置检视意见分类。

        :return: The secondary_category_enabled of this ShowProjectReviewSettingsResponse.
        :rtype: bool
        """
        return self._secondary_category_enabled

    @secondary_category_enabled.setter
    def secondary_category_enabled(self, secondary_category_enabled):
        r"""Sets the secondary_category_enabled of this ShowProjectReviewSettingsResponse.

        **参数解释：** 是否启用系统预置检视意见分类。

        :param secondary_category_enabled: The secondary_category_enabled of this ShowProjectReviewSettingsResponse.
        :type secondary_category_enabled: bool
        """
        self._secondary_category_enabled = secondary_category_enabled

    @property
    def primary_categories(self):
        r"""Gets the primary_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类(已勾选)。

        :return: The primary_categories of this ShowProjectReviewSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._primary_categories

    @primary_categories.setter
    def primary_categories(self, primary_categories):
        r"""Sets the primary_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类(已勾选)。

        :param primary_categories: The primary_categories of this ShowProjectReviewSettingsResponse.
        :type primary_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        self._primary_categories = primary_categories

    @property
    def review_default_categories(self):
        r"""Gets the review_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类的key(已勾选)。

        :return: The review_default_categories of this ShowProjectReviewSettingsResponse.
        :rtype: list[str]
        """
        return self._review_default_categories

    @review_default_categories.setter
    def review_default_categories(self, review_default_categories):
        r"""Sets the review_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类的key(已勾选)。

        :param review_default_categories: The review_default_categories of this ShowProjectReviewSettingsResponse.
        :type review_default_categories: list[str]
        """
        self._review_default_categories = review_default_categories

    @property
    def review_customized_categories(self):
        r"""Gets the review_customized_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 自定义分类。

        :return: The review_customized_categories of this ShowProjectReviewSettingsResponse.
        :rtype: list[str]
        """
        return self._review_customized_categories

    @review_customized_categories.setter
    def review_customized_categories(self, review_customized_categories):
        r"""Sets the review_customized_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 自定义分类。

        :param review_customized_categories: The review_customized_categories of this ShowProjectReviewSettingsResponse.
        :type review_customized_categories: list[str]
        """
        self._review_customized_categories = review_customized_categories

    @property
    def review_modules(self):
        r"""Gets the review_modules of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见模块。

        :return: The review_modules of this ShowProjectReviewSettingsResponse.
        :rtype: list[str]
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见模块。

        :param review_modules: The review_modules of this ShowProjectReviewSettingsResponse.
        :type review_modules: list[str]
        """
        self._review_modules = review_modules

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowProjectReviewSettingsResponse.

        **参数解释：** 仓库id。

        :return: The repository_id of this ShowProjectReviewSettingsResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowProjectReviewSettingsResponse.

        **参数解释：** 仓库id。

        :param repository_id: The repository_id of this ShowProjectReviewSettingsResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def note_required_attributes(self):
        r"""Gets the note_required_attributes of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见必填项。

        :return: The note_required_attributes of this ShowProjectReviewSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        """
        return self._note_required_attributes

    @note_required_attributes.setter
    def note_required_attributes(self, note_required_attributes):
        r"""Sets the note_required_attributes of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见必填项。

        :param note_required_attributes: The note_required_attributes of this ShowProjectReviewSettingsResponse.
        :type note_required_attributes: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        """
        self._note_required_attributes = note_required_attributes

    @property
    def codehub_default_categories(self):
        r"""Gets the codehub_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。

        :return: The codehub_default_categories of this ShowProjectReviewSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._codehub_default_categories

    @codehub_default_categories.setter
    def codehub_default_categories(self, codehub_default_categories):
        r"""Sets the codehub_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。

        :param codehub_default_categories: The codehub_default_categories of this ShowProjectReviewSettingsResponse.
        :type codehub_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        self._codehub_default_categories = codehub_default_categories

    @property
    def hicode_default_categories(self):
        r"""Gets the hicode_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。

        :return: The hicode_default_categories of this ShowProjectReviewSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._hicode_default_categories

    @hicode_default_categories.setter
    def hicode_default_categories(self, hicode_default_categories):
        r"""Sets the hicode_default_categories of this ShowProjectReviewSettingsResponse.

        **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。

        :param hicode_default_categories: The hicode_default_categories of this ShowProjectReviewSettingsResponse.
        :type hicode_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        self._hicode_default_categories = hicode_default_categories

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
        if not isinstance(other, ShowProjectReviewSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
