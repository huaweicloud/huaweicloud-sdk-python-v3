# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlgorithmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order': 'str',
        'limit': 'int',
        'offset': 'int',
        'lang': 'str',
        'id': 'str',
        'name': 'str',
        'user_id': 'str',
        'visibility': 'str',
        'create_time_start': 'int',
        'create_time_end': 'int'
    }

    attribute_map = {
        'order': 'order',
        'limit': 'limit',
        'offset': 'offset',
        'lang': 'lang',
        'id': 'id',
        'name': 'name',
        'user_id': 'user_id',
        'visibility': 'visibility',
        'create_time_start': 'create_time_start',
        'create_time_end': 'create_time_end'
    }

    def __init__(self, order=None, limit=None, offset=None, lang=None, id=None, name=None, user_id=None, visibility=None, create_time_start=None, create_time_end=None):
        r"""ListAlgorithmsRequest

        The model defined in huaweicloud sdk

        :param order: **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 
        :type order: str
        :param limit: **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 
        :type offset: int
        :param lang: **参数解释**： 编程语言，可选python,c++,java **约束限制**： 不涉及 **取值范围**： python,c++,java **默认取值**： 0 
        :type lang: str
        :param id: **参数解释**： 算法id **约束限制**： 不涉及 **取值范围**： 长度[0,64] **默认取值**： 不涉及 
        :type id: str
        :param name: **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 0 
        :type name: str
        :param user_id: **参数解释**： 用户名 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 0 
        :type user_id: str
        :param visibility: **参数解释**： 可见性 **约束限制**： 不涉及 **取值范围**： PUBLIC, PRIVATE **默认取值**： 无 
        :type visibility: str
        :param create_time_start: **参数解释**： 创建时间过滤条件，初始过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 
        :type create_time_start: int
        :param create_time_end: **参数解释**： 创建时间过滤条件，终止过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 
        :type create_time_end: int
        """
        
        

        self._order = None
        self._limit = None
        self._offset = None
        self._lang = None
        self._id = None
        self._name = None
        self._user_id = None
        self._visibility = None
        self._create_time_start = None
        self._create_time_end = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if lang is not None:
            self.lang = lang
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id
        if visibility is not None:
            self.visibility = visibility
        if create_time_start is not None:
            self.create_time_start = create_time_start
        if create_time_end is not None:
            self.create_time_end = create_time_end

    @property
    def order(self):
        r"""Gets the order of this ListAlgorithmsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 

        :return: The order of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListAlgorithmsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 

        :param order: The order of this ListAlgorithmsRequest.
        :type order: str
        """
        self._order = order

    @property
    def limit(self):
        r"""Gets the limit of this ListAlgorithmsRequest.

        **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 

        :return: The limit of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlgorithmsRequest.

        **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 

        :param limit: The limit of this ListAlgorithmsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAlgorithmsRequest.

        **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 

        :return: The offset of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlgorithmsRequest.

        **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 

        :param offset: The offset of this ListAlgorithmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def lang(self):
        r"""Gets the lang of this ListAlgorithmsRequest.

        **参数解释**： 编程语言，可选python,c++,java **约束限制**： 不涉及 **取值范围**： python,c++,java **默认取值**： 0 

        :return: The lang of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this ListAlgorithmsRequest.

        **参数解释**： 编程语言，可选python,c++,java **约束限制**： 不涉及 **取值范围**： python,c++,java **默认取值**： 0 

        :param lang: The lang of this ListAlgorithmsRequest.
        :type lang: str
        """
        self._lang = lang

    @property
    def id(self):
        r"""Gets the id of this ListAlgorithmsRequest.

        **参数解释**： 算法id **约束限制**： 不涉及 **取值范围**： 长度[0,64] **默认取值**： 不涉及 

        :return: The id of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAlgorithmsRequest.

        **参数解释**： 算法id **约束限制**： 不涉及 **取值范围**： 长度[0,64] **默认取值**： 不涉及 

        :param id: The id of this ListAlgorithmsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListAlgorithmsRequest.

        **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 0 

        :return: The name of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAlgorithmsRequest.

        **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 0 

        :param name: The name of this ListAlgorithmsRequest.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        r"""Gets the user_id of this ListAlgorithmsRequest.

        **参数解释**： 用户名 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 0 

        :return: The user_id of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListAlgorithmsRequest.

        **参数解释**： 用户名 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 0 

        :param user_id: The user_id of this ListAlgorithmsRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def visibility(self):
        r"""Gets the visibility of this ListAlgorithmsRequest.

        **参数解释**： 可见性 **约束限制**： 不涉及 **取值范围**： PUBLIC, PRIVATE **默认取值**： 无 

        :return: The visibility of this ListAlgorithmsRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListAlgorithmsRequest.

        **参数解释**： 可见性 **约束限制**： 不涉及 **取值范围**： PUBLIC, PRIVATE **默认取值**： 无 

        :param visibility: The visibility of this ListAlgorithmsRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def create_time_start(self):
        r"""Gets the create_time_start of this ListAlgorithmsRequest.

        **参数解释**： 创建时间过滤条件，初始过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 

        :return: The create_time_start of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._create_time_start

    @create_time_start.setter
    def create_time_start(self, create_time_start):
        r"""Sets the create_time_start of this ListAlgorithmsRequest.

        **参数解释**： 创建时间过滤条件，初始过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 

        :param create_time_start: The create_time_start of this ListAlgorithmsRequest.
        :type create_time_start: int
        """
        self._create_time_start = create_time_start

    @property
    def create_time_end(self):
        r"""Gets the create_time_end of this ListAlgorithmsRequest.

        **参数解释**： 创建时间过滤条件，终止过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 

        :return: The create_time_end of this ListAlgorithmsRequest.
        :rtype: int
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        r"""Sets the create_time_end of this ListAlgorithmsRequest.

        **参数解释**： 创建时间过滤条件，终止过滤时间 **约束限制**： 不涉及 **取值范围**： [0,9999999999999] **默认取值**： 无 

        :param create_time_end: The create_time_end of this ListAlgorithmsRequest.
        :type create_time_end: int
        """
        self._create_time_end = create_time_end

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
        if not isinstance(other, ListAlgorithmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
