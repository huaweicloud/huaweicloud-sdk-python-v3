# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefreshResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'url': 'url',
        'status': 'status'
    }

    def __init__(self, url=None, status=None):
        r"""RefreshResult

        The model defined in huaweicloud sdk

        :param url: 刷新URL。
        :type url: str
        :param status: 刷新任务状态。  取值如下： - PROCESSING：处理中 - SUCCEED：刷新完成 - FAILED：刷新失败 
        :type status: str
        """
        
        

        self._url = None
        self._status = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if status is not None:
            self.status = status

    @property
    def url(self):
        r"""Gets the url of this RefreshResult.

        刷新URL。

        :return: The url of this RefreshResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RefreshResult.

        刷新URL。

        :param url: The url of this RefreshResult.
        :type url: str
        """
        self._url = url

    @property
    def status(self):
        r"""Gets the status of this RefreshResult.

        刷新任务状态。  取值如下： - PROCESSING：处理中 - SUCCEED：刷新完成 - FAILED：刷新失败 

        :return: The status of this RefreshResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RefreshResult.

        刷新任务状态。  取值如下： - PROCESSING：处理中 - SUCCEED：刷新完成 - FAILED：刷新失败 

        :param status: The status of this RefreshResult.
        :type status: str
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
        if not isinstance(other, RefreshResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
