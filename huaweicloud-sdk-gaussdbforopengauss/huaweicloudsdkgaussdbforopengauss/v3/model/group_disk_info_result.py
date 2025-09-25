# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupDiskInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'name': 'str',
        'used': 'float',
        'total': 'float'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'used': 'used',
        'total': 'total'
    }

    def __init__(self, group_id=None, name=None, used=None, total=None):
        r"""GroupDiskInfoResult

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**： 分片组ID。 **取值范围**： 不涉及。
        :type group_id: str
        :param name: **参数解释**： 分片名称。 **取值范围**： 不涉及。
        :type name: str
        :param used: **参数解释**： 分片磁盘使用率。 **取值范围**： 不涉及。
        :type used: float
        :param total: **参数解释**： 分片磁盘大小。 **取值范围**： 不涉及。
        :type total: float
        """
        
        

        self._group_id = None
        self._name = None
        self._used = None
        self._total = None
        self.discriminator = None

        self.group_id = group_id
        self.name = name
        self.used = used
        self.total = total

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupDiskInfoResult.

        **参数解释**： 分片组ID。 **取值范围**： 不涉及。

        :return: The group_id of this GroupDiskInfoResult.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupDiskInfoResult.

        **参数解释**： 分片组ID。 **取值范围**： 不涉及。

        :param group_id: The group_id of this GroupDiskInfoResult.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        r"""Gets the name of this GroupDiskInfoResult.

        **参数解释**： 分片名称。 **取值范围**： 不涉及。

        :return: The name of this GroupDiskInfoResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupDiskInfoResult.

        **参数解释**： 分片名称。 **取值范围**： 不涉及。

        :param name: The name of this GroupDiskInfoResult.
        :type name: str
        """
        self._name = name

    @property
    def used(self):
        r"""Gets the used of this GroupDiskInfoResult.

        **参数解释**： 分片磁盘使用率。 **取值范围**： 不涉及。

        :return: The used of this GroupDiskInfoResult.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this GroupDiskInfoResult.

        **参数解释**： 分片磁盘使用率。 **取值范围**： 不涉及。

        :param used: The used of this GroupDiskInfoResult.
        :type used: float
        """
        self._used = used

    @property
    def total(self):
        r"""Gets the total of this GroupDiskInfoResult.

        **参数解释**： 分片磁盘大小。 **取值范围**： 不涉及。

        :return: The total of this GroupDiskInfoResult.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this GroupDiskInfoResult.

        **参数解释**： 分片磁盘大小。 **取值范围**： 不涉及。

        :param total: The total of this GroupDiskInfoResult.
        :type total: float
        """
        self._total = total

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
        if not isinstance(other, GroupDiskInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
