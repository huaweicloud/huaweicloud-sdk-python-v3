# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNaRequestDTO:

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
        'endpoint': 'str',
        'auth_type': 'str',
        'auth_aksk_info': 'AuthAkSkInfo',
        'access_type': 'str',
        'access_roma_info': 'AccessRomaInfo'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'endpoint': 'endpoint',
        'auth_type': 'auth_type',
        'auth_aksk_info': 'auth_aksk_info',
        'access_type': 'access_type',
        'access_roma_info': 'access_roma_info'
    }

    def __init__(self, name=None, description=None, endpoint=None, auth_type=None, auth_aksk_info=None, access_type=None, access_roma_info=None):
        """UpdateNaRequestDTO

        The model defined in huaweicloud sdk

        :param name: NA系统名称
        :type name: str
        :param description: 北向NA系统描述
        :type description: str
        :param endpoint: 访问URL地址
        :type endpoint: str
        :param auth_type: 鉴权方式
        :type auth_type: str
        :param auth_aksk_info: 
        :type auth_aksk_info: :class:`huaweicloudsdkiotedge.v2.AuthAkSkInfo`
        :param access_type: 接入类型
        :type access_type: str
        :param access_roma_info: 
        :type access_roma_info: :class:`huaweicloudsdkiotedge.v2.AccessRomaInfo`
        """
        
        

        self._name = None
        self._description = None
        self._endpoint = None
        self._auth_type = None
        self._auth_aksk_info = None
        self._access_type = None
        self._access_roma_info = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.endpoint = endpoint
        if auth_type is not None:
            self.auth_type = auth_type
        if auth_aksk_info is not None:
            self.auth_aksk_info = auth_aksk_info
        self.access_type = access_type
        if access_roma_info is not None:
            self.access_roma_info = access_roma_info

    @property
    def name(self):
        """Gets the name of this UpdateNaRequestDTO.

        NA系统名称

        :return: The name of this UpdateNaRequestDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNaRequestDTO.

        NA系统名称

        :param name: The name of this UpdateNaRequestDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateNaRequestDTO.

        北向NA系统描述

        :return: The description of this UpdateNaRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateNaRequestDTO.

        北向NA系统描述

        :param description: The description of this UpdateNaRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        """Gets the endpoint of this UpdateNaRequestDTO.

        访问URL地址

        :return: The endpoint of this UpdateNaRequestDTO.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this UpdateNaRequestDTO.

        访问URL地址

        :param endpoint: The endpoint of this UpdateNaRequestDTO.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def auth_type(self):
        """Gets the auth_type of this UpdateNaRequestDTO.

        鉴权方式

        :return: The auth_type of this UpdateNaRequestDTO.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this UpdateNaRequestDTO.

        鉴权方式

        :param auth_type: The auth_type of this UpdateNaRequestDTO.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_aksk_info(self):
        """Gets the auth_aksk_info of this UpdateNaRequestDTO.


        :return: The auth_aksk_info of this UpdateNaRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.AuthAkSkInfo`
        """
        return self._auth_aksk_info

    @auth_aksk_info.setter
    def auth_aksk_info(self, auth_aksk_info):
        """Sets the auth_aksk_info of this UpdateNaRequestDTO.


        :param auth_aksk_info: The auth_aksk_info of this UpdateNaRequestDTO.
        :type auth_aksk_info: :class:`huaweicloudsdkiotedge.v2.AuthAkSkInfo`
        """
        self._auth_aksk_info = auth_aksk_info

    @property
    def access_type(self):
        """Gets the access_type of this UpdateNaRequestDTO.

        接入类型

        :return: The access_type of this UpdateNaRequestDTO.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this UpdateNaRequestDTO.

        接入类型

        :param access_type: The access_type of this UpdateNaRequestDTO.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def access_roma_info(self):
        """Gets the access_roma_info of this UpdateNaRequestDTO.


        :return: The access_roma_info of this UpdateNaRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.AccessRomaInfo`
        """
        return self._access_roma_info

    @access_roma_info.setter
    def access_roma_info(self, access_roma_info):
        """Sets the access_roma_info of this UpdateNaRequestDTO.


        :param access_roma_info: The access_roma_info of this UpdateNaRequestDTO.
        :type access_roma_info: :class:`huaweicloudsdkiotedge.v2.AccessRomaInfo`
        """
        self._access_roma_info = access_roma_info

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
        if not isinstance(other, UpdateNaRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
