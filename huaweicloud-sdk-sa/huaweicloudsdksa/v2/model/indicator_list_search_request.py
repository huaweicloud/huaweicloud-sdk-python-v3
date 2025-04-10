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
        'type': 'str',
        'dataclass_id': 'str',
        'condition': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_by': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'name': 'name',
        'type': 'type',
        'dataclass_id': 'dataclass_id',
        'condition': 'condition',
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by'
    }

    def __init__(self, ids=None, name=None, type=None, dataclass_id=None, condition=None, offset=None, limit=None, sort_by=None):
        r"""IndicatorListSearchRequest

        The model defined in huaweicloud sdk

        :param ids: id list
        :type ids: list[str]
        :param name: 指标名称
        :type name: str
        :param type: 类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）
        :type type: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param condition: search condition
        :type condition: str
        :param offset: request offset, from 0
        :type offset: int
        :param limit: request limit size
        :type limit: int
        :param sort_by: sort by property, create_time.
        :type sort_by: str
        """
        
        

        self._ids = None
        self._name = None
        self._type = None
        self._dataclass_id = None
        self._condition = None
        self._offset = None
        self._limit = None
        self._sort_by = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if condition is not None:
            self.condition = condition
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def ids(self):
        r"""Gets the ids of this IndicatorListSearchRequest.

        id list

        :return: The ids of this IndicatorListSearchRequest.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this IndicatorListSearchRequest.

        id list

        :param ids: The ids of this IndicatorListSearchRequest.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def name(self):
        r"""Gets the name of this IndicatorListSearchRequest.

        指标名称

        :return: The name of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IndicatorListSearchRequest.

        指标名称

        :param name: The name of this IndicatorListSearchRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this IndicatorListSearchRequest.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :return: The type of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IndicatorListSearchRequest.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :param type: The type of this IndicatorListSearchRequest.
        :type type: str
        """
        self._type = type

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this IndicatorListSearchRequest.

        数据类ID

        :return: The dataclass_id of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this IndicatorListSearchRequest.

        数据类ID

        :param dataclass_id: The dataclass_id of this IndicatorListSearchRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def condition(self):
        r"""Gets the condition of this IndicatorListSearchRequest.

        search condition

        :return: The condition of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this IndicatorListSearchRequest.

        search condition

        :param condition: The condition of this IndicatorListSearchRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def offset(self):
        r"""Gets the offset of this IndicatorListSearchRequest.

        request offset, from 0

        :return: The offset of this IndicatorListSearchRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this IndicatorListSearchRequest.

        request offset, from 0

        :param offset: The offset of this IndicatorListSearchRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this IndicatorListSearchRequest.

        request limit size

        :return: The limit of this IndicatorListSearchRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this IndicatorListSearchRequest.

        request limit size

        :param limit: The limit of this IndicatorListSearchRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this IndicatorListSearchRequest.

        sort by property, create_time.

        :return: The sort_by of this IndicatorListSearchRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this IndicatorListSearchRequest.

        sort by property, create_time.

        :param sort_by: The sort_by of this IndicatorListSearchRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

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
