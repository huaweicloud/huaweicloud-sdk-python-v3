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

        :param collection_name: collection名称
        :type collection_name: str
        :param index_num: 索引数量
        :type index_num: int
        :param entity_num: collection中的entity数量
        :type entity_num: int
        :param load_state: 标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。
        :type load_state: str
        :param create_time: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ\&quot;
        :type create_time: str
        :param description: 描述信息
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

        collection名称

        :return: The collection_name of this ListCollectionDetails.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this ListCollectionDetails.

        collection名称

        :param collection_name: The collection_name of this ListCollectionDetails.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def index_num(self):
        r"""Gets the index_num of this ListCollectionDetails.

        索引数量

        :return: The index_num of this ListCollectionDetails.
        :rtype: int
        """
        return self._index_num

    @index_num.setter
    def index_num(self, index_num):
        r"""Sets the index_num of this ListCollectionDetails.

        索引数量

        :param index_num: The index_num of this ListCollectionDetails.
        :type index_num: int
        """
        self._index_num = index_num

    @property
    def entity_num(self):
        r"""Gets the entity_num of this ListCollectionDetails.

        collection中的entity数量

        :return: The entity_num of this ListCollectionDetails.
        :rtype: int
        """
        return self._entity_num

    @entity_num.setter
    def entity_num(self, entity_num):
        r"""Sets the entity_num of this ListCollectionDetails.

        collection中的entity数量

        :param entity_num: The entity_num of this ListCollectionDetails.
        :type entity_num: int
        """
        self._entity_num = entity_num

    @property
    def load_state(self):
        r"""Gets the load_state of this ListCollectionDetails.

        标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。

        :return: The load_state of this ListCollectionDetails.
        :rtype: str
        """
        return self._load_state

    @load_state.setter
    def load_state(self, load_state):
        r"""Sets the load_state of this ListCollectionDetails.

        标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。

        :param load_state: The load_state of this ListCollectionDetails.
        :type load_state: str
        """
        self._load_state = load_state

    @property
    def create_time(self):
        r"""Gets the create_time of this ListCollectionDetails.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ\"

        :return: The create_time of this ListCollectionDetails.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListCollectionDetails.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ\"

        :param create_time: The create_time of this ListCollectionDetails.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this ListCollectionDetails.

        描述信息

        :return: The description of this ListCollectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListCollectionDetails.

        描述信息

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
