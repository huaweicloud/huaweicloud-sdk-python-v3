# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkQualityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('conf_token')

    openapi_types = {
        'conferenceid': 'str',
        'conf_token': 'str',
        'appid': 'str',
        'confuuid': 'str',
        'body': 'RestQosRequestDTO'
    }

    attribute_map = {
        'conferenceid': 'conferenceid',
        'conf_token': 'confToken',
        'appid': 'appid',
        'confuuid': 'confuuid',
        'body': 'body'
    }

    def __init__(self, conferenceid=None, conf_token=None, appid=None, confuuid=None, body=None):
        r"""ListNetworkQualityRequest

        The model defined in huaweicloud sdk

        :param conferenceid: 会议id
        :type conferenceid: str
        :param conf_token: 会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。
        :type conf_token: str
        :param appid: 会议的appId
        :type appid: str
        :param confuuid: 会议UUID，MMR房间ID
        :type confuuid: str
        :param body: Body of the ListNetworkQualityRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.RestQosRequestDTO`
        """
        
        

        self._conferenceid = None
        self._conf_token = None
        self._appid = None
        self._confuuid = None
        self._body = None
        self.discriminator = None

        self.conferenceid = conferenceid
        self.conf_token = conf_token
        if appid is not None:
            self.appid = appid
        self.confuuid = confuuid
        if body is not None:
            self.body = body

    @property
    def conferenceid(self):
        r"""Gets the conferenceid of this ListNetworkQualityRequest.

        会议id

        :return: The conferenceid of this ListNetworkQualityRequest.
        :rtype: str
        """
        return self._conferenceid

    @conferenceid.setter
    def conferenceid(self, conferenceid):
        r"""Sets the conferenceid of this ListNetworkQualityRequest.

        会议id

        :param conferenceid: The conferenceid of this ListNetworkQualityRequest.
        :type conferenceid: str
        """
        self._conferenceid = conferenceid

    @property
    def conf_token(self):
        r"""Gets the conf_token of this ListNetworkQualityRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :return: The conf_token of this ListNetworkQualityRequest.
        :rtype: str
        """
        return self._conf_token

    @conf_token.setter
    def conf_token(self, conf_token):
        r"""Sets the conf_token of this ListNetworkQualityRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :param conf_token: The conf_token of this ListNetworkQualityRequest.
        :type conf_token: str
        """
        self._conf_token = conf_token

    @property
    def appid(self):
        r"""Gets the appid of this ListNetworkQualityRequest.

        会议的appId

        :return: The appid of this ListNetworkQualityRequest.
        :rtype: str
        """
        return self._appid

    @appid.setter
    def appid(self, appid):
        r"""Sets the appid of this ListNetworkQualityRequest.

        会议的appId

        :param appid: The appid of this ListNetworkQualityRequest.
        :type appid: str
        """
        self._appid = appid

    @property
    def confuuid(self):
        r"""Gets the confuuid of this ListNetworkQualityRequest.

        会议UUID，MMR房间ID

        :return: The confuuid of this ListNetworkQualityRequest.
        :rtype: str
        """
        return self._confuuid

    @confuuid.setter
    def confuuid(self, confuuid):
        r"""Sets the confuuid of this ListNetworkQualityRequest.

        会议UUID，MMR房间ID

        :param confuuid: The confuuid of this ListNetworkQualityRequest.
        :type confuuid: str
        """
        self._confuuid = confuuid

    @property
    def body(self):
        r"""Gets the body of this ListNetworkQualityRequest.

        :return: The body of this ListNetworkQualityRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestQosRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListNetworkQualityRequest.

        :param body: The body of this ListNetworkQualityRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.RestQosRequestDTO`
        """
        self._body = body

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
        if not isinstance(other, ListNetworkQualityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
