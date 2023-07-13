# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicipRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'fields': 'list[str]'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'fields': 'fields'
    }

    def __init__(self, publicip_id=None, fields=None):
        """ShowPublicipRequest

        The model defined in huaweicloud sdk

        :param publicip_id: 弹性公网IP的ID
        :type publicip_id: str
        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;owner&amp;...\&quot;  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/publicip_pool_name/allow_share_bandwidth_types/alias/publicip_pool_id/public_border_group
        :type fields: list[str]
        """
        
        

        self._publicip_id = None
        self._fields = None
        self.discriminator = None

        self.publicip_id = publicip_id
        if fields is not None:
            self.fields = fields

    @property
    def publicip_id(self):
        """Gets the publicip_id of this ShowPublicipRequest.

        弹性公网IP的ID

        :return: The publicip_id of this ShowPublicipRequest.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this ShowPublicipRequest.

        弹性公网IP的ID

        :param publicip_id: The publicip_id of this ShowPublicipRequest.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def fields(self):
        """Gets the fields of this ShowPublicipRequest.

        显示，形式为\"fields=id&fields=owner&...\"  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/publicip_pool_name/allow_share_bandwidth_types/alias/publicip_pool_id/public_border_group

        :return: The fields of this ShowPublicipRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowPublicipRequest.

        显示，形式为\"fields=id&fields=owner&...\"  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/publicip_pool_name/allow_share_bandwidth_types/alias/publicip_pool_id/public_border_group

        :param fields: The fields of this ShowPublicipRequest.
        :type fields: list[str]
        """
        self._fields = fields

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
        if not isinstance(other, ShowPublicipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
