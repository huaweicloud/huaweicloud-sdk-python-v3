# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiPolicyGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'protection_object': 'str',
        'object_type': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'protection_object': 'protection_object',
        'object_type': 'object_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, group_name=None, protection_object=None, object_type=None, offset=None, limit=None):
        r"""ListAiPolicyGroupsRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 
        :type group_id: str
        :param group_name: **参数解释**： 策略组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type group_name: str
        :param protection_object: **参数解释**： 防护对象 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type protection_object: str
        :param object_type: **参数解释**: 对象类型 **约束限制**: 不涉及 **取值范围**: - 0：云服务 - 1：三方  **默认取值**: 不涉及 
        :type object_type: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        """
        
        

        self._group_id = None
        self._group_name = None
        self._protection_object = None
        self._object_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if protection_object is not None:
            self.protection_object = protection_object
        if object_type is not None:
            self.object_type = object_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAiPolicyGroupsRequest.

        **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 

        :return: The group_id of this ListAiPolicyGroupsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAiPolicyGroupsRequest.

        **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 

        :param group_id: The group_id of this ListAiPolicyGroupsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListAiPolicyGroupsRequest.

        **参数解释**： 策略组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The group_name of this ListAiPolicyGroupsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListAiPolicyGroupsRequest.

        **参数解释**： 策略组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param group_name: The group_name of this ListAiPolicyGroupsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def protection_object(self):
        r"""Gets the protection_object of this ListAiPolicyGroupsRequest.

        **参数解释**： 防护对象 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The protection_object of this ListAiPolicyGroupsRequest.
        :rtype: str
        """
        return self._protection_object

    @protection_object.setter
    def protection_object(self, protection_object):
        r"""Sets the protection_object of this ListAiPolicyGroupsRequest.

        **参数解释**： 防护对象 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param protection_object: The protection_object of this ListAiPolicyGroupsRequest.
        :type protection_object: str
        """
        self._protection_object = protection_object

    @property
    def object_type(self):
        r"""Gets the object_type of this ListAiPolicyGroupsRequest.

        **参数解释**: 对象类型 **约束限制**: 不涉及 **取值范围**: - 0：云服务 - 1：三方  **默认取值**: 不涉及 

        :return: The object_type of this ListAiPolicyGroupsRequest.
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListAiPolicyGroupsRequest.

        **参数解释**: 对象类型 **约束限制**: 不涉及 **取值范围**: - 0：云服务 - 1：三方  **默认取值**: 不涉及 

        :param object_type: The object_type of this ListAiPolicyGroupsRequest.
        :type object_type: int
        """
        self._object_type = object_type

    @property
    def offset(self):
        r"""Gets the offset of this ListAiPolicyGroupsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListAiPolicyGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiPolicyGroupsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListAiPolicyGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAiPolicyGroupsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAiPolicyGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiPolicyGroupsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAiPolicyGroupsRequest.
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
        if not isinstance(other, ListAiPolicyGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
