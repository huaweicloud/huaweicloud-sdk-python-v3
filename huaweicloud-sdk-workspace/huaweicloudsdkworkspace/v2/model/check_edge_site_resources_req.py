# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckEdgeSiteResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_id': 'str',
        'flavor_id': 'str',
        'resource_counts': 'int',
        'volumes': 'list[Volume]'
    }

    attribute_map = {
        'availability_zone_id': 'availability_zone_id',
        'flavor_id': 'flavor_id',
        'resource_counts': 'resource_counts',
        'volumes': 'volumes'
    }

    def __init__(self, availability_zone_id=None, flavor_id=None, resource_counts=None, volumes=None):
        r"""CheckEdgeSiteResourcesReq

        The model defined in huaweicloud sdk

        :param availability_zone_id: 可用区id。
        :type availability_zone_id: str
        :param flavor_id: 规格id。
        :type flavor_id: str
        :param resource_counts: 需要的资源数量。
        :type resource_counts: int
        :param volumes: 磁盘列表。
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        
        

        self._availability_zone_id = None
        self._flavor_id = None
        self._resource_counts = None
        self._volumes = None
        self.discriminator = None

        self.availability_zone_id = availability_zone_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if resource_counts is not None:
            self.resource_counts = resource_counts
        if volumes is not None:
            self.volumes = volumes

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this CheckEdgeSiteResourcesReq.

        可用区id。

        :return: The availability_zone_id of this CheckEdgeSiteResourcesReq.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this CheckEdgeSiteResourcesReq.

        可用区id。

        :param availability_zone_id: The availability_zone_id of this CheckEdgeSiteResourcesReq.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CheckEdgeSiteResourcesReq.

        规格id。

        :return: The flavor_id of this CheckEdgeSiteResourcesReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CheckEdgeSiteResourcesReq.

        规格id。

        :param flavor_id: The flavor_id of this CheckEdgeSiteResourcesReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def resource_counts(self):
        r"""Gets the resource_counts of this CheckEdgeSiteResourcesReq.

        需要的资源数量。

        :return: The resource_counts of this CheckEdgeSiteResourcesReq.
        :rtype: int
        """
        return self._resource_counts

    @resource_counts.setter
    def resource_counts(self, resource_counts):
        r"""Sets the resource_counts of this CheckEdgeSiteResourcesReq.

        需要的资源数量。

        :param resource_counts: The resource_counts of this CheckEdgeSiteResourcesReq.
        :type resource_counts: int
        """
        self._resource_counts = resource_counts

    @property
    def volumes(self):
        r"""Gets the volumes of this CheckEdgeSiteResourcesReq.

        磁盘列表。

        :return: The volumes of this CheckEdgeSiteResourcesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this CheckEdgeSiteResourcesReq.

        磁盘列表。

        :param volumes: The volumes of this CheckEdgeSiteResourcesReq.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._volumes = volumes

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
        if not isinstance(other, CheckEdgeSiteResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
