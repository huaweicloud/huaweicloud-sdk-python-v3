# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTriggerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'trigger': 'str',
        'body': 'UpdateTriggerRequestBody'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'trigger': 'trigger',
        'body': 'body'
    }

    def __init__(self, namespace=None, repository=None, trigger=None, body=None):
        r"""UpdateTriggerRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param trigger: 触发器名称
        :type trigger: str
        :param body: Body of the UpdateTriggerRequest
        :type body: :class:`huaweicloudsdkswr.v2.UpdateTriggerRequestBody`
        """
        
        

        self._namespace = None
        self._repository = None
        self._trigger = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.trigger = trigger
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateTriggerRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateTriggerRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this UpdateTriggerRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this UpdateTriggerRequest.

        镜像仓库名称

        :return: The repository of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this UpdateTriggerRequest.

        镜像仓库名称

        :param repository: The repository of this UpdateTriggerRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def trigger(self):
        r"""Gets the trigger of this UpdateTriggerRequest.

        触发器名称

        :return: The trigger of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this UpdateTriggerRequest.

        触发器名称

        :param trigger: The trigger of this UpdateTriggerRequest.
        :type trigger: str
        """
        self._trigger = trigger

    @property
    def body(self):
        r"""Gets the body of this UpdateTriggerRequest.

        :return: The body of this UpdateTriggerRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateTriggerRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTriggerRequest.

        :param body: The body of this UpdateTriggerRequest.
        :type body: :class:`huaweicloudsdkswr.v2.UpdateTriggerRequestBody`
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
        if not isinstance(other, UpdateTriggerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
