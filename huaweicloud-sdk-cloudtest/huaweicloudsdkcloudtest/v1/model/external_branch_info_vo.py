# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalBranchInfoVo:

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
        'type': 'str',
        'author': 'str',
        'name': 'str',
        'region': 'str',
        'last_modifier': 'str',
        'last_modified': 'datetime',
        'last_modified_timestamp': 'int',
        'creation_date': 'datetime',
        'creation_date_timestamp': 'int',
        'author_name': 'str',
        'is_base_branch': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'author': 'author',
        'name': 'name',
        'region': 'region',
        'last_modifier': 'last_modifier',
        'last_modified': 'last_modified',
        'last_modified_timestamp': 'last_modified_timestamp',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'author_name': 'author_name',
        'is_base_branch': 'is_base_branch'
    }

    def __init__(self, id=None, type=None, author=None, name=None, region=None, last_modifier=None, last_modified=None, last_modified_timestamp=None, creation_date=None, creation_date_timestamp=None, author_name=None, is_base_branch=None):
        r"""ExternalBranchInfoVo

        The model defined in huaweicloud sdk

        :param id: 分支ID
        :type id: str
        :param type: 资源类型
        :type type: str
        :param author: 创建人
        :type author: str
        :param name: 名称
        :type name: str
        :param region: 区域
        :type region: str
        :param last_modifier: 最后修改人
        :type last_modifier: str
        :param last_modified: 最后修改时间
        :type last_modified: datetime
        :param last_modified_timestamp: 修改时间时间戳
        :type last_modified_timestamp: int
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param creation_date_timestamp: 创建时间时间戳
        :type creation_date_timestamp: int
        :param author_name: 创建人名称
        :type author_name: str
        :param is_base_branch: 是否为基线分支。0表示不是基线分支，1表示是基线分支。
        :type is_base_branch: int
        """
        
        

        self._id = None
        self._type = None
        self._author = None
        self._name = None
        self._region = None
        self._last_modifier = None
        self._last_modified = None
        self._last_modified_timestamp = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._author_name = None
        self._is_base_branch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if author is not None:
            self.author = author
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if last_modifier is not None:
            self.last_modifier = last_modifier
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if author_name is not None:
            self.author_name = author_name
        if is_base_branch is not None:
            self.is_base_branch = is_base_branch

    @property
    def id(self):
        r"""Gets the id of this ExternalBranchInfoVo.

        分支ID

        :return: The id of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExternalBranchInfoVo.

        分支ID

        :param id: The id of this ExternalBranchInfoVo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ExternalBranchInfoVo.

        资源类型

        :return: The type of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExternalBranchInfoVo.

        资源类型

        :param type: The type of this ExternalBranchInfoVo.
        :type type: str
        """
        self._type = type

    @property
    def author(self):
        r"""Gets the author of this ExternalBranchInfoVo.

        创建人

        :return: The author of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ExternalBranchInfoVo.

        创建人

        :param author: The author of this ExternalBranchInfoVo.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        r"""Gets the name of this ExternalBranchInfoVo.

        名称

        :return: The name of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExternalBranchInfoVo.

        名称

        :param name: The name of this ExternalBranchInfoVo.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this ExternalBranchInfoVo.

        区域

        :return: The region of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ExternalBranchInfoVo.

        区域

        :param region: The region of this ExternalBranchInfoVo.
        :type region: str
        """
        self._region = region

    @property
    def last_modifier(self):
        r"""Gets the last_modifier of this ExternalBranchInfoVo.

        最后修改人

        :return: The last_modifier of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        r"""Sets the last_modifier of this ExternalBranchInfoVo.

        最后修改人

        :param last_modifier: The last_modifier of this ExternalBranchInfoVo.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_modified(self):
        r"""Gets the last_modified of this ExternalBranchInfoVo.

        最后修改时间

        :return: The last_modified of this ExternalBranchInfoVo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this ExternalBranchInfoVo.

        最后修改时间

        :param last_modified: The last_modified of this ExternalBranchInfoVo.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        r"""Gets the last_modified_timestamp of this ExternalBranchInfoVo.

        修改时间时间戳

        :return: The last_modified_timestamp of this ExternalBranchInfoVo.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        r"""Sets the last_modified_timestamp of this ExternalBranchInfoVo.

        修改时间时间戳

        :param last_modified_timestamp: The last_modified_timestamp of this ExternalBranchInfoVo.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def creation_date(self):
        r"""Gets the creation_date of this ExternalBranchInfoVo.

        创建时间

        :return: The creation_date of this ExternalBranchInfoVo.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this ExternalBranchInfoVo.

        创建时间

        :param creation_date: The creation_date of this ExternalBranchInfoVo.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        r"""Gets the creation_date_timestamp of this ExternalBranchInfoVo.

        创建时间时间戳

        :return: The creation_date_timestamp of this ExternalBranchInfoVo.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        r"""Sets the creation_date_timestamp of this ExternalBranchInfoVo.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this ExternalBranchInfoVo.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def author_name(self):
        r"""Gets the author_name of this ExternalBranchInfoVo.

        创建人名称

        :return: The author_name of this ExternalBranchInfoVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this ExternalBranchInfoVo.

        创建人名称

        :param author_name: The author_name of this ExternalBranchInfoVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def is_base_branch(self):
        r"""Gets the is_base_branch of this ExternalBranchInfoVo.

        是否为基线分支。0表示不是基线分支，1表示是基线分支。

        :return: The is_base_branch of this ExternalBranchInfoVo.
        :rtype: int
        """
        return self._is_base_branch

    @is_base_branch.setter
    def is_base_branch(self, is_base_branch):
        r"""Sets the is_base_branch of this ExternalBranchInfoVo.

        是否为基线分支。0表示不是基线分支，1表示是基线分支。

        :param is_base_branch: The is_base_branch of this ExternalBranchInfoVo.
        :type is_base_branch: int
        """
        self._is_base_branch = is_base_branch

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
        if not isinstance(other, ExternalBranchInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
