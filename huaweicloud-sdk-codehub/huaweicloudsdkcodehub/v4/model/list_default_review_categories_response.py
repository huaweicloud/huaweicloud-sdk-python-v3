# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDefaultReviewCategoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'codehub_default_categories': 'list[CategoryDto]',
        'hicode_default_categories': 'list[CategoryDto]'
    }

    attribute_map = {
        'codehub_default_categories': 'codehub_default_categories',
        'hicode_default_categories': 'hicode_default_categories'
    }

    def __init__(self, codehub_default_categories=None, hicode_default_categories=None):
        r"""ListDefaultReviewCategoriesResponse

        The model defined in huaweicloud sdk

        :param codehub_default_categories: **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。
        :type codehub_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        :param hicode_default_categories: **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。
        :type hicode_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        
        super(ListDefaultReviewCategoriesResponse, self).__init__()

        self._codehub_default_categories = None
        self._hicode_default_categories = None
        self.discriminator = None

        if codehub_default_categories is not None:
            self.codehub_default_categories = codehub_default_categories
        if hicode_default_categories is not None:
            self.hicode_default_categories = hicode_default_categories

    @property
    def codehub_default_categories(self):
        r"""Gets the codehub_default_categories of this ListDefaultReviewCategoriesResponse.

        **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。

        :return: The codehub_default_categories of this ListDefaultReviewCategoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._codehub_default_categories

    @codehub_default_categories.setter
    def codehub_default_categories(self, codehub_default_categories):
        r"""Sets the codehub_default_categories of this ListDefaultReviewCategoriesResponse.

        **参数解释：** 检视意见分类(所有可勾选的，需传参with_default_review_categories: true才返回)。

        :param codehub_default_categories: The codehub_default_categories of this ListDefaultReviewCategoriesResponse.
        :type codehub_default_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        self._codehub_default_categories = codehub_default_categories

    @property
    def hicode_default_categories(self):
        r"""Gets the hicode_default_categories of this ListDefaultReviewCategoriesResponse.

        **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。

        :return: The hicode_default_categories of this ListDefaultReviewCategoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._hicode_default_categories

    @hicode_default_categories.setter
    def hicode_default_categories(self, hicode_default_categories):
        r"""Sets the hicode_default_categories of this ListDefaultReviewCategoriesResponse.

        **参数解释：** 系统预置检视意见分类(需传参with_default_review_categories: true才返回)。

        :param hicode_default_categories: The hicode_default_categories of this ListDefaultReviewCategoriesResponse.
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
        if not isinstance(other, ListDefaultReviewCategoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
