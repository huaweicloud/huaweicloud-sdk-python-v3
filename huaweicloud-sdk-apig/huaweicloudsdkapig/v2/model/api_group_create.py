# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiGroupCreate:

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
        'remark': 'str',
        'roma_app_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark',
        'roma_app_id': 'roma_app_id',
        'version': 'version'
    }

    def __init__(self, name=None, remark=None, roma_app_id=None, version=None):
        """ApiGroupCreate

        The model defined in huaweicloud sdk

        :param name: API分组的名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param remark: API分组描述。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param roma_app_id: 分组归属的集成应用编号。  分组版本V2时必填。  暂不支持
        :type roma_app_id: str
        :param version: 分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认V1
        :type version: str
        """
        
        

        self._name = None
        self._remark = None
        self._roma_app_id = None
        self._version = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this ApiGroupCreate.

        API分组的名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ApiGroupCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiGroupCreate.

        API分组的名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ApiGroupCreate.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this ApiGroupCreate.

        API分组描述。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiGroupCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiGroupCreate.

        API分组描述。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiGroupCreate.
        :type remark: str
        """
        self._remark = remark

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ApiGroupCreate.

        分组归属的集成应用编号。  分组版本V2时必填。  暂不支持

        :return: The roma_app_id of this ApiGroupCreate.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ApiGroupCreate.

        分组归属的集成应用编号。  分组版本V2时必填。  暂不支持

        :param roma_app_id: The roma_app_id of this ApiGroupCreate.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def version(self):
        """Gets the version of this ApiGroupCreate.

        分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认V1

        :return: The version of this ApiGroupCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiGroupCreate.

        分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认V1

        :param version: The version of this ApiGroupCreate.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ApiGroupCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
