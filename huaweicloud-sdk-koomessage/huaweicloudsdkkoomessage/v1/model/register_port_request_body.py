# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterPortRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str',
        'port_type': 'int',
        'sign': 'list[str]',
        'sign_check': 'int',
        'authorization_files': 'list[str]'
    }

    attribute_map = {
        'port': 'port',
        'port_type': 'port_type',
        'sign': 'sign',
        'sign_check': 'sign_check',
        'authorization_files': 'authorization_files'
    }

    def __init__(self, port=None, port_type=None, sign=None, sign_check=None, authorization_files=None):
        r"""RegisterPortRequestBody

        The model defined in huaweicloud sdk

        :param port: 通道号。 - port_type&#x3D;5时 ，长度必须为5 - port_type&#x3D;1或3，长度在21位内 
        :type port: str
        :param port_type: 通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段 
        :type port_type: int
        :param sign: 签名列表，最大长度为5。单个签名长度为2-18。
        :type sign: list[str]
        :param sign_check: 是否需要校验。  - 0：不校验  - 1：校验签名  &gt; 当port_type为3或者5时，sign_check必须为1。 
        :type sign_check: int
        :param authorization_files: 授权证明图片资源，支持jpg、bmp、png和jpeg格式，全部图片总大小不超过4M，最多支持5张。参数格式为：*资源ID:资源URL*，样例：3d214a61672846f88ad77597f935cccc:AimSauploadService/272957b708ac4891a6d5282ccd2175cccc.png。 &gt; 资源ID与资源URL对应上传智能信息服务号图片资源API返回的resource_id和resource_url。
        :type authorization_files: list[str]
        """
        
        

        self._port = None
        self._port_type = None
        self._sign = None
        self._sign_check = None
        self._authorization_files = None
        self.discriminator = None

        self.port = port
        self.port_type = port_type
        self.sign = sign
        self.sign_check = sign_check
        self.authorization_files = authorization_files

    @property
    def port(self):
        r"""Gets the port of this RegisterPortRequestBody.

        通道号。 - port_type=5时 ，长度必须为5 - port_type=1或3，长度在21位内 

        :return: The port of this RegisterPortRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this RegisterPortRequestBody.

        通道号。 - port_type=5时 ，长度必须为5 - port_type=1或3，长度在21位内 

        :param port: The port of this RegisterPortRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def port_type(self):
        r"""Gets the port_type of this RegisterPortRequestBody.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段 

        :return: The port_type of this RegisterPortRequestBody.
        :rtype: int
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        r"""Sets the port_type of this RegisterPortRequestBody.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段 

        :param port_type: The port_type of this RegisterPortRequestBody.
        :type port_type: int
        """
        self._port_type = port_type

    @property
    def sign(self):
        r"""Gets the sign of this RegisterPortRequestBody.

        签名列表，最大长度为5。单个签名长度为2-18。

        :return: The sign of this RegisterPortRequestBody.
        :rtype: list[str]
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        r"""Sets the sign of this RegisterPortRequestBody.

        签名列表，最大长度为5。单个签名长度为2-18。

        :param sign: The sign of this RegisterPortRequestBody.
        :type sign: list[str]
        """
        self._sign = sign

    @property
    def sign_check(self):
        r"""Gets the sign_check of this RegisterPortRequestBody.

        是否需要校验。  - 0：不校验  - 1：校验签名  > 当port_type为3或者5时，sign_check必须为1。 

        :return: The sign_check of this RegisterPortRequestBody.
        :rtype: int
        """
        return self._sign_check

    @sign_check.setter
    def sign_check(self, sign_check):
        r"""Sets the sign_check of this RegisterPortRequestBody.

        是否需要校验。  - 0：不校验  - 1：校验签名  > 当port_type为3或者5时，sign_check必须为1。 

        :param sign_check: The sign_check of this RegisterPortRequestBody.
        :type sign_check: int
        """
        self._sign_check = sign_check

    @property
    def authorization_files(self):
        r"""Gets the authorization_files of this RegisterPortRequestBody.

        授权证明图片资源，支持jpg、bmp、png和jpeg格式，全部图片总大小不超过4M，最多支持5张。参数格式为：*资源ID:资源URL*，样例：3d214a61672846f88ad77597f935cccc:AimSauploadService/272957b708ac4891a6d5282ccd2175cccc.png。 > 资源ID与资源URL对应上传智能信息服务号图片资源API返回的resource_id和resource_url。

        :return: The authorization_files of this RegisterPortRequestBody.
        :rtype: list[str]
        """
        return self._authorization_files

    @authorization_files.setter
    def authorization_files(self, authorization_files):
        r"""Sets the authorization_files of this RegisterPortRequestBody.

        授权证明图片资源，支持jpg、bmp、png和jpeg格式，全部图片总大小不超过4M，最多支持5张。参数格式为：*资源ID:资源URL*，样例：3d214a61672846f88ad77597f935cccc:AimSauploadService/272957b708ac4891a6d5282ccd2175cccc.png。 > 资源ID与资源URL对应上传智能信息服务号图片资源API返回的resource_id和resource_url。

        :param authorization_files: The authorization_files of this RegisterPortRequestBody.
        :type authorization_files: list[str]
        """
        self._authorization_files = authorization_files

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
        if not isinstance(other, RegisterPortRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
