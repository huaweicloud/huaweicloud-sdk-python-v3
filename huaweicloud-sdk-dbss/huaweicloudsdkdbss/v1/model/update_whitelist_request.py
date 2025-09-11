# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWhitelistRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_ids': 'list[str]',
        'desc': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'desc': 'desc',
        'enabled': 'enabled'
    }

    def __init__(self, db_ids=None, desc=None, enabled=None):
        r"""UpdateWhitelistRequest

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID列表
        :type db_ids: list[str]
        :param desc: 备注
        :type desc: str
        :param enabled: 是否启用  - true: 启用  - false: 禁用
        :type enabled: bool
        """
        
        

        self._db_ids = None
        self._desc = None
        self._enabled = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if desc is not None:
            self.desc = desc
        self.enabled = enabled

    @property
    def db_ids(self):
        r"""Gets the db_ids of this UpdateWhitelistRequest.

        数据库ID列表

        :return: The db_ids of this UpdateWhitelistRequest.
        :rtype: list[str]
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this UpdateWhitelistRequest.

        数据库ID列表

        :param db_ids: The db_ids of this UpdateWhitelistRequest.
        :type db_ids: list[str]
        """
        self._db_ids = db_ids

    @property
    def desc(self):
        r"""Gets the desc of this UpdateWhitelistRequest.

        备注

        :return: The desc of this UpdateWhitelistRequest.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UpdateWhitelistRequest.

        备注

        :param desc: The desc of this UpdateWhitelistRequest.
        :type desc: str
        """
        self._desc = desc

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateWhitelistRequest.

        是否启用  - true: 启用  - false: 禁用

        :return: The enabled of this UpdateWhitelistRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateWhitelistRequest.

        是否启用  - true: 启用  - false: 禁用

        :param enabled: The enabled of this UpdateWhitelistRequest.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UpdateWhitelistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
