# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInterruptRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slo_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'source_id': 'str',
        'region_id': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'slo_id': 'slo_id',
        'offset': 'offset',
        'limit': 'limit',
        'source_id': 'source_id',
        'region_id': 'region_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, slo_id=None, offset=None, limit=None, source_id=None, region_id=None, start_time=None, end_time=None):
        r"""ListInterruptRecordsRequest

        The model defined in huaweicloud sdk

        :param slo_id: SLO的ID
        :type slo_id: str
        :param offset: 分页指针
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param source_id: 资源ID
        :type source_id: str
        :param region_id: regionId
        :type region_id: str
        :param start_time: 时间范围 - 开始时间
        :type start_time: int
        :param end_time: 时间范围 - 结束时间
        :type end_time: int
        """
        
        

        self._slo_id = None
        self._offset = None
        self._limit = None
        self._source_id = None
        self._region_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.slo_id = slo_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if source_id is not None:
            self.source_id = source_id
        if region_id is not None:
            self.region_id = region_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def slo_id(self):
        r"""Gets the slo_id of this ListInterruptRecordsRequest.

        SLO的ID

        :return: The slo_id of this ListInterruptRecordsRequest.
        :rtype: str
        """
        return self._slo_id

    @slo_id.setter
    def slo_id(self, slo_id):
        r"""Sets the slo_id of this ListInterruptRecordsRequest.

        SLO的ID

        :param slo_id: The slo_id of this ListInterruptRecordsRequest.
        :type slo_id: str
        """
        self._slo_id = slo_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInterruptRecordsRequest.

        分页指针

        :return: The offset of this ListInterruptRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInterruptRecordsRequest.

        分页指针

        :param offset: The offset of this ListInterruptRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInterruptRecordsRequest.

        每页数量

        :return: The limit of this ListInterruptRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInterruptRecordsRequest.

        每页数量

        :param limit: The limit of this ListInterruptRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def source_id(self):
        r"""Gets the source_id of this ListInterruptRecordsRequest.

        资源ID

        :return: The source_id of this ListInterruptRecordsRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ListInterruptRecordsRequest.

        资源ID

        :param source_id: The source_id of this ListInterruptRecordsRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListInterruptRecordsRequest.

        regionId

        :return: The region_id of this ListInterruptRecordsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListInterruptRecordsRequest.

        regionId

        :param region_id: The region_id of this ListInterruptRecordsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListInterruptRecordsRequest.

        时间范围 - 开始时间

        :return: The start_time of this ListInterruptRecordsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListInterruptRecordsRequest.

        时间范围 - 开始时间

        :param start_time: The start_time of this ListInterruptRecordsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListInterruptRecordsRequest.

        时间范围 - 结束时间

        :return: The end_time of this ListInterruptRecordsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListInterruptRecordsRequest.

        时间范围 - 结束时间

        :param end_time: The end_time of this ListInterruptRecordsRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListInterruptRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
