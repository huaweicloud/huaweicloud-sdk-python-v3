# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsDatasetColumn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'comments': 'str',
        'data_id': 'str',
        'data_type': 'str',
        'fl_label_type': 'str',
        'is_discrete': 'bool',
        'length': 'int',
        'privacy_policy': 'str',
        'privacy_policy_ext': 'str',
        'sacle': 'int',
        'sql_col_privacy_type': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'comments': 'comments',
        'data_id': 'data_id',
        'data_type': 'data_type',
        'fl_label_type': 'fl_label_type',
        'is_discrete': 'is_discrete',
        'length': 'length',
        'privacy_policy': 'privacy_policy',
        'privacy_policy_ext': 'privacy_policy_ext',
        'sacle': 'sacle',
        'sql_col_privacy_type': 'sql_col_privacy_type'
    }

    def __init__(self, column_name=None, comments=None, data_id=None, data_type=None, fl_label_type=None, is_discrete=None, length=None, privacy_policy=None, privacy_policy_ext=None, sacle=None, sql_col_privacy_type=None):
        """TicsDatasetColumn

        The model defined in huaweicloud sdk

        :param column_name: 字段名称
        :type column_name: str
        :param comments: 备注信息
        :type comments: str
        :param data_id: 数据集id
        :type data_id: str
        :param data_type: 字段类型
        :type data_type: str
        :param fl_label_type: 学习数据集标签类型，UNIQUE_ID.唯一标识,FEATURE.特征,LABEL.标签,FILTER.过滤字段
        :type fl_label_type: str
        :param is_discrete: 是否离散
        :type is_discrete: bool
        :param length: 长度
        :type length: int
        :param privacy_policy: 隐私策略，HASH.哈希处理，MASK.掩码，NONE.不处理
        :type privacy_policy: str
        :param privacy_policy_ext: 隐私策略描述
        :type privacy_policy_ext: str
        :param sacle: 精度
        :type sacle: int
        :param sql_col_privacy_type: 分析数据集字段隐私类别，NON_SENSITIVE.非敏感，SENSITIVE.敏感，UNIQUE_ID.唯一主键
        :type sql_col_privacy_type: str
        """
        
        

        self._column_name = None
        self._comments = None
        self._data_id = None
        self._data_type = None
        self._fl_label_type = None
        self._is_discrete = None
        self._length = None
        self._privacy_policy = None
        self._privacy_policy_ext = None
        self._sacle = None
        self._sql_col_privacy_type = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if comments is not None:
            self.comments = comments
        if data_id is not None:
            self.data_id = data_id
        if data_type is not None:
            self.data_type = data_type
        if fl_label_type is not None:
            self.fl_label_type = fl_label_type
        if is_discrete is not None:
            self.is_discrete = is_discrete
        if length is not None:
            self.length = length
        if privacy_policy is not None:
            self.privacy_policy = privacy_policy
        if privacy_policy_ext is not None:
            self.privacy_policy_ext = privacy_policy_ext
        if sacle is not None:
            self.sacle = sacle
        if sql_col_privacy_type is not None:
            self.sql_col_privacy_type = sql_col_privacy_type

    @property
    def column_name(self):
        """Gets the column_name of this TicsDatasetColumn.

        字段名称

        :return: The column_name of this TicsDatasetColumn.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this TicsDatasetColumn.

        字段名称

        :param column_name: The column_name of this TicsDatasetColumn.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def comments(self):
        """Gets the comments of this TicsDatasetColumn.

        备注信息

        :return: The comments of this TicsDatasetColumn.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TicsDatasetColumn.

        备注信息

        :param comments: The comments of this TicsDatasetColumn.
        :type comments: str
        """
        self._comments = comments

    @property
    def data_id(self):
        """Gets the data_id of this TicsDatasetColumn.

        数据集id

        :return: The data_id of this TicsDatasetColumn.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """Sets the data_id of this TicsDatasetColumn.

        数据集id

        :param data_id: The data_id of this TicsDatasetColumn.
        :type data_id: str
        """
        self._data_id = data_id

    @property
    def data_type(self):
        """Gets the data_type of this TicsDatasetColumn.

        字段类型

        :return: The data_type of this TicsDatasetColumn.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this TicsDatasetColumn.

        字段类型

        :param data_type: The data_type of this TicsDatasetColumn.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def fl_label_type(self):
        """Gets the fl_label_type of this TicsDatasetColumn.

        学习数据集标签类型，UNIQUE_ID.唯一标识,FEATURE.特征,LABEL.标签,FILTER.过滤字段

        :return: The fl_label_type of this TicsDatasetColumn.
        :rtype: str
        """
        return self._fl_label_type

    @fl_label_type.setter
    def fl_label_type(self, fl_label_type):
        """Sets the fl_label_type of this TicsDatasetColumn.

        学习数据集标签类型，UNIQUE_ID.唯一标识,FEATURE.特征,LABEL.标签,FILTER.过滤字段

        :param fl_label_type: The fl_label_type of this TicsDatasetColumn.
        :type fl_label_type: str
        """
        self._fl_label_type = fl_label_type

    @property
    def is_discrete(self):
        """Gets the is_discrete of this TicsDatasetColumn.

        是否离散

        :return: The is_discrete of this TicsDatasetColumn.
        :rtype: bool
        """
        return self._is_discrete

    @is_discrete.setter
    def is_discrete(self, is_discrete):
        """Sets the is_discrete of this TicsDatasetColumn.

        是否离散

        :param is_discrete: The is_discrete of this TicsDatasetColumn.
        :type is_discrete: bool
        """
        self._is_discrete = is_discrete

    @property
    def length(self):
        """Gets the length of this TicsDatasetColumn.

        长度

        :return: The length of this TicsDatasetColumn.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TicsDatasetColumn.

        长度

        :param length: The length of this TicsDatasetColumn.
        :type length: int
        """
        self._length = length

    @property
    def privacy_policy(self):
        """Gets the privacy_policy of this TicsDatasetColumn.

        隐私策略，HASH.哈希处理，MASK.掩码，NONE.不处理

        :return: The privacy_policy of this TicsDatasetColumn.
        :rtype: str
        """
        return self._privacy_policy

    @privacy_policy.setter
    def privacy_policy(self, privacy_policy):
        """Sets the privacy_policy of this TicsDatasetColumn.

        隐私策略，HASH.哈希处理，MASK.掩码，NONE.不处理

        :param privacy_policy: The privacy_policy of this TicsDatasetColumn.
        :type privacy_policy: str
        """
        self._privacy_policy = privacy_policy

    @property
    def privacy_policy_ext(self):
        """Gets the privacy_policy_ext of this TicsDatasetColumn.

        隐私策略描述

        :return: The privacy_policy_ext of this TicsDatasetColumn.
        :rtype: str
        """
        return self._privacy_policy_ext

    @privacy_policy_ext.setter
    def privacy_policy_ext(self, privacy_policy_ext):
        """Sets the privacy_policy_ext of this TicsDatasetColumn.

        隐私策略描述

        :param privacy_policy_ext: The privacy_policy_ext of this TicsDatasetColumn.
        :type privacy_policy_ext: str
        """
        self._privacy_policy_ext = privacy_policy_ext

    @property
    def sacle(self):
        """Gets the sacle of this TicsDatasetColumn.

        精度

        :return: The sacle of this TicsDatasetColumn.
        :rtype: int
        """
        return self._sacle

    @sacle.setter
    def sacle(self, sacle):
        """Sets the sacle of this TicsDatasetColumn.

        精度

        :param sacle: The sacle of this TicsDatasetColumn.
        :type sacle: int
        """
        self._sacle = sacle

    @property
    def sql_col_privacy_type(self):
        """Gets the sql_col_privacy_type of this TicsDatasetColumn.

        分析数据集字段隐私类别，NON_SENSITIVE.非敏感，SENSITIVE.敏感，UNIQUE_ID.唯一主键

        :return: The sql_col_privacy_type of this TicsDatasetColumn.
        :rtype: str
        """
        return self._sql_col_privacy_type

    @sql_col_privacy_type.setter
    def sql_col_privacy_type(self, sql_col_privacy_type):
        """Sets the sql_col_privacy_type of this TicsDatasetColumn.

        分析数据集字段隐私类别，NON_SENSITIVE.非敏感，SENSITIVE.敏感，UNIQUE_ID.唯一主键

        :param sql_col_privacy_type: The sql_col_privacy_type of this TicsDatasetColumn.
        :type sql_col_privacy_type: str
        """
        self._sql_col_privacy_type = sql_col_privacy_type

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
        if not isinstance(other, TicsDatasetColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
