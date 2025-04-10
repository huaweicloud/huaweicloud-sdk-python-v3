# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDependencyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'depend_file': 'str',
        'depend_link': 'str',
        'depend_type': 'str',
        'runtime': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'depend_file': 'depend_file',
        'depend_link': 'depend_link',
        'depend_type': 'depend_type',
        'runtime': 'runtime',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, depend_file=None, depend_link=None, depend_type=None, runtime=None, name=None, description=None):
        r"""CreateDependencyRequestBody

        The model defined in huaweicloud sdk

        :param depend_file: depend_type为zip类型时必填，为文件流格式,需要base64编码zip文件。上传的文件大小限制为40M，如超过40M，请通过OBS上传。
        :type depend_file: str
        :param depend_link: depend_type为obs类型时，依赖包在obs的存储地址。
        :type depend_link: str
        :param depend_type: 导入类型，目前支持obs和zip。
        :type depend_type: str
        :param runtime: FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。
        :type runtime: str
        :param name: 依赖包名称。必须以大、小写字母开头，以字母或数字结尾，只能由字母、数字、下划线、点和中划线组成，长度不超过96个字符。
        :type name: str
        :param description: 依赖包描述，不超过512个字符。
        :type description: str
        """
        
        

        self._depend_file = None
        self._depend_link = None
        self._depend_type = None
        self._runtime = None
        self._name = None
        self._description = None
        self.discriminator = None

        if depend_file is not None:
            self.depend_file = depend_file
        if depend_link is not None:
            self.depend_link = depend_link
        self.depend_type = depend_type
        self.runtime = runtime
        self.name = name
        if description is not None:
            self.description = description

    @property
    def depend_file(self):
        r"""Gets the depend_file of this CreateDependencyRequestBody.

        depend_type为zip类型时必填，为文件流格式,需要base64编码zip文件。上传的文件大小限制为40M，如超过40M，请通过OBS上传。

        :return: The depend_file of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._depend_file

    @depend_file.setter
    def depend_file(self, depend_file):
        r"""Sets the depend_file of this CreateDependencyRequestBody.

        depend_type为zip类型时必填，为文件流格式,需要base64编码zip文件。上传的文件大小限制为40M，如超过40M，请通过OBS上传。

        :param depend_file: The depend_file of this CreateDependencyRequestBody.
        :type depend_file: str
        """
        self._depend_file = depend_file

    @property
    def depend_link(self):
        r"""Gets the depend_link of this CreateDependencyRequestBody.

        depend_type为obs类型时，依赖包在obs的存储地址。

        :return: The depend_link of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._depend_link

    @depend_link.setter
    def depend_link(self, depend_link):
        r"""Sets the depend_link of this CreateDependencyRequestBody.

        depend_type为obs类型时，依赖包在obs的存储地址。

        :param depend_link: The depend_link of this CreateDependencyRequestBody.
        :type depend_link: str
        """
        self._depend_link = depend_link

    @property
    def depend_type(self):
        r"""Gets the depend_type of this CreateDependencyRequestBody.

        导入类型，目前支持obs和zip。

        :return: The depend_type of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._depend_type

    @depend_type.setter
    def depend_type(self, depend_type):
        r"""Sets the depend_type of this CreateDependencyRequestBody.

        导入类型，目前支持obs和zip。

        :param depend_type: The depend_type of this CreateDependencyRequestBody.
        :type depend_type: str
        """
        self._depend_type = depend_type

    @property
    def runtime(self):
        r"""Gets the runtime of this CreateDependencyRequestBody.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this CreateDependencyRequestBody.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this CreateDependencyRequestBody.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def name(self):
        r"""Gets the name of this CreateDependencyRequestBody.

        依赖包名称。必须以大、小写字母开头，以字母或数字结尾，只能由字母、数字、下划线、点和中划线组成，长度不超过96个字符。

        :return: The name of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDependencyRequestBody.

        依赖包名称。必须以大、小写字母开头，以字母或数字结尾，只能由字母、数字、下划线、点和中划线组成，长度不超过96个字符。

        :param name: The name of this CreateDependencyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateDependencyRequestBody.

        依赖包描述，不超过512个字符。

        :return: The description of this CreateDependencyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDependencyRequestBody.

        依赖包描述，不超过512个字符。

        :param description: The description of this CreateDependencyRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateDependencyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
