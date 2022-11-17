# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hostname': 'str',
        'waf_type': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'waf_type': 'waf_type',
        'mode': 'mode'
    }

    def __init__(self, id=None, hostname=None, waf_type=None, mode=None):
        """BindHost

        The model defined in huaweicloud sdk

        :param id: 域名ID
        :type id: str
        :param hostname: 域名
        :type hostname: str
        :param waf_type: 域名对应模式：cloud（云模式）/premium（独享模式）
        :type waf_type: str
        :param mode: 仅独享模式涉及特殊域名模式
        :type mode: str
        """
        
        

        self._id = None
        self._hostname = None
        self._waf_type = None
        self._mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if waf_type is not None:
            self.waf_type = waf_type
        if mode is not None:
            self.mode = mode

    @property
    def id(self):
        """Gets the id of this BindHost.

        域名ID

        :return: The id of this BindHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BindHost.

        域名ID

        :param id: The id of this BindHost.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this BindHost.

        域名

        :return: The hostname of this BindHost.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this BindHost.

        域名

        :param hostname: The hostname of this BindHost.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def waf_type(self):
        """Gets the waf_type of this BindHost.

        域名对应模式：cloud（云模式）/premium（独享模式）

        :return: The waf_type of this BindHost.
        :rtype: str
        """
        return self._waf_type

    @waf_type.setter
    def waf_type(self, waf_type):
        """Sets the waf_type of this BindHost.

        域名对应模式：cloud（云模式）/premium（独享模式）

        :param waf_type: The waf_type of this BindHost.
        :type waf_type: str
        """
        self._waf_type = waf_type

    @property
    def mode(self):
        """Gets the mode of this BindHost.

        仅独享模式涉及特殊域名模式

        :return: The mode of this BindHost.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this BindHost.

        仅独享模式涉及特殊域名模式

        :param mode: The mode of this BindHost.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, BindHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
