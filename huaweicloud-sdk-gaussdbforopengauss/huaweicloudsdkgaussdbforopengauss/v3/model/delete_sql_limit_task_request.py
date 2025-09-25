# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSqlLimitTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'instance_id': 'str',
        'x_language': 'str',
        'body': 'DeleteSqlLimitTaskRequestBody'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, task_id=None, instance_id=None, x_language=None, body=None):
        r"""DeleteSqlLimitTaskRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**: 限流任务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type task_id: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param body: Body of the DeleteSqlLimitTaskRequest
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteSqlLimitTaskRequestBody`
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.task_id = task_id
        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def task_id(self):
        r"""Gets the task_id of this DeleteSqlLimitTaskRequest.

        **参数解释**: 限流任务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The task_id of this DeleteSqlLimitTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DeleteSqlLimitTaskRequest.

        **参数解释**: 限流任务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param task_id: The task_id of this DeleteSqlLimitTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteSqlLimitTaskRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this DeleteSqlLimitTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteSqlLimitTaskRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this DeleteSqlLimitTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this DeleteSqlLimitTaskRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this DeleteSqlLimitTaskRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DeleteSqlLimitTaskRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this DeleteSqlLimitTaskRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this DeleteSqlLimitTaskRequest.

        :return: The body of this DeleteSqlLimitTaskRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteSqlLimitTaskRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteSqlLimitTaskRequest.

        :param body: The body of this DeleteSqlLimitTaskRequest.
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteSqlLimitTaskRequestBody`
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
        if not isinstance(other, DeleteSqlLimitTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
