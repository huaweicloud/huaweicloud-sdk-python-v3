# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReadWriteRatioResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'read_write_ratio_list': 'list[ReadWriteRatioList]'
    }

    attribute_map = {
        'total_record': 'totalRecord',
        'read_write_ratio_list': 'readWriteRatioList'
    }

    def __init__(self, total_record=None, read_write_ratio_list=None):
        """ListReadWriteRatioResponse

        The model defined in huaweicloud sdk

        :param total_record: DDM读写比例监控信息条数。
        :type total_record: int
        :param read_write_ratio_list: DDM实例读写次数信息列表的集合。
        :type read_write_ratio_list: list[:class:`huaweicloudsdkddm.v1.ReadWriteRatioList`]
        """
        
        super(ListReadWriteRatioResponse, self).__init__()

        self._total_record = None
        self._read_write_ratio_list = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if read_write_ratio_list is not None:
            self.read_write_ratio_list = read_write_ratio_list

    @property
    def total_record(self):
        """Gets the total_record of this ListReadWriteRatioResponse.

        DDM读写比例监控信息条数。

        :return: The total_record of this ListReadWriteRatioResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListReadWriteRatioResponse.

        DDM读写比例监控信息条数。

        :param total_record: The total_record of this ListReadWriteRatioResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def read_write_ratio_list(self):
        """Gets the read_write_ratio_list of this ListReadWriteRatioResponse.

        DDM实例读写次数信息列表的集合。

        :return: The read_write_ratio_list of this ListReadWriteRatioResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ReadWriteRatioList`]
        """
        return self._read_write_ratio_list

    @read_write_ratio_list.setter
    def read_write_ratio_list(self, read_write_ratio_list):
        """Sets the read_write_ratio_list of this ListReadWriteRatioResponse.

        DDM实例读写次数信息列表的集合。

        :param read_write_ratio_list: The read_write_ratio_list of this ListReadWriteRatioResponse.
        :type read_write_ratio_list: list[:class:`huaweicloudsdkddm.v1.ReadWriteRatioList`]
        """
        self._read_write_ratio_list = read_write_ratio_list

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
        if not isinstance(other, ListReadWriteRatioResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
