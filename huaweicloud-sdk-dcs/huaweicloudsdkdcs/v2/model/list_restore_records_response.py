# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRestoreRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_record_response': 'list[InstanceRestoreInfo]',
        'total_num': 'int'
    }

    attribute_map = {
        'restore_record_response': 'restore_record_response',
        'total_num': 'total_num'
    }

    def __init__(self, restore_record_response=None, total_num=None):
        """ListRestoreRecordsResponse

        The model defined in huaweicloud sdk

        :param restore_record_response: 实例恢复记录的详情数组。
        :type restore_record_response: list[:class:`huaweicloudsdkdcs.v2.InstanceRestoreInfo`]
        :param total_num: 返回记录数。
        :type total_num: int
        """
        
        super(ListRestoreRecordsResponse, self).__init__()

        self._restore_record_response = None
        self._total_num = None
        self.discriminator = None

        if restore_record_response is not None:
            self.restore_record_response = restore_record_response
        if total_num is not None:
            self.total_num = total_num

    @property
    def restore_record_response(self):
        """Gets the restore_record_response of this ListRestoreRecordsResponse.

        实例恢复记录的详情数组。

        :return: The restore_record_response of this ListRestoreRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstanceRestoreInfo`]
        """
        return self._restore_record_response

    @restore_record_response.setter
    def restore_record_response(self, restore_record_response):
        """Sets the restore_record_response of this ListRestoreRecordsResponse.

        实例恢复记录的详情数组。

        :param restore_record_response: The restore_record_response of this ListRestoreRecordsResponse.
        :type restore_record_response: list[:class:`huaweicloudsdkdcs.v2.InstanceRestoreInfo`]
        """
        self._restore_record_response = restore_record_response

    @property
    def total_num(self):
        """Gets the total_num of this ListRestoreRecordsResponse.

        返回记录数。

        :return: The total_num of this ListRestoreRecordsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListRestoreRecordsResponse.

        返回记录数。

        :param total_num: The total_num of this ListRestoreRecordsResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ListRestoreRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
