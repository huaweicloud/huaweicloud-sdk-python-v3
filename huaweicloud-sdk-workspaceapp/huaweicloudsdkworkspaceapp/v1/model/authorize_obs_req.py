# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeObsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_file_name': 'str'
    }

    attribute_map = {
        'app_file_name': 'app_file_name'
    }

    def __init__(self, app_file_name=None):
        """AuthorizeObsReq

        The model defined in huaweicloud sdk

        :param app_file_name: 应用名称,名称需满足如下规则: 1. 文件名前缀由可见字符和空格组成，且不能为全空格。 2. 长度范围1~255个字符。 3. 结尾必须是&#x60;.msi&#x60;或者&#x60;.exe&#x60;或者&#x60;.zip&#x60;或者&#x60;.rar&#x60;。
        :type app_file_name: str
        """
        
        

        self._app_file_name = None
        self.discriminator = None

        self.app_file_name = app_file_name

    @property
    def app_file_name(self):
        """Gets the app_file_name of this AuthorizeObsReq.

        应用名称,名称需满足如下规则: 1. 文件名前缀由可见字符和空格组成，且不能为全空格。 2. 长度范围1~255个字符。 3. 结尾必须是`.msi`或者`.exe`或者`.zip`或者`.rar`。

        :return: The app_file_name of this AuthorizeObsReq.
        :rtype: str
        """
        return self._app_file_name

    @app_file_name.setter
    def app_file_name(self, app_file_name):
        """Sets the app_file_name of this AuthorizeObsReq.

        应用名称,名称需满足如下规则: 1. 文件名前缀由可见字符和空格组成，且不能为全空格。 2. 长度范围1~255个字符。 3. 结尾必须是`.msi`或者`.exe`或者`.zip`或者`.rar`。

        :param app_file_name: The app_file_name of this AuthorizeObsReq.
        :type app_file_name: str
        """
        self._app_file_name = app_file_name

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
        if not isinstance(other, AuthorizeObsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
