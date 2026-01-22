# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRespIo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'io_type': 'str',
        'storage_spec_code': 'str',
        'available_zones': 'list[str]',
        'unavailable_zones': 'list[str]',
        'volume_type': 'str'
    }

    attribute_map = {
        'io_type': 'io_type',
        'storage_spec_code': 'storage_spec_code',
        'available_zones': 'available_zones',
        'unavailable_zones': 'unavailable_zones',
        'volume_type': 'volume_type'
    }

    def __init__(self, io_type=None, storage_spec_code=None, available_zones=None, unavailable_zones=None, volume_type=None):
        r"""ListProductsRespIo

        The model defined in huaweicloud sdk

        :param io_type: **参数解释**： IO类型。 **取值范围**： 不涉及。
        :type io_type: str
        :param storage_spec_code: **参数解释**： IO规格。 **取值范围**： 不涉及。
        :type storage_spec_code: str
        :param available_zones: **参数解释**： IO未售罄的可用区列表。 **取值范围**： 不涉及。
        :type available_zones: list[str]
        :param unavailable_zones: **参数解释**： IO已售罄的不可用区列表。 **取值范围**： 不涉及。
        :type unavailable_zones: list[str]
        :param volume_type: **参数解释**： 磁盘类型。 **取值范围**： 不涉及。
        :type volume_type: str
        """
        
        

        self._io_type = None
        self._storage_spec_code = None
        self._available_zones = None
        self._unavailable_zones = None
        self._volume_type = None
        self.discriminator = None

        if io_type is not None:
            self.io_type = io_type
        if storage_spec_code is not None:
            self.storage_spec_code = storage_spec_code
        if available_zones is not None:
            self.available_zones = available_zones
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def io_type(self):
        r"""Gets the io_type of this ListProductsRespIo.

        **参数解释**： IO类型。 **取值范围**： 不涉及。

        :return: The io_type of this ListProductsRespIo.
        :rtype: str
        """
        return self._io_type

    @io_type.setter
    def io_type(self, io_type):
        r"""Sets the io_type of this ListProductsRespIo.

        **参数解释**： IO类型。 **取值范围**： 不涉及。

        :param io_type: The io_type of this ListProductsRespIo.
        :type io_type: str
        """
        self._io_type = io_type

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this ListProductsRespIo.

        **参数解释**： IO规格。 **取值范围**： 不涉及。

        :return: The storage_spec_code of this ListProductsRespIo.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this ListProductsRespIo.

        **参数解释**： IO规格。 **取值范围**： 不涉及。

        :param storage_spec_code: The storage_spec_code of this ListProductsRespIo.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListProductsRespIo.

        **参数解释**： IO未售罄的可用区列表。 **取值范围**： 不涉及。

        :return: The available_zones of this ListProductsRespIo.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListProductsRespIo.

        **参数解释**： IO未售罄的可用区列表。 **取值范围**： 不涉及。

        :param available_zones: The available_zones of this ListProductsRespIo.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this ListProductsRespIo.

        **参数解释**： IO已售罄的不可用区列表。 **取值范围**： 不涉及。

        :return: The unavailable_zones of this ListProductsRespIo.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this ListProductsRespIo.

        **参数解释**： IO已售罄的不可用区列表。 **取值范围**： 不涉及。

        :param unavailable_zones: The unavailable_zones of this ListProductsRespIo.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ListProductsRespIo.

        **参数解释**： 磁盘类型。 **取值范围**： 不涉及。

        :return: The volume_type of this ListProductsRespIo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ListProductsRespIo.

        **参数解释**： 磁盘类型。 **取值范围**： 不涉及。

        :param volume_type: The volume_type of this ListProductsRespIo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListProductsRespIo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
