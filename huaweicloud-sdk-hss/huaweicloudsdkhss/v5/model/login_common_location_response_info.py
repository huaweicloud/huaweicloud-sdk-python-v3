# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginCommonLocationResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'area_code': 'int',
        'total_num': 'int',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'area_code': 'area_code',
        'total_num': 'total_num',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, area_code=None, total_num=None, host_id_list=None):
        r"""LoginCommonLocationResponseInfo

        The model defined in huaweicloud sdk

        :param area_code: 国家城市的编码
        :type area_code: int
        :param total_num: 这个常用登陆地的主机个数
        :type total_num: int
        :param host_id_list: 服务器列表
        :type host_id_list: list[str]
        """
        
        

        self._area_code = None
        self._total_num = None
        self._host_id_list = None
        self.discriminator = None

        if area_code is not None:
            self.area_code = area_code
        if total_num is not None:
            self.total_num = total_num
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def area_code(self):
        r"""Gets the area_code of this LoginCommonLocationResponseInfo.

        国家城市的编码

        :return: The area_code of this LoginCommonLocationResponseInfo.
        :rtype: int
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        r"""Sets the area_code of this LoginCommonLocationResponseInfo.

        国家城市的编码

        :param area_code: The area_code of this LoginCommonLocationResponseInfo.
        :type area_code: int
        """
        self._area_code = area_code

    @property
    def total_num(self):
        r"""Gets the total_num of this LoginCommonLocationResponseInfo.

        这个常用登陆地的主机个数

        :return: The total_num of this LoginCommonLocationResponseInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this LoginCommonLocationResponseInfo.

        这个常用登陆地的主机个数

        :param total_num: The total_num of this LoginCommonLocationResponseInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this LoginCommonLocationResponseInfo.

        服务器列表

        :return: The host_id_list of this LoginCommonLocationResponseInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this LoginCommonLocationResponseInfo.

        服务器列表

        :param host_id_list: The host_id_list of this LoginCommonLocationResponseInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, LoginCommonLocationResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
