# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MuteConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ends_at': 'int',
        'scope': 'list[str]',
        'starts_at': 'int',
        'type': 'str'
    }

    attribute_map = {
        'ends_at': 'ends_at',
        'scope': 'scope',
        'starts_at': 'starts_at',
        'type': 'type'
    }

    def __init__(self, ends_at=None, scope=None, starts_at=None, type=None):
        """MuteConfig

        The model defined in huaweicloud sdk

        :param ends_at: 静默规则结束时间
        :type ends_at: int
        :param scope: 当type为每周或者每月时，scope不能为空
        :type scope: list[str]
        :param starts_at: 静默规则开始时间
        :type starts_at: int
        :param type: 静默规则生效时间种类。FIXED:固定方式统计,DAILY:按日合计,WEEKLY:按周统计,MONTHLY:按月统计
        :type type: str
        """
        
        

        self._ends_at = None
        self._scope = None
        self._starts_at = None
        self._type = None
        self.discriminator = None

        if ends_at is not None:
            self.ends_at = ends_at
        if scope is not None:
            self.scope = scope
        self.starts_at = starts_at
        self.type = type

    @property
    def ends_at(self):
        """Gets the ends_at of this MuteConfig.

        静默规则结束时间

        :return: The ends_at of this MuteConfig.
        :rtype: int
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this MuteConfig.

        静默规则结束时间

        :param ends_at: The ends_at of this MuteConfig.
        :type ends_at: int
        """
        self._ends_at = ends_at

    @property
    def scope(self):
        """Gets the scope of this MuteConfig.

        当type为每周或者每月时，scope不能为空

        :return: The scope of this MuteConfig.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this MuteConfig.

        当type为每周或者每月时，scope不能为空

        :param scope: The scope of this MuteConfig.
        :type scope: list[str]
        """
        self._scope = scope

    @property
    def starts_at(self):
        """Gets the starts_at of this MuteConfig.

        静默规则开始时间

        :return: The starts_at of this MuteConfig.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this MuteConfig.

        静默规则开始时间

        :param starts_at: The starts_at of this MuteConfig.
        :type starts_at: int
        """
        self._starts_at = starts_at

    @property
    def type(self):
        """Gets the type of this MuteConfig.

        静默规则生效时间种类。FIXED:固定方式统计,DAILY:按日合计,WEEKLY:按周统计,MONTHLY:按月统计

        :return: The type of this MuteConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MuteConfig.

        静默规则生效时间种类。FIXED:固定方式统计,DAILY:按日合计,WEEKLY:按周统计,MONTHLY:按月统计

        :param type: The type of this MuteConfig.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MuteConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
