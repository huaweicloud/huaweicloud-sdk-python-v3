# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectionDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collection_name': 'str',
        'index_num': 'int',
        'entity_num': 'int',
        'load_state': 'str',
        'create_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'collection_name': 'collection_name',
        'index_num': 'index_num',
        'entity_num': 'entity_num',
        'load_state': 'load_state',
        'create_time': 'create_time',
        'description': 'description'
    }

    def __init__(self, collection_name=None, index_num=None, entity_num=None, load_state=None, create_time=None, description=None):
        r"""ListCollectionDetails

        The model defined in huaweicloud sdk

        :param collection_name: **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type collection_name: str
        :param index_num: **参数解释：** 索引数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type index_num: int
        :param entity_num: **参数解释：** collection中的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type entity_num: int
        :param load_state: **参数解释：** 标识当前Collection加载状态。 **约束限制：** 不涉及。 **取值范围：** 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。 **默认取值:** 不涉及。
        :type load_state: str
        :param create_time: **参数解释：** 创建时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ\&quot;。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type create_time: str
        :param description: **参数解释：** collection的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type description: str
        """
        
        

        self._collection_name = None
        self._index_num = None
        self._entity_num = None
        self._load_state = None
        self._create_time = None
        self._description = None
        self.discriminator = None

        if collection_name is not None:
            self.collection_name = collection_name
        if index_num is not None:
            self.index_num = index_num
        if entity_num is not None:
            self.entity_num = entity_num
        if load_state is not None:
            self.load_state = load_state
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description

    @property
    def collection_name(self):
        r"""Gets the collection_name of this ListCollectionDetails.

        **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The collection_name of this ListCollectionDetails.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this ListCollectionDetails.

        **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param collection_name: The collection_name of this ListCollectionDetails.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def index_num(self):
        r"""Gets the index_num of this ListCollectionDetails.

        **参数解释：** 索引数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The index_num of this ListCollectionDetails.
        :rtype: int
        """
        return self._index_num

    @index_num.setter
    def index_num(self, index_num):
        r"""Sets the index_num of this ListCollectionDetails.

        **参数解释：** 索引数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param index_num: The index_num of this ListCollectionDetails.
        :type index_num: int
        """
        self._index_num = index_num

    @property
    def entity_num(self):
        r"""Gets the entity_num of this ListCollectionDetails.

        **参数解释：** collection中的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The entity_num of this ListCollectionDetails.
        :rtype: int
        """
        return self._entity_num

    @entity_num.setter
    def entity_num(self, entity_num):
        r"""Sets the entity_num of this ListCollectionDetails.

        **参数解释：** collection中的entity数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param entity_num: The entity_num of this ListCollectionDetails.
        :type entity_num: int
        """
        self._entity_num = entity_num

    @property
    def load_state(self):
        r"""Gets the load_state of this ListCollectionDetails.

        **参数解释：** 标识当前Collection加载状态。 **约束限制：** 不涉及。 **取值范围：** 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。 **默认取值:** 不涉及。

        :return: The load_state of this ListCollectionDetails.
        :rtype: str
        """
        return self._load_state

    @load_state.setter
    def load_state(self, load_state):
        r"""Sets the load_state of this ListCollectionDetails.

        **参数解释：** 标识当前Collection加载状态。 **约束限制：** 不涉及。 **取值范围：** 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。 **默认取值:** 不涉及。

        :param load_state: The load_state of this ListCollectionDetails.
        :type load_state: str
        """
        self._load_state = load_state

    @property
    def create_time(self):
        r"""Gets the create_time of this ListCollectionDetails.

        **参数解释：** 创建时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ\"。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The create_time of this ListCollectionDetails.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListCollectionDetails.

        **参数解释：** 创建时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ\"。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param create_time: The create_time of this ListCollectionDetails.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this ListCollectionDetails.

        **参数解释：** collection的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The description of this ListCollectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListCollectionDetails.

        **参数解释：** collection的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param description: The description of this ListCollectionDetails.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListCollectionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
