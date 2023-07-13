# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefreshTaskRequestBody:

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
        'mode': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'mode': 'mode',
        'urls': 'urls'
    }

    def __init__(self, type=None, mode=None, urls=None):
        """RefreshTaskRequestBody

        The model defined in huaweicloud sdk

        :param type: 刷新的类型，其值可以为file 或directory，默认为file
        :type type: str
        :param mode: 目录刷新方式，all：刷新目录下全部资源；detect_modify_refresh：刷新目录下已变更的资源，默认值为all。
        :type mode: str
        :param urls: 输入URL必须带有“http://”或“https://”，多个URL用逗号分隔，单个url的长度限制为4096字符，单次最多输入1000个url。 &gt;   如果您需要刷新的URL中有中文，请同时刷新中文URL和转码后的URL。
        :type urls: list[str]
        """
        
        

        self._type = None
        self._mode = None
        self._urls = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode
        self.urls = urls

    @property
    def type(self):
        """Gets the type of this RefreshTaskRequestBody.

        刷新的类型，其值可以为file 或directory，默认为file

        :return: The type of this RefreshTaskRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefreshTaskRequestBody.

        刷新的类型，其值可以为file 或directory，默认为file

        :param type: The type of this RefreshTaskRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def mode(self):
        """Gets the mode of this RefreshTaskRequestBody.

        目录刷新方式，all：刷新目录下全部资源；detect_modify_refresh：刷新目录下已变更的资源，默认值为all。

        :return: The mode of this RefreshTaskRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RefreshTaskRequestBody.

        目录刷新方式，all：刷新目录下全部资源；detect_modify_refresh：刷新目录下已变更的资源，默认值为all。

        :param mode: The mode of this RefreshTaskRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def urls(self):
        """Gets the urls of this RefreshTaskRequestBody.

        输入URL必须带有“http://”或“https://”，多个URL用逗号分隔，单个url的长度限制为4096字符，单次最多输入1000个url。 >   如果您需要刷新的URL中有中文，请同时刷新中文URL和转码后的URL。

        :return: The urls of this RefreshTaskRequestBody.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this RefreshTaskRequestBody.

        输入URL必须带有“http://”或“https://”，多个URL用逗号分隔，单个url的长度限制为4096字符，单次最多输入1000个url。 >   如果您需要刷新的URL中有中文，请同时刷新中文URL和转码后的URL。

        :param urls: The urls of this RefreshTaskRequestBody.
        :type urls: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, RefreshTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
