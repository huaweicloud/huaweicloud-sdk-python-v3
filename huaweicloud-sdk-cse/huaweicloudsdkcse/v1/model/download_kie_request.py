# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadKieRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str',
        'x_engine_id': 'str',
        'label': 'str',
        'match': 'str',
        'body': 'DownloadKieReqBody'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'x_engine_id': 'x-engine-id',
        'label': 'label',
        'match': 'match',
        'body': 'body'
    }

    def __init__(self, x_enterprise_project_id=None, x_engine_id=None, label=None, match=None, body=None):
        r"""DownloadKieRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 如果不带则默认企业项目为\&quot;default\&quot;，ID为\&quot;0\&quot;
        :type x_enterprise_project_id: str
        :param x_engine_id: 微服务引擎ID。
        :type x_engine_id: str
        :param label: 按label过滤项导出，格式为：{标签key}:{标签value}
        :type label: str
        :param match: 对label过滤项的匹配选项，如果值为exact：表示严格匹配，包括label个数和内容相等；不填表示包含匹配
        :type match: str
        :param body: Body of the DownloadKieRequest
        :type body: :class:`huaweicloudsdkcse.v1.DownloadKieReqBody`
        """
        
        

        self._x_enterprise_project_id = None
        self._x_engine_id = None
        self._label = None
        self._match = None
        self._body = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.x_engine_id = x_engine_id
        if label is not None:
            self.label = label
        if match is not None:
            self.match = match
        if body is not None:
            self.body = body

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this DownloadKieRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :return: The x_enterprise_project_id of this DownloadKieRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this DownloadKieRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :param x_enterprise_project_id: The x_enterprise_project_id of this DownloadKieRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_engine_id(self):
        r"""Gets the x_engine_id of this DownloadKieRequest.

        微服务引擎ID。

        :return: The x_engine_id of this DownloadKieRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        r"""Sets the x_engine_id of this DownloadKieRequest.

        微服务引擎ID。

        :param x_engine_id: The x_engine_id of this DownloadKieRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def label(self):
        r"""Gets the label of this DownloadKieRequest.

        按label过滤项导出，格式为：{标签key}:{标签value}

        :return: The label of this DownloadKieRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this DownloadKieRequest.

        按label过滤项导出，格式为：{标签key}:{标签value}

        :param label: The label of this DownloadKieRequest.
        :type label: str
        """
        self._label = label

    @property
    def match(self):
        r"""Gets the match of this DownloadKieRequest.

        对label过滤项的匹配选项，如果值为exact：表示严格匹配，包括label个数和内容相等；不填表示包含匹配

        :return: The match of this DownloadKieRequest.
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        r"""Sets the match of this DownloadKieRequest.

        对label过滤项的匹配选项，如果值为exact：表示严格匹配，包括label个数和内容相等；不填表示包含匹配

        :param match: The match of this DownloadKieRequest.
        :type match: str
        """
        self._match = match

    @property
    def body(self):
        r"""Gets the body of this DownloadKieRequest.

        :return: The body of this DownloadKieRequest.
        :rtype: :class:`huaweicloudsdkcse.v1.DownloadKieReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DownloadKieRequest.

        :param body: The body of this DownloadKieRequest.
        :type body: :class:`huaweicloudsdkcse.v1.DownloadKieReqBody`
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
        if not isinstance(other, DownloadKieRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
