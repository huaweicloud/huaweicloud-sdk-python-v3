# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rtmp_urls': 'list[str]'
    }

    attribute_map = {
        'rtmp_urls': 'rtmp_urls'
    }

    def __init__(self, rtmp_urls=None):
        """PublishParam

        The model defined in huaweicloud sdk

        :param rtmp_urls: 合流任务完成后，转推的RTMP推流地址。
        :type rtmp_urls: list[str]
        """
        
        

        self._rtmp_urls = None
        self.discriminator = None

        self.rtmp_urls = rtmp_urls

    @property
    def rtmp_urls(self):
        """Gets the rtmp_urls of this PublishParam.

        合流任务完成后，转推的RTMP推流地址。

        :return: The rtmp_urls of this PublishParam.
        :rtype: list[str]
        """
        return self._rtmp_urls

    @rtmp_urls.setter
    def rtmp_urls(self, rtmp_urls):
        """Sets the rtmp_urls of this PublishParam.

        合流任务完成后，转推的RTMP推流地址。

        :param rtmp_urls: The rtmp_urls of this PublishParam.
        :type rtmp_urls: list[str]
        """
        self._rtmp_urls = rtmp_urls

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
        if not isinstance(other, PublishParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
