# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSummaryResponseItemRegions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'count': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'count': 'count'
    }

    def __init__(self, region_id=None, count=None):
        r"""ResourceSummaryResponseItemRegions

        The model defined in huaweicloud sdk

        :param region_id: 区域id
        :type region_id: str
        :param count: 该资源类型在当前区域的数量
        :type count: int
        """
        
        

        self._region_id = None
        self._count = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if count is not None:
            self.count = count

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceSummaryResponseItemRegions.

        区域id

        :return: The region_id of this ResourceSummaryResponseItemRegions.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceSummaryResponseItemRegions.

        区域id

        :param region_id: The region_id of this ResourceSummaryResponseItemRegions.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def count(self):
        r"""Gets the count of this ResourceSummaryResponseItemRegions.

        该资源类型在当前区域的数量

        :return: The count of this ResourceSummaryResponseItemRegions.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ResourceSummaryResponseItemRegions.

        该资源类型在当前区域的数量

        :param count: The count of this ResourceSummaryResponseItemRegions.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ResourceSummaryResponseItemRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
