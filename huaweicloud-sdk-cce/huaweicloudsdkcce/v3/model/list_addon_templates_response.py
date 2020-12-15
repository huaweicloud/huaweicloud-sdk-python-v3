# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListAddonTemplatesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'items': 'list[AddonTemplate]',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'items': 'items',
        'kind': 'kind'
    }

    def __init__(self, api_version='v3', items=None, kind='Addon'):
        """ListAddonTemplatesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._api_version = None
        self._items = None
        self._kind = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items
        if kind is not None:
            self.kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this ListAddonTemplatesResponse.

        API版本，固定值“v3”，该值不可修改。

        :return: The api_version of this ListAddonTemplatesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ListAddonTemplatesResponse.

        API版本，固定值“v3”，该值不可修改。

        :param api_version: The api_version of this ListAddonTemplatesResponse.
        :type: str
        """
        self._api_version = api_version

    @property
    def items(self):
        """Gets the items of this ListAddonTemplatesResponse.

        插件模板列表

        :return: The items of this ListAddonTemplatesResponse.
        :rtype: list[AddonTemplate]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListAddonTemplatesResponse.

        插件模板列表

        :param items: The items of this ListAddonTemplatesResponse.
        :type: list[AddonTemplate]
        """
        self._items = items

    @property
    def kind(self):
        """Gets the kind of this ListAddonTemplatesResponse.

        API类型，固定值“Addon”，该值不可修改。

        :return: The kind of this ListAddonTemplatesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListAddonTemplatesResponse.

        API类型，固定值“Addon”，该值不可修改。

        :param kind: The kind of this ListAddonTemplatesResponse.
        :type: str
        """
        self._kind = kind

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAddonTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
