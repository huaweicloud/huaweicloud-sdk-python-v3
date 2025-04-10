# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductTopicRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission': 'int',
        'name': 'str',
        'version': 'str',
        'description': 'str'
    }

    attribute_map = {
        'permission': 'permission',
        'name': 'name',
        'version': 'version',
        'description': 'description'
    }

    def __init__(self, permission=None, name=None, version=None, description=None):
        r"""CreateProductTopicRequestBody

        The model defined in huaweicloud sdk

        :param permission: 主题权限 0-发布 1-订阅
        :type permission: int
        :param name: 产品级主题名称&lt;br&gt;Topic类格式必须以“/”进行分层，区分每个类目。其中第一个为用户自定义的版本号；第二个已经规定好，为${deviceId}通配设备ID；第三个为用户自定义的topic类名（即本字段）。Topic类组成即为：/${version}/${deviceId}/${customizePart}。简单来说，Topic类：/v1/${deviceId}/customizePart是具体Topic：/v1/deviceid1/customizePart1和/v1/deviceid2/customizePart2等的集合。
        :type name: str
        :param version: 版本号,输入2-50个字符。值以字母或数字开头和结尾。仅允许使用字母，数字，中划线和点号。
        :type version: str
        :param description: 描述
        :type description: str
        """
        
        

        self._permission = None
        self._name = None
        self._version = None
        self._description = None
        self.discriminator = None

        self.permission = permission
        self.name = name
        self.version = version
        if description is not None:
            self.description = description

    @property
    def permission(self):
        r"""Gets the permission of this CreateProductTopicRequestBody.

        主题权限 0-发布 1-订阅

        :return: The permission of this CreateProductTopicRequestBody.
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this CreateProductTopicRequestBody.

        主题权限 0-发布 1-订阅

        :param permission: The permission of this CreateProductTopicRequestBody.
        :type permission: int
        """
        self._permission = permission

    @property
    def name(self):
        r"""Gets the name of this CreateProductTopicRequestBody.

        产品级主题名称<br>Topic类格式必须以“/”进行分层，区分每个类目。其中第一个为用户自定义的版本号；第二个已经规定好，为${deviceId}通配设备ID；第三个为用户自定义的topic类名（即本字段）。Topic类组成即为：/${version}/${deviceId}/${customizePart}。简单来说，Topic类：/v1/${deviceId}/customizePart是具体Topic：/v1/deviceid1/customizePart1和/v1/deviceid2/customizePart2等的集合。

        :return: The name of this CreateProductTopicRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateProductTopicRequestBody.

        产品级主题名称<br>Topic类格式必须以“/”进行分层，区分每个类目。其中第一个为用户自定义的版本号；第二个已经规定好，为${deviceId}通配设备ID；第三个为用户自定义的topic类名（即本字段）。Topic类组成即为：/${version}/${deviceId}/${customizePart}。简单来说，Topic类：/v1/${deviceId}/customizePart是具体Topic：/v1/deviceid1/customizePart1和/v1/deviceid2/customizePart2等的集合。

        :param name: The name of this CreateProductTopicRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this CreateProductTopicRequestBody.

        版本号,输入2-50个字符。值以字母或数字开头和结尾。仅允许使用字母，数字，中划线和点号。

        :return: The version of this CreateProductTopicRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateProductTopicRequestBody.

        版本号,输入2-50个字符。值以字母或数字开头和结尾。仅允许使用字母，数字，中划线和点号。

        :param version: The version of this CreateProductTopicRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this CreateProductTopicRequestBody.

        描述

        :return: The description of this CreateProductTopicRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProductTopicRequestBody.

        描述

        :param description: The description of this CreateProductTopicRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateProductTopicRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
