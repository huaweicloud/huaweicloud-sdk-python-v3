# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRecordSetByZoneResponse(SdkResponse):


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
        'recordsets': 'list[ShowRecordSetByZoneResp]',
        'metadata': 'Metedata'
    }

    attribute_map = {
        'links': 'links',
        'recordsets': 'recordsets',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, recordsets=None, metadata=None):
        """ShowRecordSetByZoneResponse - a model defined in huaweicloud sdk"""
        
        super(ShowRecordSetByZoneResponse, self).__init__()

        self._links = None
        self._recordsets = None
        self._metadata = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if recordsets is not None:
            self.recordsets = recordsets
        if metadata is not None:
            self.metadata = metadata

    @property
    def links(self):
        """Gets the links of this ShowRecordSetByZoneResponse.


        :return: The links of this ShowRecordSetByZoneResponse.
        :rtype: PageLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowRecordSetByZoneResponse.


        :param links: The links of this ShowRecordSetByZoneResponse.
        :type: PageLink
        """
        self._links = links

    @property
    def recordsets(self):
        """Gets the recordsets of this ShowRecordSetByZoneResponse.


        :return: The recordsets of this ShowRecordSetByZoneResponse.
        :rtype: list[ShowRecordSetByZoneResp]
        """
        return self._recordsets

    @recordsets.setter
    def recordsets(self, recordsets):
        """Sets the recordsets of this ShowRecordSetByZoneResponse.


        :param recordsets: The recordsets of this ShowRecordSetByZoneResponse.
        :type: list[ShowRecordSetByZoneResp]
        """
        self._recordsets = recordsets

    @property
    def metadata(self):
        """Gets the metadata of this ShowRecordSetByZoneResponse.


        :return: The metadata of this ShowRecordSetByZoneResponse.
        :rtype: Metedata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowRecordSetByZoneResponse.


        :param metadata: The metadata of this ShowRecordSetByZoneResponse.
        :type: Metedata
        """
        self._metadata = metadata

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
        if not isinstance(other, ShowRecordSetByZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
