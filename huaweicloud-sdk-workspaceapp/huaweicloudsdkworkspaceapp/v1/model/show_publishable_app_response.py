# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublishableAppResponse(SdkResponse):

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
        'group_images': 'list[str]',
        'items': 'list[PublishableApp]'
    }

    attribute_map = {
        'count': 'count',
        'group_images': 'group_images',
        'items': 'items'
    }

    def __init__(self, count=None, group_images=None, items=None):
        r"""ShowPublishableAppResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param group_images: 组下面的镜像ID列表。
        :type group_images: list[str]
        :param items: 查询到的应用列表。
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishableApp`]
        """
        
        super(ShowPublishableAppResponse, self).__init__()

        self._count = None
        self._group_images = None
        self._items = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if group_images is not None:
            self.group_images = group_images
        if items is not None:
            self.items = items

    @property
    def count(self):
        r"""Gets the count of this ShowPublishableAppResponse.

        总数。

        :return: The count of this ShowPublishableAppResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowPublishableAppResponse.

        总数。

        :param count: The count of this ShowPublishableAppResponse.
        :type count: int
        """
        self._count = count

    @property
    def group_images(self):
        r"""Gets the group_images of this ShowPublishableAppResponse.

        组下面的镜像ID列表。

        :return: The group_images of this ShowPublishableAppResponse.
        :rtype: list[str]
        """
        return self._group_images

    @group_images.setter
    def group_images(self, group_images):
        r"""Sets the group_images of this ShowPublishableAppResponse.

        组下面的镜像ID列表。

        :param group_images: The group_images of this ShowPublishableAppResponse.
        :type group_images: list[str]
        """
        self._group_images = group_images

    @property
    def items(self):
        r"""Gets the items of this ShowPublishableAppResponse.

        查询到的应用列表。

        :return: The items of this ShowPublishableAppResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishableApp`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ShowPublishableAppResponse.

        查询到的应用列表。

        :param items: The items of this ShowPublishableAppResponse.
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishableApp`]
        """
        self._items = items

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
        if not isinstance(other, ShowPublishableAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
