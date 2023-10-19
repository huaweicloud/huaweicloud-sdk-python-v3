# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[LakeCatConfiguration]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'configs': 'configs',
        'page_info': 'page_info'
    }

    def __init__(self, configs=None, page_info=None):
        """ListConfigsResponse

        The model defined in huaweicloud sdk

        :param configs: 配置项
        :type configs: list[:class:`huaweicloudsdklakeformation.v1.LakeCatConfiguration`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(ListConfigsResponse, self).__init__()

        self._configs = None
        self._page_info = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        if page_info is not None:
            self.page_info = page_info

    @property
    def configs(self):
        """Gets the configs of this ListConfigsResponse.

        配置项

        :return: The configs of this ListConfigsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.LakeCatConfiguration`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ListConfigsResponse.

        配置项

        :param configs: The configs of this ListConfigsResponse.
        :type configs: list[:class:`huaweicloudsdklakeformation.v1.LakeCatConfiguration`]
        """
        self._configs = configs

    @property
    def page_info(self):
        """Gets the page_info of this ListConfigsResponse.

        :return: The page_info of this ListConfigsResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListConfigsResponse.

        :param page_info: The page_info of this ListConfigsResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
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
        if not isinstance(other, ListConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
