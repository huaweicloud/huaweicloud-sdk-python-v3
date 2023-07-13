# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateDnatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dnat_rules': 'list[PrivateDnat]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'dnat_rules': 'dnat_rules',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, dnat_rules=None, request_id=None, page_info=None):
        """ListPrivateDnatsResponse

        The model defined in huaweicloud sdk

        :param dnat_rules: 查询DNAT规则列表的响应体。
        :type dnat_rules: list[:class:`huaweicloudsdknat.v2.PrivateDnat`]
        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        
        super(ListPrivateDnatsResponse, self).__init__()

        self._dnat_rules = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if dnat_rules is not None:
            self.dnat_rules = dnat_rules
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def dnat_rules(self):
        """Gets the dnat_rules of this ListPrivateDnatsResponse.

        查询DNAT规则列表的响应体。

        :return: The dnat_rules of this ListPrivateDnatsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateDnat`]
        """
        return self._dnat_rules

    @dnat_rules.setter
    def dnat_rules(self, dnat_rules):
        """Sets the dnat_rules of this ListPrivateDnatsResponse.

        查询DNAT规则列表的响应体。

        :param dnat_rules: The dnat_rules of this ListPrivateDnatsResponse.
        :type dnat_rules: list[:class:`huaweicloudsdknat.v2.PrivateDnat`]
        """
        self._dnat_rules = dnat_rules

    @property
    def request_id(self):
        """Gets the request_id of this ListPrivateDnatsResponse.

        请求ID。

        :return: The request_id of this ListPrivateDnatsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListPrivateDnatsResponse.

        请求ID。

        :param request_id: The request_id of this ListPrivateDnatsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListPrivateDnatsResponse.

        :return: The page_info of this ListPrivateDnatsResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPrivateDnatsResponse.

        :param page_info: The page_info of this ListPrivateDnatsResponse.
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
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
        if not isinstance(other, ListPrivateDnatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
