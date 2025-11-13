# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelVendorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'type': 'type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, type=None, sort_key=None, sort_dir=None, limit=None, offset=None):
        r"""ListModelVendorsRequest

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 供应商类型。 **约束限制**： 不涉及 **取值范围**： * system：系统内置 * custom：自定义 **默认取值**： 不涉及 
        :type type: str
        :param sort_key: **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - name：根据创建时间排列。 - status：模型服务状态 - update_time：根据更新时间排列。 **默认取值**： update_time 
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 
        :type sort_dir: str
        :param limit: **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： [0-100000000] **默认取值**： 0 
        :type offset: int
        """
        
        

        self._type = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def type(self):
        r"""Gets the type of this ListModelVendorsRequest.

        **参数解释**： 供应商类型。 **约束限制**： 不涉及 **取值范围**： * system：系统内置 * custom：自定义 **默认取值**： 不涉及 

        :return: The type of this ListModelVendorsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListModelVendorsRequest.

        **参数解释**： 供应商类型。 **约束限制**： 不涉及 **取值范围**： * system：系统内置 * custom：自定义 **默认取值**： 不涉及 

        :param type: The type of this ListModelVendorsRequest.
        :type type: str
        """
        self._type = type

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListModelVendorsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - name：根据创建时间排列。 - status：模型服务状态 - update_time：根据更新时间排列。 **默认取值**： update_time 

        :return: The sort_key of this ListModelVendorsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListModelVendorsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - name：根据创建时间排列。 - status：模型服务状态 - update_time：根据更新时间排列。 **默认取值**： update_time 

        :param sort_key: The sort_key of this ListModelVendorsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListModelVendorsRequest.

        **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 

        :return: The sort_dir of this ListModelVendorsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListModelVendorsRequest.

        **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 

        :param sort_dir: The sort_dir of this ListModelVendorsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListModelVendorsRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 

        :return: The limit of this ListModelVendorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelVendorsRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 

        :param limit: The limit of this ListModelVendorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListModelVendorsRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： [0-100000000] **默认取值**： 0 

        :return: The offset of this ListModelVendorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelVendorsRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： [0-100000000] **默认取值**： 0 

        :param offset: The offset of this ListModelVendorsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListModelVendorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
