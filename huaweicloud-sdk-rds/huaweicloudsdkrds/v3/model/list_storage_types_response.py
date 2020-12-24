# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListStorageTypesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'storage_type': 'list[Storage]',
        'dsspool_info': 'list[DssPoolInfo]'
    }

    attribute_map = {
        'storage_type': 'storage_type',
        'dsspool_info': 'dsspool_info'
    }

    def __init__(self, storage_type=None, dsspool_info=None):
        """ListStorageTypesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._storage_type = None
        self._dsspool_info = None
        self.discriminator = None

        if storage_type is not None:
            self.storage_type = storage_type
        if dsspool_info is not None:
            self.dsspool_info = dsspool_info

    @property
    def storage_type(self):
        """Gets the storage_type of this ListStorageTypesResponse.

        实例磁盘类型信息。

        :return: The storage_type of this ListStorageTypesResponse.
        :rtype: list[Storage]
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ListStorageTypesResponse.

        实例磁盘类型信息。

        :param storage_type: The storage_type of this ListStorageTypesResponse.
        :type: list[Storage]
        """
        self._storage_type = storage_type

    @property
    def dsspool_info(self):
        """Gets the dsspool_info of this ListStorageTypesResponse.

        实例专属存储信息。

        :return: The dsspool_info of this ListStorageTypesResponse.
        :rtype: list[DssPoolInfo]
        """
        return self._dsspool_info

    @dsspool_info.setter
    def dsspool_info(self, dsspool_info):
        """Sets the dsspool_info of this ListStorageTypesResponse.

        实例专属存储信息。

        :param dsspool_info: The dsspool_info of this ListStorageTypesResponse.
        :type: list[DssPoolInfo]
        """
        self._dsspool_info = dsspool_info

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
        if not isinstance(other, ListStorageTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
