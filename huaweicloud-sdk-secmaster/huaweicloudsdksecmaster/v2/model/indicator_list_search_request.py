# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorListSearchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'name': 'str',
        'dataclass_id': 'str',
        'condition': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'name': 'name',
        'dataclass_id': 'dataclass_id',
        'condition': 'condition',
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, ids=None, name=None, dataclass_id=None, condition=None, offset=None, limit=None, sort_by=None, from_date=None, to_date=None):
        """IndicatorListSearchRequest

        The model defined in huaweicloud sdk

        :param ids: 指标ID列表
        :type ids: list[str]
        :param name: 指标名称
        :type name: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param condition: 查询条件
        :type condition: str
        :param offset: request offset, from 0
        :type offset: int
        :param limit: request limit size
        :type limit: int
        :param sort_by: sort by property, create_time.
        :type sort_by: str
        :param from_date: 查询起始时间
        :type from_date: str
        :param to_date: 查询截止时间
        :type to_date: str
        """
        
        

        self._ids = None
        self._name = None
        self._dataclass_id = None
        self._condition = None
        self._offset = None
        self._limit = None
        self._sort_by = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        self.condition = condition
        self.offset = offset
        self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def ids(self):
        """Gets the ids of this IndicatorListSearchRequest.

        指标ID列表

        :return: The ids of this IndicatorListSearchRequest.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this IndicatorListSearchRequest.

        指标ID列表

        :param ids: The ids of this IndicatorListSearchRequest.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def name(self):
        """Gets the name of this IndicatorListSearchRequest.

        指标名称

        :return: The name of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndicatorListSearchRequest.

        指标名称

        :param name: The name of this IndicatorListSearchRequest.
        :type name: str
        """
        self._name = name

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this IndicatorListSearchRequest.

        数据类ID

        :return: The dataclass_id of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this IndicatorListSearchRequest.

        数据类ID

        :param dataclass_id: The dataclass_id of this IndicatorListSearchRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def condition(self):
        """Gets the condition of this IndicatorListSearchRequest.

        查询条件

        :return: The condition of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this IndicatorListSearchRequest.

        查询条件

        :param condition: The condition of this IndicatorListSearchRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def offset(self):
        """Gets the offset of this IndicatorListSearchRequest.

        request offset, from 0

        :return: The offset of this IndicatorListSearchRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this IndicatorListSearchRequest.

        request offset, from 0

        :param offset: The offset of this IndicatorListSearchRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this IndicatorListSearchRequest.

        request limit size

        :return: The limit of this IndicatorListSearchRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this IndicatorListSearchRequest.

        request limit size

        :param limit: The limit of this IndicatorListSearchRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        """Gets the sort_by of this IndicatorListSearchRequest.

        sort by property, create_time.

        :return: The sort_by of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this IndicatorListSearchRequest.

        sort by property, create_time.

        :param sort_by: The sort_by of this IndicatorListSearchRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def from_date(self):
        """Gets the from_date of this IndicatorListSearchRequest.

        查询起始时间

        :return: The from_date of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this IndicatorListSearchRequest.

        查询起始时间

        :param from_date: The from_date of this IndicatorListSearchRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this IndicatorListSearchRequest.

        查询截止时间

        :return: The to_date of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this IndicatorListSearchRequest.

        查询截止时间

        :param to_date: The to_date of this IndicatorListSearchRequest.
        :type to_date: str
        """
        self._to_date = to_date

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
        if not isinstance(other, IndicatorListSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
