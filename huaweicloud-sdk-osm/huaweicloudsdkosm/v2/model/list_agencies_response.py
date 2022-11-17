# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgenciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'agency_list': 'list[AgencyV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'agency_list': 'agency_list'
    }

    def __init__(self, total_count=None, agency_list=None):
        """ListAgenciesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param agency_list: 委托列表
        :type agency_list: list[:class:`huaweicloudsdkosm.v2.AgencyV2`]
        """
        
        super(ListAgenciesResponse, self).__init__()

        self._total_count = None
        self._agency_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if agency_list is not None:
            self.agency_list = agency_list

    @property
    def total_count(self):
        """Gets the total_count of this ListAgenciesResponse.

        总数

        :return: The total_count of this ListAgenciesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListAgenciesResponse.

        总数

        :param total_count: The total_count of this ListAgenciesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def agency_list(self):
        """Gets the agency_list of this ListAgenciesResponse.

        委托列表

        :return: The agency_list of this ListAgenciesResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.AgencyV2`]
        """
        return self._agency_list

    @agency_list.setter
    def agency_list(self, agency_list):
        """Sets the agency_list of this ListAgenciesResponse.

        委托列表

        :param agency_list: The agency_list of this ListAgenciesResponse.
        :type agency_list: list[:class:`huaweicloudsdkosm.v2.AgencyV2`]
        """
        self._agency_list = agency_list

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
        if not isinstance(other, ListAgenciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
