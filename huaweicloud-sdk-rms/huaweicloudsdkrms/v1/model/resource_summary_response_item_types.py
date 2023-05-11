# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSummaryResponseItemTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'regions': 'list[ResourceSummaryResponseItemRegions]'
    }

    attribute_map = {
        'type': 'type',
        'regions': 'regions'
    }

    def __init__(self, type=None, regions=None):
        """ResourceSummaryResponseItemTypes

        The model defined in huaweicloud sdk

        :param type: 资源类型名称
        :type type: str
        :param regions: 区域列表
        :type regions: list[:class:`huaweicloudsdkrms.v1.ResourceSummaryResponseItemRegions`]
        """
        
        

        self._type = None
        self._regions = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if regions is not None:
            self.regions = regions

    @property
    def type(self):
        """Gets the type of this ResourceSummaryResponseItemTypes.

        资源类型名称

        :return: The type of this ResourceSummaryResponseItemTypes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceSummaryResponseItemTypes.

        资源类型名称

        :param type: The type of this ResourceSummaryResponseItemTypes.
        :type type: str
        """
        self._type = type

    @property
    def regions(self):
        """Gets the regions of this ResourceSummaryResponseItemTypes.

        区域列表

        :return: The regions of this ResourceSummaryResponseItemTypes.
        :rtype: list[:class:`huaweicloudsdkrms.v1.ResourceSummaryResponseItemRegions`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ResourceSummaryResponseItemTypes.

        区域列表

        :param regions: The regions of this ResourceSummaryResponseItemTypes.
        :type regions: list[:class:`huaweicloudsdkrms.v1.ResourceSummaryResponseItemRegions`]
        """
        self._regions = regions

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
        if not isinstance(other, ResourceSummaryResponseItemTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
