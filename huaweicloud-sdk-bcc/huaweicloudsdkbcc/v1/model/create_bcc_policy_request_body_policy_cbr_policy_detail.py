# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBccPolicyRequestBodyPolicyCbrPolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_definition': 'CreateBccPolicyRequestBodyPolicyCbrPolicyDetailOperationDefinition',
        'operation_type': 'str',
        'trigger': 'CreateBccPolicyRequestBodyPolicyCbrPolicyDetailTrigger'
    }

    attribute_map = {
        'operation_definition': 'operation_definition',
        'operation_type': 'operation_type',
        'trigger': 'trigger'
    }

    def __init__(self, operation_definition=None, operation_type=None, trigger=None):
        r"""CreateBccPolicyRequestBodyPolicyCbrPolicyDetail

        The model defined in huaweicloud sdk

        :param operation_definition: 
        :type operation_definition: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailOperationDefinition`
        :param operation_type: 保护类型,本地备份backup，异地复制replication
        :type operation_type: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailTrigger`
        """
        
        

        self._operation_definition = None
        self._operation_type = None
        self._trigger = None
        self.discriminator = None

        self.operation_definition = operation_definition
        self.operation_type = operation_type
        self.trigger = trigger

    @property
    def operation_definition(self):
        r"""Gets the operation_definition of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        :return: The operation_definition of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailOperationDefinition`
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        r"""Sets the operation_definition of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        :param operation_definition: The operation_definition of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :type operation_definition: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailOperationDefinition`
        """
        self._operation_definition = operation_definition

    @property
    def operation_type(self):
        r"""Gets the operation_type of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        保护类型,本地备份backup，异地复制replication

        :return: The operation_type of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        保护类型,本地备份backup，异地复制replication

        :param operation_type: The operation_type of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def trigger(self):
        r"""Gets the trigger of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        :return: The trigger of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailTrigger`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.

        :param trigger: The trigger of this CreateBccPolicyRequestBodyPolicyCbrPolicyDetail.
        :type trigger: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetailTrigger`
        """
        self._trigger = trigger

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
        if not isinstance(other, CreateBccPolicyRequestBodyPolicyCbrPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
