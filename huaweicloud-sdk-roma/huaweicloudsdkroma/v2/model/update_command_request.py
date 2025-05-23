# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCommandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'service_id': 'str',
        'command_id': 'int',
        'body': 'UpdateCommandRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'service_id': 'service_id',
        'command_id': 'command_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, service_id=None, command_id=None, body=None):
        r"""UpdateCommandRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param service_id: 服务ID
        :type service_id: str
        :param command_id: 命令ID
        :type command_id: int
        :param body: Body of the UpdateCommandRequest
        :type body: :class:`huaweicloudsdkroma.v2.UpdateCommandRequestBody`
        """
        
        

        self._instance_id = None
        self._service_id = None
        self._command_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.service_id = service_id
        self.command_id = command_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateCommandRequest.

        实例ID

        :return: The instance_id of this UpdateCommandRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateCommandRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateCommandRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def service_id(self):
        r"""Gets the service_id of this UpdateCommandRequest.

        服务ID

        :return: The service_id of this UpdateCommandRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this UpdateCommandRequest.

        服务ID

        :param service_id: The service_id of this UpdateCommandRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def command_id(self):
        r"""Gets the command_id of this UpdateCommandRequest.

        命令ID

        :return: The command_id of this UpdateCommandRequest.
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this UpdateCommandRequest.

        命令ID

        :param command_id: The command_id of this UpdateCommandRequest.
        :type command_id: int
        """
        self._command_id = command_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCommandRequest.

        :return: The body of this UpdateCommandRequest.
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateCommandRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCommandRequest.

        :param body: The body of this UpdateCommandRequest.
        :type body: :class:`huaweicloudsdkroma.v2.UpdateCommandRequestBody`
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
        if not isinstance(other, UpdateCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
