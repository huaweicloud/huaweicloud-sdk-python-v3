# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFeatureConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[FeatureConfig]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'configs': 'configs',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, configs=None, page_info=None, request_id=None):
        """ListFeatureConfigsResponse

        The model defined in huaweicloud sdk

        :param configs: 参数解释：特性配置列表。
        :type configs: list[:class:`huaweicloudsdkelb.v3.FeatureConfig`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        :param request_id: 参数解释：请求ID。  注：自动生成 。
        :type request_id: str
        """
        
        super(ListFeatureConfigsResponse, self).__init__()

        self._configs = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def configs(self):
        """Gets the configs of this ListFeatureConfigsResponse.

        参数解释：特性配置列表。

        :return: The configs of this ListFeatureConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.FeatureConfig`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ListFeatureConfigsResponse.

        参数解释：特性配置列表。

        :param configs: The configs of this ListFeatureConfigsResponse.
        :type configs: list[:class:`huaweicloudsdkelb.v3.FeatureConfig`]
        """
        self._configs = configs

    @property
    def page_info(self):
        """Gets the page_info of this ListFeatureConfigsResponse.

        :return: The page_info of this ListFeatureConfigsResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListFeatureConfigsResponse.

        :param page_info: The page_info of this ListFeatureConfigsResponse.
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListFeatureConfigsResponse.

        参数解释：请求ID。  注：自动生成 。

        :return: The request_id of this ListFeatureConfigsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListFeatureConfigsResponse.

        参数解释：请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListFeatureConfigsResponse.
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
        if not isinstance(other, ListFeatureConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
