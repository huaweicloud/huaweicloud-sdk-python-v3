# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionCodeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'func_code': 'FuncCode',
        'depend_list': 'list[str]',
        'depend_version_list': 'list[str]'
    }

    attribute_map = {
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'func_code': 'func_code',
        'depend_list': 'depend_list',
        'depend_version_list': 'depend_version_list'
    }

    def __init__(self, code_type=None, code_url=None, code_filename=None, func_code=None, depend_list=None, depend_version_list=None):
        """UpdateFunctionCodeRequestBody

        The model defined in huaweicloud sdk

        :param code_type: 函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。
        :type code_type: str
        :param code_url: 当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。
        :type code_url: str
        :param code_filename: 函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。
        :type code_filename: str
        :param func_code: 
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        :param depend_list: 依赖id列表
        :type depend_list: list[str]
        :param depend_version_list: 依赖版本id列表
        :type depend_version_list: list[str]
        """
        
        

        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._func_code = None
        self._depend_list = None
        self._depend_version_list = None
        self.discriminator = None

        self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        self.func_code = func_code
        if depend_list is not None:
            self.depend_list = depend_list
        if depend_version_list is not None:
            self.depend_version_list = depend_version_list

    @property
    def code_type(self):
        """Gets the code_type of this UpdateFunctionCodeRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :return: The code_type of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this UpdateFunctionCodeRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :param code_type: The code_type of this UpdateFunctionCodeRequestBody.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        """Gets the code_url of this UpdateFunctionCodeRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this UpdateFunctionCodeRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this UpdateFunctionCodeRequestBody.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        """Gets the code_filename of this UpdateFunctionCodeRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        """Sets the code_filename of this UpdateFunctionCodeRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this UpdateFunctionCodeRequestBody.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def func_code(self):
        """Gets the func_code of this UpdateFunctionCodeRequestBody.

        :return: The func_code of this UpdateFunctionCodeRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        return self._func_code

    @func_code.setter
    def func_code(self, func_code):
        """Sets the func_code of this UpdateFunctionCodeRequestBody.

        :param func_code: The func_code of this UpdateFunctionCodeRequestBody.
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        self._func_code = func_code

    @property
    def depend_list(self):
        """Gets the depend_list of this UpdateFunctionCodeRequestBody.

        依赖id列表

        :return: The depend_list of this UpdateFunctionCodeRequestBody.
        :rtype: list[str]
        """
        return self._depend_list

    @depend_list.setter
    def depend_list(self, depend_list):
        """Sets the depend_list of this UpdateFunctionCodeRequestBody.

        依赖id列表

        :param depend_list: The depend_list of this UpdateFunctionCodeRequestBody.
        :type depend_list: list[str]
        """
        self._depend_list = depend_list

    @property
    def depend_version_list(self):
        """Gets the depend_version_list of this UpdateFunctionCodeRequestBody.

        依赖版本id列表

        :return: The depend_version_list of this UpdateFunctionCodeRequestBody.
        :rtype: list[str]
        """
        return self._depend_version_list

    @depend_version_list.setter
    def depend_version_list(self, depend_version_list):
        """Sets the depend_version_list of this UpdateFunctionCodeRequestBody.

        依赖版本id列表

        :param depend_version_list: The depend_version_list of this UpdateFunctionCodeRequestBody.
        :type depend_version_list: list[str]
        """
        self._depend_version_list = depend_version_list

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
        if not isinstance(other, UpdateFunctionCodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
