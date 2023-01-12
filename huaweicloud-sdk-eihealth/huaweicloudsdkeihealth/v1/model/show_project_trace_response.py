# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectTraceResponse(SdkResponse):

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
        'bucket_size': 'int'
    }

    attribute_map = {
        'count': 'count',
        'datas': 'datas',
        'bucket_size': 'bucket_size'
    }

    def __init__(self, count=None, datas=None, bucket_size=None):
        """ShowProjectTraceResponse

        The model defined in huaweicloud sdk

        :param count: 数据对象（目录，文件）总数量
        :type count: int
        :param datas: 数据对象列表
        :type datas: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        :param bucket_size: 桶存量
        :type bucket_size: int
        """
        
        super(ShowProjectTraceResponse, self).__init__()

        self._count = None
        self._datas = None
        self._bucket_size = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if datas is not None:
            self.datas = datas
        if bucket_size is not None:
            self.bucket_size = bucket_size

    @property
    def count(self):
        """Gets the count of this ShowProjectTraceResponse.

        数据对象（目录，文件）总数量

        :return: The count of this ShowProjectTraceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowProjectTraceResponse.

        数据对象（目录，文件）总数量

        :param count: The count of this ShowProjectTraceResponse.
        :type count: int
        """
        self._count = count

    @property
    def datas(self):
        """Gets the datas of this ShowProjectTraceResponse.

        数据对象列表

        :return: The datas of this ShowProjectTraceResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        """
        return self._datas

    @datas.setter
    def datas(self, datas):
        """Sets the datas of this ShowProjectTraceResponse.

        数据对象列表

        :param datas: The datas of this ShowProjectTraceResponse.
        :type datas: list[:class:`huaweicloudsdkeihealth.v1.DataRsp`]
        """
        self._datas = datas

    @property
    def bucket_size(self):
        """Gets the bucket_size of this ShowProjectTraceResponse.

        桶存量

        :return: The bucket_size of this ShowProjectTraceResponse.
        :rtype: int
        """
        return self._bucket_size

    @bucket_size.setter
    def bucket_size(self, bucket_size):
        """Sets the bucket_size of this ShowProjectTraceResponse.

        桶存量

        :param bucket_size: The bucket_size of this ShowProjectTraceResponse.
        :type bucket_size: int
        """
        self._bucket_size = bucket_size

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
        if not isinstance(other, ShowProjectTraceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
