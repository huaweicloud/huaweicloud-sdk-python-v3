# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpBlacklistVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'effect_scope': 'list[int]',
        'import_status': 'int',
        'import_time': 'int',
        'error_message': 'str'
    }

    attribute_map = {
        'name': 'name',
        'effect_scope': 'effect_scope',
        'import_status': 'import_status',
        'import_time': 'import_time',
        'error_message': 'error_message'
    }

    def __init__(self, name=None, effect_scope=None, import_status=None, import_time=None, error_message=None):
        r"""IpBlacklistVO

        The model defined in huaweicloud sdk

        :param name: IP黑名单的文件名，对应导出时的文件名
        :type name: str
        :param effect_scope: IP黑名单的生效范围，1表示EIP，2表示NAT
        :type effect_scope: list[int]
        :param import_status: IP黑名单的导入状态，有三种状态：2：生成中、1：成功、0：失败。
        :type import_status: int
        :param import_time: IP黑名单的导入时间
        :type import_time: int
        :param error_message: 导入失败的错误信息
        :type error_message: str
        """
        
        

        self._name = None
        self._effect_scope = None
        self._import_status = None
        self._import_time = None
        self._error_message = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if effect_scope is not None:
            self.effect_scope = effect_scope
        if import_status is not None:
            self.import_status = import_status
        if import_time is not None:
            self.import_time = import_time
        if error_message is not None:
            self.error_message = error_message

    @property
    def name(self):
        r"""Gets the name of this IpBlacklistVO.

        IP黑名单的文件名，对应导出时的文件名

        :return: The name of this IpBlacklistVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpBlacklistVO.

        IP黑名单的文件名，对应导出时的文件名

        :param name: The name of this IpBlacklistVO.
        :type name: str
        """
        self._name = name

    @property
    def effect_scope(self):
        r"""Gets the effect_scope of this IpBlacklistVO.

        IP黑名单的生效范围，1表示EIP，2表示NAT

        :return: The effect_scope of this IpBlacklistVO.
        :rtype: list[int]
        """
        return self._effect_scope

    @effect_scope.setter
    def effect_scope(self, effect_scope):
        r"""Sets the effect_scope of this IpBlacklistVO.

        IP黑名单的生效范围，1表示EIP，2表示NAT

        :param effect_scope: The effect_scope of this IpBlacklistVO.
        :type effect_scope: list[int]
        """
        self._effect_scope = effect_scope

    @property
    def import_status(self):
        r"""Gets the import_status of this IpBlacklistVO.

        IP黑名单的导入状态，有三种状态：2：生成中、1：成功、0：失败。

        :return: The import_status of this IpBlacklistVO.
        :rtype: int
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        r"""Sets the import_status of this IpBlacklistVO.

        IP黑名单的导入状态，有三种状态：2：生成中、1：成功、0：失败。

        :param import_status: The import_status of this IpBlacklistVO.
        :type import_status: int
        """
        self._import_status = import_status

    @property
    def import_time(self):
        r"""Gets the import_time of this IpBlacklistVO.

        IP黑名单的导入时间

        :return: The import_time of this IpBlacklistVO.
        :rtype: int
        """
        return self._import_time

    @import_time.setter
    def import_time(self, import_time):
        r"""Sets the import_time of this IpBlacklistVO.

        IP黑名单的导入时间

        :param import_time: The import_time of this IpBlacklistVO.
        :type import_time: int
        """
        self._import_time = import_time

    @property
    def error_message(self):
        r"""Gets the error_message of this IpBlacklistVO.

        导入失败的错误信息

        :return: The error_message of this IpBlacklistVO.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this IpBlacklistVO.

        导入失败的错误信息

        :param error_message: The error_message of this IpBlacklistVO.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, IpBlacklistVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
