# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpDetectResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'GetHttpDetectResponseBodyDetail',
        'status': 'int',
        'request_id': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'status': 'status',
        'request_id': 'request_id'
    }

    def __init__(self, detail=None, status=None, request_id=None):
        r"""ShowHttpDetectResultResponse

        The model defined in huaweicloud sdk

        :param detail: 
        :type detail: :class:`huaweicloudsdksmn.v2.GetHttpDetectResponseBodyDetail`
        :param status: http探测任务状态，0代表执行成功，终端可用，1代表未执行，2代表执行失败，终端不可用
        :type status: int
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ShowHttpDetectResultResponse, self).__init__()

        self._detail = None
        self._status = None
        self._request_id = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if request_id is not None:
            self.request_id = request_id

    @property
    def detail(self):
        r"""Gets the detail of this ShowHttpDetectResultResponse.

        :return: The detail of this ShowHttpDetectResultResponse.
        :rtype: :class:`huaweicloudsdksmn.v2.GetHttpDetectResponseBodyDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ShowHttpDetectResultResponse.

        :param detail: The detail of this ShowHttpDetectResultResponse.
        :type detail: :class:`huaweicloudsdksmn.v2.GetHttpDetectResponseBodyDetail`
        """
        self._detail = detail

    @property
    def status(self):
        r"""Gets the status of this ShowHttpDetectResultResponse.

        http探测任务状态，0代表执行成功，终端可用，1代表未执行，2代表执行失败，终端不可用

        :return: The status of this ShowHttpDetectResultResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowHttpDetectResultResponse.

        http探测任务状态，0代表执行成功，终端可用，1代表未执行，2代表执行失败，终端不可用

        :param status: The status of this ShowHttpDetectResultResponse.
        :type status: int
        """
        self._status = status

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowHttpDetectResultResponse.

        请求ID

        :return: The request_id of this ShowHttpDetectResultResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowHttpDetectResultResponse.

        请求ID

        :param request_id: The request_id of this ShowHttpDetectResultResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowHttpDetectResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
