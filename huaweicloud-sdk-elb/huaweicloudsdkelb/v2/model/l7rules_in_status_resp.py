# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7rulesInStatusResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, type=None, id=None, provisioning_status=None):
        """L7rulesInStatusResp

        The model defined in huaweicloud sdk

        :param type: 转发规则的匹配内容。PATH：匹配请求中的路径；HOST_NAME：匹配请求中的域名
        :type type: str
        :param id: 转发规则ID
        :type id: str
        :param provisioning_status: 转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。
        :type provisioning_status: str
        """
        
        

        self._type = None
        self._id = None
        self._provisioning_status = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.provisioning_status = provisioning_status

    @property
    def type(self):
        """Gets the type of this L7rulesInStatusResp.

        转发规则的匹配内容。PATH：匹配请求中的路径；HOST_NAME：匹配请求中的域名

        :return: The type of this L7rulesInStatusResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this L7rulesInStatusResp.

        转发规则的匹配内容。PATH：匹配请求中的路径；HOST_NAME：匹配请求中的域名

        :param type: The type of this L7rulesInStatusResp.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this L7rulesInStatusResp.

        转发规则ID

        :return: The id of this L7rulesInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7rulesInStatusResp.

        转发规则ID

        :param id: The id of this L7rulesInStatusResp.
        :type id: str
        """
        self._id = id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7rulesInStatusResp.

        转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this L7rulesInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7rulesInStatusResp.

        转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7rulesInStatusResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, L7rulesInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
