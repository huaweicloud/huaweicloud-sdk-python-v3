# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowRadarsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'radars': 'list[RadarResourceDTO]'
    }

    attribute_map = {
        'count': 'count',
        'radars': 'radars'
    }

    def __init__(self, count=None, radars=None):
        """BatchShowRadarsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：总数 
        :type count: int
        :param radars: **参数说明**：数据列表 
        :type radars: list[:class:`huaweicloudsdkdris.v1.RadarResourceDTO`]
        """
        
        super(BatchShowRadarsResponse, self).__init__()

        self._count = None
        self._radars = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if radars is not None:
            self.radars = radars

    @property
    def count(self):
        """Gets the count of this BatchShowRadarsResponse.

        **参数说明**：总数 

        :return: The count of this BatchShowRadarsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchShowRadarsResponse.

        **参数说明**：总数 

        :param count: The count of this BatchShowRadarsResponse.
        :type count: int
        """
        self._count = count

    @property
    def radars(self):
        """Gets the radars of this BatchShowRadarsResponse.

        **参数说明**：数据列表 

        :return: The radars of this BatchShowRadarsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.RadarResourceDTO`]
        """
        return self._radars

    @radars.setter
    def radars(self, radars):
        """Sets the radars of this BatchShowRadarsResponse.

        **参数说明**：数据列表 

        :param radars: The radars of this BatchShowRadarsResponse.
        :type radars: list[:class:`huaweicloudsdkdris.v1.RadarResourceDTO`]
        """
        self._radars = radars

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
        if not isinstance(other, BatchShowRadarsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
