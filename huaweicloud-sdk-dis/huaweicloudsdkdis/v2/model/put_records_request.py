# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'stream_id': 'str',
        'records': 'list[PutRecordsRequestEntry]'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'stream_id': 'stream_id',
        'records': 'records'
    }

    def __init__(self, stream_name=None, stream_id=None, records=None):
        r"""PutRecordsRequest

        The model defined in huaweicloud sdk

        :param stream_name: 已创建的通道名称。
        :type stream_name: str
        :param stream_id: 通道唯一标识符。  当使用stream_name没有找到对应通道且stream_id不为空时，会使用stream_id去查找通道。  说明：  上传数据到被授权的通道时，必须配置此参数。
        :type stream_id: str
        :param records: 待上传的记录列表。
        :type records: list[:class:`huaweicloudsdkdis.v2.PutRecordsRequestEntry`]
        """
        
        

        self._stream_name = None
        self._stream_id = None
        self._records = None
        self.discriminator = None

        self.stream_name = stream_name
        if stream_id is not None:
            self.stream_id = stream_id
        self.records = records

    @property
    def stream_name(self):
        r"""Gets the stream_name of this PutRecordsRequest.

        已创建的通道名称。

        :return: The stream_name of this PutRecordsRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this PutRecordsRequest.

        已创建的通道名称。

        :param stream_name: The stream_name of this PutRecordsRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def stream_id(self):
        r"""Gets the stream_id of this PutRecordsRequest.

        通道唯一标识符。  当使用stream_name没有找到对应通道且stream_id不为空时，会使用stream_id去查找通道。  说明：  上传数据到被授权的通道时，必须配置此参数。

        :return: The stream_id of this PutRecordsRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this PutRecordsRequest.

        通道唯一标识符。  当使用stream_name没有找到对应通道且stream_id不为空时，会使用stream_id去查找通道。  说明：  上传数据到被授权的通道时，必须配置此参数。

        :param stream_id: The stream_id of this PutRecordsRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def records(self):
        r"""Gets the records of this PutRecordsRequest.

        待上传的记录列表。

        :return: The records of this PutRecordsRequest.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PutRecordsRequestEntry`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this PutRecordsRequest.

        待上传的记录列表。

        :param records: The records of this PutRecordsRequest.
        :type records: list[:class:`huaweicloudsdkdis.v2.PutRecordsRequestEntry`]
        """
        self._records = records

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
        if not isinstance(other, PutRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
