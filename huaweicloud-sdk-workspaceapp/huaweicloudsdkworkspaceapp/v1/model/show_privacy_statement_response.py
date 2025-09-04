# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrivacyStatementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'content': 'str',
        'publish_time': 'datetime',
        'language': 'str',
        'signed_history_record': 'bool',
        'signed_newest_record': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'content': 'content',
        'publish_time': 'publish_time',
        'language': 'language',
        'signed_history_record': 'signed_history_record',
        'signed_newest_record': 'signed_newest_record'
    }

    def __init__(self, version=None, content=None, publish_time=None, language=None, signed_history_record=None, signed_newest_record=None):
        r"""ShowPrivacyStatementResponse

        The model defined in huaweicloud sdk

        :param version: 隐私声明版本号。
        :type version: str
        :param content: 隐私声明内容。
        :type content: str
        :param publish_time: 隐私声明发布时间。
        :type publish_time: datetime
        :param language: 隐私声明对应的语言。
        :type language: str
        :param signed_history_record: 是否签署过历史隐私声明，非第一次签署，提示用户旧版过期需重新签署。
        :type signed_history_record: bool
        :param signed_newest_record: 是否签署过当前最新的隐私申明 没有签署需需要提醒用户重新签署。
        :type signed_newest_record: bool
        """
        
        super(ShowPrivacyStatementResponse, self).__init__()

        self._version = None
        self._content = None
        self._publish_time = None
        self._language = None
        self._signed_history_record = None
        self._signed_newest_record = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if content is not None:
            self.content = content
        if publish_time is not None:
            self.publish_time = publish_time
        if language is not None:
            self.language = language
        if signed_history_record is not None:
            self.signed_history_record = signed_history_record
        if signed_newest_record is not None:
            self.signed_newest_record = signed_newest_record

    @property
    def version(self):
        r"""Gets the version of this ShowPrivacyStatementResponse.

        隐私声明版本号。

        :return: The version of this ShowPrivacyStatementResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowPrivacyStatementResponse.

        隐私声明版本号。

        :param version: The version of this ShowPrivacyStatementResponse.
        :type version: str
        """
        self._version = version

    @property
    def content(self):
        r"""Gets the content of this ShowPrivacyStatementResponse.

        隐私声明内容。

        :return: The content of this ShowPrivacyStatementResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowPrivacyStatementResponse.

        隐私声明内容。

        :param content: The content of this ShowPrivacyStatementResponse.
        :type content: str
        """
        self._content = content

    @property
    def publish_time(self):
        r"""Gets the publish_time of this ShowPrivacyStatementResponse.

        隐私声明发布时间。

        :return: The publish_time of this ShowPrivacyStatementResponse.
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this ShowPrivacyStatementResponse.

        隐私声明发布时间。

        :param publish_time: The publish_time of this ShowPrivacyStatementResponse.
        :type publish_time: datetime
        """
        self._publish_time = publish_time

    @property
    def language(self):
        r"""Gets the language of this ShowPrivacyStatementResponse.

        隐私声明对应的语言。

        :return: The language of this ShowPrivacyStatementResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowPrivacyStatementResponse.

        隐私声明对应的语言。

        :param language: The language of this ShowPrivacyStatementResponse.
        :type language: str
        """
        self._language = language

    @property
    def signed_history_record(self):
        r"""Gets the signed_history_record of this ShowPrivacyStatementResponse.

        是否签署过历史隐私声明，非第一次签署，提示用户旧版过期需重新签署。

        :return: The signed_history_record of this ShowPrivacyStatementResponse.
        :rtype: bool
        """
        return self._signed_history_record

    @signed_history_record.setter
    def signed_history_record(self, signed_history_record):
        r"""Sets the signed_history_record of this ShowPrivacyStatementResponse.

        是否签署过历史隐私声明，非第一次签署，提示用户旧版过期需重新签署。

        :param signed_history_record: The signed_history_record of this ShowPrivacyStatementResponse.
        :type signed_history_record: bool
        """
        self._signed_history_record = signed_history_record

    @property
    def signed_newest_record(self):
        r"""Gets the signed_newest_record of this ShowPrivacyStatementResponse.

        是否签署过当前最新的隐私申明 没有签署需需要提醒用户重新签署。

        :return: The signed_newest_record of this ShowPrivacyStatementResponse.
        :rtype: bool
        """
        return self._signed_newest_record

    @signed_newest_record.setter
    def signed_newest_record(self, signed_newest_record):
        r"""Sets the signed_newest_record of this ShowPrivacyStatementResponse.

        是否签署过当前最新的隐私申明 没有签署需需要提醒用户重新签署。

        :param signed_newest_record: The signed_newest_record of this ShowPrivacyStatementResponse.
        :type signed_newest_record: bool
        """
        self._signed_newest_record = signed_newest_record

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
        if not isinstance(other, ShowPrivacyStatementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
