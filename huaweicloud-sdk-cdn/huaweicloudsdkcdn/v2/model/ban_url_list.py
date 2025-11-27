# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BanUrlList:

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
        'url': 'str',
        'create_time': 'int',
        'modify_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url',
        'create_time': 'create_time',
        'modify_time': 'modify_time'
    }

    def __init__(self, type=None, url=None, create_time=None, modify_time=None):
        r"""BanUrlList

        The model defined in huaweicloud sdk

        :param type: 封禁类型。
        :type type: str
        :param url: url信息。
        :type url: str
        :param create_time: 创建时间戳（毫秒）。
        :type create_time: int
        :param modify_time: 更新时间戳（毫秒）。
        :type modify_time: int
        """
        
        

        self._type = None
        self._url = None
        self._create_time = None
        self._modify_time = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time

    @property
    def type(self):
        r"""Gets the type of this BanUrlList.

        封禁类型。

        :return: The type of this BanUrlList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BanUrlList.

        封禁类型。

        :param type: The type of this BanUrlList.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this BanUrlList.

        url信息。

        :return: The url of this BanUrlList.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this BanUrlList.

        url信息。

        :param url: The url of this BanUrlList.
        :type url: str
        """
        self._url = url

    @property
    def create_time(self):
        r"""Gets the create_time of this BanUrlList.

        创建时间戳（毫秒）。

        :return: The create_time of this BanUrlList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BanUrlList.

        创建时间戳（毫秒）。

        :param create_time: The create_time of this BanUrlList.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this BanUrlList.

        更新时间戳（毫秒）。

        :return: The modify_time of this BanUrlList.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this BanUrlList.

        更新时间戳（毫秒）。

        :param modify_time: The modify_time of this BanUrlList.
        :type modify_time: int
        """
        self._modify_time = modify_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BanUrlList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
