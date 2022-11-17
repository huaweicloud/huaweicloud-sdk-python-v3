# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowParamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'params_list': 'list[QueryDbParamsResp]',
        'count': 'int'
    }

    attribute_map = {
        'params_list': 'params_list',
        'count': 'count'
    }

    def __init__(self, params_list=None, count=None):
        """BatchShowParamsResponse

        The model defined in huaweicloud sdk

        :param params_list: 查询数据库参数响应体
        :type params_list: list[:class:`huaweicloudsdkdrs.v3.QueryDbParamsResp`]
        :param count: 总数
        :type count: int
        """
        
        super(BatchShowParamsResponse, self).__init__()

        self._params_list = None
        self._count = None
        self.discriminator = None

        if params_list is not None:
            self.params_list = params_list
        if count is not None:
            self.count = count

    @property
    def params_list(self):
        """Gets the params_list of this BatchShowParamsResponse.

        查询数据库参数响应体

        :return: The params_list of this BatchShowParamsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.QueryDbParamsResp`]
        """
        return self._params_list

    @params_list.setter
    def params_list(self, params_list):
        """Sets the params_list of this BatchShowParamsResponse.

        查询数据库参数响应体

        :param params_list: The params_list of this BatchShowParamsResponse.
        :type params_list: list[:class:`huaweicloudsdkdrs.v3.QueryDbParamsResp`]
        """
        self._params_list = params_list

    @property
    def count(self):
        """Gets the count of this BatchShowParamsResponse.

        总数

        :return: The count of this BatchShowParamsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchShowParamsResponse.

        总数

        :param count: The count of this BatchShowParamsResponse.
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
        if not isinstance(other, BatchShowParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
