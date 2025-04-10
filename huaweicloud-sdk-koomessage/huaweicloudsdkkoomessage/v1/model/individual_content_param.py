# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndividualContentParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'content_type': 'str',
        'content_source': 'str',
        'content_detail': 'str'
    }

    attribute_map = {
        'param_name': 'param_name',
        'content_type': 'content_type',
        'content_source': 'content_source',
        'content_detail': 'content_detail'
    }

    def __init__(self, param_name=None, content_type=None, content_source=None, content_detail=None):
        r"""IndividualContentParam

        The model defined in huaweicloud sdk

        :param param_name: 智能信息基础版参数名称。
        :type param_name: str
        :param content_type: 智能信息基础版参数类型。txt：纯文字动参。 
        :type content_type: str
        :param content_source: 智能信息基础版参数源。txt：内容源自纯文字。 
        :type content_source: str
        :param content_detail: 智能信息基础版参数内容，填写经过utf-8编码的文字。 
        :type content_detail: str
        """
        
        

        self._param_name = None
        self._content_type = None
        self._content_source = None
        self._content_detail = None
        self.discriminator = None

        self.param_name = param_name
        self.content_type = content_type
        self.content_source = content_source
        self.content_detail = content_detail

    @property
    def param_name(self):
        r"""Gets the param_name of this IndividualContentParam.

        智能信息基础版参数名称。

        :return: The param_name of this IndividualContentParam.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this IndividualContentParam.

        智能信息基础版参数名称。

        :param param_name: The param_name of this IndividualContentParam.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def content_type(self):
        r"""Gets the content_type of this IndividualContentParam.

        智能信息基础版参数类型。txt：纯文字动参。 

        :return: The content_type of this IndividualContentParam.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this IndividualContentParam.

        智能信息基础版参数类型。txt：纯文字动参。 

        :param content_type: The content_type of this IndividualContentParam.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def content_source(self):
        r"""Gets the content_source of this IndividualContentParam.

        智能信息基础版参数源。txt：内容源自纯文字。 

        :return: The content_source of this IndividualContentParam.
        :rtype: str
        """
        return self._content_source

    @content_source.setter
    def content_source(self, content_source):
        r"""Sets the content_source of this IndividualContentParam.

        智能信息基础版参数源。txt：内容源自纯文字。 

        :param content_source: The content_source of this IndividualContentParam.
        :type content_source: str
        """
        self._content_source = content_source

    @property
    def content_detail(self):
        r"""Gets the content_detail of this IndividualContentParam.

        智能信息基础版参数内容，填写经过utf-8编码的文字。 

        :return: The content_detail of this IndividualContentParam.
        :rtype: str
        """
        return self._content_detail

    @content_detail.setter
    def content_detail(self, content_detail):
        r"""Sets the content_detail of this IndividualContentParam.

        智能信息基础版参数内容，填写经过utf-8编码的文字。 

        :param content_detail: The content_detail of this IndividualContentParam.
        :type content_detail: str
        """
        self._content_detail = content_detail

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
        if not isinstance(other, IndividualContentParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
