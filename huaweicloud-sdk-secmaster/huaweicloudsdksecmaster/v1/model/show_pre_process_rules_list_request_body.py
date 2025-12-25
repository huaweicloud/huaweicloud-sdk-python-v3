# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPreProcessRulesListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapper_ids': 'list[str]',
        'name': 'str',
        'mapping_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'mapper_ids': 'mapper_ids',
        'name': 'name',
        'mapping_id': 'mapping_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, mapper_ids=None, name=None, mapping_id=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ShowPreProcessRulesListRequestBody

        The model defined in huaweicloud sdk

        :param mapper_ids: 映射id列表
        :type mapper_ids: list[str]
        :param name: 名称
        :type name: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param start_time: 创建开始时间
        :type start_time: datetime
        :param end_time: 创建结束时间
        :type end_time: datetime
        :param offset: **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释**: 当前页码 **约束限制**: 不涉及
        :type limit: int
        """
        
        

        self._mapper_ids = None
        self._name = None
        self._mapping_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if mapper_ids is not None:
            self.mapper_ids = mapper_ids
        self.name = name
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.offset = offset
        self.limit = limit

    @property
    def mapper_ids(self):
        r"""Gets the mapper_ids of this ShowPreProcessRulesListRequestBody.

        映射id列表

        :return: The mapper_ids of this ShowPreProcessRulesListRequestBody.
        :rtype: list[str]
        """
        return self._mapper_ids

    @mapper_ids.setter
    def mapper_ids(self, mapper_ids):
        r"""Sets the mapper_ids of this ShowPreProcessRulesListRequestBody.

        映射id列表

        :param mapper_ids: The mapper_ids of this ShowPreProcessRulesListRequestBody.
        :type mapper_ids: list[str]
        """
        self._mapper_ids = mapper_ids

    @property
    def name(self):
        r"""Gets the name of this ShowPreProcessRulesListRequestBody.

        名称

        :return: The name of this ShowPreProcessRulesListRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPreProcessRulesListRequestBody.

        名称

        :param name: The name of this ShowPreProcessRulesListRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this ShowPreProcessRulesListRequestBody.

        映射id

        :return: The mapping_id of this ShowPreProcessRulesListRequestBody.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this ShowPreProcessRulesListRequestBody.

        映射id

        :param mapping_id: The mapping_id of this ShowPreProcessRulesListRequestBody.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowPreProcessRulesListRequestBody.

        创建开始时间

        :return: The start_time of this ShowPreProcessRulesListRequestBody.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowPreProcessRulesListRequestBody.

        创建开始时间

        :param start_time: The start_time of this ShowPreProcessRulesListRequestBody.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowPreProcessRulesListRequestBody.

        创建结束时间

        :return: The end_time of this ShowPreProcessRulesListRequestBody.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowPreProcessRulesListRequestBody.

        创建结束时间

        :param end_time: The end_time of this ShowPreProcessRulesListRequestBody.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowPreProcessRulesListRequestBody.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ShowPreProcessRulesListRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowPreProcessRulesListRequestBody.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ShowPreProcessRulesListRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowPreProcessRulesListRequestBody.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :return: The limit of this ShowPreProcessRulesListRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowPreProcessRulesListRequestBody.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :param limit: The limit of this ShowPreProcessRulesListRequestBody.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowPreProcessRulesListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
