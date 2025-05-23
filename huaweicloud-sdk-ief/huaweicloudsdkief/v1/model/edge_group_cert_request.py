# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeGroupCertRequest:

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
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, description=None):
        r"""EdgeGroupCertRequest

        The model defined in huaweicloud sdk

        :param name: 证书名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param type: 证书类型，支持填写： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书
        :type type: str
        :param description: 证书描述。最大长度为255个字符
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this EdgeGroupCertRequest.

        证书名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this EdgeGroupCertRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EdgeGroupCertRequest.

        证书名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this EdgeGroupCertRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this EdgeGroupCertRequest.

        证书类型，支持填写： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :return: The type of this EdgeGroupCertRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EdgeGroupCertRequest.

        证书类型，支持填写： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :param type: The type of this EdgeGroupCertRequest.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this EdgeGroupCertRequest.

        证书描述。最大长度为255个字符

        :return: The description of this EdgeGroupCertRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgeGroupCertRequest.

        证书描述。最大长度为255个字符

        :param description: The description of this EdgeGroupCertRequest.
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
        if not isinstance(other, EdgeGroupCertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
