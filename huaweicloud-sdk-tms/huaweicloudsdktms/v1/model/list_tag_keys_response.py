# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagKeysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keys': 'list[str]',
        'page_info': 'PageInfoTagKeys'
    }

    attribute_map = {
        'keys': 'keys',
        'page_info': 'page_info'
    }

    def __init__(self, keys=None, page_info=None):
        """ListTagKeysResponse

        The model defined in huaweicloud sdk

        :param keys: 标签键列表
        :type keys: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfoTagKeys`
        """
        
        super(ListTagKeysResponse, self).__init__()

        self._keys = None
        self._page_info = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if page_info is not None:
            self.page_info = page_info

    @property
    def keys(self):
        """Gets the keys of this ListTagKeysResponse.

        标签键列表

        :return: The keys of this ListTagKeysResponse.
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ListTagKeysResponse.

        标签键列表

        :param keys: The keys of this ListTagKeysResponse.
        :type keys: list[str]
        """
        self._keys = keys

    @property
    def page_info(self):
        """Gets the page_info of this ListTagKeysResponse.

        :return: The page_info of this ListTagKeysResponse.
        :rtype: :class:`huaweicloudsdktms.v1.PageInfoTagKeys`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListTagKeysResponse.

        :param page_info: The page_info of this ListTagKeysResponse.
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfoTagKeys`
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
        if not isinstance(other, ListTagKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
