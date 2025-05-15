# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'area_id': 'AreaIdDef'
    }

    attribute_map = {
        'area_id': 'area_id'
    }

    def __init__(self, area_id=None):
        r"""AreaId

        The model defined in huaweicloud sdk

        :param area_id: 
        :type area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        
        

        self._area_id = None
        self.discriminator = None

        self.area_id = area_id

    @property
    def area_id(self):
        r"""Gets the area_id of this AreaId.

        :return: The area_id of this AreaId.
        :rtype: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        r"""Sets the area_id of this AreaId.

        :param area_id: The area_id of this AreaId.
        :type area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        self._area_id = area_id

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
        if not isinstance(other, AreaId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
