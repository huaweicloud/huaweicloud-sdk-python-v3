# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimTemplateReportsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_ids': 'list[str]',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'tpl_ids': 'tpl_ids',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, tpl_ids=None, begin_time=None, end_time=None, offset=None, limit=None):
        """ListAimTemplateReportsRequestBody

        The model defined in huaweicloud sdk

        :param tpl_ids: 智能信息模板ID列表，一次最多请求100个。 
        :type tpl_ids: list[str]
        :param begin_time: 模板报表查询开始时间。样例：2019-10-12T07:20:50.522Z。  &gt;开始时间和结束时间最多间隔90天，超出时间限制返回为空。 
        :type begin_time: str
        :param end_time: 模板报表查询结束时间。样例：2019-10-12T07:20:50.522Z。  &gt;开始时间和结束时间最多间隔90天，超出时间限制返回为空。 
        :type end_time: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。 
        :type offset: int
        :param limit: 每页显示的条目数量。 
        :type limit: int
        """
        
        

        self._tpl_ids = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.tpl_ids = tpl_ids
        self.begin_time = begin_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def tpl_ids(self):
        """Gets the tpl_ids of this ListAimTemplateReportsRequestBody.

        智能信息模板ID列表，一次最多请求100个。 

        :return: The tpl_ids of this ListAimTemplateReportsRequestBody.
        :rtype: list[str]
        """
        return self._tpl_ids

    @tpl_ids.setter
    def tpl_ids(self, tpl_ids):
        """Sets the tpl_ids of this ListAimTemplateReportsRequestBody.

        智能信息模板ID列表，一次最多请求100个。 

        :param tpl_ids: The tpl_ids of this ListAimTemplateReportsRequestBody.
        :type tpl_ids: list[str]
        """
        self._tpl_ids = tpl_ids

    @property
    def begin_time(self):
        """Gets the begin_time of this ListAimTemplateReportsRequestBody.

        模板报表查询开始时间。样例：2019-10-12T07:20:50.522Z。  >开始时间和结束时间最多间隔90天，超出时间限制返回为空。 

        :return: The begin_time of this ListAimTemplateReportsRequestBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListAimTemplateReportsRequestBody.

        模板报表查询开始时间。样例：2019-10-12T07:20:50.522Z。  >开始时间和结束时间最多间隔90天，超出时间限制返回为空。 

        :param begin_time: The begin_time of this ListAimTemplateReportsRequestBody.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAimTemplateReportsRequestBody.

        模板报表查询结束时间。样例：2019-10-12T07:20:50.522Z。  >开始时间和结束时间最多间隔90天，超出时间限制返回为空。 

        :return: The end_time of this ListAimTemplateReportsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAimTemplateReportsRequestBody.

        模板报表查询结束时间。样例：2019-10-12T07:20:50.522Z。  >开始时间和结束时间最多间隔90天，超出时间限制返回为空。 

        :param end_time: The end_time of this ListAimTemplateReportsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListAimTemplateReportsRequestBody.

        偏移量，表示从此偏移量开始查询，offset大于等于0。 

        :return: The offset of this ListAimTemplateReportsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAimTemplateReportsRequestBody.

        偏移量，表示从此偏移量开始查询，offset大于等于0。 

        :param offset: The offset of this ListAimTemplateReportsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAimTemplateReportsRequestBody.

        每页显示的条目数量。 

        :return: The limit of this ListAimTemplateReportsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAimTemplateReportsRequestBody.

        每页显示的条目数量。 

        :param limit: The limit of this ListAimTemplateReportsRequestBody.
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
        if not isinstance(other, ListAimTemplateReportsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
