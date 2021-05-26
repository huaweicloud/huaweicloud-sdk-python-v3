# coding: utf-8

import pprint
import re

import six





class EipMetaData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'metadata_bandwidth_share_type': 'str',
        'metadata_eip_id': 'str',
        'metadataeip_address': 'str'
    }

    attribute_map = {
        'metadata_bandwidth_share_type': 'metadata_bandwidth_share_type',
        'metadata_eip_id': 'metadata_eip_id',
        'metadataeip_address': 'metadataeip_address'
    }

    def __init__(self, metadata_bandwidth_share_type=None, metadata_eip_id=None, metadataeip_address=None):
        """EipMetaData - a model defined in huaweicloud sdk"""
        
        

        self._metadata_bandwidth_share_type = None
        self._metadata_eip_id = None
        self._metadataeip_address = None
        self.discriminator = None

        if metadata_bandwidth_share_type is not None:
            self.metadata_bandwidth_share_type = metadata_bandwidth_share_type
        if metadata_eip_id is not None:
            self.metadata_eip_id = metadata_eip_id
        if metadataeip_address is not None:
            self.metadataeip_address = metadataeip_address

    @property
    def metadata_bandwidth_share_type(self):
        """Gets the metadata_bandwidth_share_type of this EipMetaData.

        伸缩带宽策略中带宽对应的共享类型。

        :return: The metadata_bandwidth_share_type of this EipMetaData.
        :rtype: str
        """
        return self._metadata_bandwidth_share_type

    @metadata_bandwidth_share_type.setter
    def metadata_bandwidth_share_type(self, metadata_bandwidth_share_type):
        """Sets the metadata_bandwidth_share_type of this EipMetaData.

        伸缩带宽策略中带宽对应的共享类型。

        :param metadata_bandwidth_share_type: The metadata_bandwidth_share_type of this EipMetaData.
        :type: str
        """
        self._metadata_bandwidth_share_type = metadata_bandwidth_share_type

    @property
    def metadata_eip_id(self):
        """Gets the metadata_eip_id of this EipMetaData.

        伸缩带宽策略中带宽对应的EIP的ID。

        :return: The metadata_eip_id of this EipMetaData.
        :rtype: str
        """
        return self._metadata_eip_id

    @metadata_eip_id.setter
    def metadata_eip_id(self, metadata_eip_id):
        """Sets the metadata_eip_id of this EipMetaData.

        伸缩带宽策略中带宽对应的EIP的ID。

        :param metadata_eip_id: The metadata_eip_id of this EipMetaData.
        :type: str
        """
        self._metadata_eip_id = metadata_eip_id

    @property
    def metadataeip_address(self):
        """Gets the metadataeip_address of this EipMetaData.

        伸缩带宽策略中带宽对应的EIP地址。

        :return: The metadataeip_address of this EipMetaData.
        :rtype: str
        """
        return self._metadataeip_address

    @metadataeip_address.setter
    def metadataeip_address(self, metadataeip_address):
        """Sets the metadataeip_address of this EipMetaData.

        伸缩带宽策略中带宽对应的EIP地址。

        :param metadataeip_address: The metadataeip_address of this EipMetaData.
        :type: str
        """
        self._metadataeip_address = metadataeip_address

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
        if not isinstance(other, EipMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
