# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArchiveRuleSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('name')

    openapi_types = {
        'created_at': 'datetime',
        'filters': 'list[FindingFilter]',
        'id': 'str',
        'name': 'str',
        'updated_at': 'datetime',
        'urn': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'filters': 'filters',
        'id': 'id',
        'name': 'name',
        'updated_at': 'updated_at',
        'urn': 'urn'
    }

    def __init__(self, created_at=None, filters=None, id=None, name=None, updated_at=None, urn=None):
        r"""ArchiveRuleSummary

        The model defined in huaweicloud sdk

        :param created_at: 创建存档规则的时间。
        :type created_at: datetime
        :param filters: 匹配要返回的访问分析结果的筛选器。
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        :param id: 存档规则的唯一标识符。
        :type id: str
        :param name: 创建存档规则的名称。
        :type name: str
        :param updated_at: 上次更新存档规则的时间。
        :type updated_at: datetime
        :param urn: 存档规则的唯一资源标识符。
        :type urn: str
        """
        
        

        self._created_at = None
        self._filters = None
        self._id = None
        self._name = None
        self._updated_at = None
        self._urn = None
        self.discriminator = None

        self.created_at = created_at
        self.filters = filters
        self.id = id
        self.name = name
        self.updated_at = updated_at
        self.urn = urn

    @property
    def created_at(self):
        r"""Gets the created_at of this ArchiveRuleSummary.

        创建存档规则的时间。

        :return: The created_at of this ArchiveRuleSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ArchiveRuleSummary.

        创建存档规则的时间。

        :param created_at: The created_at of this ArchiveRuleSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def filters(self):
        r"""Gets the filters of this ArchiveRuleSummary.

        匹配要返回的访问分析结果的筛选器。

        :return: The filters of this ArchiveRuleSummary.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ArchiveRuleSummary.

        匹配要返回的访问分析结果的筛选器。

        :param filters: The filters of this ArchiveRuleSummary.
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        self._filters = filters

    @property
    def id(self):
        r"""Gets the id of this ArchiveRuleSummary.

        存档规则的唯一标识符。

        :return: The id of this ArchiveRuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ArchiveRuleSummary.

        存档规则的唯一标识符。

        :param id: The id of this ArchiveRuleSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ArchiveRuleSummary.

        创建存档规则的名称。

        :return: The name of this ArchiveRuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArchiveRuleSummary.

        创建存档规则的名称。

        :param name: The name of this ArchiveRuleSummary.
        :type name: str
        """
        self._name = name

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ArchiveRuleSummary.

        上次更新存档规则的时间。

        :return: The updated_at of this ArchiveRuleSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ArchiveRuleSummary.

        上次更新存档规则的时间。

        :param updated_at: The updated_at of this ArchiveRuleSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def urn(self):
        r"""Gets the urn of this ArchiveRuleSummary.

        存档规则的唯一资源标识符。

        :return: The urn of this ArchiveRuleSummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this ArchiveRuleSummary.

        存档规则的唯一资源标识符。

        :param urn: The urn of this ArchiveRuleSummary.
        :type urn: str
        """
        self._urn = urn

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
        if not isinstance(other, ArchiveRuleSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
