# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHbaInfoHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListHbaInfoHistoryRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param start_time: **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当天0点（UTC时区）。
        :type start_time: datetime
        :param end_time: **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当前时间（UTC时区）。
        :type end_time: datetime
        :param offset: **参数描述** 偏移量。 **约束限制**: 不涉及。 **取值范围** 大于等于0。 **默认值** 0 
        :type offset: int
        :param limit: **参数描述** 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认值** 10 
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListHbaInfoHistoryRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListHbaInfoHistoryRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListHbaInfoHistoryRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListHbaInfoHistoryRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListHbaInfoHistoryRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListHbaInfoHistoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListHbaInfoHistoryRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListHbaInfoHistoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHbaInfoHistoryRequest.

        **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当天0点（UTC时区）。

        :return: The start_time of this ListHbaInfoHistoryRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHbaInfoHistoryRequest.

        **参数解释**: 开始时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当天0点（UTC时区）。

        :param start_time: The start_time of this ListHbaInfoHistoryRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHbaInfoHistoryRequest.

        **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当前时间（UTC时区）。

        :return: The end_time of this ListHbaInfoHistoryRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHbaInfoHistoryRequest.

        **参数解释**: 结束时间。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 默认当前时间（UTC时区）。

        :param end_time: The end_time of this ListHbaInfoHistoryRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListHbaInfoHistoryRequest.

        **参数描述** 偏移量。 **约束限制**: 不涉及。 **取值范围** 大于等于0。 **默认值** 0 

        :return: The offset of this ListHbaInfoHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHbaInfoHistoryRequest.

        **参数描述** 偏移量。 **约束限制**: 不涉及。 **取值范围** 大于等于0。 **默认值** 0 

        :param offset: The offset of this ListHbaInfoHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHbaInfoHistoryRequest.

        **参数描述** 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认值** 10 

        :return: The limit of this ListHbaInfoHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHbaInfoHistoryRequest.

        **参数描述** 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认值** 10 

        :param limit: The limit of this ListHbaInfoHistoryRequest.
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
        if not isinstance(other, ListHbaInfoHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
