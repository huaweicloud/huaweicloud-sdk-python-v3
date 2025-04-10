# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_process_info': 'list[DataProcessInfo]',
        'count': 'int'
    }

    attribute_map = {
        'data_process_info': 'data_process_info',
        'count': 'count'
    }

    def __init__(self, data_process_info=None, count=None):
        r"""ShowDataProgressResponse

        The model defined in huaweicloud sdk

        :param data_process_info: 数据加工规则响应体
        :type data_process_info: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        :param count: 数据加工规则总数目
        :type count: int
        """
        
        super(ShowDataProgressResponse, self).__init__()

        self._data_process_info = None
        self._count = None
        self.discriminator = None

        if data_process_info is not None:
            self.data_process_info = data_process_info
        if count is not None:
            self.count = count

    @property
    def data_process_info(self):
        r"""Gets the data_process_info of this ShowDataProgressResponse.

        数据加工规则响应体

        :return: The data_process_info of this ShowDataProgressResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        """
        return self._data_process_info

    @data_process_info.setter
    def data_process_info(self, data_process_info):
        r"""Sets the data_process_info of this ShowDataProgressResponse.

        数据加工规则响应体

        :param data_process_info: The data_process_info of this ShowDataProgressResponse.
        :type data_process_info: list[:class:`huaweicloudsdkdrs.v5.DataProcessInfo`]
        """
        self._data_process_info = data_process_info

    @property
    def count(self):
        r"""Gets the count of this ShowDataProgressResponse.

        数据加工规则总数目

        :return: The count of this ShowDataProgressResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowDataProgressResponse.

        数据加工规则总数目

        :param count: The count of this ShowDataProgressResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ShowDataProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
