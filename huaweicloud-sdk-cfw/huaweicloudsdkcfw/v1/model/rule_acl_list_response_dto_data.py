# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAclListResponseDTOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'object_id': 'str',
        'up_rules_count': 'int',
        'records': 'list[RuleAclListResponseDTODataRecords]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'object_id': 'object_id',
        'up_rules_count': 'up_rules_count',
        'records': 'records'
    }

    def __init__(self, offset=None, limit=None, total=None, object_id=None, up_rules_count=None, records=None):
        r"""RuleAclListResponseDTOData

        The model defined in huaweicloud sdk

        :param offset: **参数解释**： 偏移量：指定返回记录的开始位置 **取值范围**： 大于或等于0
        :type offset: int
        :param limit: **参数解释**： 每页显示个数 **取值范围**： 1-1024
        :type limit: int
        :param total: **参数解释**： 查询规则列表总条数 **取值范围**： 大于0
        :type total: int
        :param object_id: **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得  **取值范围**：  32位UUID
        :type object_id: str
        :param up_rules_count: **参数解释**： 顶部规则数量 **取值范围**： 不涉及
        :type up_rules_count: int
        :param records: **参数解释**： 查询规则列表记录
        :type records: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        
        

        self._offset = None
        self._limit = None
        self._total = None
        self._object_id = None
        self._up_rules_count = None
        self._records = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if object_id is not None:
            self.object_id = object_id
        if up_rules_count is not None:
            self.up_rules_count = up_rules_count
        if records is not None:
            self.records = records

    @property
    def offset(self):
        r"""Gets the offset of this RuleAclListResponseDTOData.

        **参数解释**： 偏移量：指定返回记录的开始位置 **取值范围**： 大于或等于0

        :return: The offset of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this RuleAclListResponseDTOData.

        **参数解释**： 偏移量：指定返回记录的开始位置 **取值范围**： 大于或等于0

        :param offset: The offset of this RuleAclListResponseDTOData.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this RuleAclListResponseDTOData.

        **参数解释**： 每页显示个数 **取值范围**： 1-1024

        :return: The limit of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this RuleAclListResponseDTOData.

        **参数解释**： 每页显示个数 **取值范围**： 1-1024

        :param limit: The limit of this RuleAclListResponseDTOData.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this RuleAclListResponseDTOData.

        **参数解释**： 查询规则列表总条数 **取值范围**： 大于0

        :return: The total of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this RuleAclListResponseDTOData.

        **参数解释**： 查询规则列表总条数 **取值范围**： 大于0

        :param total: The total of this RuleAclListResponseDTOData.
        :type total: int
        """
        self._total = total

    @property
    def object_id(self):
        r"""Gets the object_id of this RuleAclListResponseDTOData.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得  **取值范围**：  32位UUID

        :return: The object_id of this RuleAclListResponseDTOData.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this RuleAclListResponseDTOData.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得  **取值范围**：  32位UUID

        :param object_id: The object_id of this RuleAclListResponseDTOData.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def up_rules_count(self):
        r"""Gets the up_rules_count of this RuleAclListResponseDTOData.

        **参数解释**： 顶部规则数量 **取值范围**： 不涉及

        :return: The up_rules_count of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._up_rules_count

    @up_rules_count.setter
    def up_rules_count(self, up_rules_count):
        r"""Sets the up_rules_count of this RuleAclListResponseDTOData.

        **参数解释**： 顶部规则数量 **取值范围**： 不涉及

        :param up_rules_count: The up_rules_count of this RuleAclListResponseDTOData.
        :type up_rules_count: int
        """
        self._up_rules_count = up_rules_count

    @property
    def records(self):
        r"""Gets the records of this RuleAclListResponseDTOData.

        **参数解释**： 查询规则列表记录

        :return: The records of this RuleAclListResponseDTOData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this RuleAclListResponseDTOData.

        **参数解释**： 查询规则列表记录

        :param records: The records of this RuleAclListResponseDTOData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        self._records = records

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
        if not isinstance(other, RuleAclListResponseDTOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
