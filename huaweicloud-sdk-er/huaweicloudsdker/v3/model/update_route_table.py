# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRouteTable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'bgp_options': 'BgpOptions'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bgp_options': 'bgp_options'
    }

    def __init__(self, name=None, description=None, bgp_options=None):
        """UpdateRouteTable

        The model defined in huaweicloud sdk

        :param name: 路由器表名称
        :type name: str
        :param description: 路由器表描述信息
        :type description: str
        :param bgp_options: 
        :type bgp_options: :class:`huaweicloudsdker.v3.BgpOptions`
        """
        
        

        self._name = None
        self._description = None
        self._bgp_options = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bgp_options is not None:
            self.bgp_options = bgp_options

    @property
    def name(self):
        """Gets the name of this UpdateRouteTable.

        路由器表名称

        :return: The name of this UpdateRouteTable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRouteTable.

        路由器表名称

        :param name: The name of this UpdateRouteTable.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateRouteTable.

        路由器表描述信息

        :return: The description of this UpdateRouteTable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRouteTable.

        路由器表描述信息

        :param description: The description of this UpdateRouteTable.
        :type description: str
        """
        self._description = description

    @property
    def bgp_options(self):
        """Gets the bgp_options of this UpdateRouteTable.


        :return: The bgp_options of this UpdateRouteTable.
        :rtype: :class:`huaweicloudsdker.v3.BgpOptions`
        """
        return self._bgp_options

    @bgp_options.setter
    def bgp_options(self, bgp_options):
        """Sets the bgp_options of this UpdateRouteTable.


        :param bgp_options: The bgp_options of this UpdateRouteTable.
        :type bgp_options: :class:`huaweicloudsdker.v3.BgpOptions`
        """
        self._bgp_options = bgp_options

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
        if not isinstance(other, UpdateRouteTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
