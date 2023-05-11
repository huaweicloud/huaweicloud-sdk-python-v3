# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OBSInfo:

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
        'addr': 'str'
    }

    attribute_map = {
        'name': 'name',
        'addr': 'addr'
    }

    def __init__(self, name=None, addr=None):
        """OBSInfo

        The model defined in huaweicloud sdk

        :param name: OBS桶名称
        :type name: str
        :param addr: OBS桶地址
        :type addr: str
        """
        
        

        self._name = None
        self._addr = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if addr is not None:
            self.addr = addr

    @property
    def name(self):
        """Gets the name of this OBSInfo.

        OBS桶名称

        :return: The name of this OBSInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OBSInfo.

        OBS桶名称

        :param name: The name of this OBSInfo.
        :type name: str
        """
        self._name = name

    @property
    def addr(self):
        """Gets the addr of this OBSInfo.

        OBS桶地址

        :return: The addr of this OBSInfo.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this OBSInfo.

        OBS桶地址

        :param addr: The addr of this OBSInfo.
        :type addr: str
        """
        self._addr = addr

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
        if not isinstance(other, OBSInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
