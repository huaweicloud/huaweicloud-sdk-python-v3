# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineTemplatesQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'is_system': 'bool',
        'name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'language': 'language',
        'is_system': 'is_system',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, language=None, is_system=None, name=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListPipelineTemplatesQuery

        The model defined in huaweicloud sdk

        :param language: 创建模板时，用户选择的语言
        :type language: str
        :param is_system: 是否系统模板
        :type is_system: bool
        :param name: 模板名称
        :type name: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0，默认为0
        :type offset: int
        :param limit: 每次查询的条目数量，默认为10。
        :type limit: int
        :param sort_key: 用于排序的字段，非必选。取值为：name，create_time
        :type sort_key: str
        :param sort_dir: 排序类型，非必选。asc按排序字段升序，desc按排序字段降序
        :type sort_dir: str
        """
        
        

        self._language = None
        self._is_system = None
        self._name = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if is_system is not None:
            self.is_system = is_system
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def language(self):
        r"""Gets the language of this ListPipelineTemplatesQuery.

        创建模板时，用户选择的语言

        :return: The language of this ListPipelineTemplatesQuery.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListPipelineTemplatesQuery.

        创建模板时，用户选择的语言

        :param language: The language of this ListPipelineTemplatesQuery.
        :type language: str
        """
        self._language = language

    @property
    def is_system(self):
        r"""Gets the is_system of this ListPipelineTemplatesQuery.

        是否系统模板

        :return: The is_system of this ListPipelineTemplatesQuery.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        r"""Sets the is_system of this ListPipelineTemplatesQuery.

        是否系统模板

        :param is_system: The is_system of this ListPipelineTemplatesQuery.
        :type is_system: bool
        """
        self._is_system = is_system

    @property
    def name(self):
        r"""Gets the name of this ListPipelineTemplatesQuery.

        模板名称

        :return: The name of this ListPipelineTemplatesQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPipelineTemplatesQuery.

        模板名称

        :param name: The name of this ListPipelineTemplatesQuery.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineTemplatesQuery.

        偏移量，表示从此偏移量开始查询，offset大于等于0，默认为0

        :return: The offset of this ListPipelineTemplatesQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineTemplatesQuery.

        偏移量，表示从此偏移量开始查询，offset大于等于0，默认为0

        :param offset: The offset of this ListPipelineTemplatesQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineTemplatesQuery.

        每次查询的条目数量，默认为10。

        :return: The limit of this ListPipelineTemplatesQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineTemplatesQuery.

        每次查询的条目数量，默认为10。

        :param limit: The limit of this ListPipelineTemplatesQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPipelineTemplatesQuery.

        用于排序的字段，非必选。取值为：name，create_time

        :return: The sort_key of this ListPipelineTemplatesQuery.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPipelineTemplatesQuery.

        用于排序的字段，非必选。取值为：name，create_time

        :param sort_key: The sort_key of this ListPipelineTemplatesQuery.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPipelineTemplatesQuery.

        排序类型，非必选。asc按排序字段升序，desc按排序字段降序

        :return: The sort_dir of this ListPipelineTemplatesQuery.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPipelineTemplatesQuery.

        排序类型，非必选。asc按排序字段升序，desc按排序字段降序

        :param sort_dir: The sort_dir of this ListPipelineTemplatesQuery.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListPipelineTemplatesQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
