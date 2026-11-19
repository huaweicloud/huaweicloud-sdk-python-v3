# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeFlavorItemDetail:

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
        'media_type': 'str',
        'az_status': 'dict(str, str)',
        'support_compute_group_type': 'list[str]'
    }

    attribute_map = {
        'io_type': 'io_type',
        'media_type': 'media_type',
        'az_status': 'az_status',
        'support_compute_group_type': 'support_compute_group_type'
    }

    def __init__(self, io_type=None, media_type=None, az_status=None, support_compute_group_type=None):
        r"""VolumeFlavorItemDetail

        The model defined in huaweicloud sdk

        :param io_type: **参数解释**: IO类型。 **取值范围**: - ULTRAHIGH：超高IO。 - ESSD：极速型SSD。
        :type io_type: str
        :param media_type: **参数解释**: 存储介质类型。 **取值范围**: - SAS：高IO云硬盘。 - SSD：超高IO云硬盘。 - ESSD：极速型SSD云硬盘。
        :type media_type: str
        :param az_status: **参数解释**: 存储规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。
        :type az_status: dict(str, str)
        :param support_compute_group_type: **参数解释**: 该存储规格支持的计算规格组类型列表。 **取值范围**: 不涉及。
        :type support_compute_group_type: list[str]
        """
        
        

        self._io_type = None
        self._media_type = None
        self._az_status = None
        self._support_compute_group_type = None
        self.discriminator = None

        if io_type is not None:
            self.io_type = io_type
        if media_type is not None:
            self.media_type = media_type
        if az_status is not None:
            self.az_status = az_status
        if support_compute_group_type is not None:
            self.support_compute_group_type = support_compute_group_type

    @property
    def io_type(self):
        r"""Gets the io_type of this VolumeFlavorItemDetail.

        **参数解释**: IO类型。 **取值范围**: - ULTRAHIGH：超高IO。 - ESSD：极速型SSD。

        :return: The io_type of this VolumeFlavorItemDetail.
        :rtype: str
        """
        return self._io_type

    @io_type.setter
    def io_type(self, io_type):
        r"""Sets the io_type of this VolumeFlavorItemDetail.

        **参数解释**: IO类型。 **取值范围**: - ULTRAHIGH：超高IO。 - ESSD：极速型SSD。

        :param io_type: The io_type of this VolumeFlavorItemDetail.
        :type io_type: str
        """
        self._io_type = io_type

    @property
    def media_type(self):
        r"""Gets the media_type of this VolumeFlavorItemDetail.

        **参数解释**: 存储介质类型。 **取值范围**: - SAS：高IO云硬盘。 - SSD：超高IO云硬盘。 - ESSD：极速型SSD云硬盘。

        :return: The media_type of this VolumeFlavorItemDetail.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        r"""Sets the media_type of this VolumeFlavorItemDetail.

        **参数解释**: 存储介质类型。 **取值范围**: - SAS：高IO云硬盘。 - SSD：超高IO云硬盘。 - ESSD：极速型SSD云硬盘。

        :param media_type: The media_type of this VolumeFlavorItemDetail.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def az_status(self):
        r"""Gets the az_status of this VolumeFlavorItemDetail.

        **参数解释**: 存储规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。

        :return: The az_status of this VolumeFlavorItemDetail.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this VolumeFlavorItemDetail.

        **参数解释**: 存储规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。

        :param az_status: The az_status of this VolumeFlavorItemDetail.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def support_compute_group_type(self):
        r"""Gets the support_compute_group_type of this VolumeFlavorItemDetail.

        **参数解释**: 该存储规格支持的计算规格组类型列表。 **取值范围**: 不涉及。

        :return: The support_compute_group_type of this VolumeFlavorItemDetail.
        :rtype: list[str]
        """
        return self._support_compute_group_type

    @support_compute_group_type.setter
    def support_compute_group_type(self, support_compute_group_type):
        r"""Sets the support_compute_group_type of this VolumeFlavorItemDetail.

        **参数解释**: 该存储规格支持的计算规格组类型列表。 **取值范围**: 不涉及。

        :param support_compute_group_type: The support_compute_group_type of this VolumeFlavorItemDetail.
        :type support_compute_group_type: list[str]
        """
        self._support_compute_group_type = support_compute_group_type

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
        if not isinstance(other, VolumeFlavorItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
