# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPtrRecordsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'links': 'PageLink',
        'metadata': 'Metedata',
        'floatingips': 'list[ListPtrRecordsFloatingResp]'
    }

    attribute_map = {
        'links': 'links',
        'metadata': 'metadata',
        'floatingips': 'floatingips'
    }

    def __init__(self, links=None, metadata=None, floatingips=None):
        """ListPtrRecordsResponse - a model defined in huaweicloud sdk"""
        
        super(ListPtrRecordsResponse, self).__init__()

        self._links = None
        self._metadata = None
        self._floatingips = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata
        if floatingips is not None:
            self.floatingips = floatingips

    @property
    def links(self):
        """Gets the links of this ListPtrRecordsResponse.


        :return: The links of this ListPtrRecordsResponse.
        :rtype: PageLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListPtrRecordsResponse.


        :param links: The links of this ListPtrRecordsResponse.
        :type: PageLink
        """
        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this ListPtrRecordsResponse.


        :return: The metadata of this ListPtrRecordsResponse.
        :rtype: Metedata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ListPtrRecordsResponse.


        :param metadata: The metadata of this ListPtrRecordsResponse.
        :type: Metedata
        """
        self._metadata = metadata

    @property
    def floatingips(self):
        """Gets the floatingips of this ListPtrRecordsResponse.


        :return: The floatingips of this ListPtrRecordsResponse.
        :rtype: list[ListPtrRecordsFloatingResp]
        """
        return self._floatingips

    @floatingips.setter
    def floatingips(self, floatingips):
        """Sets the floatingips of this ListPtrRecordsResponse.


        :param floatingips: The floatingips of this ListPtrRecordsResponse.
        :type: list[ListPtrRecordsFloatingResp]
        """
        self._floatingips = floatingips

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
        if not isinstance(other, ListPtrRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
