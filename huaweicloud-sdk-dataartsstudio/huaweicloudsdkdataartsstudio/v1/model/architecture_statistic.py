# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArchitectureStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'children': 'list[ArchitectureStatistic]',
        'count': 'int',
        'guid': 'str',
        'name': 'str'
    }

    attribute_map = {
        'children': 'children',
        'count': 'count',
        'guid': 'guid',
        'name': 'name'
    }

    def __init__(self, children=None, count=None, guid=None, name=None):
        r"""ArchitectureStatistic

        The model defined in huaweicloud sdk

        :param children: 子指标
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        :param count: 子指标个数
        :type count: int
        :param guid: guid
        :type guid: str
        :param name: 名称
        :type name: str
        """
        
        

        self._children = None
        self._count = None
        self._guid = None
        self._name = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if count is not None:
            self.count = count
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name

    @property
    def children(self):
        r"""Gets the children of this ArchitectureStatistic.

        子指标

        :return: The children of this ArchitectureStatistic.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ArchitectureStatistic.

        子指标

        :param children: The children of this ArchitectureStatistic.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        """
        self._children = children

    @property
    def count(self):
        r"""Gets the count of this ArchitectureStatistic.

        子指标个数

        :return: The count of this ArchitectureStatistic.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ArchitectureStatistic.

        子指标个数

        :param count: The count of this ArchitectureStatistic.
        :type count: int
        """
        self._count = count

    @property
    def guid(self):
        r"""Gets the guid of this ArchitectureStatistic.

        guid

        :return: The guid of this ArchitectureStatistic.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ArchitectureStatistic.

        guid

        :param guid: The guid of this ArchitectureStatistic.
        :type guid: str
        """
        self._guid = guid

    @property
    def name(self):
        r"""Gets the name of this ArchitectureStatistic.

        名称

        :return: The name of this ArchitectureStatistic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArchitectureStatistic.

        名称

        :param name: The name of this ArchitectureStatistic.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ArchitectureStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
