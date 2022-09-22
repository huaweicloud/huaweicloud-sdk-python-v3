# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebHookConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'corp_id': 'str',
        'sp_id': 'str',
        'subscriber_id': 'str',
        'subscriber_key': 'str',
        'url': 'str'
    }

    attribute_map = {
        'corp_id': 'corpId',
        'sp_id': 'spId',
        'subscriber_id': 'subscriberId',
        'subscriber_key': 'subscriberKey',
        'url': 'url'
    }

    def __init__(self, corp_id=None, sp_id=None, subscriber_id=None, subscriber_key=None, url=None):
        """WebHookConfigRequest

        The model defined in huaweicloud sdk

        :param corp_id: 企业ID。按企业注册回调时需要填写。
        :type corp_id: str
        :param sp_id: SP ID。多租户场景下，按SP注册回调时需要填写。
        :type sp_id: str
        :param subscriber_id: 订阅者ID。
        :type subscriber_id: str
        :param subscriber_key: 订阅者秘钥。
        :type subscriber_key: str
        :param url: 订阅url。 &gt; 必须使用HTTPS。 
        :type url: str
        """
        
        

        self._corp_id = None
        self._sp_id = None
        self._subscriber_id = None
        self._subscriber_key = None
        self._url = None
        self.discriminator = None

        if corp_id is not None:
            self.corp_id = corp_id
        if sp_id is not None:
            self.sp_id = sp_id
        self.subscriber_id = subscriber_id
        self.subscriber_key = subscriber_key
        self.url = url

    @property
    def corp_id(self):
        """Gets the corp_id of this WebHookConfigRequest.

        企业ID。按企业注册回调时需要填写。

        :return: The corp_id of this WebHookConfigRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this WebHookConfigRequest.

        企业ID。按企业注册回调时需要填写。

        :param corp_id: The corp_id of this WebHookConfigRequest.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def sp_id(self):
        """Gets the sp_id of this WebHookConfigRequest.

        SP ID。多租户场景下，按SP注册回调时需要填写。

        :return: The sp_id of this WebHookConfigRequest.
        :rtype: str
        """
        return self._sp_id

    @sp_id.setter
    def sp_id(self, sp_id):
        """Sets the sp_id of this WebHookConfigRequest.

        SP ID。多租户场景下，按SP注册回调时需要填写。

        :param sp_id: The sp_id of this WebHookConfigRequest.
        :type sp_id: str
        """
        self._sp_id = sp_id

    @property
    def subscriber_id(self):
        """Gets the subscriber_id of this WebHookConfigRequest.

        订阅者ID。

        :return: The subscriber_id of this WebHookConfigRequest.
        :rtype: str
        """
        return self._subscriber_id

    @subscriber_id.setter
    def subscriber_id(self, subscriber_id):
        """Sets the subscriber_id of this WebHookConfigRequest.

        订阅者ID。

        :param subscriber_id: The subscriber_id of this WebHookConfigRequest.
        :type subscriber_id: str
        """
        self._subscriber_id = subscriber_id

    @property
    def subscriber_key(self):
        """Gets the subscriber_key of this WebHookConfigRequest.

        订阅者秘钥。

        :return: The subscriber_key of this WebHookConfigRequest.
        :rtype: str
        """
        return self._subscriber_key

    @subscriber_key.setter
    def subscriber_key(self, subscriber_key):
        """Sets the subscriber_key of this WebHookConfigRequest.

        订阅者秘钥。

        :param subscriber_key: The subscriber_key of this WebHookConfigRequest.
        :type subscriber_key: str
        """
        self._subscriber_key = subscriber_key

    @property
    def url(self):
        """Gets the url of this WebHookConfigRequest.

        订阅url。 > 必须使用HTTPS。 

        :return: The url of this WebHookConfigRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebHookConfigRequest.

        订阅url。 > 必须使用HTTPS。 

        :param url: The url of this WebHookConfigRequest.
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
        if not isinstance(other, WebHookConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
