# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVmsTemplateStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'tpl_name': 'str',
        'tpl_type': 'str',
        'has_param': 'bool',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'tpl_type': 'tpl_type',
        'has_param': 'has_param',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, tpl_id=None, tpl_name=None, tpl_type=None, has_param=None, begin_time=None, end_time=None, offset=None, limit=None):
        """ListVmsTemplateStatusRequest

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息基础版模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息基础版模板名称。
        :type tpl_name: str
        :param tpl_type: 智能信息基础版模板分类。 - public：公共模板 - private：个人模板
        :type tpl_type: str
        :param has_param: 智能信息基础版模板是否携带参数，不传查全部模板。
        :type has_param: bool
        :param begin_time: 智能信息基础版模板创建开始时间。 样例为：2019-10-12T07:20:50Z。  &gt; begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 
        :type begin_time: str
        :param end_time: 智能信息基础版模板创建结束时间。 样例为：2019-10-12T07:20:50Z。  &gt; begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 
        :type end_time: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._tpl_id = None
        self._tpl_name = None
        self._tpl_type = None
        self._has_param = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if tpl_type is not None:
            self.tpl_type = tpl_type
        if has_param is not None:
            self.has_param = has_param
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        self.offset = offset
        self.limit = limit

    @property
    def tpl_id(self):
        """Gets the tpl_id of this ListVmsTemplateStatusRequest.

        智能信息基础版模板ID。

        :return: The tpl_id of this ListVmsTemplateStatusRequest.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this ListVmsTemplateStatusRequest.

        智能信息基础版模板ID。

        :param tpl_id: The tpl_id of this ListVmsTemplateStatusRequest.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        """Gets the tpl_name of this ListVmsTemplateStatusRequest.

        智能信息基础版模板名称。

        :return: The tpl_name of this ListVmsTemplateStatusRequest.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this ListVmsTemplateStatusRequest.

        智能信息基础版模板名称。

        :param tpl_name: The tpl_name of this ListVmsTemplateStatusRequest.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def tpl_type(self):
        """Gets the tpl_type of this ListVmsTemplateStatusRequest.

        智能信息基础版模板分类。 - public：公共模板 - private：个人模板

        :return: The tpl_type of this ListVmsTemplateStatusRequest.
        :rtype: str
        """
        return self._tpl_type

    @tpl_type.setter
    def tpl_type(self, tpl_type):
        """Sets the tpl_type of this ListVmsTemplateStatusRequest.

        智能信息基础版模板分类。 - public：公共模板 - private：个人模板

        :param tpl_type: The tpl_type of this ListVmsTemplateStatusRequest.
        :type tpl_type: str
        """
        self._tpl_type = tpl_type

    @property
    def has_param(self):
        """Gets the has_param of this ListVmsTemplateStatusRequest.

        智能信息基础版模板是否携带参数，不传查全部模板。

        :return: The has_param of this ListVmsTemplateStatusRequest.
        :rtype: bool
        """
        return self._has_param

    @has_param.setter
    def has_param(self, has_param):
        """Sets the has_param of this ListVmsTemplateStatusRequest.

        智能信息基础版模板是否携带参数，不传查全部模板。

        :param has_param: The has_param of this ListVmsTemplateStatusRequest.
        :type has_param: bool
        """
        self._has_param = has_param

    @property
    def begin_time(self):
        """Gets the begin_time of this ListVmsTemplateStatusRequest.

        智能信息基础版模板创建开始时间。 样例为：2019-10-12T07:20:50Z。  > begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 

        :return: The begin_time of this ListVmsTemplateStatusRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListVmsTemplateStatusRequest.

        智能信息基础版模板创建开始时间。 样例为：2019-10-12T07:20:50Z。  > begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 

        :param begin_time: The begin_time of this ListVmsTemplateStatusRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListVmsTemplateStatusRequest.

        智能信息基础版模板创建结束时间。 样例为：2019-10-12T07:20:50Z。  > begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 

        :return: The end_time of this ListVmsTemplateStatusRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListVmsTemplateStatusRequest.

        智能信息基础版模板创建结束时间。 样例为：2019-10-12T07:20:50Z。  > begin_time和end_time必须全部为空或全部不为空，并且begin_time不能大于end_time。 

        :param end_time: The end_time of this ListVmsTemplateStatusRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListVmsTemplateStatusRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListVmsTemplateStatusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVmsTemplateStatusRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListVmsTemplateStatusRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListVmsTemplateStatusRequest.

        每页显示的条目数量。

        :return: The limit of this ListVmsTemplateStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVmsTemplateStatusRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListVmsTemplateStatusRequest.
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
        if not isinstance(other, ListVmsTemplateStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
