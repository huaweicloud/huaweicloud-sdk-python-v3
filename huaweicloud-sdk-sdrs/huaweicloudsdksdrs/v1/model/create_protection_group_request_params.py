# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProtectionGroupRequestParams:

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
        'source_availability_zone': 'str',
        'target_availability_zone': 'str',
        'domain_id': 'str',
        'source_vpc_id': 'str',
        'dr_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source_availability_zone': 'source_availability_zone',
        'target_availability_zone': 'target_availability_zone',
        'domain_id': 'domain_id',
        'source_vpc_id': 'source_vpc_id',
        'dr_type': 'dr_type'
    }

    def __init__(self, name=None, description=None, source_availability_zone=None, target_availability_zone=None, domain_id=None, source_vpc_id=None, dr_type=None):
        r"""CreateProtectionGroupRequestParams

        The model defined in huaweicloud sdk

        :param name: 指定保护组的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。
        :type name: str
        :param description: 指定保护组的描述，最大支持长度为64个字节。不能包含左尖括号（&lt;）或右尖括号（&gt;）。
        :type description: str
        :param source_availability_zone: 指定保护组的生产站点可用区名称。
        :type source_availability_zone: str
        :param target_availability_zone: 指定保护组的容灾站点可用区名称。
        :type target_availability_zone: str
        :param domain_id: 指定双活域的ID。
        :type domain_id: str
        :param source_vpc_id: 生产站点虚拟私有云ID。
        :type source_vpc_id: str
        :param dr_type: 部署模式。默认值为“migration”，migration表示VPC内迁移。
        :type dr_type: str
        """
        
        

        self._name = None
        self._description = None
        self._source_availability_zone = None
        self._target_availability_zone = None
        self._domain_id = None
        self._source_vpc_id = None
        self._dr_type = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.source_availability_zone = source_availability_zone
        self.target_availability_zone = target_availability_zone
        self.domain_id = domain_id
        self.source_vpc_id = source_vpc_id
        if dr_type is not None:
            self.dr_type = dr_type

    @property
    def name(self):
        r"""Gets the name of this CreateProtectionGroupRequestParams.

        指定保护组的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :return: The name of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateProtectionGroupRequestParams.

        指定保护组的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :param name: The name of this CreateProtectionGroupRequestParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateProtectionGroupRequestParams.

        指定保护组的描述，最大支持长度为64个字节。不能包含左尖括号（<）或右尖括号（>）。

        :return: The description of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProtectionGroupRequestParams.

        指定保护组的描述，最大支持长度为64个字节。不能包含左尖括号（<）或右尖括号（>）。

        :param description: The description of this CreateProtectionGroupRequestParams.
        :type description: str
        """
        self._description = description

    @property
    def source_availability_zone(self):
        r"""Gets the source_availability_zone of this CreateProtectionGroupRequestParams.

        指定保护组的生产站点可用区名称。

        :return: The source_availability_zone of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._source_availability_zone

    @source_availability_zone.setter
    def source_availability_zone(self, source_availability_zone):
        r"""Sets the source_availability_zone of this CreateProtectionGroupRequestParams.

        指定保护组的生产站点可用区名称。

        :param source_availability_zone: The source_availability_zone of this CreateProtectionGroupRequestParams.
        :type source_availability_zone: str
        """
        self._source_availability_zone = source_availability_zone

    @property
    def target_availability_zone(self):
        r"""Gets the target_availability_zone of this CreateProtectionGroupRequestParams.

        指定保护组的容灾站点可用区名称。

        :return: The target_availability_zone of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._target_availability_zone

    @target_availability_zone.setter
    def target_availability_zone(self, target_availability_zone):
        r"""Sets the target_availability_zone of this CreateProtectionGroupRequestParams.

        指定保护组的容灾站点可用区名称。

        :param target_availability_zone: The target_availability_zone of this CreateProtectionGroupRequestParams.
        :type target_availability_zone: str
        """
        self._target_availability_zone = target_availability_zone

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateProtectionGroupRequestParams.

        指定双活域的ID。

        :return: The domain_id of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateProtectionGroupRequestParams.

        指定双活域的ID。

        :param domain_id: The domain_id of this CreateProtectionGroupRequestParams.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def source_vpc_id(self):
        r"""Gets the source_vpc_id of this CreateProtectionGroupRequestParams.

        生产站点虚拟私有云ID。

        :return: The source_vpc_id of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._source_vpc_id

    @source_vpc_id.setter
    def source_vpc_id(self, source_vpc_id):
        r"""Sets the source_vpc_id of this CreateProtectionGroupRequestParams.

        生产站点虚拟私有云ID。

        :param source_vpc_id: The source_vpc_id of this CreateProtectionGroupRequestParams.
        :type source_vpc_id: str
        """
        self._source_vpc_id = source_vpc_id

    @property
    def dr_type(self):
        r"""Gets the dr_type of this CreateProtectionGroupRequestParams.

        部署模式。默认值为“migration”，migration表示VPC内迁移。

        :return: The dr_type of this CreateProtectionGroupRequestParams.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        r"""Sets the dr_type of this CreateProtectionGroupRequestParams.

        部署模式。默认值为“migration”，migration表示VPC内迁移。

        :param dr_type: The dr_type of this CreateProtectionGroupRequestParams.
        :type dr_type: str
        """
        self._dr_type = dr_type

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
        if not isinstance(other, CreateProtectionGroupRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
