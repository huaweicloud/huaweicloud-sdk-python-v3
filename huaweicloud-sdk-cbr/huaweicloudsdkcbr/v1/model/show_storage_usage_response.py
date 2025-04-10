# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStorageUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_count': 'int',
        'storage_usage': 'list[StorageUsage]'
    }

    attribute_map = {
        'resource_count': 'resource_count',
        'storage_usage': 'storage_usage'
    }

    def __init__(self, resource_count=None, storage_usage=None):
        r"""ShowStorageUsageResponse

        The model defined in huaweicloud sdk

        :param resource_count: 满足过滤条件的资源总条数
        :type resource_count: int
        :param storage_usage: 
        :type storage_usage: list[:class:`huaweicloudsdkcbr.v1.StorageUsage`]
        """
        
        super(ShowStorageUsageResponse, self).__init__()

        self._resource_count = None
        self._storage_usage = None
        self.discriminator = None

        if resource_count is not None:
            self.resource_count = resource_count
        if storage_usage is not None:
            self.storage_usage = storage_usage

    @property
    def resource_count(self):
        r"""Gets the resource_count of this ShowStorageUsageResponse.

        满足过滤条件的资源总条数

        :return: The resource_count of this ShowStorageUsageResponse.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this ShowStorageUsageResponse.

        满足过滤条件的资源总条数

        :param resource_count: The resource_count of this ShowStorageUsageResponse.
        :type resource_count: int
        """
        self._resource_count = resource_count

    @property
    def storage_usage(self):
        r"""Gets the storage_usage of this ShowStorageUsageResponse.

        

        :return: The storage_usage of this ShowStorageUsageResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.StorageUsage`]
        """
        return self._storage_usage

    @storage_usage.setter
    def storage_usage(self, storage_usage):
        r"""Sets the storage_usage of this ShowStorageUsageResponse.

        

        :param storage_usage: The storage_usage of this ShowStorageUsageResponse.
        :type storage_usage: list[:class:`huaweicloudsdkcbr.v1.StorageUsage`]
        """
        self._storage_usage = storage_usage

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
        if not isinstance(other, ShowStorageUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
