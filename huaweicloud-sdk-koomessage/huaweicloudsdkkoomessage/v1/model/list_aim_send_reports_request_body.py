# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimSendReportsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_type': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'report_type': 'report_type',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, report_type=None, tpl_id=None, tpl_name=None, begin_time=None, end_time=None, offset=None, limit=None):
        r"""ListAimSendReportsRequestBody

        The model defined in huaweicloud sdk

        :param report_type: 报表类型。  - 1：日报表 - 2：月报表  &gt; 若不填，默认是1，即查询日报表。 
        :type report_type: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param begin_time: 开始时间。格式为：2022-05-01T00:00:00Z。
        :type begin_time: str
        :param end_time: 结束时间。格式为：2022-05-01T00:00:00Z。
        :type end_time: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。  &gt; 为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 
        :type offset: int
        :param limit: 每页显示的条目数量。 
        :type limit: int
        """
        
        

        self._report_type = None
        self._tpl_id = None
        self._tpl_name = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if report_type is not None:
            self.report_type = report_type
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def report_type(self):
        r"""Gets the report_type of this ListAimSendReportsRequestBody.

        报表类型。  - 1：日报表 - 2：月报表  > 若不填，默认是1，即查询日报表。 

        :return: The report_type of this ListAimSendReportsRequestBody.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        r"""Sets the report_type of this ListAimSendReportsRequestBody.

        报表类型。  - 1：日报表 - 2：月报表  > 若不填，默认是1，即查询日报表。 

        :param report_type: The report_type of this ListAimSendReportsRequestBody.
        :type report_type: str
        """
        self._report_type = report_type

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this ListAimSendReportsRequestBody.

        智能信息模板ID。

        :return: The tpl_id of this ListAimSendReportsRequestBody.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this ListAimSendReportsRequestBody.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this ListAimSendReportsRequestBody.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this ListAimSendReportsRequestBody.

        智能信息模板名称。

        :return: The tpl_name of this ListAimSendReportsRequestBody.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this ListAimSendReportsRequestBody.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this ListAimSendReportsRequestBody.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListAimSendReportsRequestBody.

        开始时间。格式为：2022-05-01T00:00:00Z。

        :return: The begin_time of this ListAimSendReportsRequestBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListAimSendReportsRequestBody.

        开始时间。格式为：2022-05-01T00:00:00Z。

        :param begin_time: The begin_time of this ListAimSendReportsRequestBody.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAimSendReportsRequestBody.

        结束时间。格式为：2022-05-01T00:00:00Z。

        :return: The end_time of this ListAimSendReportsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAimSendReportsRequestBody.

        结束时间。格式为：2022-05-01T00:00:00Z。

        :param end_time: The end_time of this ListAimSendReportsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListAimSendReportsRequestBody.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  > 为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :return: The offset of this ListAimSendReportsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAimSendReportsRequestBody.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  > 为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :param offset: The offset of this ListAimSendReportsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAimSendReportsRequestBody.

        每页显示的条目数量。 

        :return: The limit of this ListAimSendReportsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAimSendReportsRequestBody.

        每页显示的条目数量。 

        :param limit: The limit of this ListAimSendReportsRequestBody.
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
        if not isinstance(other, ListAimSendReportsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
