# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComponentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'components': 'list[ComponentView]'
    }

    attribute_map = {
        'count': 'count',
        'components': 'components'
    }

    def __init__(self, count=None, components=None):
        """ListComponentsResponse

        The model defined in huaweicloud sdk

        :param count: 组件个数。
        :type count: int
        :param components: 组件列表。
        :type components: list[:class:`huaweicloudsdkservicestage.v2.ComponentView`]
        """
        
        super(ListComponentsResponse, self).__init__()

        self._count = None
        self._components = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if components is not None:
            self.components = components

    @property
    def count(self):
        """Gets the count of this ListComponentsResponse.

        组件个数。

        :return: The count of this ListComponentsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListComponentsResponse.

        组件个数。

        :param count: The count of this ListComponentsResponse.
        :type count: int
        """
        self._count = count

    @property
    def components(self):
        """Gets the components of this ListComponentsResponse.

        组件列表。

        :return: The components of this ListComponentsResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ComponentView`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ListComponentsResponse.

        组件列表。

        :param components: The components of this ListComponentsResponse.
        :type components: list[:class:`huaweicloudsdkservicestage.v2.ComponentView`]
        """
        self._components = components

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
        if not isinstance(other, ListComponentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
