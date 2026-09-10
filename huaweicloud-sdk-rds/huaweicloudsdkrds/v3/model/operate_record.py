# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'user_name': 'str',
        'operate_time': 'int',
        'level': 'str'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'user_name': 'user_name',
        'operate_time': 'operate_time',
        'level': 'level'
    }

    def __init__(self, operate_type=None, user_name=None, operate_time=None, level=None):
        r"""OperateRecord

        The model defined in huaweicloud sdk

        :param operate_type: 操作类型
        :type operate_type: str
        :param user_name: 用户名称
        :type user_name: str
        :param operate_time: 操作时间
        :type operate_time: int
        :param level: 事件等级
        :type level: str
        """
        
        

        self._operate_type = None
        self._user_name = None
        self._operate_time = None
        self._level = None
        self.discriminator = None

        if operate_type is not None:
            self.operate_type = operate_type
        if user_name is not None:
            self.user_name = user_name
        if operate_time is not None:
            self.operate_time = operate_time
        if level is not None:
            self.level = level

    @property
    def operate_type(self):
        r"""Gets the operate_type of this OperateRecord.

        操作类型

        :return: The operate_type of this OperateRecord.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this OperateRecord.

        操作类型

        :param operate_type: The operate_type of this OperateRecord.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def user_name(self):
        r"""Gets the user_name of this OperateRecord.

        用户名称

        :return: The user_name of this OperateRecord.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this OperateRecord.

        用户名称

        :param user_name: The user_name of this OperateRecord.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def operate_time(self):
        r"""Gets the operate_time of this OperateRecord.

        操作时间

        :return: The operate_time of this OperateRecord.
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this OperateRecord.

        操作时间

        :param operate_time: The operate_time of this OperateRecord.
        :type operate_time: int
        """
        self._operate_time = operate_time

    @property
    def level(self):
        r"""Gets the level of this OperateRecord.

        事件等级

        :return: The level of this OperateRecord.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this OperateRecord.

        事件等级

        :param level: The level of this OperateRecord.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, OperateRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
