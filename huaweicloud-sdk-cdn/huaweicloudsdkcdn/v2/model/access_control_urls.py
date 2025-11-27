# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessControlUrls:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urls': 'list[str]',
        'ban_duration': 'int'
    }

    attribute_map = {
        'urls': 'urls',
        'ban_duration': 'ban_duration'
    }

    def __init__(self, urls=None, ban_duration=None):
        r"""AccessControlUrls

        The model defined in huaweicloud sdk

        :param urls: URL必须带有“http://”或“https://”，单次最多输入1000个url。
        :type urls: list[str]
        :param ban_duration: URL封禁天数，默认7天，取值范围1-30。
        :type ban_duration: int
        """
        
        

        self._urls = None
        self._ban_duration = None
        self.discriminator = None

        self.urls = urls
        if ban_duration is not None:
            self.ban_duration = ban_duration

    @property
    def urls(self):
        r"""Gets the urls of this AccessControlUrls.

        URL必须带有“http://”或“https://”，单次最多输入1000个url。

        :return: The urls of this AccessControlUrls.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this AccessControlUrls.

        URL必须带有“http://”或“https://”，单次最多输入1000个url。

        :param urls: The urls of this AccessControlUrls.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def ban_duration(self):
        r"""Gets the ban_duration of this AccessControlUrls.

        URL封禁天数，默认7天，取值范围1-30。

        :return: The ban_duration of this AccessControlUrls.
        :rtype: int
        """
        return self._ban_duration

    @ban_duration.setter
    def ban_duration(self, ban_duration):
        r"""Sets the ban_duration of this AccessControlUrls.

        URL封禁天数，默认7天，取值范围1-30。

        :param ban_duration: The ban_duration of this AccessControlUrls.
        :type ban_duration: int
        """
        self._ban_duration = ban_duration

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
        if not isinstance(other, AccessControlUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
