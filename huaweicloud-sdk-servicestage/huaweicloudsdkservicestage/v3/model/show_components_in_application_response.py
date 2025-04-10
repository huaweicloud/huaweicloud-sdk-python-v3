# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentsInApplicationResponse(SdkResponse):

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
        'components': 'list[ComponentList]'
    }

    attribute_map = {
        'count': 'count',
        'components': 'components'
    }

    def __init__(self, count=None, components=None):
        r"""ShowComponentsInApplicationResponse

        The model defined in huaweicloud sdk

        :param count: 组件数量
        :type count: int
        :param components: 
        :type components: list[:class:`huaweicloudsdkservicestage.v3.ComponentList`]
        """
        
        super(ShowComponentsInApplicationResponse, self).__init__()

        self._count = None
        self._components = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if components is not None:
            self.components = components

    @property
    def count(self):
        r"""Gets the count of this ShowComponentsInApplicationResponse.

        组件数量

        :return: The count of this ShowComponentsInApplicationResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowComponentsInApplicationResponse.

        组件数量

        :param count: The count of this ShowComponentsInApplicationResponse.
        :type count: int
        """
        self._count = count

    @property
    def components(self):
        r"""Gets the components of this ShowComponentsInApplicationResponse.

        :return: The components of this ShowComponentsInApplicationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentList`]
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this ShowComponentsInApplicationResponse.

        :param components: The components of this ShowComponentsInApplicationResponse.
        :type components: list[:class:`huaweicloudsdkservicestage.v3.ComponentList`]
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
        if not isinstance(other, ShowComponentsInApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
