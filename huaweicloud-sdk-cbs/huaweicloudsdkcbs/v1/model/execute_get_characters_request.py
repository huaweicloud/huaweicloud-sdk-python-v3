# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetCharactersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'str',
        'limit': 'str',
        'type': 'int',
        'train_status': 'int',
        'character_name': 'str',
        'support_interact': 'bool',
        'gender': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'train_status': 'train_status',
        'character_name': 'character_name',
        'support_interact': 'support_interact',
        'gender': 'gender'
    }

    def __init__(self, offset=None, limit=None, type=None, train_status=None, character_name=None, support_interact=None, gender=None):
        r"""ExecuteGetCharactersRequest

        The model defined in huaweicloud sdk

        :param offset: 
        :type offset: str
        :param limit: 
        :type limit: str
        :param type: 形象类型： 0：预制形象 1：用户自定义形象
        :type type: int
        :param train_status: 训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中
        :type train_status: int
        :param character_name: 
        :type character_name: str
        :param support_interact: 是否只获取支持交互式的数字人；默认：false 获取全部
        :type support_interact: bool
        :param gender: 性别
        :type gender: str
        """
        
        

        self._offset = None
        self._limit = None
        self._type = None
        self._train_status = None
        self._character_name = None
        self._support_interact = None
        self._gender = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if train_status is not None:
            self.train_status = train_status
        if character_name is not None:
            self.character_name = character_name
        if support_interact is not None:
            self.support_interact = support_interact
        if gender is not None:
            self.gender = gender

    @property
    def offset(self):
        r"""Gets the offset of this ExecuteGetCharactersRequest.

        :return: The offset of this ExecuteGetCharactersRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExecuteGetCharactersRequest.

        :param offset: The offset of this ExecuteGetCharactersRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ExecuteGetCharactersRequest.

        :return: The limit of this ExecuteGetCharactersRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExecuteGetCharactersRequest.

        :param limit: The limit of this ExecuteGetCharactersRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ExecuteGetCharactersRequest.

        形象类型： 0：预制形象 1：用户自定义形象

        :return: The type of this ExecuteGetCharactersRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExecuteGetCharactersRequest.

        形象类型： 0：预制形象 1：用户自定义形象

        :param type: The type of this ExecuteGetCharactersRequest.
        :type type: int
        """
        self._type = type

    @property
    def train_status(self):
        r"""Gets the train_status of this ExecuteGetCharactersRequest.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :return: The train_status of this ExecuteGetCharactersRequest.
        :rtype: int
        """
        return self._train_status

    @train_status.setter
    def train_status(self, train_status):
        r"""Sets the train_status of this ExecuteGetCharactersRequest.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :param train_status: The train_status of this ExecuteGetCharactersRequest.
        :type train_status: int
        """
        self._train_status = train_status

    @property
    def character_name(self):
        r"""Gets the character_name of this ExecuteGetCharactersRequest.

        :return: The character_name of this ExecuteGetCharactersRequest.
        :rtype: str
        """
        return self._character_name

    @character_name.setter
    def character_name(self, character_name):
        r"""Sets the character_name of this ExecuteGetCharactersRequest.

        :param character_name: The character_name of this ExecuteGetCharactersRequest.
        :type character_name: str
        """
        self._character_name = character_name

    @property
    def support_interact(self):
        r"""Gets the support_interact of this ExecuteGetCharactersRequest.

        是否只获取支持交互式的数字人；默认：false 获取全部

        :return: The support_interact of this ExecuteGetCharactersRequest.
        :rtype: bool
        """
        return self._support_interact

    @support_interact.setter
    def support_interact(self, support_interact):
        r"""Sets the support_interact of this ExecuteGetCharactersRequest.

        是否只获取支持交互式的数字人；默认：false 获取全部

        :param support_interact: The support_interact of this ExecuteGetCharactersRequest.
        :type support_interact: bool
        """
        self._support_interact = support_interact

    @property
    def gender(self):
        r"""Gets the gender of this ExecuteGetCharactersRequest.

        性别

        :return: The gender of this ExecuteGetCharactersRequest.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this ExecuteGetCharactersRequest.

        性别

        :param gender: The gender of this ExecuteGetCharactersRequest.
        :type gender: str
        """
        self._gender = gender

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
        if not isinstance(other, ExecuteGetCharactersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
