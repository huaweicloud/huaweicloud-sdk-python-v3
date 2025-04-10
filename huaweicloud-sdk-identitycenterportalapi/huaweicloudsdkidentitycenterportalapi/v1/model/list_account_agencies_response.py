# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAgenciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_list': 'list[AgencyInfo]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'agency_list': 'agency_list',
        'page_info': 'page_info'
    }

    def __init__(self, agency_list=None, page_info=None):
        r"""ListAccountAgenciesResponse

        The model defined in huaweicloud sdk

        :param agency_list: 满足查询条件的委托或信任委托对象列表
        :type agency_list: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyInfo`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
        """
        
        super(ListAccountAgenciesResponse, self).__init__()

        self._agency_list = None
        self._page_info = None
        self.discriminator = None

        if agency_list is not None:
            self.agency_list = agency_list
        if page_info is not None:
            self.page_info = page_info

    @property
    def agency_list(self):
        r"""Gets the agency_list of this ListAccountAgenciesResponse.

        满足查询条件的委托或信任委托对象列表

        :return: The agency_list of this ListAccountAgenciesResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyInfo`]
        """
        return self._agency_list

    @agency_list.setter
    def agency_list(self, agency_list):
        r"""Sets the agency_list of this ListAccountAgenciesResponse.

        满足查询条件的委托或信任委托对象列表

        :param agency_list: The agency_list of this ListAccountAgenciesResponse.
        :type agency_list: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyInfo`]
        """
        self._agency_list = agency_list

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAccountAgenciesResponse.

        :return: The page_info of this ListAccountAgenciesResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAccountAgenciesResponse.

        :param page_info: The page_info of this ListAccountAgenciesResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAccountAgenciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
