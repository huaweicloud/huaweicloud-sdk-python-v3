# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateSnatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snat_rules': 'list[PrivateSnat]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'snat_rules': 'snat_rules',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, snat_rules=None, page_info=None, request_id=None):
        r"""ListPrivateSnatsResponse

        The model defined in huaweicloud sdk

        :param snat_rules: 查询SNAT规则列表的响应体。
        :type snat_rules: list[:class:`huaweicloudsdknat.v2.PrivateSnat`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListPrivateSnatsResponse, self).__init__()

        self._snat_rules = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if snat_rules is not None:
            self.snat_rules = snat_rules
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def snat_rules(self):
        r"""Gets the snat_rules of this ListPrivateSnatsResponse.

        查询SNAT规则列表的响应体。

        :return: The snat_rules of this ListPrivateSnatsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateSnat`]
        """
        return self._snat_rules

    @snat_rules.setter
    def snat_rules(self, snat_rules):
        r"""Sets the snat_rules of this ListPrivateSnatsResponse.

        查询SNAT规则列表的响应体。

        :param snat_rules: The snat_rules of this ListPrivateSnatsResponse.
        :type snat_rules: list[:class:`huaweicloudsdknat.v2.PrivateSnat`]
        """
        self._snat_rules = snat_rules

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPrivateSnatsResponse.

        :return: The page_info of this ListPrivateSnatsResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPrivateSnatsResponse.

        :param page_info: The page_info of this ListPrivateSnatsResponse.
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPrivateSnatsResponse.

        请求ID。

        :return: The request_id of this ListPrivateSnatsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPrivateSnatsResponse.

        请求ID。

        :param request_id: The request_id of this ListPrivateSnatsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListPrivateSnatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
