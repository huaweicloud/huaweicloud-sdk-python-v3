# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBlackWhiteDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list_ids': 'list[str]',
        'list_type': 'int',
        'object_id': 'str'
    }

    attribute_map = {
        'list_ids': 'list_ids',
        'list_type': 'list_type',
        'object_id': 'object_id'
    }

    def __init__(self, list_ids=None, list_type=None, object_id=None):
        r"""DeleteBlackWhiteDto

        The model defined in huaweicloud sdk

        :param list_ids: **参数解释**： 黑白名单列表ID **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type list_ids: list[str]
        :param list_type: **参数解释**： 黑白名单列表类型 **约束限制**： 不涉及 **取值范围**： 4：黑名单 5：白名单 **默认取值**： 不涉及
        :type list_type: int
        :param object_id: **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type object_id: str
        """
        
        

        self._list_ids = None
        self._list_type = None
        self._object_id = None
        self.discriminator = None

        self.list_ids = list_ids
        self.list_type = list_type
        self.object_id = object_id

    @property
    def list_ids(self):
        r"""Gets the list_ids of this DeleteBlackWhiteDto.

        **参数解释**： 黑白名单列表ID **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The list_ids of this DeleteBlackWhiteDto.
        :rtype: list[str]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        r"""Sets the list_ids of this DeleteBlackWhiteDto.

        **参数解释**： 黑白名单列表ID **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param list_ids: The list_ids of this DeleteBlackWhiteDto.
        :type list_ids: list[str]
        """
        self._list_ids = list_ids

    @property
    def list_type(self):
        r"""Gets the list_type of this DeleteBlackWhiteDto.

        **参数解释**： 黑白名单列表类型 **约束限制**： 不涉及 **取值范围**： 4：黑名单 5：白名单 **默认取值**： 不涉及

        :return: The list_type of this DeleteBlackWhiteDto.
        :rtype: int
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        r"""Sets the list_type of this DeleteBlackWhiteDto.

        **参数解释**： 黑白名单列表类型 **约束限制**： 不涉及 **取值范围**： 4：黑名单 5：白名单 **默认取值**： 不涉及

        :param list_type: The list_type of this DeleteBlackWhiteDto.
        :type list_type: int
        """
        self._list_type = list_type

    @property
    def object_id(self):
        r"""Gets the object_id of this DeleteBlackWhiteDto.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The object_id of this DeleteBlackWhiteDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this DeleteBlackWhiteDto.

        **参数解释**： 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param object_id: The object_id of this DeleteBlackWhiteDto.
        :type object_id: str
        """
        self._object_id = object_id

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
        if not isinstance(other, DeleteBlackWhiteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
