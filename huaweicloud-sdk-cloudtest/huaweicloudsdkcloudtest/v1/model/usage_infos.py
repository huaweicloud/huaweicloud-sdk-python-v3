# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsageInfos:

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
        'id': 'str',
        'amount': 'str',
        'used': 'str',
        'used_percent': 'int',
        'usage_info': 'list[UsageInfos]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'amount': 'amount',
        'used': 'used',
        'used_percent': 'used_percent',
        'usage_info': 'usage_info'
    }

    def __init__(self, name=None, id=None, amount=None, used=None, used_percent=None, usage_info=None):
        r"""UsageInfos

        The model defined in huaweicloud sdk

        :param name: 资源名称
        :type name: str
        :param id: 资源标识
        :type id: str
        :param amount: 资源总量
        :type amount: str
        :param used: 已消耗用量
        :type used: str
        :param used_percent: 资源已用容量百分比,例如80% 值为80
        :type used_percent: int
        :param usage_info: 版本超限信息
        :type usage_info: list[:class:`huaweicloudsdkcloudtest.v1.UsageInfos`]
        """
        
        

        self._name = None
        self._id = None
        self._amount = None
        self._used = None
        self._used_percent = None
        self._usage_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount
        if used is not None:
            self.used = used
        if used_percent is not None:
            self.used_percent = used_percent
        if usage_info is not None:
            self.usage_info = usage_info

    @property
    def name(self):
        r"""Gets the name of this UsageInfos.

        资源名称

        :return: The name of this UsageInfos.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UsageInfos.

        资源名称

        :param name: The name of this UsageInfos.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this UsageInfos.

        资源标识

        :return: The id of this UsageInfos.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UsageInfos.

        资源标识

        :param id: The id of this UsageInfos.
        :type id: str
        """
        self._id = id

    @property
    def amount(self):
        r"""Gets the amount of this UsageInfos.

        资源总量

        :return: The amount of this UsageInfos.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this UsageInfos.

        资源总量

        :param amount: The amount of this UsageInfos.
        :type amount: str
        """
        self._amount = amount

    @property
    def used(self):
        r"""Gets the used of this UsageInfos.

        已消耗用量

        :return: The used of this UsageInfos.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this UsageInfos.

        已消耗用量

        :param used: The used of this UsageInfos.
        :type used: str
        """
        self._used = used

    @property
    def used_percent(self):
        r"""Gets the used_percent of this UsageInfos.

        资源已用容量百分比,例如80% 值为80

        :return: The used_percent of this UsageInfos.
        :rtype: int
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        r"""Sets the used_percent of this UsageInfos.

        资源已用容量百分比,例如80% 值为80

        :param used_percent: The used_percent of this UsageInfos.
        :type used_percent: int
        """
        self._used_percent = used_percent

    @property
    def usage_info(self):
        r"""Gets the usage_info of this UsageInfos.

        版本超限信息

        :return: The usage_info of this UsageInfos.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.UsageInfos`]
        """
        return self._usage_info

    @usage_info.setter
    def usage_info(self, usage_info):
        r"""Sets the usage_info of this UsageInfos.

        版本超限信息

        :param usage_info: The usage_info of this UsageInfos.
        :type usage_info: list[:class:`huaweicloudsdkcloudtest.v1.UsageInfos`]
        """
        self._usage_info = usage_info

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
        if not isinstance(other, UsageInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
