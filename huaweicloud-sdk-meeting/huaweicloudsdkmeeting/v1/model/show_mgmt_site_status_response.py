# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMgmtSiteStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'redirect_join_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'redirect_join_url': 'redirectJoinUrl'
    }

    def __init__(self, status=None, redirect_join_url=None):
        r"""ShowMgmtSiteStatusResponse

        The model defined in huaweicloud sdk

        :param status: 管理站点状态 NORMAL:正常  FAULT:故障
        :type status: str
        :param redirect_join_url: 链接入会跳转url
        :type redirect_join_url: str
        """
        
        super(ShowMgmtSiteStatusResponse, self).__init__()

        self._status = None
        self._redirect_join_url = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if redirect_join_url is not None:
            self.redirect_join_url = redirect_join_url

    @property
    def status(self):
        r"""Gets the status of this ShowMgmtSiteStatusResponse.

        管理站点状态 NORMAL:正常  FAULT:故障

        :return: The status of this ShowMgmtSiteStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMgmtSiteStatusResponse.

        管理站点状态 NORMAL:正常  FAULT:故障

        :param status: The status of this ShowMgmtSiteStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def redirect_join_url(self):
        r"""Gets the redirect_join_url of this ShowMgmtSiteStatusResponse.

        链接入会跳转url

        :return: The redirect_join_url of this ShowMgmtSiteStatusResponse.
        :rtype: str
        """
        return self._redirect_join_url

    @redirect_join_url.setter
    def redirect_join_url(self, redirect_join_url):
        r"""Sets the redirect_join_url of this ShowMgmtSiteStatusResponse.

        链接入会跳转url

        :param redirect_join_url: The redirect_join_url of this ShowMgmtSiteStatusResponse.
        :type redirect_join_url: str
        """
        self._redirect_join_url = redirect_join_url

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
        if not isinstance(other, ShowMgmtSiteStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
