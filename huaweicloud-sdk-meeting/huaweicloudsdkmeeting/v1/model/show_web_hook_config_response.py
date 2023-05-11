# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebHookConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'return_code': 'int',
        'return_desc': 'str',
        'id': 'str',
        'subscriber_id': 'str',
        'url': 'str',
        'status': 'int'
    }

    attribute_map = {
        'return_code': 'returnCode',
        'return_desc': 'returnDesc',
        'id': 'id',
        'subscriber_id': 'subscriberId',
        'url': 'url',
        'status': 'status'
    }

    def __init__(self, return_code=None, return_desc=None, id=None, subscriber_id=None, url=None, status=None):
        """ShowWebHookConfigResponse

        The model defined in huaweicloud sdk

        :param return_code: 结果码。
        :type return_code: int
        :param return_desc: 结果描述。
        :type return_desc: str
        :param id: 订阅配置记录ID。
        :type id: str
        :param subscriber_id: 订阅ID。
        :type subscriber_id: str
        :param url: 订阅url。
        :type url: str
        :param status: 事件推送状态。 * 0：已启用 * 1：未启动 * 2：已锁定 
        :type status: int
        """
        
        super(ShowWebHookConfigResponse, self).__init__()

        self._return_code = None
        self._return_desc = None
        self._id = None
        self._subscriber_id = None
        self._url = None
        self._status = None
        self.discriminator = None

        self.return_code = return_code
        if return_desc is not None:
            self.return_desc = return_desc
        if id is not None:
            self.id = id
        if subscriber_id is not None:
            self.subscriber_id = subscriber_id
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status

    @property
    def return_code(self):
        """Gets the return_code of this ShowWebHookConfigResponse.

        结果码。

        :return: The return_code of this ShowWebHookConfigResponse.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this ShowWebHookConfigResponse.

        结果码。

        :param return_code: The return_code of this ShowWebHookConfigResponse.
        :type return_code: int
        """
        self._return_code = return_code

    @property
    def return_desc(self):
        """Gets the return_desc of this ShowWebHookConfigResponse.

        结果描述。

        :return: The return_desc of this ShowWebHookConfigResponse.
        :rtype: str
        """
        return self._return_desc

    @return_desc.setter
    def return_desc(self, return_desc):
        """Sets the return_desc of this ShowWebHookConfigResponse.

        结果描述。

        :param return_desc: The return_desc of this ShowWebHookConfigResponse.
        :type return_desc: str
        """
        self._return_desc = return_desc

    @property
    def id(self):
        """Gets the id of this ShowWebHookConfigResponse.

        订阅配置记录ID。

        :return: The id of this ShowWebHookConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowWebHookConfigResponse.

        订阅配置记录ID。

        :param id: The id of this ShowWebHookConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def subscriber_id(self):
        """Gets the subscriber_id of this ShowWebHookConfigResponse.

        订阅ID。

        :return: The subscriber_id of this ShowWebHookConfigResponse.
        :rtype: str
        """
        return self._subscriber_id

    @subscriber_id.setter
    def subscriber_id(self, subscriber_id):
        """Sets the subscriber_id of this ShowWebHookConfigResponse.

        订阅ID。

        :param subscriber_id: The subscriber_id of this ShowWebHookConfigResponse.
        :type subscriber_id: str
        """
        self._subscriber_id = subscriber_id

    @property
    def url(self):
        """Gets the url of this ShowWebHookConfigResponse.

        订阅url。

        :return: The url of this ShowWebHookConfigResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowWebHookConfigResponse.

        订阅url。

        :param url: The url of this ShowWebHookConfigResponse.
        :type url: str
        """
        self._url = url

    @property
    def status(self):
        """Gets the status of this ShowWebHookConfigResponse.

        事件推送状态。 * 0：已启用 * 1：未启动 * 2：已锁定 

        :return: The status of this ShowWebHookConfigResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowWebHookConfigResponse.

        事件推送状态。 * 0：已启用 * 1：未启动 * 2：已锁定 

        :param status: The status of this ShowWebHookConfigResponse.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ShowWebHookConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
