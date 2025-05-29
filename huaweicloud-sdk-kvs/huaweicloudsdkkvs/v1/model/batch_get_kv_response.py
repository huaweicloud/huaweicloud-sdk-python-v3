# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchGetKvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exception_opers': 'list[ExceptionOpersOfTable]',
        'returned_kv_items_of_all': 'list[ReturnedKvItemsOfTable]'
    }

    attribute_map = {
        'exception_opers': 'exception_opers',
        'returned_kv_items_of_all': 'returned_kv_items_of_all'
    }

    def __init__(self, exception_opers=None, returned_kv_items_of_all=None):
        r"""BatchGetKvResponse

        The model defined in huaweicloud sdk

        :param exception_opers: 异常处理的操作，按照table分类组织。
        :type exception_opers: list[:class:`huaweicloudsdkkvs.v1.ExceptionOpersOfTable`]
        :param returned_kv_items_of_all: 返回的kvdoc列表，按照table分类组织。
        :type returned_kv_items_of_all: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItemsOfTable`]
        """
        
        super(BatchGetKvResponse, self).__init__()

        self._exception_opers = None
        self._returned_kv_items_of_all = None
        self.discriminator = None

        if exception_opers is not None:
            self.exception_opers = exception_opers
        if returned_kv_items_of_all is not None:
            self.returned_kv_items_of_all = returned_kv_items_of_all

    @property
    def exception_opers(self):
        r"""Gets the exception_opers of this BatchGetKvResponse.

        异常处理的操作，按照table分类组织。

        :return: The exception_opers of this BatchGetKvResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.ExceptionOpersOfTable`]
        """
        return self._exception_opers

    @exception_opers.setter
    def exception_opers(self, exception_opers):
        r"""Sets the exception_opers of this BatchGetKvResponse.

        异常处理的操作，按照table分类组织。

        :param exception_opers: The exception_opers of this BatchGetKvResponse.
        :type exception_opers: list[:class:`huaweicloudsdkkvs.v1.ExceptionOpersOfTable`]
        """
        self._exception_opers = exception_opers

    @property
    def returned_kv_items_of_all(self):
        r"""Gets the returned_kv_items_of_all of this BatchGetKvResponse.

        返回的kvdoc列表，按照table分类组织。

        :return: The returned_kv_items_of_all of this BatchGetKvResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItemsOfTable`]
        """
        return self._returned_kv_items_of_all

    @returned_kv_items_of_all.setter
    def returned_kv_items_of_all(self, returned_kv_items_of_all):
        r"""Sets the returned_kv_items_of_all of this BatchGetKvResponse.

        返回的kvdoc列表，按照table分类组织。

        :param returned_kv_items_of_all: The returned_kv_items_of_all of this BatchGetKvResponse.
        :type returned_kv_items_of_all: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItemsOfTable`]
        """
        self._returned_kv_items_of_all = returned_kv_items_of_all

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
        if not isinstance(other, BatchGetKvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
