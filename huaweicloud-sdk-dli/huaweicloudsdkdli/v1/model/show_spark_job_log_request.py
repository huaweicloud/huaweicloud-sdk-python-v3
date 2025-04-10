# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_id': 'str',
        '_from': 'int',
        'index': 'int',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'batch_id': 'batch_id',
        '_from': 'from',
        'index': 'index',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, batch_id=None, _from=None, index=None, size=None, type=None):
        r"""ShowSparkJobLogRequest

        The model defined in huaweicloud sdk

        :param batch_id: 批处理作业的ID。
        :type batch_id: str
        :param _from: 起始日志的行号，默认显示最后100行日志。如果日志不足100行，从0行开始显示。
        :type _from: int
        :param index: 当提交的作业进行重试时，会有多个driver日志。index用于指定driver日志的索引号，默认为0。需与type参数一起使用。
        :type index: int
        :param size: 查询日志的数量。
        :type size: int
        :param type: 当type填写driver时，输出Spark Driver日志。
        :type type: str
        """
        
        

        self._batch_id = None
        self.__from = None
        self._index = None
        self._size = None
        self._type = None
        self.discriminator = None

        self.batch_id = batch_id
        if _from is not None:
            self._from = _from
        if index is not None:
            self.index = index
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def batch_id(self):
        r"""Gets the batch_id of this ShowSparkJobLogRequest.

        批处理作业的ID。

        :return: The batch_id of this ShowSparkJobLogRequest.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this ShowSparkJobLogRequest.

        批处理作业的ID。

        :param batch_id: The batch_id of this ShowSparkJobLogRequest.
        :type batch_id: str
        """
        self._batch_id = batch_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowSparkJobLogRequest.

        起始日志的行号，默认显示最后100行日志。如果日志不足100行，从0行开始显示。

        :return: The _from of this ShowSparkJobLogRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowSparkJobLogRequest.

        起始日志的行号，默认显示最后100行日志。如果日志不足100行，从0行开始显示。

        :param _from: The _from of this ShowSparkJobLogRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def index(self):
        r"""Gets the index of this ShowSparkJobLogRequest.

        当提交的作业进行重试时，会有多个driver日志。index用于指定driver日志的索引号，默认为0。需与type参数一起使用。

        :return: The index of this ShowSparkJobLogRequest.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ShowSparkJobLogRequest.

        当提交的作业进行重试时，会有多个driver日志。index用于指定driver日志的索引号，默认为0。需与type参数一起使用。

        :param index: The index of this ShowSparkJobLogRequest.
        :type index: int
        """
        self._index = index

    @property
    def size(self):
        r"""Gets the size of this ShowSparkJobLogRequest.

        查询日志的数量。

        :return: The size of this ShowSparkJobLogRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowSparkJobLogRequest.

        查询日志的数量。

        :param size: The size of this ShowSparkJobLogRequest.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ShowSparkJobLogRequest.

        当type填写driver时，输出Spark Driver日志。

        :return: The type of this ShowSparkJobLogRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSparkJobLogRequest.

        当type填写driver时，输出Spark Driver日志。

        :param type: The type of this ShowSparkJobLogRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowSparkJobLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
