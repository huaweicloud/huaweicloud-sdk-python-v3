# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'datas': 'list[DataRsp]',
        'next_marker': 'str'
    }

    attribute_map = {
        'count': 'count',
        'datas': 'datas',
        'next_marker': 'next_marker'
    }

    def __init__(self, count=None, datas=None, next_marker=None):
        """ListDataResponse

        The model defined in huaweicloud sdk

        :param count: 数据对象（目录，文件）总数量
        :type count: int
        :param datas: 数据对象列表
        :type datas: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        :param next_marker: 下一页开始标签
        :type next_marker: str
        """
        
        super(ListDataResponse, self).__init__()

        self._count = None
        self._datas = None
        self._next_marker = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if datas is not None:
            self.datas = datas
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def count(self):
        """Gets the count of this ListDataResponse.

        数据对象（目录，文件）总数量

        :return: The count of this ListDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDataResponse.

        数据对象（目录，文件）总数量

        :param count: The count of this ListDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def datas(self):
        """Gets the datas of this ListDataResponse.

        数据对象列表

        :return: The datas of this ListDataResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        """
        return self._datas

    @datas.setter
    def datas(self, datas):
        """Sets the datas of this ListDataResponse.

        数据对象列表

        :param datas: The datas of this ListDataResponse.
        :type datas: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        """
        self._datas = datas

    @property
    def next_marker(self):
        """Gets the next_marker of this ListDataResponse.

        下一页开始标签

        :return: The next_marker of this ListDataResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListDataResponse.

        下一页开始标签

        :param next_marker: The next_marker of this ListDataResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
