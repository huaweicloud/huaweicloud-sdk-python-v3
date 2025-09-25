# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageAppsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_type': 'str',
        'app_version': 'str',
        'vul_num': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_type': 'app_type',
        'app_version': 'app_version',
        'vul_num': 'vul_num'
    }

    def __init__(self, app_name=None, app_type=None, app_version=None, vul_num=None):
        r"""ImageAppsInfo

        The model defined in huaweicloud sdk

        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度0-64位 
        :type app_name: str
        :param app_type: **参数解释**: 软件类型 **取值范围**: 字符长度0-64位 
        :type app_type: str
        :param app_version: **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 
        :type app_version: str
        :param vul_num: **参数解释**: 软件漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        """
        
        

        self._app_name = None
        self._app_type = None
        self._app_version = None
        self._vul_num = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_type is not None:
            self.app_type = app_type
        if app_version is not None:
            self.app_version = app_version
        if vul_num is not None:
            self.vul_num = vul_num

    @property
    def app_name(self):
        r"""Gets the app_name of this ImageAppsInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-64位 

        :return: The app_name of this ImageAppsInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ImageAppsInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-64位 

        :param app_name: The app_name of this ImageAppsInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_type(self):
        r"""Gets the app_type of this ImageAppsInfo.

        **参数解释**: 软件类型 **取值范围**: 字符长度0-64位 

        :return: The app_type of this ImageAppsInfo.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ImageAppsInfo.

        **参数解释**: 软件类型 **取值范围**: 字符长度0-64位 

        :param app_type: The app_type of this ImageAppsInfo.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_version(self):
        r"""Gets the app_version of this ImageAppsInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :return: The app_version of this ImageAppsInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ImageAppsInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :param app_version: The app_version of this ImageAppsInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ImageAppsInfo.

        **参数解释**: 软件漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this ImageAppsInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ImageAppsInfo.

        **参数解释**: 软件漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this ImageAppsInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

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
        if not isinstance(other, ImageAppsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
