# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqUpdateDehMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auto_placement': 'str',
        'name': 'str'
    }

    attribute_map = {
        'auto_placement': 'auto_placement',
        'name': 'name'
    }

    def __init__(self, auto_placement=None, name=None):
        """ReqUpdateDehMessage

        The model defined in huaweicloud sdk

        :param auto_placement: 在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。  取值范围：“on”或“off”。
        :type auto_placement: str
        :param name: 专属主机名称。
        :type name: str
        """
        
        

        self._auto_placement = None
        self._name = None
        self.discriminator = None

        if auto_placement is not None:
            self.auto_placement = auto_placement
        if name is not None:
            self.name = name

    @property
    def auto_placement(self):
        """Gets the auto_placement of this ReqUpdateDehMessage.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。  取值范围：“on”或“off”。

        :return: The auto_placement of this ReqUpdateDehMessage.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this ReqUpdateDehMessage.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。  取值范围：“on”或“off”。

        :param auto_placement: The auto_placement of this ReqUpdateDehMessage.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def name(self):
        """Gets the name of this ReqUpdateDehMessage.

        专属主机名称。

        :return: The name of this ReqUpdateDehMessage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReqUpdateDehMessage.

        专属主机名称。

        :param name: The name of this ReqUpdateDehMessage.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ReqUpdateDehMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
