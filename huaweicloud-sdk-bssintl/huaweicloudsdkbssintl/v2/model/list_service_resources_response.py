# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceResourcesResponse(SdkResponse):

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
        'infos': 'list[ServiceResourceInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'infos': 'infos'
    }

    def __init__(self, total_count=None, infos=None):
        r"""ListServiceResourcesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param infos: 资源基本信息列表，具体请参见表3。
        :type infos: list[:class:`huaweicloudsdkbssintl.v2.ServiceResourceInfo`]
        """
        
        super(ListServiceResourcesResponse, self).__init__()

        self._total_count = None
        self._infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if infos is not None:
            self.infos = infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListServiceResourcesResponse.

        总数。

        :return: The total_count of this ListServiceResourcesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListServiceResourcesResponse.

        总数。

        :param total_count: The total_count of this ListServiceResourcesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def infos(self):
        r"""Gets the infos of this ListServiceResourcesResponse.

        资源基本信息列表，具体请参见表3。

        :return: The infos of this ListServiceResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.ServiceResourceInfo`]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        r"""Sets the infos of this ListServiceResourcesResponse.

        资源基本信息列表，具体请参见表3。

        :param infos: The infos of this ListServiceResourcesResponse.
        :type infos: list[:class:`huaweicloudsdkbssintl.v2.ServiceResourceInfo`]
        """
        self._infos = infos

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
        if not isinstance(other, ListServiceResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
