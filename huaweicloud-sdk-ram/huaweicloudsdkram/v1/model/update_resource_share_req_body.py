# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceShareReqBody:

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
        'allow_external_principals': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'allow_external_principals': 'allow_external_principals'
    }

    def __init__(self, name=None, description=None, allow_external_principals=None):
        r"""UpdateResourceShareReqBody

        The model defined in huaweicloud sdk

        :param name: 资源共享实例的名称。
        :type name: str
        :param description: 资源共享实例的描述。
        :type description: str
        :param allow_external_principals: 资源共享实例是否支持共享给组织外账号。
        :type allow_external_principals: bool
        """
        
        

        self._name = None
        self._description = None
        self._allow_external_principals = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if allow_external_principals is not None:
            self.allow_external_principals = allow_external_principals

    @property
    def name(self):
        r"""Gets the name of this UpdateResourceShareReqBody.

        资源共享实例的名称。

        :return: The name of this UpdateResourceShareReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateResourceShareReqBody.

        资源共享实例的名称。

        :param name: The name of this UpdateResourceShareReqBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateResourceShareReqBody.

        资源共享实例的描述。

        :return: The description of this UpdateResourceShareReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateResourceShareReqBody.

        资源共享实例的描述。

        :param description: The description of this UpdateResourceShareReqBody.
        :type description: str
        """
        self._description = description

    @property
    def allow_external_principals(self):
        r"""Gets the allow_external_principals of this UpdateResourceShareReqBody.

        资源共享实例是否支持共享给组织外账号。

        :return: The allow_external_principals of this UpdateResourceShareReqBody.
        :rtype: bool
        """
        return self._allow_external_principals

    @allow_external_principals.setter
    def allow_external_principals(self, allow_external_principals):
        r"""Sets the allow_external_principals of this UpdateResourceShareReqBody.

        资源共享实例是否支持共享给组织外账号。

        :param allow_external_principals: The allow_external_principals of this UpdateResourceShareReqBody.
        :type allow_external_principals: bool
        """
        self._allow_external_principals = allow_external_principals

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
        if not isinstance(other, UpdateResourceShareReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
