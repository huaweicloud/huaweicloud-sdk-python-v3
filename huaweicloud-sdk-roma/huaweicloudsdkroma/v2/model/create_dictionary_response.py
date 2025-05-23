# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDictionaryResponse(SdkResponse):

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
        'name': 'str',
        'remark': 'str',
        'code': 'str',
        'extend_one': 'str',
        'extend_two': 'str',
        'parent_code': 'str',
        'type': 'DictionaryType',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'code': 'code',
        'extend_one': 'extend_one',
        'extend_two': 'extend_two',
        'parent_code': 'parent_code',
        'type': 'type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, remark=None, code=None, extend_one=None, extend_two=None, parent_code=None, type=None, create_time=None, update_time=None):
        r"""CreateDictionaryResponse

        The model defined in huaweicloud sdk

        :param id: 字典ID
        :type id: str
        :param name: 字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type name: str
        :param remark: 字典描述
        :type remark: str
        :param code: 字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type code: str
        :param extend_one: 字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_one: str
        :param extend_two: 字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_two: str
        :param parent_code: 父字典编码,为空时代表自身就是最顶级字典
        :type parent_code: str
        :param type: 
        :type type: :class:`huaweicloudsdkroma.v2.DictionaryType`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super(CreateDictionaryResponse, self).__init__()

        self._id = None
        self._name = None
        self._remark = None
        self._code = None
        self._extend_one = None
        self._extend_two = None
        self._parent_code = None
        self._type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if code is not None:
            self.code = code
        if extend_one is not None:
            self.extend_one = extend_one
        if extend_two is not None:
            self.extend_two = extend_two
        if parent_code is not None:
            self.parent_code = parent_code
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CreateDictionaryResponse.

        字典ID

        :return: The id of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateDictionaryResponse.

        字典ID

        :param id: The id of this CreateDictionaryResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateDictionaryResponse.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The name of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDictionaryResponse.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param name: The name of this CreateDictionaryResponse.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        r"""Gets the remark of this CreateDictionaryResponse.

        字典描述

        :return: The remark of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this CreateDictionaryResponse.

        字典描述

        :param remark: The remark of this CreateDictionaryResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def code(self):
        r"""Gets the code of this CreateDictionaryResponse.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The code of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateDictionaryResponse.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param code: The code of this CreateDictionaryResponse.
        :type code: str
        """
        self._code = code

    @property
    def extend_one(self):
        r"""Gets the extend_one of this CreateDictionaryResponse.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_one of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._extend_one

    @extend_one.setter
    def extend_one(self, extend_one):
        r"""Sets the extend_one of this CreateDictionaryResponse.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_one: The extend_one of this CreateDictionaryResponse.
        :type extend_one: str
        """
        self._extend_one = extend_one

    @property
    def extend_two(self):
        r"""Gets the extend_two of this CreateDictionaryResponse.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_two of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._extend_two

    @extend_two.setter
    def extend_two(self, extend_two):
        r"""Sets the extend_two of this CreateDictionaryResponse.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_two: The extend_two of this CreateDictionaryResponse.
        :type extend_two: str
        """
        self._extend_two = extend_two

    @property
    def parent_code(self):
        r"""Gets the parent_code of this CreateDictionaryResponse.

        父字典编码,为空时代表自身就是最顶级字典

        :return: The parent_code of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._parent_code

    @parent_code.setter
    def parent_code(self, parent_code):
        r"""Sets the parent_code of this CreateDictionaryResponse.

        父字典编码,为空时代表自身就是最顶级字典

        :param parent_code: The parent_code of this CreateDictionaryResponse.
        :type parent_code: str
        """
        self._parent_code = parent_code

    @property
    def type(self):
        r"""Gets the type of this CreateDictionaryResponse.

        :return: The type of this CreateDictionaryResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.DictionaryType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateDictionaryResponse.

        :param type: The type of this CreateDictionaryResponse.
        :type type: :class:`huaweicloudsdkroma.v2.DictionaryType`
        """
        self._type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateDictionaryResponse.

        创建时间

        :return: The create_time of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateDictionaryResponse.

        创建时间

        :param create_time: The create_time of this CreateDictionaryResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateDictionaryResponse.

        更新时间

        :return: The update_time of this CreateDictionaryResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateDictionaryResponse.

        更新时间

        :param update_time: The update_time of this CreateDictionaryResponse.
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
        if not isinstance(other, CreateDictionaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
