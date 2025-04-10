# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowPhoneConnectInfosResponse(SdkResponse):

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
        'connect_infos': 'list[ConnectInfo]',
        'errors': 'list[ConnectErrorInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'connect_infos': 'connect_infos',
        'errors': 'errors'
    }

    def __init__(self, request_id=None, connect_infos=None, errors=None):
        r"""BatchShowPhoneConnectInfosResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param connect_infos: 云手机接入信息列表
        :type connect_infos: list[:class:`huaweicloudsdkcph.v1.ConnectInfo`]
        :param errors: 错误信息
        :type errors: list[:class:`huaweicloudsdkcph.v1.ConnectErrorInfo`]
        """
        
        super(BatchShowPhoneConnectInfosResponse, self).__init__()

        self._request_id = None
        self._connect_infos = None
        self._errors = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if connect_infos is not None:
            self.connect_infos = connect_infos
        if errors is not None:
            self.errors = errors

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchShowPhoneConnectInfosResponse.

        请求的唯一标识ID。

        :return: The request_id of this BatchShowPhoneConnectInfosResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchShowPhoneConnectInfosResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this BatchShowPhoneConnectInfosResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def connect_infos(self):
        r"""Gets the connect_infos of this BatchShowPhoneConnectInfosResponse.

        云手机接入信息列表

        :return: The connect_infos of this BatchShowPhoneConnectInfosResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ConnectInfo`]
        """
        return self._connect_infos

    @connect_infos.setter
    def connect_infos(self, connect_infos):
        r"""Sets the connect_infos of this BatchShowPhoneConnectInfosResponse.

        云手机接入信息列表

        :param connect_infos: The connect_infos of this BatchShowPhoneConnectInfosResponse.
        :type connect_infos: list[:class:`huaweicloudsdkcph.v1.ConnectInfo`]
        """
        self._connect_infos = connect_infos

    @property
    def errors(self):
        r"""Gets the errors of this BatchShowPhoneConnectInfosResponse.

        错误信息

        :return: The errors of this BatchShowPhoneConnectInfosResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ConnectErrorInfo`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this BatchShowPhoneConnectInfosResponse.

        错误信息

        :param errors: The errors of this BatchShowPhoneConnectInfosResponse.
        :type errors: list[:class:`huaweicloudsdkcph.v1.ConnectErrorInfo`]
        """
        self._errors = errors

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
        if not isinstance(other, BatchShowPhoneConnectInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
