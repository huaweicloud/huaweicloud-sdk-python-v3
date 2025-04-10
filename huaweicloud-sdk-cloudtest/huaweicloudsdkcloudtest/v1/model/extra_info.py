# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'child_import_package': 'list[str]',
        'document_link': 'str',
        'http_method': 'str',
        'http_url': 'str',
        'import_package': 'list[str]',
        'mock': 'MockInfo',
        'output_param': 'list[AwVariable]',
        'param_dependent': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'child_import_package': 'childImportPackage',
        'document_link': 'document_link',
        'http_method': 'http_method',
        'http_url': 'http_url',
        'import_package': 'importPackage',
        'mock': 'mock',
        'output_param': 'outputParam',
        'param_dependent': 'param_dependent',
        'summary': 'summary'
    }

    def __init__(self, child_import_package=None, document_link=None, http_method=None, http_url=None, import_package=None, mock=None, output_param=None, param_dependent=None, summary=None):
        r"""ExtraInfo

        The model defined in huaweicloud sdk

        :param child_import_package: 子级导入的包
        :type child_import_package: list[str]
        :param document_link: 文档链接
        :type document_link: str
        :param http_method: http请求方法
        :type http_method: str
        :param http_url: HTTP请求的URL
        :type http_url: str
        :param import_package: 导入的包
        :type import_package: list[str]
        :param mock: 
        :type mock: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        :param output_param: 输出参数
        :type output_param: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param param_dependent: 参数依赖
        :type param_dependent: str
        :param summary: 摘要
        :type summary: str
        """
        
        

        self._child_import_package = None
        self._document_link = None
        self._http_method = None
        self._http_url = None
        self._import_package = None
        self._mock = None
        self._output_param = None
        self._param_dependent = None
        self._summary = None
        self.discriminator = None

        if child_import_package is not None:
            self.child_import_package = child_import_package
        if document_link is not None:
            self.document_link = document_link
        if http_method is not None:
            self.http_method = http_method
        if http_url is not None:
            self.http_url = http_url
        if import_package is not None:
            self.import_package = import_package
        if mock is not None:
            self.mock = mock
        if output_param is not None:
            self.output_param = output_param
        if param_dependent is not None:
            self.param_dependent = param_dependent
        if summary is not None:
            self.summary = summary

    @property
    def child_import_package(self):
        r"""Gets the child_import_package of this ExtraInfo.

        子级导入的包

        :return: The child_import_package of this ExtraInfo.
        :rtype: list[str]
        """
        return self._child_import_package

    @child_import_package.setter
    def child_import_package(self, child_import_package):
        r"""Sets the child_import_package of this ExtraInfo.

        子级导入的包

        :param child_import_package: The child_import_package of this ExtraInfo.
        :type child_import_package: list[str]
        """
        self._child_import_package = child_import_package

    @property
    def document_link(self):
        r"""Gets the document_link of this ExtraInfo.

        文档链接

        :return: The document_link of this ExtraInfo.
        :rtype: str
        """
        return self._document_link

    @document_link.setter
    def document_link(self, document_link):
        r"""Sets the document_link of this ExtraInfo.

        文档链接

        :param document_link: The document_link of this ExtraInfo.
        :type document_link: str
        """
        self._document_link = document_link

    @property
    def http_method(self):
        r"""Gets the http_method of this ExtraInfo.

        http请求方法

        :return: The http_method of this ExtraInfo.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this ExtraInfo.

        http请求方法

        :param http_method: The http_method of this ExtraInfo.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def http_url(self):
        r"""Gets the http_url of this ExtraInfo.

        HTTP请求的URL

        :return: The http_url of this ExtraInfo.
        :rtype: str
        """
        return self._http_url

    @http_url.setter
    def http_url(self, http_url):
        r"""Sets the http_url of this ExtraInfo.

        HTTP请求的URL

        :param http_url: The http_url of this ExtraInfo.
        :type http_url: str
        """
        self._http_url = http_url

    @property
    def import_package(self):
        r"""Gets the import_package of this ExtraInfo.

        导入的包

        :return: The import_package of this ExtraInfo.
        :rtype: list[str]
        """
        return self._import_package

    @import_package.setter
    def import_package(self, import_package):
        r"""Sets the import_package of this ExtraInfo.

        导入的包

        :param import_package: The import_package of this ExtraInfo.
        :type import_package: list[str]
        """
        self._import_package = import_package

    @property
    def mock(self):
        r"""Gets the mock of this ExtraInfo.

        :return: The mock of this ExtraInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        """
        return self._mock

    @mock.setter
    def mock(self, mock):
        r"""Sets the mock of this ExtraInfo.

        :param mock: The mock of this ExtraInfo.
        :type mock: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        """
        self._mock = mock

    @property
    def output_param(self):
        r"""Gets the output_param of this ExtraInfo.

        输出参数

        :return: The output_param of this ExtraInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._output_param

    @output_param.setter
    def output_param(self, output_param):
        r"""Sets the output_param of this ExtraInfo.

        输出参数

        :param output_param: The output_param of this ExtraInfo.
        :type output_param: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._output_param = output_param

    @property
    def param_dependent(self):
        r"""Gets the param_dependent of this ExtraInfo.

        参数依赖

        :return: The param_dependent of this ExtraInfo.
        :rtype: str
        """
        return self._param_dependent

    @param_dependent.setter
    def param_dependent(self, param_dependent):
        r"""Sets the param_dependent of this ExtraInfo.

        参数依赖

        :param param_dependent: The param_dependent of this ExtraInfo.
        :type param_dependent: str
        """
        self._param_dependent = param_dependent

    @property
    def summary(self):
        r"""Gets the summary of this ExtraInfo.

        摘要

        :return: The summary of this ExtraInfo.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ExtraInfo.

        摘要

        :param summary: The summary of this ExtraInfo.
        :type summary: str
        """
        self._summary = summary

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
        if not isinstance(other, ExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
