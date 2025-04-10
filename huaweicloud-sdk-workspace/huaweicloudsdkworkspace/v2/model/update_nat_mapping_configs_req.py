# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatMappingConfigsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'nat_on': 'bool',
        'nat_vag_maps': 'list[UpdateNatMappingConfig]'
    }

    attribute_map = {
        'site_id': 'site_id',
        'nat_on': 'nat_on',
        'nat_vag_maps': 'nat_vag_maps'
    }

    def __init__(self, site_id=None, nat_on=None, nat_vag_maps=None):
        r"""UpdateNatMappingConfigsReq

        The model defined in huaweicloud sdk

        :param site_id: 站点ID。
        :type site_id: str
        :param nat_on: 是否开启nat映射。
        :type nat_on: bool
        :param nat_vag_maps: NAT映射配置表。
        :type nat_vag_maps: list[:class:`huaweicloudsdkworkspace.v2.UpdateNatMappingConfig`]
        """
        
        

        self._site_id = None
        self._nat_on = None
        self._nat_vag_maps = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if nat_on is not None:
            self.nat_on = nat_on
        if nat_vag_maps is not None:
            self.nat_vag_maps = nat_vag_maps

    @property
    def site_id(self):
        r"""Gets the site_id of this UpdateNatMappingConfigsReq.

        站点ID。

        :return: The site_id of this UpdateNatMappingConfigsReq.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this UpdateNatMappingConfigsReq.

        站点ID。

        :param site_id: The site_id of this UpdateNatMappingConfigsReq.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def nat_on(self):
        r"""Gets the nat_on of this UpdateNatMappingConfigsReq.

        是否开启nat映射。

        :return: The nat_on of this UpdateNatMappingConfigsReq.
        :rtype: bool
        """
        return self._nat_on

    @nat_on.setter
    def nat_on(self, nat_on):
        r"""Sets the nat_on of this UpdateNatMappingConfigsReq.

        是否开启nat映射。

        :param nat_on: The nat_on of this UpdateNatMappingConfigsReq.
        :type nat_on: bool
        """
        self._nat_on = nat_on

    @property
    def nat_vag_maps(self):
        r"""Gets the nat_vag_maps of this UpdateNatMappingConfigsReq.

        NAT映射配置表。

        :return: The nat_vag_maps of this UpdateNatMappingConfigsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UpdateNatMappingConfig`]
        """
        return self._nat_vag_maps

    @nat_vag_maps.setter
    def nat_vag_maps(self, nat_vag_maps):
        r"""Sets the nat_vag_maps of this UpdateNatMappingConfigsReq.

        NAT映射配置表。

        :param nat_vag_maps: The nat_vag_maps of this UpdateNatMappingConfigsReq.
        :type nat_vag_maps: list[:class:`huaweicloudsdkworkspace.v2.UpdateNatMappingConfig`]
        """
        self._nat_vag_maps = nat_vag_maps

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
        if not isinstance(other, UpdateNatMappingConfigsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
