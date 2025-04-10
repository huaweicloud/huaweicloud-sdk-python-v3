# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertRemediation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommendation': 'str',
        'url': 'str'
    }

    attribute_map = {
        'recommendation': 'recommendation',
        'url': 'url'
    }

    def __init__(self, recommendation=None, url=None):
        r"""AlertRemediation

        The model defined in huaweicloud sdk

        :param recommendation: 推荐处理方法
        :type recommendation: str
        :param url: 链接，指向该事件的一般修复信息。该URL必须可以从公网访问，不需要提供凭证
        :type url: str
        """
        
        

        self._recommendation = None
        self._url = None
        self.discriminator = None

        if recommendation is not None:
            self.recommendation = recommendation
        if url is not None:
            self.url = url

    @property
    def recommendation(self):
        r"""Gets the recommendation of this AlertRemediation.

        推荐处理方法

        :return: The recommendation of this AlertRemediation.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        r"""Sets the recommendation of this AlertRemediation.

        推荐处理方法

        :param recommendation: The recommendation of this AlertRemediation.
        :type recommendation: str
        """
        self._recommendation = recommendation

    @property
    def url(self):
        r"""Gets the url of this AlertRemediation.

        链接，指向该事件的一般修复信息。该URL必须可以从公网访问，不需要提供凭证

        :return: The url of this AlertRemediation.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AlertRemediation.

        链接，指向该事件的一般修复信息。该URL必须可以从公网访问，不需要提供凭证

        :param url: The url of this AlertRemediation.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, AlertRemediation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
