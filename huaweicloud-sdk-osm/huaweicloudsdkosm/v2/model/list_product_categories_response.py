# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductCategoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'incident_product_category_list': 'list[IncidentProductCategoryV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'incident_product_category_list': 'incident_product_category_list'
    }

    def __init__(self, total_count=None, incident_product_category_list=None):
        """ListProductCategoriesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param incident_product_category_list: 产品类型列表
        :type incident_product_category_list: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        
        super(ListProductCategoriesResponse, self).__init__()

        self._total_count = None
        self._incident_product_category_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if incident_product_category_list is not None:
            self.incident_product_category_list = incident_product_category_list

    @property
    def total_count(self):
        """Gets the total_count of this ListProductCategoriesResponse.

        总数

        :return: The total_count of this ListProductCategoriesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListProductCategoriesResponse.

        总数

        :param total_count: The total_count of this ListProductCategoriesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def incident_product_category_list(self):
        """Gets the incident_product_category_list of this ListProductCategoriesResponse.

        产品类型列表

        :return: The incident_product_category_list of this ListProductCategoriesResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        return self._incident_product_category_list

    @incident_product_category_list.setter
    def incident_product_category_list(self, incident_product_category_list):
        """Sets the incident_product_category_list of this ListProductCategoriesResponse.

        产品类型列表

        :param incident_product_category_list: The incident_product_category_list of this ListProductCategoriesResponse.
        :type incident_product_category_list: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        self._incident_product_category_list = incident_product_category_list

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
        if not isinstance(other, ListProductCategoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
