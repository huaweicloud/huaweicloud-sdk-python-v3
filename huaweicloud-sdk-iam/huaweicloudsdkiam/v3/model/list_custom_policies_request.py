# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, page=None, per_page=None):
        """ListCustomPoliciesRequest

        The model defined in huaweicloud sdk

        :param page: 分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。
        :type page: int
        :param per_page: 分页查询时每页的数据个数，取值范围为[1,300]。需要与page同时存在。
        :type per_page: int
        """
        
        

        self._page = None
        self._per_page = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def page(self):
        """Gets the page of this ListCustomPoliciesRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。

        :return: The page of this ListCustomPoliciesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCustomPoliciesRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。

        :param page: The page of this ListCustomPoliciesRequest.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this ListCustomPoliciesRequest.

        分页查询时每页的数据个数，取值范围为[1,300]。需要与page同时存在。

        :return: The per_page of this ListCustomPoliciesRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListCustomPoliciesRequest.

        分页查询时每页的数据个数，取值范围为[1,300]。需要与page同时存在。

        :param per_page: The per_page of this ListCustomPoliciesRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ListCustomPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
