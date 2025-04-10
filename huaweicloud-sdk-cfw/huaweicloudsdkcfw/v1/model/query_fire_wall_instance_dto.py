# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryFireWallInstanceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'key_word': 'str',
        'tags': 'list[TagInfo]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'key_word': 'key_word',
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, key_word=None, tags=None, limit=None, offset=None):
        r"""QueryFireWallInstanceDto

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param key_word: 查询关键字，可为防火墙id或防火墙名称的一部分。可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type key_word: str
        :param tags: 标签列表，可通过查询标签服务查询标签接口获得，返回值即为标签列表
        :type tags: list[:class:`huaweicloudsdkcfw.v1.TagInfo`]
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._key_word = None
        self._tags = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if key_word is not None:
            self.key_word = key_word
        if tags is not None:
            self.tags = tags
        self.limit = limit
        self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QueryFireWallInstanceDto.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this QueryFireWallInstanceDto.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QueryFireWallInstanceDto.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this QueryFireWallInstanceDto.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def key_word(self):
        r"""Gets the key_word of this QueryFireWallInstanceDto.

        查询关键字，可为防火墙id或防火墙名称的一部分。可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The key_word of this QueryFireWallInstanceDto.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this QueryFireWallInstanceDto.

        查询关键字，可为防火墙id或防火墙名称的一部分。可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param key_word: The key_word of this QueryFireWallInstanceDto.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def tags(self):
        r"""Gets the tags of this QueryFireWallInstanceDto.

        标签列表，可通过查询标签服务查询标签接口获得，返回值即为标签列表

        :return: The tags of this QueryFireWallInstanceDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TagInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QueryFireWallInstanceDto.

        标签列表，可通过查询标签服务查询标签接口获得，返回值即为标签列表

        :param tags: The tags of this QueryFireWallInstanceDto.
        :type tags: list[:class:`huaweicloudsdkcfw.v1.TagInfo`]
        """
        self._tags = tags

    @property
    def limit(self):
        r"""Gets the limit of this QueryFireWallInstanceDto.

        每页显示个数，范围为1-1024

        :return: The limit of this QueryFireWallInstanceDto.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryFireWallInstanceDto.

        每页显示个数，范围为1-1024

        :param limit: The limit of this QueryFireWallInstanceDto.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this QueryFireWallInstanceDto.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this QueryFireWallInstanceDto.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryFireWallInstanceDto.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this QueryFireWallInstanceDto.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, QueryFireWallInstanceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
