# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachedEnterpriseRouterRegionId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_er_table_region_id': 'str'
    }

    attribute_map = {
        'attached_er_table_region_id': 'attached_er_table_region_id'
    }

    def __init__(self, attached_er_table_region_id=None):
        """AttachedEnterpriseRouterRegionId

        The model defined in huaweicloud sdk

        :param attached_er_table_region_id: ER路由器的regionID。
        :type attached_er_table_region_id: str
        """
        
        

        self._attached_er_table_region_id = None
        self.discriminator = None

        self.attached_er_table_region_id = attached_er_table_region_id

    @property
    def attached_er_table_region_id(self):
        """Gets the attached_er_table_region_id of this AttachedEnterpriseRouterRegionId.

        ER路由器的regionID。

        :return: The attached_er_table_region_id of this AttachedEnterpriseRouterRegionId.
        :rtype: str
        """
        return self._attached_er_table_region_id

    @attached_er_table_region_id.setter
    def attached_er_table_region_id(self, attached_er_table_region_id):
        """Sets the attached_er_table_region_id of this AttachedEnterpriseRouterRegionId.

        ER路由器的regionID。

        :param attached_er_table_region_id: The attached_er_table_region_id of this AttachedEnterpriseRouterRegionId.
        :type attached_er_table_region_id: str
        """
        self._attached_er_table_region_id = attached_er_table_region_id

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
        if not isinstance(other, AttachedEnterpriseRouterRegionId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
