# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricRelationsResultDataValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all': 'list[object]',
        'links': 'object',
        'groups': 'object',
        'total': 'int'
    }

    attribute_map = {
        'all': 'all',
        'links': 'links',
        'groups': 'groups',
        'total': 'total'
    }

    def __init__(self, all=None, links=None, groups=None, total=None):
        r"""ListMetricRelationsResultDataValue

        The model defined in huaweicloud sdk

        :param all: 所有的业务指标信息。
        :type all: list[object]
        :param links: 指标关联。
        :type links: object
        :param groups: 分组。
        :type groups: object
        :param total: 总数。
        :type total: int
        """
        
        

        self._all = None
        self._links = None
        self._groups = None
        self._total = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if links is not None:
            self.links = links
        if groups is not None:
            self.groups = groups
        if total is not None:
            self.total = total

    @property
    def all(self):
        r"""Gets the all of this ListMetricRelationsResultDataValue.

        所有的业务指标信息。

        :return: The all of this ListMetricRelationsResultDataValue.
        :rtype: list[object]
        """
        return self._all

    @all.setter
    def all(self, all):
        r"""Sets the all of this ListMetricRelationsResultDataValue.

        所有的业务指标信息。

        :param all: The all of this ListMetricRelationsResultDataValue.
        :type all: list[object]
        """
        self._all = all

    @property
    def links(self):
        r"""Gets the links of this ListMetricRelationsResultDataValue.

        指标关联。

        :return: The links of this ListMetricRelationsResultDataValue.
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListMetricRelationsResultDataValue.

        指标关联。

        :param links: The links of this ListMetricRelationsResultDataValue.
        :type links: object
        """
        self._links = links

    @property
    def groups(self):
        r"""Gets the groups of this ListMetricRelationsResultDataValue.

        分组。

        :return: The groups of this ListMetricRelationsResultDataValue.
        :rtype: object
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ListMetricRelationsResultDataValue.

        分组。

        :param groups: The groups of this ListMetricRelationsResultDataValue.
        :type groups: object
        """
        self._groups = groups

    @property
    def total(self):
        r"""Gets the total of this ListMetricRelationsResultDataValue.

        总数。

        :return: The total of this ListMetricRelationsResultDataValue.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListMetricRelationsResultDataValue.

        总数。

        :param total: The total of this ListMetricRelationsResultDataValue.
        :type total: int
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
        if not isinstance(other, ListMetricRelationsResultDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
