# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourcesUsageRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resource_records': 'list[FreeResourceRecord]',
        'total_count': 'int'
    }

    attribute_map = {
        'free_resource_records': 'free_resource_records',
        'total_count': 'total_count'
    }

    def __init__(self, free_resource_records=None, total_count=None):
        """ListFreeResourcesUsageRecordsResponse

        The model defined in huaweicloud sdk

        :param free_resource_records: 资源包使用明细记录，具体参见表1。
        :type free_resource_records: list[:class:`huaweicloudsdkbss.v2.FreeResourceRecord`]
        :param total_count: 满足条件的总个数。
        :type total_count: int
        """
        
        super(ListFreeResourcesUsageRecordsResponse, self).__init__()

        self._free_resource_records = None
        self._total_count = None
        self.discriminator = None

        if free_resource_records is not None:
            self.free_resource_records = free_resource_records
        if total_count is not None:
            self.total_count = total_count

    @property
    def free_resource_records(self):
        """Gets the free_resource_records of this ListFreeResourcesUsageRecordsResponse.

        资源包使用明细记录，具体参见表1。

        :return: The free_resource_records of this ListFreeResourcesUsageRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FreeResourceRecord`]
        """
        return self._free_resource_records

    @free_resource_records.setter
    def free_resource_records(self, free_resource_records):
        """Sets the free_resource_records of this ListFreeResourcesUsageRecordsResponse.

        资源包使用明细记录，具体参见表1。

        :param free_resource_records: The free_resource_records of this ListFreeResourcesUsageRecordsResponse.
        :type free_resource_records: list[:class:`huaweicloudsdkbss.v2.FreeResourceRecord`]
        """
        self._free_resource_records = free_resource_records

    @property
    def total_count(self):
        """Gets the total_count of this ListFreeResourcesUsageRecordsResponse.

        满足条件的总个数。

        :return: The total_count of this ListFreeResourcesUsageRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListFreeResourcesUsageRecordsResponse.

        满足条件的总个数。

        :param total_count: The total_count of this ListFreeResourcesUsageRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListFreeResourcesUsageRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
