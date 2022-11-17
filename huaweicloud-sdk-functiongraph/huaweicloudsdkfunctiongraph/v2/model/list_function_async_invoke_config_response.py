# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionAsyncInvokeConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'async_invoke_configs': 'list[ListFunctionAsyncInvokeConfigResult]',
        'count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'async_invoke_configs': 'async_invoke_configs',
        'count': 'count',
        'page_info': 'page_info'
    }

    def __init__(self, async_invoke_configs=None, count=None, page_info=None):
        """ListFunctionAsyncInvokeConfigResponse

        The model defined in huaweicloud sdk

        :param async_invoke_configs: 函数异步配置列表。
        :type async_invoke_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigResult`]
        :param count: 列表总数。
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
        """
        
        super(ListFunctionAsyncInvokeConfigResponse, self).__init__()

        self._async_invoke_configs = None
        self._count = None
        self._page_info = None
        self.discriminator = None

        if async_invoke_configs is not None:
            self.async_invoke_configs = async_invoke_configs
        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info

    @property
    def async_invoke_configs(self):
        """Gets the async_invoke_configs of this ListFunctionAsyncInvokeConfigResponse.

        函数异步配置列表。

        :return: The async_invoke_configs of this ListFunctionAsyncInvokeConfigResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigResult`]
        """
        return self._async_invoke_configs

    @async_invoke_configs.setter
    def async_invoke_configs(self, async_invoke_configs):
        """Sets the async_invoke_configs of this ListFunctionAsyncInvokeConfigResponse.

        函数异步配置列表。

        :param async_invoke_configs: The async_invoke_configs of this ListFunctionAsyncInvokeConfigResponse.
        :type async_invoke_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigResult`]
        """
        self._async_invoke_configs = async_invoke_configs

    @property
    def count(self):
        """Gets the count of this ListFunctionAsyncInvokeConfigResponse.

        列表总数。

        :return: The count of this ListFunctionAsyncInvokeConfigResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFunctionAsyncInvokeConfigResponse.

        列表总数。

        :param count: The count of this ListFunctionAsyncInvokeConfigResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        """Gets the page_info of this ListFunctionAsyncInvokeConfigResponse.

        :return: The page_info of this ListFunctionAsyncInvokeConfigResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListFunctionAsyncInvokeConfigResponse.

        :param page_info: The page_info of this ListFunctionAsyncInvokeConfigResponse.
        :type page_info: :class:`huaweicloudsdkfunctiongraph.v2.PageInfo`
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
        if not isinstance(other, ListFunctionAsyncInvokeConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
