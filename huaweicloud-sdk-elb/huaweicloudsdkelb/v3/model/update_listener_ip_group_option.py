# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateListenerIpGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ipgroup_id': 'str',
        'enable_ipgroup': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'ipgroup_id': 'ipgroup_id',
        'enable_ipgroup': 'enable_ipgroup',
        'type': 'type'
    }

    def __init__(self, ipgroup_id=None, enable_ipgroup=None, type=None):
        """UpdateListenerIpGroupOption

        The model defined in huaweicloud sdk

        :param ipgroup_id: 监听器关联的访问控制组的id。 创建时必选，更新时非必选。 指定的ipgroup必须已存在，不能指定为null，否则与enable_ipgroup冲突。 
        :type ipgroup_id: str
        :param enable_ipgroup: 访问控制组的状态。 True:开启访问控制； Flase：关闭访问控制； 开启访问控制的监听器，允许直接删除。
        :type enable_ipgroup: bool
        :param type: 访问控制组的类型。 white:白名单，只允许指定ip访问； black:黑名单，不允许指定ip访问； 
        :type type: str
        """
        
        

        self._ipgroup_id = None
        self._enable_ipgroup = None
        self._type = None
        self.discriminator = None

        if ipgroup_id is not None:
            self.ipgroup_id = ipgroup_id
        if enable_ipgroup is not None:
            self.enable_ipgroup = enable_ipgroup
        if type is not None:
            self.type = type

    @property
    def ipgroup_id(self):
        """Gets the ipgroup_id of this UpdateListenerIpGroupOption.

        监听器关联的访问控制组的id。 创建时必选，更新时非必选。 指定的ipgroup必须已存在，不能指定为null，否则与enable_ipgroup冲突。 

        :return: The ipgroup_id of this UpdateListenerIpGroupOption.
        :rtype: str
        """
        return self._ipgroup_id

    @ipgroup_id.setter
    def ipgroup_id(self, ipgroup_id):
        """Sets the ipgroup_id of this UpdateListenerIpGroupOption.

        监听器关联的访问控制组的id。 创建时必选，更新时非必选。 指定的ipgroup必须已存在，不能指定为null，否则与enable_ipgroup冲突。 

        :param ipgroup_id: The ipgroup_id of this UpdateListenerIpGroupOption.
        :type ipgroup_id: str
        """
        self._ipgroup_id = ipgroup_id

    @property
    def enable_ipgroup(self):
        """Gets the enable_ipgroup of this UpdateListenerIpGroupOption.

        访问控制组的状态。 True:开启访问控制； Flase：关闭访问控制； 开启访问控制的监听器，允许直接删除。

        :return: The enable_ipgroup of this UpdateListenerIpGroupOption.
        :rtype: bool
        """
        return self._enable_ipgroup

    @enable_ipgroup.setter
    def enable_ipgroup(self, enable_ipgroup):
        """Sets the enable_ipgroup of this UpdateListenerIpGroupOption.

        访问控制组的状态。 True:开启访问控制； Flase：关闭访问控制； 开启访问控制的监听器，允许直接删除。

        :param enable_ipgroup: The enable_ipgroup of this UpdateListenerIpGroupOption.
        :type enable_ipgroup: bool
        """
        self._enable_ipgroup = enable_ipgroup

    @property
    def type(self):
        """Gets the type of this UpdateListenerIpGroupOption.

        访问控制组的类型。 white:白名单，只允许指定ip访问； black:黑名单，不允许指定ip访问； 

        :return: The type of this UpdateListenerIpGroupOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateListenerIpGroupOption.

        访问控制组的类型。 white:白名单，只允许指定ip访问； black:黑名单，不允许指定ip访问； 

        :param type: The type of this UpdateListenerIpGroupOption.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, UpdateListenerIpGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
