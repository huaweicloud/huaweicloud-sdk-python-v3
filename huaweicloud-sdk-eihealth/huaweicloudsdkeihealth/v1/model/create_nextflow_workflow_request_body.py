# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNextflowWorkflowRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_file': 'file',
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'main_file': 'str',
        'params': 'file'
    }

    attribute_map = {
        'workflow_file': 'workflow_file',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'main_file': 'main_file',
        'params': 'params'
    }

    def __init__(self, workflow_file=None, name=None, description=None, labels=None, main_file=None, params=None):
        r"""CreateNextflowWorkflowRequestBody

        The model defined in huaweicloud sdk

        :param workflow_file: 流程文件，文件大小[0,10M]
        :type workflow_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param name: 流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。
        :type name: str
        :param description: 流程描述 取值范围[0,65535]
        :type description: str
        :param labels: 流程标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。
        :type labels: list[str]
        :param main_file: 主文件名
        :type main_file: str
        :param params: 流程参数列表文件，取值范围[0, 10M]
        :type params: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._workflow_file = None
        self._name = None
        self._description = None
        self._labels = None
        self._main_file = None
        self._params = None
        self.discriminator = None

        self.workflow_file = workflow_file
        self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.main_file = main_file
        if params is not None:
            self.params = params

    @property
    def workflow_file(self):
        r"""Gets the workflow_file of this CreateNextflowWorkflowRequestBody.

        流程文件，文件大小[0,10M]

        :return: The workflow_file of this CreateNextflowWorkflowRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._workflow_file

    @workflow_file.setter
    def workflow_file(self, workflow_file):
        r"""Sets the workflow_file of this CreateNextflowWorkflowRequestBody.

        流程文件，文件大小[0,10M]

        :param workflow_file: The workflow_file of this CreateNextflowWorkflowRequestBody.
        :type workflow_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._workflow_file = workflow_file

    @property
    def name(self):
        r"""Gets the name of this CreateNextflowWorkflowRequestBody.

        流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。

        :return: The name of this CreateNextflowWorkflowRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateNextflowWorkflowRequestBody.

        流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。

        :param name: The name of this CreateNextflowWorkflowRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateNextflowWorkflowRequestBody.

        流程描述 取值范围[0,65535]

        :return: The description of this CreateNextflowWorkflowRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateNextflowWorkflowRequestBody.

        流程描述 取值范围[0,65535]

        :param description: The description of this CreateNextflowWorkflowRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this CreateNextflowWorkflowRequestBody.

        流程标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :return: The labels of this CreateNextflowWorkflowRequestBody.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateNextflowWorkflowRequestBody.

        流程标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :param labels: The labels of this CreateNextflowWorkflowRequestBody.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def main_file(self):
        r"""Gets the main_file of this CreateNextflowWorkflowRequestBody.

        主文件名

        :return: The main_file of this CreateNextflowWorkflowRequestBody.
        :rtype: str
        """
        return self._main_file

    @main_file.setter
    def main_file(self, main_file):
        r"""Sets the main_file of this CreateNextflowWorkflowRequestBody.

        主文件名

        :param main_file: The main_file of this CreateNextflowWorkflowRequestBody.
        :type main_file: str
        """
        self._main_file = main_file

    @property
    def params(self):
        r"""Gets the params of this CreateNextflowWorkflowRequestBody.

        流程参数列表文件，取值范围[0, 10M]

        :return: The params of this CreateNextflowWorkflowRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateNextflowWorkflowRequestBody.

        流程参数列表文件，取值范围[0, 10M]

        :param params: The params of this CreateNextflowWorkflowRequestBody.
        :type params: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._params = params

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
        if not isinstance(other, CreateNextflowWorkflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
