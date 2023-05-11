# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateRomaAppResponse(SdkResponse):

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
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark'
    }

    def __init__(self, id=None, name=None, remark=None):
        """ValidateRomaAppResponse

        The model defined in huaweicloud sdk

        :param id: 应用ID
        :type id: str
        :param name: 应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一
        :type name: str
        :param remark: 应用描述
        :type remark: str
        """
        
        super(ValidateRomaAppResponse, self).__init__()

        self._id = None
        self._name = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this ValidateRomaAppResponse.

        应用ID

        :return: The id of this ValidateRomaAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ValidateRomaAppResponse.

        应用ID

        :param id: The id of this ValidateRomaAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ValidateRomaAppResponse.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :return: The name of this ValidateRomaAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateRomaAppResponse.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :param name: The name of this ValidateRomaAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this ValidateRomaAppResponse.

        应用描述

        :return: The remark of this ValidateRomaAppResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ValidateRomaAppResponse.

        应用描述

        :param remark: The remark of this ValidateRomaAppResponse.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, ValidateRomaAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
