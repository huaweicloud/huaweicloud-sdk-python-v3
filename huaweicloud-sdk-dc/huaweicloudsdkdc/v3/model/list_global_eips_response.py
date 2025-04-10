# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalEipsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'global_eips': 'list[ListBindingGeip]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'global_eips': 'global_eips',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, global_eips=None, total_count=None, page_info=None):
        r"""ListGlobalEipsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param global_eips: 全局弹性公网IP
        :type global_eips: list[:class:`huaweicloudsdkdc.v3.ListBindingGeip`]
        :param total_count: 总记录数。
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListGlobalEipsResponse, self).__init__()

        self._request_id = None
        self._global_eips = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if global_eips is not None:
            self.global_eips = global_eips
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListGlobalEipsResponse.

        请求ID

        :return: The request_id of this ListGlobalEipsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListGlobalEipsResponse.

        请求ID

        :param request_id: The request_id of this ListGlobalEipsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def global_eips(self):
        r"""Gets the global_eips of this ListGlobalEipsResponse.

        全局弹性公网IP

        :return: The global_eips of this ListGlobalEipsResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.ListBindingGeip`]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this ListGlobalEipsResponse.

        全局弹性公网IP

        :param global_eips: The global_eips of this ListGlobalEipsResponse.
        :type global_eips: list[:class:`huaweicloudsdkdc.v3.ListBindingGeip`]
        """
        self._global_eips = global_eips

    @property
    def total_count(self):
        r"""Gets the total_count of this ListGlobalEipsResponse.

        总记录数。

        :return: The total_count of this ListGlobalEipsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListGlobalEipsResponse.

        总记录数。

        :param total_count: The total_count of this ListGlobalEipsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGlobalEipsResponse.

        :return: The page_info of this ListGlobalEipsResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGlobalEipsResponse.

        :param page_info: The page_info of this ListGlobalEipsResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
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
        if not isinstance(other, ListGlobalEipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
