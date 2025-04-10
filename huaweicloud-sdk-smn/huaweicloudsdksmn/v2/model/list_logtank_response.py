# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogtankResponse(SdkResponse):

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
        'count': 'int',
        'logtanks': 'list[LogtankItem]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'count': 'count',
        'logtanks': 'logtanks'
    }

    def __init__(self, request_id=None, count=None, logtanks=None):
        r"""ListLogtankResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识
        :type request_id: str
        :param count: 云日志信息数量
        :type count: int
        :param logtanks: 云日志信息列表
        :type logtanks: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        
        super(ListLogtankResponse, self).__init__()

        self._request_id = None
        self._count = None
        self._logtanks = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if count is not None:
            self.count = count
        if logtanks is not None:
            self.logtanks = logtanks

    @property
    def request_id(self):
        r"""Gets the request_id of this ListLogtankResponse.

        请求的唯一标识

        :return: The request_id of this ListLogtankResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListLogtankResponse.

        请求的唯一标识

        :param request_id: The request_id of this ListLogtankResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def count(self):
        r"""Gets the count of this ListLogtankResponse.

        云日志信息数量

        :return: The count of this ListLogtankResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListLogtankResponse.

        云日志信息数量

        :param count: The count of this ListLogtankResponse.
        :type count: int
        """
        self._count = count

    @property
    def logtanks(self):
        r"""Gets the logtanks of this ListLogtankResponse.

        云日志信息列表

        :return: The logtanks of this ListLogtankResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        return self._logtanks

    @logtanks.setter
    def logtanks(self, logtanks):
        r"""Sets the logtanks of this ListLogtankResponse.

        云日志信息列表

        :param logtanks: The logtanks of this ListLogtankResponse.
        :type logtanks: list[:class:`huaweicloudsdksmn.v2.LogtankItem`]
        """
        self._logtanks = logtanks

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
        if not isinstance(other, ListLogtankResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
