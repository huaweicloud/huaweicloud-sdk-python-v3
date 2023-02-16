# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizAppParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'display_name': 'str',
        'eps_id': 'str',
        'name': 'str',
        'register_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'eps_id': 'eps_id',
        'name': 'name',
        'register_type': 'register_type'
    }

    def __init__(self, description=None, display_name=None, eps_id=None, name=None, register_type=None):
        """BizAppParam

        The model defined in huaweicloud sdk

        :param description: 应用描述
        :type description: str
        :param display_name: 应用名称.字符集长度2-64，仅支持字符集：中文字符、英文字母、数字、下划线、中划线、点
        :type display_name: str
        :param eps_id: 应用关联的企业项目id。企业级用户必传
        :type eps_id: str
        :param name: 唯一标识.字符集长度2-64，仅支持字符集：英文字母、数字、下划线、中划线、点
        :type name: str
        :param register_type: 前端默认是CONSOLE，不需要传参。rest接口无参数是API，有参数只能是：SERVICE_DISCOVERY
        :type register_type: str
        """
        
        

        self._description = None
        self._display_name = None
        self._eps_id = None
        self._name = None
        self._register_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if eps_id is not None:
            self.eps_id = eps_id
        self.name = name
        if register_type is not None:
            self.register_type = register_type

    @property
    def description(self):
        """Gets the description of this BizAppParam.

        应用描述

        :return: The description of this BizAppParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BizAppParam.

        应用描述

        :param description: The description of this BizAppParam.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this BizAppParam.

        应用名称.字符集长度2-64，仅支持字符集：中文字符、英文字母、数字、下划线、中划线、点

        :return: The display_name of this BizAppParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BizAppParam.

        应用名称.字符集长度2-64，仅支持字符集：中文字符、英文字母、数字、下划线、中划线、点

        :param display_name: The display_name of this BizAppParam.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def eps_id(self):
        """Gets the eps_id of this BizAppParam.

        应用关联的企业项目id。企业级用户必传

        :return: The eps_id of this BizAppParam.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this BizAppParam.

        应用关联的企业项目id。企业级用户必传

        :param eps_id: The eps_id of this BizAppParam.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def name(self):
        """Gets the name of this BizAppParam.

        唯一标识.字符集长度2-64，仅支持字符集：英文字母、数字、下划线、中划线、点

        :return: The name of this BizAppParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BizAppParam.

        唯一标识.字符集长度2-64，仅支持字符集：英文字母、数字、下划线、中划线、点

        :param name: The name of this BizAppParam.
        :type name: str
        """
        self._name = name

    @property
    def register_type(self):
        """Gets the register_type of this BizAppParam.

        前端默认是CONSOLE，不需要传参。rest接口无参数是API，有参数只能是：SERVICE_DISCOVERY

        :return: The register_type of this BizAppParam.
        :rtype: str
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        """Sets the register_type of this BizAppParam.

        前端默认是CONSOLE，不需要传参。rest接口无参数是API，有参数只能是：SERVICE_DISCOVERY

        :param register_type: The register_type of this BizAppParam.
        :type register_type: str
        """
        self._register_type = register_type

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
        if not isinstance(other, BizAppParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
