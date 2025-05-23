# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueryAllSearchCriteriasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_criterias': 'list[SearchCriteriasBody]'
    }

    attribute_map = {
        'search_criterias': 'search_criterias'
    }

    def __init__(self, search_criterias=None):
        r"""ListQueryAllSearchCriteriasResponse

        The model defined in huaweicloud sdk

        :param search_criterias: 快速查询
        :type search_criterias: list[:class:`huaweicloudsdklts.v2.SearchCriteriasBody`]
        """
        
        super(ListQueryAllSearchCriteriasResponse, self).__init__()

        self._search_criterias = None
        self.discriminator = None

        if search_criterias is not None:
            self.search_criterias = search_criterias

    @property
    def search_criterias(self):
        r"""Gets the search_criterias of this ListQueryAllSearchCriteriasResponse.

        快速查询

        :return: The search_criterias of this ListQueryAllSearchCriteriasResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.SearchCriteriasBody`]
        """
        return self._search_criterias

    @search_criterias.setter
    def search_criterias(self, search_criterias):
        r"""Sets the search_criterias of this ListQueryAllSearchCriteriasResponse.

        快速查询

        :param search_criterias: The search_criterias of this ListQueryAllSearchCriteriasResponse.
        :type search_criterias: list[:class:`huaweicloudsdklts.v2.SearchCriteriasBody`]
        """
        self._search_criterias = search_criterias

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
        if not isinstance(other, ListQueryAllSearchCriteriasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
