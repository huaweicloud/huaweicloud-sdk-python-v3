# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiCheckInfo:

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
        'ld_api_name': 'str',
        'ld_api_method': 'str',
        'ld_api_path': 'str',
        'roma_app_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'ld_api_name': 'ld_api_name',
        'ld_api_method': 'ld_api_method',
        'ld_api_path': 'ld_api_path',
        'roma_app_id': 'roma_app_id'
    }

    def __init__(self, type=None, ld_api_name=None, ld_api_method=None, ld_api_path=None, roma_app_id=None):
        r"""LdApiCheckInfo

        The model defined in huaweicloud sdk

        :param type: 校验类型：   - path：路径类型   - name：名称类型
        :type type: str
        :param ld_api_name: 自定义后端API名称。  type &#x3D; name时必填
        :type ld_api_name: str
        :param ld_api_method: 自定义后端API请求方式。  type &#x3D; path时必填
        :type ld_api_method: str
        :param ld_api_path: 自定义后端API的访问地址。  type &#x3D; path时必填
        :type ld_api_path: str
        :param roma_app_id: 集成应用ID。  校验应用下后端API定义是否重复时必填
        :type roma_app_id: str
        """
        
        

        self._type = None
        self._ld_api_name = None
        self._ld_api_method = None
        self._ld_api_path = None
        self._roma_app_id = None
        self.discriminator = None

        self.type = type
        if ld_api_name is not None:
            self.ld_api_name = ld_api_name
        if ld_api_method is not None:
            self.ld_api_method = ld_api_method
        if ld_api_path is not None:
            self.ld_api_path = ld_api_path
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id

    @property
    def type(self):
        r"""Gets the type of this LdApiCheckInfo.

        校验类型：   - path：路径类型   - name：名称类型

        :return: The type of this LdApiCheckInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LdApiCheckInfo.

        校验类型：   - path：路径类型   - name：名称类型

        :param type: The type of this LdApiCheckInfo.
        :type type: str
        """
        self._type = type

    @property
    def ld_api_name(self):
        r"""Gets the ld_api_name of this LdApiCheckInfo.

        自定义后端API名称。  type = name时必填

        :return: The ld_api_name of this LdApiCheckInfo.
        :rtype: str
        """
        return self._ld_api_name

    @ld_api_name.setter
    def ld_api_name(self, ld_api_name):
        r"""Sets the ld_api_name of this LdApiCheckInfo.

        自定义后端API名称。  type = name时必填

        :param ld_api_name: The ld_api_name of this LdApiCheckInfo.
        :type ld_api_name: str
        """
        self._ld_api_name = ld_api_name

    @property
    def ld_api_method(self):
        r"""Gets the ld_api_method of this LdApiCheckInfo.

        自定义后端API请求方式。  type = path时必填

        :return: The ld_api_method of this LdApiCheckInfo.
        :rtype: str
        """
        return self._ld_api_method

    @ld_api_method.setter
    def ld_api_method(self, ld_api_method):
        r"""Sets the ld_api_method of this LdApiCheckInfo.

        自定义后端API请求方式。  type = path时必填

        :param ld_api_method: The ld_api_method of this LdApiCheckInfo.
        :type ld_api_method: str
        """
        self._ld_api_method = ld_api_method

    @property
    def ld_api_path(self):
        r"""Gets the ld_api_path of this LdApiCheckInfo.

        自定义后端API的访问地址。  type = path时必填

        :return: The ld_api_path of this LdApiCheckInfo.
        :rtype: str
        """
        return self._ld_api_path

    @ld_api_path.setter
    def ld_api_path(self, ld_api_path):
        r"""Sets the ld_api_path of this LdApiCheckInfo.

        自定义后端API的访问地址。  type = path时必填

        :param ld_api_path: The ld_api_path of this LdApiCheckInfo.
        :type ld_api_path: str
        """
        self._ld_api_path = ld_api_path

    @property
    def roma_app_id(self):
        r"""Gets the roma_app_id of this LdApiCheckInfo.

        集成应用ID。  校验应用下后端API定义是否重复时必填

        :return: The roma_app_id of this LdApiCheckInfo.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        r"""Sets the roma_app_id of this LdApiCheckInfo.

        集成应用ID。  校验应用下后端API定义是否重复时必填

        :param roma_app_id: The roma_app_id of this LdApiCheckInfo.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

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
        if not isinstance(other, LdApiCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
