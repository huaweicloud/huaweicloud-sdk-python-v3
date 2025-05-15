# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNetworkInstance:

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
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cidrs': 'cidrs'
    }

    def __init__(self, name=None, description=None, cidrs=None):
        r"""UpdateNetworkInstance

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param cidrs: 网络实例发布的网段路由列表。
        :type cidrs: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._cidrs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def name(self):
        r"""Gets the name of this UpdateNetworkInstance.

        实例名称。

        :return: The name of this UpdateNetworkInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateNetworkInstance.

        实例名称。

        :param name: The name of this UpdateNetworkInstance.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateNetworkInstance.

        实例描述。不支持 <>。

        :return: The description of this UpdateNetworkInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateNetworkInstance.

        实例描述。不支持 <>。

        :param description: The description of this UpdateNetworkInstance.
        :type description: str
        """
        self._description = description

    @property
    def cidrs(self):
        r"""Gets the cidrs of this UpdateNetworkInstance.

        网络实例发布的网段路由列表。

        :return: The cidrs of this UpdateNetworkInstance.
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        r"""Sets the cidrs of this UpdateNetworkInstance.

        网络实例发布的网段路由列表。

        :param cidrs: The cidrs of this UpdateNetworkInstance.
        :type cidrs: list[str]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, UpdateNetworkInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
