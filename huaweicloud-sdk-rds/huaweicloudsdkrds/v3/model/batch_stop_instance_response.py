# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStopInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[ShutdownInstanceRecord]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'records': 'records',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, records=None, x_request_id=None):
        r"""BatchStopInstanceResponse

        The model defined in huaweicloud sdk

        :param records: 停止实例结果列表
        :type records: list[:class:`huaweicloudsdkrds.v3.ShutdownInstanceRecord`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(BatchStopInstanceResponse, self).__init__()

        self._records = None
        self._x_request_id = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def records(self):
        r"""Gets the records of this BatchStopInstanceResponse.

        停止实例结果列表

        :return: The records of this BatchStopInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ShutdownInstanceRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BatchStopInstanceResponse.

        停止实例结果列表

        :param records: The records of this BatchStopInstanceResponse.
        :type records: list[:class:`huaweicloudsdkrds.v3.ShutdownInstanceRecord`]
        """
        self._records = records

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this BatchStopInstanceResponse.

        :return: The x_request_id of this BatchStopInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this BatchStopInstanceResponse.

        :param x_request_id: The x_request_id of this BatchStopInstanceResponse.
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
        if not isinstance(other, BatchStopInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
