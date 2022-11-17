# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRouteTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_table': 'UpdateRouteTable'
    }

    attribute_map = {
        'route_table': 'route_table'
    }

    def __init__(self, route_table=None):
        """UpdateRouteTableRequestBody

        The model defined in huaweicloud sdk

        :param route_table: 
        :type route_table: :class:`huaweicloudsdker.v3.UpdateRouteTable`
        """
        
        

        self._route_table = None
        self.discriminator = None

        if route_table is not None:
            self.route_table = route_table

    @property
    def route_table(self):
        """Gets the route_table of this UpdateRouteTableRequestBody.

        :return: The route_table of this UpdateRouteTableRequestBody.
        :rtype: :class:`huaweicloudsdker.v3.UpdateRouteTable`
        """
        return self._route_table

    @route_table.setter
    def route_table(self, route_table):
        """Sets the route_table of this UpdateRouteTableRequestBody.

        :param route_table: The route_table of this UpdateRouteTableRequestBody.
        :type route_table: :class:`huaweicloudsdker.v3.UpdateRouteTable`
        """
        self._route_table = route_table

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
        if not isinstance(other, UpdateRouteTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
