# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkCapabilitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capability': 'list[CentralNetworkCapabilityEnum]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'capability': 'capability',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, capability=None, limit=None, marker=None):
        r"""ListCentralNetworkCapabilitiesRequest

        The model defined in huaweicloud sdk

        :param capability: 根据租户能力名查询，可查询多个类型。
        :type capability: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        """
        
        

        self._capability = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if capability is not None:
            self.capability = capability
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def capability(self):
        r"""Gets the capability of this ListCentralNetworkCapabilitiesRequest.

        根据租户能力名查询，可查询多个类型。

        :return: The capability of this ListCentralNetworkCapabilitiesRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        r"""Sets the capability of this ListCentralNetworkCapabilitiesRequest.

        根据租户能力名查询，可查询多个类型。

        :param capability: The capability of this ListCentralNetworkCapabilitiesRequest.
        :type capability: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        """
        self._capability = capability

    @property
    def limit(self):
        r"""Gets the limit of this ListCentralNetworkCapabilitiesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCentralNetworkCapabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCentralNetworkCapabilitiesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCentralNetworkCapabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCentralNetworkCapabilitiesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListCentralNetworkCapabilitiesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCentralNetworkCapabilitiesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListCentralNetworkCapabilitiesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListCentralNetworkCapabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
