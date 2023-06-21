# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JudgementTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notify_url': 'str',
        'code_type': 'str',
        'source_code': 'str',
        'description': 'str',
        'runtime_type': 'str',
        'timeout': 'int',
        'output_type': 'str',
        'testcases': 'list[JudgementCaseInfo]'
    }

    attribute_map = {
        'notify_url': 'notify_url',
        'code_type': 'code_type',
        'source_code': 'source_code',
        'description': 'description',
        'runtime_type': 'runtime_type',
        'timeout': 'timeout',
        'output_type': 'output_type',
        'testcases': 'testcases'
    }

    def __init__(self, notify_url=None, code_type=None, source_code=None, description=None, runtime_type=None, timeout=None, output_type=None, testcases=None):
        """JudgementTaskRequestBody

        The model defined in huaweicloud sdk

        :param notify_url: 第三方指定的判题结果回调url，取值来源于伙伴通道“判题管理配置”-“接口管理”中设置的回调地址相同
        :type notify_url: str
        :param code_type: 代码来源：inline（源代码）
        :type code_type: str
        :param source_code: 源代码，需Base64编码
        :type source_code: str
        :param description: 任务描述
        :type description: str
        :param runtime_type: 支持语言类型：java、c、cpp、python、javaScript
        :type runtime_type: str
        :param timeout: 代码运行超时时间，单位为秒
        :type timeout: int
        :param output_type: 结果返回类型：sysout（标准输出）、fileout（以文件形式输出）、imgout（以图片形式输出）、caseout（用例运行返回）、judgeout（用例对比返回）
        :type output_type: str
        :param testcases: 当判题结果类型是caseout和judgeout类型才需要传的字段，表示用例数据
        :type testcases: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseInfo`]
        """
        
        

        self._notify_url = None
        self._code_type = None
        self._source_code = None
        self._description = None
        self._runtime_type = None
        self._timeout = None
        self._output_type = None
        self._testcases = None
        self.discriminator = None

        self.notify_url = notify_url
        self.code_type = code_type
        self.source_code = source_code
        if description is not None:
            self.description = description
        self.runtime_type = runtime_type
        if timeout is not None:
            self.timeout = timeout
        self.output_type = output_type
        if testcases is not None:
            self.testcases = testcases

    @property
    def notify_url(self):
        """Gets the notify_url of this JudgementTaskRequestBody.

        第三方指定的判题结果回调url，取值来源于伙伴通道“判题管理配置”-“接口管理”中设置的回调地址相同

        :return: The notify_url of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this JudgementTaskRequestBody.

        第三方指定的判题结果回调url，取值来源于伙伴通道“判题管理配置”-“接口管理”中设置的回调地址相同

        :param notify_url: The notify_url of this JudgementTaskRequestBody.
        :type notify_url: str
        """
        self._notify_url = notify_url

    @property
    def code_type(self):
        """Gets the code_type of this JudgementTaskRequestBody.

        代码来源：inline（源代码）

        :return: The code_type of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this JudgementTaskRequestBody.

        代码来源：inline（源代码）

        :param code_type: The code_type of this JudgementTaskRequestBody.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def source_code(self):
        """Gets the source_code of this JudgementTaskRequestBody.

        源代码，需Base64编码

        :return: The source_code of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this JudgementTaskRequestBody.

        源代码，需Base64编码

        :param source_code: The source_code of this JudgementTaskRequestBody.
        :type source_code: str
        """
        self._source_code = source_code

    @property
    def description(self):
        """Gets the description of this JudgementTaskRequestBody.

        任务描述

        :return: The description of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JudgementTaskRequestBody.

        任务描述

        :param description: The description of this JudgementTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def runtime_type(self):
        """Gets the runtime_type of this JudgementTaskRequestBody.

        支持语言类型：java、c、cpp、python、javaScript

        :return: The runtime_type of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this JudgementTaskRequestBody.

        支持语言类型：java、c、cpp、python、javaScript

        :param runtime_type: The runtime_type of this JudgementTaskRequestBody.
        :type runtime_type: str
        """
        self._runtime_type = runtime_type

    @property
    def timeout(self):
        """Gets the timeout of this JudgementTaskRequestBody.

        代码运行超时时间，单位为秒

        :return: The timeout of this JudgementTaskRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this JudgementTaskRequestBody.

        代码运行超时时间，单位为秒

        :param timeout: The timeout of this JudgementTaskRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_type(self):
        """Gets the output_type of this JudgementTaskRequestBody.

        结果返回类型：sysout（标准输出）、fileout（以文件形式输出）、imgout（以图片形式输出）、caseout（用例运行返回）、judgeout（用例对比返回）

        :return: The output_type of this JudgementTaskRequestBody.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """Sets the output_type of this JudgementTaskRequestBody.

        结果返回类型：sysout（标准输出）、fileout（以文件形式输出）、imgout（以图片形式输出）、caseout（用例运行返回）、judgeout（用例对比返回）

        :param output_type: The output_type of this JudgementTaskRequestBody.
        :type output_type: str
        """
        self._output_type = output_type

    @property
    def testcases(self):
        """Gets the testcases of this JudgementTaskRequestBody.

        当判题结果类型是caseout和judgeout类型才需要传的字段，表示用例数据

        :return: The testcases of this JudgementTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseInfo`]
        """
        return self._testcases

    @testcases.setter
    def testcases(self, testcases):
        """Sets the testcases of this JudgementTaskRequestBody.

        当判题结果类型是caseout和judgeout类型才需要传的字段，表示用例数据

        :param testcases: The testcases of this JudgementTaskRequestBody.
        :type testcases: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseInfo`]
        """
        self._testcases = testcases

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
        if not isinstance(other, JudgementTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
