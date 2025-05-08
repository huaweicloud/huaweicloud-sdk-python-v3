# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteDocumentRequsetBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'parameters': 'list[ExecuteDocumentRequsetBodyParameters]',
        'sys_tags': 'list[ExecuteDocumentRequsetBodySysTags]',
        'target_parameter_name': 'str',
        'targets': 'list[ExecuteDocumentRequsetBodyTargets]',
        'document_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'version': 'version',
        'parameters': 'parameters',
        'sys_tags': 'sys_tags',
        'target_parameter_name': 'target_parameter_name',
        'targets': 'targets',
        'document_type': 'document_type',
        'description': 'description'
    }

    def __init__(self, version=None, parameters=None, sys_tags=None, target_parameter_name=None, targets=None, document_type=None, description=None):
        r"""ExecuteDocumentRequsetBody

        The model defined in huaweicloud sdk

        :param version: 作业版本号，若不传则默认为最新版本
        :type version: str
        :param parameters: 全局参数
        :type parameters: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyParameters`]
        :param sys_tags: 系统标签列表
        :type sys_tags: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodySysTags`]
        :param target_parameter_name: 速率控制模式下，批量执行对象的参数名
        :type target_parameter_name: str
        :param targets: 与target_parameter_name搭配使用。选择实例化target_parameter_name参数的方式。
        :type targets: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyTargets`]
        :param document_type: 执行的作业类型
        :type document_type: str
        :param description: 执行描述
        :type description: str
        """
        
        

        self._version = None
        self._parameters = None
        self._sys_tags = None
        self._target_parameter_name = None
        self._targets = None
        self._document_type = None
        self._description = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if parameters is not None:
            self.parameters = parameters
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if target_parameter_name is not None:
            self.target_parameter_name = target_parameter_name
        if targets is not None:
            self.targets = targets
        if document_type is not None:
            self.document_type = document_type
        if description is not None:
            self.description = description

    @property
    def version(self):
        r"""Gets the version of this ExecuteDocumentRequsetBody.

        作业版本号，若不传则默认为最新版本

        :return: The version of this ExecuteDocumentRequsetBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ExecuteDocumentRequsetBody.

        作业版本号，若不传则默认为最新版本

        :param version: The version of this ExecuteDocumentRequsetBody.
        :type version: str
        """
        self._version = version

    @property
    def parameters(self):
        r"""Gets the parameters of this ExecuteDocumentRequsetBody.

        全局参数

        :return: The parameters of this ExecuteDocumentRequsetBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyParameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ExecuteDocumentRequsetBody.

        全局参数

        :param parameters: The parameters of this ExecuteDocumentRequsetBody.
        :type parameters: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyParameters`]
        """
        self._parameters = parameters

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ExecuteDocumentRequsetBody.

        系统标签列表

        :return: The sys_tags of this ExecuteDocumentRequsetBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodySysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ExecuteDocumentRequsetBody.

        系统标签列表

        :param sys_tags: The sys_tags of this ExecuteDocumentRequsetBody.
        :type sys_tags: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodySysTags`]
        """
        self._sys_tags = sys_tags

    @property
    def target_parameter_name(self):
        r"""Gets the target_parameter_name of this ExecuteDocumentRequsetBody.

        速率控制模式下，批量执行对象的参数名

        :return: The target_parameter_name of this ExecuteDocumentRequsetBody.
        :rtype: str
        """
        return self._target_parameter_name

    @target_parameter_name.setter
    def target_parameter_name(self, target_parameter_name):
        r"""Sets the target_parameter_name of this ExecuteDocumentRequsetBody.

        速率控制模式下，批量执行对象的参数名

        :param target_parameter_name: The target_parameter_name of this ExecuteDocumentRequsetBody.
        :type target_parameter_name: str
        """
        self._target_parameter_name = target_parameter_name

    @property
    def targets(self):
        r"""Gets the targets of this ExecuteDocumentRequsetBody.

        与target_parameter_name搭配使用。选择实例化target_parameter_name参数的方式。

        :return: The targets of this ExecuteDocumentRequsetBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyTargets`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this ExecuteDocumentRequsetBody.

        与target_parameter_name搭配使用。选择实例化target_parameter_name参数的方式。

        :param targets: The targets of this ExecuteDocumentRequsetBody.
        :type targets: list[:class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequsetBodyTargets`]
        """
        self._targets = targets

    @property
    def document_type(self):
        r"""Gets the document_type of this ExecuteDocumentRequsetBody.

        执行的作业类型

        :return: The document_type of this ExecuteDocumentRequsetBody.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        r"""Sets the document_type of this ExecuteDocumentRequsetBody.

        执行的作业类型

        :param document_type: The document_type of this ExecuteDocumentRequsetBody.
        :type document_type: str
        """
        self._document_type = document_type

    @property
    def description(self):
        r"""Gets the description of this ExecuteDocumentRequsetBody.

        执行描述

        :return: The description of this ExecuteDocumentRequsetBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExecuteDocumentRequsetBody.

        执行描述

        :param description: The description of this ExecuteDocumentRequsetBody.
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
        if not isinstance(other, ExecuteDocumentRequsetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
