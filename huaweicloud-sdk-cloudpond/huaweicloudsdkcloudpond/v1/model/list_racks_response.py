# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRacksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'racks': 'list[Rack]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'racks': 'racks',
        'page_info': 'page_info'
    }

    def __init__(self, racks=None, page_info=None):
        r"""ListRacksResponse

        The model defined in huaweicloud sdk

        :param racks: 机柜列表
        :type racks: list[:class:`huaweicloudsdkcloudpond.v1.Rack`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        
        super(ListRacksResponse, self).__init__()

        self._racks = None
        self._page_info = None
        self.discriminator = None

        if racks is not None:
            self.racks = racks
        if page_info is not None:
            self.page_info = page_info

    @property
    def racks(self):
        r"""Gets the racks of this ListRacksResponse.

        机柜列表

        :return: The racks of this ListRacksResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v1.Rack`]
        """
        return self._racks

    @racks.setter
    def racks(self, racks):
        r"""Sets the racks of this ListRacksResponse.

        机柜列表

        :param racks: The racks of this ListRacksResponse.
        :type racks: list[:class:`huaweicloudsdkcloudpond.v1.Rack`]
        """
        self._racks = racks

    @property
    def page_info(self):
        r"""Gets the page_info of this ListRacksResponse.

        :return: The page_info of this ListRacksResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListRacksResponse.

        :param page_info: The page_info of this ListRacksResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListRacksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
