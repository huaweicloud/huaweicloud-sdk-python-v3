# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCategoriesTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories': 'list[CategoryInfo]'
    }

    attribute_map = {
        'categories': 'categories'
    }

    def __init__(self, categories=None):
        r"""ListCategoriesTreeResponse

        The model defined in huaweicloud sdk

        :param categories: 目录树信息。
        :type categories: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
        """
        
        super(ListCategoriesTreeResponse, self).__init__()

        self._categories = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories

    @property
    def categories(self):
        r"""Gets the categories of this ListCategoriesTreeResponse.

        目录树信息。

        :return: The categories of this ListCategoriesTreeResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ListCategoriesTreeResponse.

        目录树信息。

        :param categories: The categories of this ListCategoriesTreeResponse.
        :type categories: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
        """
        self._categories = categories

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
        if not isinstance(other, ListCategoriesTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
