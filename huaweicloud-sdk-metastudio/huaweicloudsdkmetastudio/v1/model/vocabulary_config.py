# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VocabularyConfig:

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
        'key': 'str',
        'value': 'str',
        'type': 'str',
        'group_id': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'value': 'value',
        'type': 'type',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, key=None, value=None, type=None, group_id=None, create_time=None, update_time=None):
        r"""VocabularyConfig

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param key: 原始词
        :type key: str
        :param value: 设置的自定义读法
        :type value: str
        :param type: TTSS支持配置的词表类型 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法
        :type type: str
        :param group_id: 分组id
        :type group_id: str
        :param create_time: 创建时间。
        :type create_time: str
        :param update_time: 更新时间。
        :type update_time: str
        """
        
        

        self._id = None
        self._key = None
        self._value = None
        self._type = None
        self._group_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if group_id is not None:
            self.group_id = group_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this VocabularyConfig.

        id

        :return: The id of this VocabularyConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VocabularyConfig.

        id

        :param id: The id of this VocabularyConfig.
        :type id: str
        """
        self._id = id

    @property
    def key(self):
        r"""Gets the key of this VocabularyConfig.

        原始词

        :return: The key of this VocabularyConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this VocabularyConfig.

        原始词

        :param key: The key of this VocabularyConfig.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this VocabularyConfig.

        设置的自定义读法

        :return: The value of this VocabularyConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this VocabularyConfig.

        设置的自定义读法

        :param value: The value of this VocabularyConfig.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this VocabularyConfig.

        TTSS支持配置的词表类型 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法

        :return: The type of this VocabularyConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VocabularyConfig.

        TTSS支持配置的词表类型 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法

        :param type: The type of this VocabularyConfig.
        :type type: str
        """
        self._type = type

    @property
    def group_id(self):
        r"""Gets the group_id of this VocabularyConfig.

        分组id

        :return: The group_id of this VocabularyConfig.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this VocabularyConfig.

        分组id

        :param group_id: The group_id of this VocabularyConfig.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this VocabularyConfig.

        创建时间。

        :return: The create_time of this VocabularyConfig.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VocabularyConfig.

        创建时间。

        :param create_time: The create_time of this VocabularyConfig.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this VocabularyConfig.

        更新时间。

        :return: The update_time of this VocabularyConfig.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this VocabularyConfig.

        更新时间。

        :param update_time: The update_time of this VocabularyConfig.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, VocabularyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
