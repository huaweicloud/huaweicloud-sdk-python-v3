# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryAlarmInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListFactoryAlarmInfoRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID
        :type workspace: str
        :param start_time: 告警的开始时间，默认当前时间的前一个小时，13位时间戳
        :type start_time: int
        :param end_time: 告警的最后时间，默认为当前时间，13位时间戳
        :type end_time: int
        :param offset: 分页的起始页，默认值为0。取值范围大于等于0。
        :type offset: int
        :param limit: 分页返回结果，指定每页最大记录数。默认值10
        :type limit: int
        """
        
        

        self._workspace = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryAlarmInfoRequest.

        工作空间ID

        :return: The workspace of this ListFactoryAlarmInfoRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryAlarmInfoRequest.

        工作空间ID

        :param workspace: The workspace of this ListFactoryAlarmInfoRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def start_time(self):
        r"""Gets the start_time of this ListFactoryAlarmInfoRequest.

        告警的开始时间，默认当前时间的前一个小时，13位时间戳

        :return: The start_time of this ListFactoryAlarmInfoRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListFactoryAlarmInfoRequest.

        告警的开始时间，默认当前时间的前一个小时，13位时间戳

        :param start_time: The start_time of this ListFactoryAlarmInfoRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFactoryAlarmInfoRequest.

        告警的最后时间，默认为当前时间，13位时间戳

        :return: The end_time of this ListFactoryAlarmInfoRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFactoryAlarmInfoRequest.

        告警的最后时间，默认为当前时间，13位时间戳

        :param end_time: The end_time of this ListFactoryAlarmInfoRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryAlarmInfoRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :return: The offset of this ListFactoryAlarmInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryAlarmInfoRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :param offset: The offset of this ListFactoryAlarmInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryAlarmInfoRequest.

        分页返回结果，指定每页最大记录数。默认值10

        :return: The limit of this ListFactoryAlarmInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryAlarmInfoRequest.

        分页返回结果，指定每页最大记录数。默认值10

        :param limit: The limit of this ListFactoryAlarmInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFactoryAlarmInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
