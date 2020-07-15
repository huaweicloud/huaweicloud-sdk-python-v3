# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class KeystoneShowCatalogResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'catalog': 'list[Catalog]',
        'links': 'LinksSelf'
    }

    attribute_map = {
        'catalog': 'catalog',
        'links': 'links'
    }

    def __init__(self, catalog=None, links=None):
        """KeystoneShowCatalogResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._catalog = None
        self._links = None
        self.discriminator = None

        if catalog is not None:
            self.catalog = catalog
        if links is not None:
            self.links = links

    @property
    def catalog(self):
        """Gets the catalog of this KeystoneShowCatalogResponse.

        服务目录信息列表。

        :return: The catalog of this KeystoneShowCatalogResponse.
        :rtype: list[Catalog]
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this KeystoneShowCatalogResponse.

        服务目录信息列表。

        :param catalog: The catalog of this KeystoneShowCatalogResponse.
        :type: list[Catalog]
        """
        self._catalog = catalog

    @property
    def links(self):
        """Gets the links of this KeystoneShowCatalogResponse.


        :return: The links of this KeystoneShowCatalogResponse.
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneShowCatalogResponse.


        :param links: The links of this KeystoneShowCatalogResponse.
        :type: LinksSelf
        """
        self._links = links

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
        if not isinstance(other, KeystoneShowCatalogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
