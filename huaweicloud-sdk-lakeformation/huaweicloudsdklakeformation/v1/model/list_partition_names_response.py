# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartitionNamesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_name_list': 'list[str]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'partition_name_list': 'partition_name_list',
        'page_info': 'page_info'
    }

    def __init__(self, partition_name_list=None, page_info=None):
        """ListPartitionNamesResponse

        The model defined in huaweicloud sdk

        :param partition_name_list: 分区名字列表
        :type partition_name_list: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(ListPartitionNamesResponse, self).__init__()

        self._partition_name_list = None
        self._page_info = None
        self.discriminator = None

        if partition_name_list is not None:
            self.partition_name_list = partition_name_list
        if page_info is not None:
            self.page_info = page_info

    @property
    def partition_name_list(self):
        """Gets the partition_name_list of this ListPartitionNamesResponse.

        分区名字列表

        :return: The partition_name_list of this ListPartitionNamesResponse.
        :rtype: list[str]
        """
        return self._partition_name_list

    @partition_name_list.setter
    def partition_name_list(self, partition_name_list):
        """Sets the partition_name_list of this ListPartitionNamesResponse.

        分区名字列表

        :param partition_name_list: The partition_name_list of this ListPartitionNamesResponse.
        :type partition_name_list: list[str]
        """
        self._partition_name_list = partition_name_list

    @property
    def page_info(self):
        """Gets the page_info of this ListPartitionNamesResponse.

        :return: The page_info of this ListPartitionNamesResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPartitionNamesResponse.

        :param page_info: The page_info of this ListPartitionNamesResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListPartitionNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
