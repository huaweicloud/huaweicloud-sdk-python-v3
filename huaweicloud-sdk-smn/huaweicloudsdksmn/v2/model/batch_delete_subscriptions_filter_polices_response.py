# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteSubscriptionsFilterPolicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'batch_result': 'list[BatchResult]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'batch_result': 'batch_result'
    }

    def __init__(self, request_id=None, batch_result=None):
        r"""BatchDeleteSubscriptionsFilterPolicesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param batch_result: 批量结果
        :type batch_result: list[:class:`huaweicloudsdksmn.v2.BatchResult`]
        """
        
        super(BatchDeleteSubscriptionsFilterPolicesResponse, self).__init__()

        self._request_id = None
        self._batch_result = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if batch_result is not None:
            self.batch_result = batch_result

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchDeleteSubscriptionsFilterPolicesResponse.

        请求的唯一标识ID。

        :return: The request_id of this BatchDeleteSubscriptionsFilterPolicesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchDeleteSubscriptionsFilterPolicesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this BatchDeleteSubscriptionsFilterPolicesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def batch_result(self):
        r"""Gets the batch_result of this BatchDeleteSubscriptionsFilterPolicesResponse.

        批量结果

        :return: The batch_result of this BatchDeleteSubscriptionsFilterPolicesResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.BatchResult`]
        """
        return self._batch_result

    @batch_result.setter
    def batch_result(self, batch_result):
        r"""Sets the batch_result of this BatchDeleteSubscriptionsFilterPolicesResponse.

        批量结果

        :param batch_result: The batch_result of this BatchDeleteSubscriptionsFilterPolicesResponse.
        :type batch_result: list[:class:`huaweicloudsdksmn.v2.BatchResult`]
        """
        self._batch_result = batch_result

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
        if not isinstance(other, BatchDeleteSubscriptionsFilterPolicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
