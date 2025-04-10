# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationObjectOverviewInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'src_count': 'str',
        'dst_count': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'type': 'type',
        'src_count': 'src_count',
        'dst_count': 'dst_count',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, type=None, src_count=None, dst_count=None, status=None, start_time=None, end_time=None):
        r"""MigrationObjectOverviewInfo

        The model defined in huaweicloud sdk

        :param type: 类型。
        :type type: str
        :param src_count: 待迁移数量。
        :type src_count: str
        :param dst_count: 已迁移数量。
        :type dst_count: str
        :param status: 状态.
        :type status: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        """
        
        

        self._type = None
        self._src_count = None
        self._dst_count = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if src_count is not None:
            self.src_count = src_count
        if dst_count is not None:
            self.dst_count = dst_count
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def type(self):
        r"""Gets the type of this MigrationObjectOverviewInfo.

        类型。

        :return: The type of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MigrationObjectOverviewInfo.

        类型。

        :param type: The type of this MigrationObjectOverviewInfo.
        :type type: str
        """
        self._type = type

    @property
    def src_count(self):
        r"""Gets the src_count of this MigrationObjectOverviewInfo.

        待迁移数量。

        :return: The src_count of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._src_count

    @src_count.setter
    def src_count(self, src_count):
        r"""Sets the src_count of this MigrationObjectOverviewInfo.

        待迁移数量。

        :param src_count: The src_count of this MigrationObjectOverviewInfo.
        :type src_count: str
        """
        self._src_count = src_count

    @property
    def dst_count(self):
        r"""Gets the dst_count of this MigrationObjectOverviewInfo.

        已迁移数量。

        :return: The dst_count of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._dst_count

    @dst_count.setter
    def dst_count(self, dst_count):
        r"""Sets the dst_count of this MigrationObjectOverviewInfo.

        已迁移数量。

        :param dst_count: The dst_count of this MigrationObjectOverviewInfo.
        :type dst_count: str
        """
        self._dst_count = dst_count

    @property
    def status(self):
        r"""Gets the status of this MigrationObjectOverviewInfo.

        状态.

        :return: The status of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MigrationObjectOverviewInfo.

        状态.

        :param status: The status of this MigrationObjectOverviewInfo.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this MigrationObjectOverviewInfo.

        开始时间。

        :return: The start_time of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this MigrationObjectOverviewInfo.

        开始时间。

        :param start_time: The start_time of this MigrationObjectOverviewInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this MigrationObjectOverviewInfo.

        结束时间。

        :return: The end_time of this MigrationObjectOverviewInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this MigrationObjectOverviewInfo.

        结束时间。

        :param end_time: The end_time of this MigrationObjectOverviewInfo.
        :type end_time: str
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
        if not isinstance(other, MigrationObjectOverviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
