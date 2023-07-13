# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicipPoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_pool_id': 'str',
        'fields': 'str'
    }

    attribute_map = {
        'publicip_pool_id': 'publicip_pool_id',
        'fields': 'fields'
    }

    def __init__(self, publicip_pool_id=None, fields=None):
        """ShowPublicipPoolRequest

        The model defined in huaweicloud sdk

        :param publicip_pool_id: 公网IP池ID唯一标识
        :type publicip_pool_id: str
        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;name&amp;...\&quot;  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group
        :type fields: str
        """
        
        

        self._publicip_pool_id = None
        self._fields = None
        self.discriminator = None

        self.publicip_pool_id = publicip_pool_id
        if fields is not None:
            self.fields = fields

    @property
    def publicip_pool_id(self):
        """Gets the publicip_pool_id of this ShowPublicipPoolRequest.

        公网IP池ID唯一标识

        :return: The publicip_pool_id of this ShowPublicipPoolRequest.
        :rtype: str
        """
        return self._publicip_pool_id

    @publicip_pool_id.setter
    def publicip_pool_id(self, publicip_pool_id):
        """Sets the publicip_pool_id of this ShowPublicipPoolRequest.

        公网IP池ID唯一标识

        :param publicip_pool_id: The publicip_pool_id of this ShowPublicipPoolRequest.
        :type publicip_pool_id: str
        """
        self._publicip_pool_id = publicip_pool_id

    @property
    def fields(self):
        """Gets the fields of this ShowPublicipPoolRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group

        :return: The fields of this ShowPublicipPoolRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowPublicipPoolRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：id/name/size/used/project_id/status/billing_info/created_at/updated_at/type/shared/is_common/description/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group

        :param fields: The fields of this ShowPublicipPoolRequest.
        :type fields: str
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
        if not isinstance(other, ShowPublicipPoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
