# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordContentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'record_contents': 'list[RecordContentInfoV2]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'record_contents': 'record_contents',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, total=None, record_contents=None, x_request_id=None):
        r"""ListRecordContentsResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总元素数量
        :type total: int
        :param record_contents: 录制内容数组
        :type record_contents: list[:class:`huaweicloudsdklive.v1.RecordContentInfoV2`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRecordContentsResponse, self).__init__()

        self._total = None
        self._record_contents = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if record_contents is not None:
            self.record_contents = record_contents
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListRecordContentsResponse.

        查询结果的总元素数量

        :return: The total of this ListRecordContentsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRecordContentsResponse.

        查询结果的总元素数量

        :param total: The total of this ListRecordContentsResponse.
        :type total: int
        """
        self._total = total

    @property
    def record_contents(self):
        r"""Gets the record_contents of this ListRecordContentsResponse.

        录制内容数组

        :return: The record_contents of this ListRecordContentsResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.RecordContentInfoV2`]
        """
        return self._record_contents

    @record_contents.setter
    def record_contents(self, record_contents):
        r"""Sets the record_contents of this ListRecordContentsResponse.

        录制内容数组

        :param record_contents: The record_contents of this ListRecordContentsResponse.
        :type record_contents: list[:class:`huaweicloudsdklive.v1.RecordContentInfoV2`]
        """
        self._record_contents = record_contents

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListRecordContentsResponse.

        :return: The x_request_id of this ListRecordContentsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListRecordContentsResponse.

        :param x_request_id: The x_request_id of this ListRecordContentsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRecordContentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
