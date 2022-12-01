# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodeResponse(SdkResponse):

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
        'name': 'str',
        'package': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'package': 'package'
    }

    def __init__(self, id=None, name=None, package=None):
        """CreateNodeResponse

        The model defined in huaweicloud sdk

        :param id: 设备ID
        :type id: str
        :param name: 设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param package: 将设备配置和证书文件node.conf/certificate/private_key打成.tar.gz包后用base64编码的字符串。node.conf包含节点信息配置
        :type package: str
        """
        
        super(CreateNodeResponse, self).__init__()

        self._id = None
        self._name = None
        self._package = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if package is not None:
            self.package = package

    @property
    def id(self):
        """Gets the id of this CreateNodeResponse.

        设备ID

        :return: The id of this CreateNodeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateNodeResponse.

        设备ID

        :param id: The id of this CreateNodeResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateNodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this CreateNodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this CreateNodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def package(self):
        """Gets the package of this CreateNodeResponse.

        将设备配置和证书文件node.conf/certificate/private_key打成.tar.gz包后用base64编码的字符串。node.conf包含节点信息配置

        :return: The package of this CreateNodeResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this CreateNodeResponse.

        将设备配置和证书文件node.conf/certificate/private_key打成.tar.gz包后用base64编码的字符串。node.conf包含节点信息配置

        :param package: The package of this CreateNodeResponse.
        :type package: str
        """
        self._package = package

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
        if not isinstance(other, CreateNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
