# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPackageLevel:

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
        'level': 'str',
        'name_cn': 'str',
        'name_en': 'str',
        'display_priority': 'int',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'display_priority': 'display_priority',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, level=None, name_cn=None, name_en=None, display_priority=None, description=None, created_at=None, updated_at=None):
        r"""BandwidthPackageLevel

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param level: 带宽包等级。
        :type level: str
        :param name_cn: 实例名称。
        :type name_cn: str
        :param name_en: 实例名称。
        :type name_en: str
        :param display_priority: 展示优先级，数值越低，优先级越高。 铂金系列优先级范围：1-50。 金牌系列优先级范围：51-100。 银牌系列优先级范围：101-150。 其他：大于151。
        :type display_priority: int
        :param description: 描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._level = None
        self._name_cn = None
        self._name_en = None
        self._display_priority = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if display_priority is not None:
            self.display_priority = display_priority
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this BandwidthPackageLevel.

        实例ID。

        :return: The id of this BandwidthPackageLevel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandwidthPackageLevel.

        实例ID。

        :param id: The id of this BandwidthPackageLevel.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        r"""Gets the level of this BandwidthPackageLevel.

        带宽包等级。

        :return: The level of this BandwidthPackageLevel.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this BandwidthPackageLevel.

        带宽包等级。

        :param level: The level of this BandwidthPackageLevel.
        :type level: str
        """
        self._level = level

    @property
    def name_cn(self):
        r"""Gets the name_cn of this BandwidthPackageLevel.

        实例名称。

        :return: The name_cn of this BandwidthPackageLevel.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this BandwidthPackageLevel.

        实例名称。

        :param name_cn: The name_cn of this BandwidthPackageLevel.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this BandwidthPackageLevel.

        实例名称。

        :return: The name_en of this BandwidthPackageLevel.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this BandwidthPackageLevel.

        实例名称。

        :param name_en: The name_en of this BandwidthPackageLevel.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def display_priority(self):
        r"""Gets the display_priority of this BandwidthPackageLevel.

        展示优先级，数值越低，优先级越高。 铂金系列优先级范围：1-50。 金牌系列优先级范围：51-100。 银牌系列优先级范围：101-150。 其他：大于151。

        :return: The display_priority of this BandwidthPackageLevel.
        :rtype: int
        """
        return self._display_priority

    @display_priority.setter
    def display_priority(self, display_priority):
        r"""Sets the display_priority of this BandwidthPackageLevel.

        展示优先级，数值越低，优先级越高。 铂金系列优先级范围：1-50。 金牌系列优先级范围：51-100。 银牌系列优先级范围：101-150。 其他：大于151。

        :param display_priority: The display_priority of this BandwidthPackageLevel.
        :type display_priority: int
        """
        self._display_priority = display_priority

    @property
    def description(self):
        r"""Gets the description of this BandwidthPackageLevel.

        描述。不支持 <>。

        :return: The description of this BandwidthPackageLevel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BandwidthPackageLevel.

        描述。不支持 <>。

        :param description: The description of this BandwidthPackageLevel.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this BandwidthPackageLevel.

        创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this BandwidthPackageLevel.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BandwidthPackageLevel.

        创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this BandwidthPackageLevel.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this BandwidthPackageLevel.

        更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this BandwidthPackageLevel.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this BandwidthPackageLevel.

        更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this BandwidthPackageLevel.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, BandwidthPackageLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
