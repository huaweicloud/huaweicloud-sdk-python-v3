# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnumDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_deleted': 'bool',
        'match_type': 'str',
        'ticket_id': 'str',
        'real_ticket_id': 'str',
        'name_zh': 'str',
        'name_en': 'str',
        'user_name': 'str',
        'biz_id': 'str',
        'prop_id': 'str',
        'model_id': 'str'
    }

    attribute_map = {
        'is_deleted': 'is_deleted',
        'match_type': 'match_type',
        'ticket_id': 'ticket_id',
        'real_ticket_id': 'real_ticket_id',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'user_name': 'user_name',
        'biz_id': 'biz_id',
        'prop_id': 'prop_id',
        'model_id': 'model_id'
    }

    def __init__(self, is_deleted=None, match_type=None, ticket_id=None, real_ticket_id=None, name_zh=None, name_en=None, user_name=None, biz_id=None, prop_id=None, model_id=None):
        r"""EnumDataInfo

        The model defined in huaweicloud sdk

        :param is_deleted: 是否删除
        :type is_deleted: bool
        :param match_type: 匹配类型
        :type match_type: str
        :param ticket_id: 所属单号
        :type ticket_id: str
        :param real_ticket_id: 所属真实单号。
        :type real_ticket_id: str
        :param name_zh: 中文名
        :type name_zh: str
        :param name_en: 英文名
        :type name_en: str
        :param user_name: 工号
        :type user_name: str
        :param biz_id: 唯一id
        :type biz_id: str
        :param prop_id: 字段id
        :type prop_id: str
        :param model_id: 模型id
        :type model_id: str
        """
        
        

        self._is_deleted = None
        self._match_type = None
        self._ticket_id = None
        self._real_ticket_id = None
        self._name_zh = None
        self._name_en = None
        self._user_name = None
        self._biz_id = None
        self._prop_id = None
        self._model_id = None
        self.discriminator = None

        if is_deleted is not None:
            self.is_deleted = is_deleted
        if match_type is not None:
            self.match_type = match_type
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if real_ticket_id is not None:
            self.real_ticket_id = real_ticket_id
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if user_name is not None:
            self.user_name = user_name
        if biz_id is not None:
            self.biz_id = biz_id
        if prop_id is not None:
            self.prop_id = prop_id
        if model_id is not None:
            self.model_id = model_id

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this EnumDataInfo.

        是否删除

        :return: The is_deleted of this EnumDataInfo.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this EnumDataInfo.

        是否删除

        :param is_deleted: The is_deleted of this EnumDataInfo.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def match_type(self):
        r"""Gets the match_type of this EnumDataInfo.

        匹配类型

        :return: The match_type of this EnumDataInfo.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this EnumDataInfo.

        匹配类型

        :param match_type: The match_type of this EnumDataInfo.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this EnumDataInfo.

        所属单号

        :return: The ticket_id of this EnumDataInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this EnumDataInfo.

        所属单号

        :param ticket_id: The ticket_id of this EnumDataInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def real_ticket_id(self):
        r"""Gets the real_ticket_id of this EnumDataInfo.

        所属真实单号。

        :return: The real_ticket_id of this EnumDataInfo.
        :rtype: str
        """
        return self._real_ticket_id

    @real_ticket_id.setter
    def real_ticket_id(self, real_ticket_id):
        r"""Sets the real_ticket_id of this EnumDataInfo.

        所属真实单号。

        :param real_ticket_id: The real_ticket_id of this EnumDataInfo.
        :type real_ticket_id: str
        """
        self._real_ticket_id = real_ticket_id

    @property
    def name_zh(self):
        r"""Gets the name_zh of this EnumDataInfo.

        中文名

        :return: The name_zh of this EnumDataInfo.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this EnumDataInfo.

        中文名

        :param name_zh: The name_zh of this EnumDataInfo.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this EnumDataInfo.

        英文名

        :return: The name_en of this EnumDataInfo.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this EnumDataInfo.

        英文名

        :param name_en: The name_en of this EnumDataInfo.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def user_name(self):
        r"""Gets the user_name of this EnumDataInfo.

        工号

        :return: The user_name of this EnumDataInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this EnumDataInfo.

        工号

        :param user_name: The user_name of this EnumDataInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def biz_id(self):
        r"""Gets the biz_id of this EnumDataInfo.

        唯一id

        :return: The biz_id of this EnumDataInfo.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this EnumDataInfo.

        唯一id

        :param biz_id: The biz_id of this EnumDataInfo.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def prop_id(self):
        r"""Gets the prop_id of this EnumDataInfo.

        字段id

        :return: The prop_id of this EnumDataInfo.
        :rtype: str
        """
        return self._prop_id

    @prop_id.setter
    def prop_id(self, prop_id):
        r"""Sets the prop_id of this EnumDataInfo.

        字段id

        :param prop_id: The prop_id of this EnumDataInfo.
        :type prop_id: str
        """
        self._prop_id = prop_id

    @property
    def model_id(self):
        r"""Gets the model_id of this EnumDataInfo.

        模型id

        :return: The model_id of this EnumDataInfo.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this EnumDataInfo.

        模型id

        :param model_id: The model_id of this EnumDataInfo.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, EnumDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
