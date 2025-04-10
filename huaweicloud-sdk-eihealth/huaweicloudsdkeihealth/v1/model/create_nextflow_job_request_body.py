# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNextflowJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'workflow_id': 'str',
        'params': 'file',
        'priority': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'workflow_id': 'workflow_id',
        'params': 'params',
        'priority': 'priority'
    }

    def __init__(self, name=None, description=None, labels=None, workflow_id=None, params=None, priority=None):
        r"""CreateNextflowJobRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 作业的描述,取值范围：输入字符最大长度为255
        :type description: str
        :param labels: 作业标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。
        :type labels: list[str]
        :param workflow_id: 作业依赖的流程id
        :type workflow_id: str
        :param params: 流程参数列表文件，取值范围[0, 10M]
        :type params: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param priority: 作业的优先级,取值范围[0,9]，0最低，默认数值0
        :type priority: int
        """
        
        

        self._name = None
        self._description = None
        self._labels = None
        self._workflow_id = None
        self._params = None
        self._priority = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.workflow_id = workflow_id
        if params is not None:
            self.params = params
        if priority is not None:
            self.priority = priority

    @property
    def name(self):
        r"""Gets the name of this CreateNextflowJobRequestBody.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this CreateNextflowJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateNextflowJobRequestBody.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this CreateNextflowJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateNextflowJobRequestBody.

        作业的描述,取值范围：输入字符最大长度为255

        :return: The description of this CreateNextflowJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateNextflowJobRequestBody.

        作业的描述,取值范围：输入字符最大长度为255

        :param description: The description of this CreateNextflowJobRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this CreateNextflowJobRequestBody.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :return: The labels of this CreateNextflowJobRequestBody.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateNextflowJobRequestBody.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :param labels: The labels of this CreateNextflowJobRequestBody.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CreateNextflowJobRequestBody.

        作业依赖的流程id

        :return: The workflow_id of this CreateNextflowJobRequestBody.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CreateNextflowJobRequestBody.

        作业依赖的流程id

        :param workflow_id: The workflow_id of this CreateNextflowJobRequestBody.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def params(self):
        r"""Gets the params of this CreateNextflowJobRequestBody.

        流程参数列表文件，取值范围[0, 10M]

        :return: The params of this CreateNextflowJobRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateNextflowJobRequestBody.

        流程参数列表文件，取值范围[0, 10M]

        :param params: The params of this CreateNextflowJobRequestBody.
        :type params: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._params = params

    @property
    def priority(self):
        r"""Gets the priority of this CreateNextflowJobRequestBody.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :return: The priority of this CreateNextflowJobRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateNextflowJobRequestBody.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :param priority: The priority of this CreateNextflowJobRequestBody.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, CreateNextflowJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
