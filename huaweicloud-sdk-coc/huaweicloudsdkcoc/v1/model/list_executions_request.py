# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecutionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'creator': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'document_name': 'str',
        'document_id': 'str',
        'tags': 'str',
        'exclude_child_executions': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'creator': 'creator',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'document_name': 'document_name',
        'document_id': 'document_id',
        'tags': 'tags',
        'exclude_child_executions': 'exclude_child_executions'
    }

    def __init__(self, limit=None, offset=None, creator=None, start_time=None, end_time=None, document_name=None, document_id=None, tags=None, exclude_child_executions=None):
        r"""ListExecutionsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页参数：每页返回记录个数限制 不传默认第一页查10个
        :type limit: int
        :param offset: 分页参数：从offset指定的下一条数据开始查询，不传默认0
        :type offset: int
        :param creator: 创建人，模糊查询
        :type creator: str
        :param start_time: 开始时间，大于
        :type start_time: int
        :param end_time: 结束时间，小于
        :type end_time: int
        :param document_name: 作业名称，模糊查询
        :type document_name: str
        :param document_id: 作业id
        :type document_id: str
        :param tags: 标签过滤条件，例：?tags&#x3D;key1&#x3D;value1,key2&#x3D;value2
        :type tags: str
        :param exclude_child_executions: 列表查询不返回子工单
        :type exclude_child_executions: bool
        """
        
        

        self._limit = None
        self._offset = None
        self._creator = None
        self._start_time = None
        self._end_time = None
        self._document_name = None
        self._document_id = None
        self._tags = None
        self._exclude_child_executions = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if creator is not None:
            self.creator = creator
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if document_name is not None:
            self.document_name = document_name
        if document_id is not None:
            self.document_id = document_id
        if tags is not None:
            self.tags = tags
        if exclude_child_executions is not None:
            self.exclude_child_executions = exclude_child_executions

    @property
    def limit(self):
        r"""Gets the limit of this ListExecutionsRequest.

        分页参数：每页返回记录个数限制 不传默认第一页查10个

        :return: The limit of this ListExecutionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExecutionsRequest.

        分页参数：每页返回记录个数限制 不传默认第一页查10个

        :param limit: The limit of this ListExecutionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListExecutionsRequest.

        分页参数：从offset指定的下一条数据开始查询，不传默认0

        :return: The offset of this ListExecutionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExecutionsRequest.

        分页参数：从offset指定的下一条数据开始查询，不传默认0

        :param offset: The offset of this ListExecutionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def creator(self):
        r"""Gets the creator of this ListExecutionsRequest.

        创建人，模糊查询

        :return: The creator of this ListExecutionsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListExecutionsRequest.

        创建人，模糊查询

        :param creator: The creator of this ListExecutionsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def start_time(self):
        r"""Gets the start_time of this ListExecutionsRequest.

        开始时间，大于

        :return: The start_time of this ListExecutionsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListExecutionsRequest.

        开始时间，大于

        :param start_time: The start_time of this ListExecutionsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListExecutionsRequest.

        结束时间，小于

        :return: The end_time of this ListExecutionsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListExecutionsRequest.

        结束时间，小于

        :param end_time: The end_time of this ListExecutionsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def document_name(self):
        r"""Gets the document_name of this ListExecutionsRequest.

        作业名称，模糊查询

        :return: The document_name of this ListExecutionsRequest.
        :rtype: str
        """
        return self._document_name

    @document_name.setter
    def document_name(self, document_name):
        r"""Sets the document_name of this ListExecutionsRequest.

        作业名称，模糊查询

        :param document_name: The document_name of this ListExecutionsRequest.
        :type document_name: str
        """
        self._document_name = document_name

    @property
    def document_id(self):
        r"""Gets the document_id of this ListExecutionsRequest.

        作业id

        :return: The document_id of this ListExecutionsRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this ListExecutionsRequest.

        作业id

        :param document_id: The document_id of this ListExecutionsRequest.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def tags(self):
        r"""Gets the tags of this ListExecutionsRequest.

        标签过滤条件，例：?tags=key1=value1,key2=value2

        :return: The tags of this ListExecutionsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListExecutionsRequest.

        标签过滤条件，例：?tags=key1=value1,key2=value2

        :param tags: The tags of this ListExecutionsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def exclude_child_executions(self):
        r"""Gets the exclude_child_executions of this ListExecutionsRequest.

        列表查询不返回子工单

        :return: The exclude_child_executions of this ListExecutionsRequest.
        :rtype: bool
        """
        return self._exclude_child_executions

    @exclude_child_executions.setter
    def exclude_child_executions(self, exclude_child_executions):
        r"""Sets the exclude_child_executions of this ListExecutionsRequest.

        列表查询不返回子工单

        :param exclude_child_executions: The exclude_child_executions of this ListExecutionsRequest.
        :type exclude_child_executions: bool
        """
        self._exclude_child_executions = exclude_child_executions

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
        if not isinstance(other, ListExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
