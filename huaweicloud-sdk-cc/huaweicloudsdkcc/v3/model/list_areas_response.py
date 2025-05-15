# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAreasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'areas': 'list[Area]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'areas': 'areas'
    }

    def __init__(self, request_id=None, areas=None):
        r"""ListAreasResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param areas: 大区列表。
        :type areas: list[:class:`huaweicloudsdkcc.v3.Area`]
        """
        
        super(ListAreasResponse, self).__init__()

        self._request_id = None
        self._areas = None
        self.discriminator = None

        self.request_id = request_id
        self.areas = areas

    @property
    def request_id(self):
        r"""Gets the request_id of this ListAreasResponse.

        请求ID。

        :return: The request_id of this ListAreasResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListAreasResponse.

        请求ID。

        :param request_id: The request_id of this ListAreasResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def areas(self):
        r"""Gets the areas of this ListAreasResponse.

        大区列表。

        :return: The areas of this ListAreasResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Area`]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        r"""Sets the areas of this ListAreasResponse.

        大区列表。

        :param areas: The areas of this ListAreasResponse.
        :type areas: list[:class:`huaweicloudsdkcc.v3.Area`]
        """
        self._areas = areas

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
        if not isinstance(other, ListAreasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
