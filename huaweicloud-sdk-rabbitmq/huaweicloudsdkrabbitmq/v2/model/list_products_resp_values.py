# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRespValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'list[ListProductsRespDetail]',
        'name': 'str',
        'unavailable_zones': 'list[str]',
        'available_zones': 'list[str]'
    }

    attribute_map = {
        'detail': 'detail',
        'name': 'name',
        'unavailable_zones': 'unavailable_zones',
        'available_zones': 'available_zones'
    }

    def __init__(self, detail=None, name=None, unavailable_zones=None, available_zones=None):
        r"""ListProductsRespValues

        The model defined in huaweicloud sdk

        :param detail: 规格详情。
        :type detail: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespDetail`]
        :param name: 实例类型。
        :type name: str
        :param unavailable_zones: 资源售罄的可用区列表。
        :type unavailable_zones: list[str]
        :param available_zones: 有可用资源的可用区列表。
        :type available_zones: list[str]
        """
        
        

        self._detail = None
        self._name = None
        self._unavailable_zones = None
        self._available_zones = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if name is not None:
            self.name = name
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def detail(self):
        r"""Gets the detail of this ListProductsRespValues.

        规格详情。

        :return: The detail of this ListProductsRespValues.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespDetail`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ListProductsRespValues.

        规格详情。

        :param detail: The detail of this ListProductsRespValues.
        :type detail: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespDetail`]
        """
        self._detail = detail

    @property
    def name(self):
        r"""Gets the name of this ListProductsRespValues.

        实例类型。

        :return: The name of this ListProductsRespValues.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListProductsRespValues.

        实例类型。

        :param name: The name of this ListProductsRespValues.
        :type name: str
        """
        self._name = name

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this ListProductsRespValues.

        资源售罄的可用区列表。

        :return: The unavailable_zones of this ListProductsRespValues.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this ListProductsRespValues.

        资源售罄的可用区列表。

        :param unavailable_zones: The unavailable_zones of this ListProductsRespValues.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListProductsRespValues.

        有可用资源的可用区列表。

        :return: The available_zones of this ListProductsRespValues.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListProductsRespValues.

        有可用资源的可用区列表。

        :param available_zones: The available_zones of this ListProductsRespValues.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, ListProductsRespValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
