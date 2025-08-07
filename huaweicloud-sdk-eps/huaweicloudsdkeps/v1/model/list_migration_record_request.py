# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigrationRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'str',
        'limit': 'int',
        'resource_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id'
    }

    def __init__(self, start_time=None, end_time=None, offset=None, limit=None, resource_id=None):
        r"""ListMigrationRecordRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param offset: 索引位置，从offset指定的下一条数据开始查询
        :type offset: str
        :param limit: 查询记录数
        :type limit: int
        :param resource_id: 资源ID
        :type resource_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._resource_id = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListMigrationRecordRequest.

        开始时间

        :return: The start_time of this ListMigrationRecordRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListMigrationRecordRequest.

        开始时间

        :param start_time: The start_time of this ListMigrationRecordRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListMigrationRecordRequest.

        结束时间

        :return: The end_time of this ListMigrationRecordRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListMigrationRecordRequest.

        结束时间

        :param end_time: The end_time of this ListMigrationRecordRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListMigrationRecordRequest.

        索引位置，从offset指定的下一条数据开始查询

        :return: The offset of this ListMigrationRecordRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMigrationRecordRequest.

        索引位置，从offset指定的下一条数据开始查询

        :param offset: The offset of this ListMigrationRecordRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMigrationRecordRequest.

        查询记录数

        :return: The limit of this ListMigrationRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMigrationRecordRequest.

        查询记录数

        :param limit: The limit of this ListMigrationRecordRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListMigrationRecordRequest.

        资源ID

        :return: The resource_id of this ListMigrationRecordRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListMigrationRecordRequest.

        资源ID

        :param resource_id: The resource_id of this ListMigrationRecordRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ListMigrationRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
