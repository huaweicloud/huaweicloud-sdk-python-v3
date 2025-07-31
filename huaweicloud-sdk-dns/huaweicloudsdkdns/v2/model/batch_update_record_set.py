# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateRecordSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'description': 'str',
        'ttl': 'int',
        'weight': 'int',
        'records': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'ttl': 'ttl',
        'weight': 'weight',
        'records': 'records'
    }

    def __init__(self, id=None, description=None, ttl=None, weight=None, records=None):
        r"""BatchUpdateRecordSet

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param description: **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。
        :type description: str
        :param ttl: **参数解释：** 记录集的有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300
        :type ttl: int
        :param weight: **参数解释：** 解析记录的权重。 **约束限制：** 在相同域名、类型、线路下的解析记录，规则如下： - 全部设置权重，或全部不设置权重。 - 当不设置权重时，只能创建一个解析记录。 - 当设置权重时，最多能创建20个解析记录。  **取值范围：** 0~1000。 - 当weight&#x3D;null时，表示该解析记录不设置权重。 - 当weight&#x3D;0，表示备用域名解析记录。 - 当weight&gt;0，表示主用域名解析记录。  **默认取值：** null。
        :type weight: int
        :param records: **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type records: list[str]
        """
        
        

        self._id = None
        self._description = None
        self._ttl = None
        self._weight = None
        self._records = None
        self.discriminator = None

        self.id = id
        if description is not None:
            self.description = description
        if ttl is not None:
            self.ttl = ttl
        if weight is not None:
            self.weight = weight
        self.records = records

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateRecordSet.

        **参数解释：** 记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this BatchUpdateRecordSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateRecordSet.

        **参数解释：** 记录集ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this BatchUpdateRecordSet.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this BatchUpdateRecordSet.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :return: The description of this BatchUpdateRecordSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchUpdateRecordSet.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :param description: The description of this BatchUpdateRecordSet.
        :type description: str
        """
        self._description = description

    @property
    def ttl(self):
        r"""Gets the ttl of this BatchUpdateRecordSet.

        **参数解释：** 记录集的有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :return: The ttl of this BatchUpdateRecordSet.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this BatchUpdateRecordSet.

        **参数解释：** 记录集的有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :param ttl: The ttl of this BatchUpdateRecordSet.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def weight(self):
        r"""Gets the weight of this BatchUpdateRecordSet.

        **参数解释：** 解析记录的权重。 **约束限制：** 在相同域名、类型、线路下的解析记录，规则如下： - 全部设置权重，或全部不设置权重。 - 当不设置权重时，只能创建一个解析记录。 - 当设置权重时，最多能创建20个解析记录。  **取值范围：** 0~1000。 - 当weight=null时，表示该解析记录不设置权重。 - 当weight=0，表示备用域名解析记录。 - 当weight>0，表示主用域名解析记录。  **默认取值：** null。

        :return: The weight of this BatchUpdateRecordSet.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this BatchUpdateRecordSet.

        **参数解释：** 解析记录的权重。 **约束限制：** 在相同域名、类型、线路下的解析记录，规则如下： - 全部设置权重，或全部不设置权重。 - 当不设置权重时，只能创建一个解析记录。 - 当设置权重时，最多能创建20个解析记录。  **取值范围：** 0~1000。 - 当weight=null时，表示该解析记录不设置权重。 - 当weight=0，表示备用域名解析记录。 - 当weight>0，表示主用域名解析记录。  **默认取值：** null。

        :param weight: The weight of this BatchUpdateRecordSet.
        :type weight: int
        """
        self._weight = weight

    @property
    def records(self):
        r"""Gets the records of this BatchUpdateRecordSet.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The records of this BatchUpdateRecordSet.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BatchUpdateRecordSet.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param records: The records of this BatchUpdateRecordSet.
        :type records: list[str]
        """
        self._records = records

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
        if not isinstance(other, BatchUpdateRecordSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
