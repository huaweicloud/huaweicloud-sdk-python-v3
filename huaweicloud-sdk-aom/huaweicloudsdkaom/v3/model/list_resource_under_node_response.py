# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceUnderNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[object]',
        'page_info': 'object'
    }

    attribute_map = {
        'data': 'data',
        'page_info': 'page_info'
    }

    def __init__(self, data=None, page_info=None):
        """ListResourceUnderNodeResponse

        The model defined in huaweicloud sdk

        :param data: 分页查询的数据。
        :type data: list[object]
        :param page_info: 分页信息。
        :type page_info: object
        """
        
        super(ListResourceUnderNodeResponse, self).__init__()

        self._data = None
        self._page_info = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if page_info is not None:
            self.page_info = page_info

    @property
    def data(self):
        """Gets the data of this ListResourceUnderNodeResponse.

        分页查询的数据。

        :return: The data of this ListResourceUnderNodeResponse.
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListResourceUnderNodeResponse.

        分页查询的数据。

        :param data: The data of this ListResourceUnderNodeResponse.
        :type data: list[object]
        """
        self._data = data

    @property
    def page_info(self):
        """Gets the page_info of this ListResourceUnderNodeResponse.

        分页信息。

        :return: The page_info of this ListResourceUnderNodeResponse.
        :rtype: object
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListResourceUnderNodeResponse.

        分页信息。

        :param page_info: The page_info of this ListResourceUnderNodeResponse.
        :type page_info: object
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
        if not isinstance(other, ListResourceUnderNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
