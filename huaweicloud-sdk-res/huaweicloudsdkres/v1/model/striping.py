# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Striping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nearest_neighborhood': 'int',
        'band': 'int',
        'row': 'int'
    }

    attribute_map = {
        'nearest_neighborhood': 'nearest_neighborhood',
        'band': 'band',
        'row': 'row'
    }

    def __init__(self, nearest_neighborhood=None, band=None, row=None):
        """Striping

        The model defined in huaweicloud sdk

        :param nearest_neighborhood: 最近领域个数。
        :type nearest_neighborhood: int
        :param band: 相似程度。
        :type band: int
        :param row: 相似距离。
        :type row: int
        """
        
        

        self._nearest_neighborhood = None
        self._band = None
        self._row = None
        self.discriminator = None

        self.nearest_neighborhood = nearest_neighborhood
        self.band = band
        self.row = row

    @property
    def nearest_neighborhood(self):
        """Gets the nearest_neighborhood of this Striping.

        最近领域个数。

        :return: The nearest_neighborhood of this Striping.
        :rtype: int
        """
        return self._nearest_neighborhood

    @nearest_neighborhood.setter
    def nearest_neighborhood(self, nearest_neighborhood):
        """Sets the nearest_neighborhood of this Striping.

        最近领域个数。

        :param nearest_neighborhood: The nearest_neighborhood of this Striping.
        :type nearest_neighborhood: int
        """
        self._nearest_neighborhood = nearest_neighborhood

    @property
    def band(self):
        """Gets the band of this Striping.

        相似程度。

        :return: The band of this Striping.
        :rtype: int
        """
        return self._band

    @band.setter
    def band(self, band):
        """Sets the band of this Striping.

        相似程度。

        :param band: The band of this Striping.
        :type band: int
        """
        self._band = band

    @property
    def row(self):
        """Gets the row of this Striping.

        相似距离。

        :return: The row of this Striping.
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this Striping.

        相似距离。

        :param row: The row of this Striping.
        :type row: int
        """
        self._row = row

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
        if not isinstance(other, Striping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
