# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedislogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'file_list': 'list[RunlogItem]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'file_list': 'file_list'
    }

    def __init__(self, total_num=None, file_list=None):
        """ListRedislogResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param file_list: 运行日志列表
        :type file_list: list[:class:`huaweicloudsdkdcs.v2.RunlogItem`]
        """
        
        super(ListRedislogResponse, self).__init__()

        self._total_num = None
        self._file_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if file_list is not None:
            self.file_list = file_list

    @property
    def total_num(self):
        """Gets the total_num of this ListRedislogResponse.

        总数

        :return: The total_num of this ListRedislogResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListRedislogResponse.

        总数

        :param total_num: The total_num of this ListRedislogResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def file_list(self):
        """Gets the file_list of this ListRedislogResponse.

        运行日志列表

        :return: The file_list of this ListRedislogResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.RunlogItem`]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        """Sets the file_list of this ListRedislogResponse.

        运行日志列表

        :param file_list: The file_list of this ListRedislogResponse.
        :type file_list: list[:class:`huaweicloudsdkdcs.v2.RunlogItem`]
        """
        self._file_list = file_list

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
        if not isinstance(other, ListRedislogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
