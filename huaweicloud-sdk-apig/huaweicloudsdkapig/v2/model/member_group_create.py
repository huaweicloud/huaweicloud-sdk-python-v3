# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberGroupCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_group_name': 'str',
        'member_group_remark': 'str',
        'member_group_weight': 'int',
        'dict_code': 'str',
        'microservice_version': 'str',
        'microservice_port': 'int',
        'microservice_labels': 'list[MicroserviceLabel]'
    }

    attribute_map = {
        'member_group_name': 'member_group_name',
        'member_group_remark': 'member_group_remark',
        'member_group_weight': 'member_group_weight',
        'dict_code': 'dict_code',
        'microservice_version': 'microservice_version',
        'microservice_port': 'microservice_port',
        'microservice_labels': 'microservice_labels'
    }

    def __init__(self, member_group_name=None, member_group_remark=None, member_group_weight=None, dict_code=None, microservice_version=None, microservice_port=None, microservice_labels=None):
        """MemberGroupCreate

        The model defined in huaweicloud sdk

        :param member_group_name: VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type member_group_name: str
        :param member_group_remark: VPC通道后端服务器组描述。
        :type member_group_remark: str
        :param member_group_weight: VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。
        :type member_group_weight: int
        :param dict_code: VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
        :param microservice_version: VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。
        :type microservice_version: str
        :param microservice_port: VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。
        :type microservice_port: int
        :param microservice_labels: VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。
        :type microservice_labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        
        

        self._member_group_name = None
        self._member_group_remark = None
        self._member_group_weight = None
        self._dict_code = None
        self._microservice_version = None
        self._microservice_port = None
        self._microservice_labels = None
        self.discriminator = None

        self.member_group_name = member_group_name
        if member_group_remark is not None:
            self.member_group_remark = member_group_remark
        if member_group_weight is not None:
            self.member_group_weight = member_group_weight
        if dict_code is not None:
            self.dict_code = dict_code
        if microservice_version is not None:
            self.microservice_version = microservice_version
        if microservice_port is not None:
            self.microservice_port = microservice_port
        if microservice_labels is not None:
            self.microservice_labels = microservice_labels

    @property
    def member_group_name(self):
        """Gets the member_group_name of this MemberGroupCreate.

        VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The member_group_name of this MemberGroupCreate.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        """Sets the member_group_name of this MemberGroupCreate.

        VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param member_group_name: The member_group_name of this MemberGroupCreate.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def member_group_remark(self):
        """Gets the member_group_remark of this MemberGroupCreate.

        VPC通道后端服务器组描述。

        :return: The member_group_remark of this MemberGroupCreate.
        :rtype: str
        """
        return self._member_group_remark

    @member_group_remark.setter
    def member_group_remark(self, member_group_remark):
        """Sets the member_group_remark of this MemberGroupCreate.

        VPC通道后端服务器组描述。

        :param member_group_remark: The member_group_remark of this MemberGroupCreate.
        :type member_group_remark: str
        """
        self._member_group_remark = member_group_remark

    @property
    def member_group_weight(self):
        """Gets the member_group_weight of this MemberGroupCreate.

        VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。

        :return: The member_group_weight of this MemberGroupCreate.
        :rtype: int
        """
        return self._member_group_weight

    @member_group_weight.setter
    def member_group_weight(self, member_group_weight):
        """Sets the member_group_weight of this MemberGroupCreate.

        VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。

        :param member_group_weight: The member_group_weight of this MemberGroupCreate.
        :type member_group_weight: int
        """
        self._member_group_weight = member_group_weight

    @property
    def dict_code(self):
        """Gets the dict_code of this MemberGroupCreate.

        VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this MemberGroupCreate.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        """Sets the dict_code of this MemberGroupCreate.

        VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this MemberGroupCreate.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def microservice_version(self):
        """Gets the microservice_version of this MemberGroupCreate.

        VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。

        :return: The microservice_version of this MemberGroupCreate.
        :rtype: str
        """
        return self._microservice_version

    @microservice_version.setter
    def microservice_version(self, microservice_version):
        """Sets the microservice_version of this MemberGroupCreate.

        VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。

        :param microservice_version: The microservice_version of this MemberGroupCreate.
        :type microservice_version: str
        """
        self._microservice_version = microservice_version

    @property
    def microservice_port(self):
        """Gets the microservice_port of this MemberGroupCreate.

        VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。

        :return: The microservice_port of this MemberGroupCreate.
        :rtype: int
        """
        return self._microservice_port

    @microservice_port.setter
    def microservice_port(self, microservice_port):
        """Sets the microservice_port of this MemberGroupCreate.

        VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。

        :param microservice_port: The microservice_port of this MemberGroupCreate.
        :type microservice_port: int
        """
        self._microservice_port = microservice_port

    @property
    def microservice_labels(self):
        """Gets the microservice_labels of this MemberGroupCreate.

        VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。

        :return: The microservice_labels of this MemberGroupCreate.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        return self._microservice_labels

    @microservice_labels.setter
    def microservice_labels(self, microservice_labels):
        """Sets the microservice_labels of this MemberGroupCreate.

        VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。

        :param microservice_labels: The microservice_labels of this MemberGroupCreate.
        :type microservice_labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        self._microservice_labels = microservice_labels

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
        if not isinstance(other, MemberGroupCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
