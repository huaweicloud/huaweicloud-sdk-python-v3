# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEmailRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'send_status': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'send_status': 'send_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, datastore_type=None, start_at=None, end_at=None, send_status=None, offset=None, limit=None):
        r"""ListEmailRecordRequest

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。
        :type datastore_type: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param send_status: 发送状态
        :type send_status: int
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页记录数
        :type limit: int
        """
        
        

        self._datastore_type = None
        self._start_at = None
        self._end_at = None
        self._send_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.datastore_type = datastore_type
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if send_status is not None:
            self.send_status = send_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListEmailRecordRequest.

        数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。

        :return: The datastore_type of this ListEmailRecordRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListEmailRecordRequest.

        数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。

        :param datastore_type: The datastore_type of this ListEmailRecordRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def start_at(self):
        r"""Gets the start_at of this ListEmailRecordRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ListEmailRecordRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListEmailRecordRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ListEmailRecordRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListEmailRecordRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ListEmailRecordRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListEmailRecordRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ListEmailRecordRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def send_status(self):
        r"""Gets the send_status of this ListEmailRecordRequest.

        发送状态

        :return: The send_status of this ListEmailRecordRequest.
        :rtype: int
        """
        return self._send_status

    @send_status.setter
    def send_status(self, send_status):
        r"""Sets the send_status of this ListEmailRecordRequest.

        发送状态

        :param send_status: The send_status of this ListEmailRecordRequest.
        :type send_status: int
        """
        self._send_status = send_status

    @property
    def offset(self):
        r"""Gets the offset of this ListEmailRecordRequest.

        偏移量

        :return: The offset of this ListEmailRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEmailRecordRequest.

        偏移量

        :param offset: The offset of this ListEmailRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEmailRecordRequest.

        每页记录数

        :return: The limit of this ListEmailRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEmailRecordRequest.

        每页记录数

        :param limit: The limit of this ListEmailRecordRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEmailRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
