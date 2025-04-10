# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretDetailResp:

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
        'description': 'str',
        'secrets': 'dict(str, str)',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'secrets': 'secrets',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, description=None, secrets=None, project_id=None, created_at=None, updated_at=None, type=None):
        r"""SecretDetailResp

        The model defined in huaweicloud sdk

        :param id: 密钥ID
        :type id: str
        :param name: 密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾
        :type name: str
        :param description: 密钥描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param secrets: secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\&quot;a\&quot;: \&quot;b\&quot;}转为标准字符串后为&#39;{\&quot;a\&quot;: \&quot;b\&quot;}&#39;，长度为10
        :type secrets: dict(str, str)
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param type: 密钥类型，目前只支持“Opaque”类型
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._secrets = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.secrets = secrets
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this SecretDetailResp.

        密钥ID

        :return: The id of this SecretDetailResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SecretDetailResp.

        密钥ID

        :param id: The id of this SecretDetailResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SecretDetailResp.

        密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾

        :return: The name of this SecretDetailResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SecretDetailResp.

        密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾

        :param name: The name of this SecretDetailResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SecretDetailResp.

        密钥描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this SecretDetailResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SecretDetailResp.

        密钥描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this SecretDetailResp.
        :type description: str
        """
        self._description = description

    @property
    def secrets(self):
        r"""Gets the secrets of this SecretDetailResp.

        secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :return: The secrets of this SecretDetailResp.
        :rtype: dict(str, str)
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        r"""Sets the secrets of this SecretDetailResp.

        secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :param secrets: The secrets of this SecretDetailResp.
        :type secrets: dict(str, str)
        """
        self._secrets = secrets

    @property
    def project_id(self):
        r"""Gets the project_id of this SecretDetailResp.

        项目ID

        :return: The project_id of this SecretDetailResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SecretDetailResp.

        项目ID

        :param project_id: The project_id of this SecretDetailResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this SecretDetailResp.

        创建时间

        :return: The created_at of this SecretDetailResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SecretDetailResp.

        创建时间

        :param created_at: The created_at of this SecretDetailResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SecretDetailResp.

        更新时间

        :return: The updated_at of this SecretDetailResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SecretDetailResp.

        更新时间

        :param updated_at: The updated_at of this SecretDetailResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def type(self):
        r"""Gets the type of this SecretDetailResp.

        密钥类型，目前只支持“Opaque”类型

        :return: The type of this SecretDetailResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SecretDetailResp.

        密钥类型，目前只支持“Opaque”类型

        :param type: The type of this SecretDetailResp.
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
        if not isinstance(other, SecretDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
