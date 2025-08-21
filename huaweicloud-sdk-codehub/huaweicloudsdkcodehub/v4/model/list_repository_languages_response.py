# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryLanguagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'languages': 'list[LanguagesDto]',
        'status': 'str',
        'x_total': 'str'
    }

    attribute_map = {
        'languages': 'languages',
        'status': 'status',
        'x_total': 'X-Total'
    }

    def __init__(self, languages=None, status=None, x_total=None):
        r"""ListRepositoryLanguagesResponse

        The model defined in huaweicloud sdk

        :param languages: **参数解释：** 语言描述。
        :type languages: list[:class:`huaweicloudsdkcodehub.v4.LanguagesDto`]
        :param status: **参数解释：** 返回状态。
        :type status: str
        :param x_total: 
        :type x_total: str
        """
        
        super(ListRepositoryLanguagesResponse, self).__init__()

        self._languages = None
        self._status = None
        self._x_total = None
        self.discriminator = None

        if languages is not None:
            self.languages = languages
        if status is not None:
            self.status = status
        if x_total is not None:
            self.x_total = x_total

    @property
    def languages(self):
        r"""Gets the languages of this ListRepositoryLanguagesResponse.

        **参数解释：** 语言描述。

        :return: The languages of this ListRepositoryLanguagesResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.LanguagesDto`]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        r"""Sets the languages of this ListRepositoryLanguagesResponse.

        **参数解释：** 语言描述。

        :param languages: The languages of this ListRepositoryLanguagesResponse.
        :type languages: list[:class:`huaweicloudsdkcodehub.v4.LanguagesDto`]
        """
        self._languages = languages

    @property
    def status(self):
        r"""Gets the status of this ListRepositoryLanguagesResponse.

        **参数解释：** 返回状态。

        :return: The status of this ListRepositoryLanguagesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRepositoryLanguagesResponse.

        **参数解释：** 返回状态。

        :param status: The status of this ListRepositoryLanguagesResponse.
        :type status: str
        """
        self._status = status

    @property
    def x_total(self):
        r"""Gets the x_total of this ListRepositoryLanguagesResponse.

        :return: The x_total of this ListRepositoryLanguagesResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ListRepositoryLanguagesResponse.

        :param x_total: The x_total of this ListRepositoryLanguagesResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ListRepositoryLanguagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
