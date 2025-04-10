# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTranscodingsTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'domain': 'str',
        'templates': 'list[AppQualityInfo]'
    }

    attribute_map = {
        'total': 'total',
        'domain': 'domain',
        'templates': 'templates'
    }

    def __init__(self, total=None, domain=None, templates=None):
        r"""ShowTranscodingsTemplateResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总元素数量
        :type total: int
        :param domain: 播放域名
        :type domain: str
        :param templates: 转码模板
        :type templates: list[:class:`huaweicloudsdklive.v1.AppQualityInfo`]
        """
        
        super(ShowTranscodingsTemplateResponse, self).__init__()

        self._total = None
        self._domain = None
        self._templates = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if domain is not None:
            self.domain = domain
        if templates is not None:
            self.templates = templates

    @property
    def total(self):
        r"""Gets the total of this ShowTranscodingsTemplateResponse.

        查询结果的总元素数量

        :return: The total of this ShowTranscodingsTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowTranscodingsTemplateResponse.

        查询结果的总元素数量

        :param total: The total of this ShowTranscodingsTemplateResponse.
        :type total: int
        """
        self._total = total

    @property
    def domain(self):
        r"""Gets the domain of this ShowTranscodingsTemplateResponse.

        播放域名

        :return: The domain of this ShowTranscodingsTemplateResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ShowTranscodingsTemplateResponse.

        播放域名

        :param domain: The domain of this ShowTranscodingsTemplateResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def templates(self):
        r"""Gets the templates of this ShowTranscodingsTemplateResponse.

        转码模板

        :return: The templates of this ShowTranscodingsTemplateResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.AppQualityInfo`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ShowTranscodingsTemplateResponse.

        转码模板

        :param templates: The templates of this ShowTranscodingsTemplateResponse.
        :type templates: list[:class:`huaweicloudsdklive.v1.AppQualityInfo`]
        """
        self._templates = templates

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
        if not isinstance(other, ShowTranscodingsTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
