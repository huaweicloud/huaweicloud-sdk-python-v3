# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7RulesResponse(SdkResponse):

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
        'page_info': 'PageInfo',
        'rules': 'list[L7Rule]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'rules': 'rules'
    }

    def __init__(self, request_id=None, page_info=None, rules=None):
        """ListL7RulesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        :param rules: 规则对象列表。
        :type rules: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        
        super(ListL7RulesResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._rules = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        if rules is not None:
            self.rules = rules

    @property
    def request_id(self):
        """Gets the request_id of this ListL7RulesResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListL7RulesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListL7RulesResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListL7RulesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListL7RulesResponse.

        :return: The page_info of this ListL7RulesResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListL7RulesResponse.

        :param page_info: The page_info of this ListL7RulesResponse.
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def rules(self):
        """Gets the rules of this ListL7RulesResponse.

        规则对象列表。

        :return: The rules of this ListL7RulesResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ListL7RulesResponse.

        规则对象列表。

        :param rules: The rules of this ListL7RulesResponse.
        :type rules: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        self._rules = rules

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
        if not isinstance(other, ListL7RulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
