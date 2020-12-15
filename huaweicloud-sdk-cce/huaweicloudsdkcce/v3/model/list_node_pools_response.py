# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNodePoolsResponse(SdkResponse):


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
        'items': 'list[NodePool]',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'items': 'items',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, items=None, kind=None):
        """ListNodePoolsResponse - a model defined in huaweicloud sdk"""
        
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
        """Gets the api_version of this ListNodePoolsResponse.

        API version. The value is fixed to v3.

        :return: The api_version of this ListNodePoolsResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ListNodePoolsResponse.

        API version. The value is fixed to v3.

        :param api_version: The api_version of this ListNodePoolsResponse.
        :type: str
        """
        self._api_version = api_version

    @property
    def items(self):
        """Gets the items of this ListNodePoolsResponse.

        /

        :return: The items of this ListNodePoolsResponse.
        :rtype: list[NodePool]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListNodePoolsResponse.

        /

        :param items: The items of this ListNodePoolsResponse.
        :type: list[NodePool]
        """
        self._items = items

    @property
    def kind(self):
        """Gets the kind of this ListNodePoolsResponse.

        API type. The value is fixed to List.

        :return: The kind of this ListNodePoolsResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListNodePoolsResponse.

        API type. The value is fixed to List.

        :param kind: The kind of this ListNodePoolsResponse.
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
        if not isinstance(other, ListNodePoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
