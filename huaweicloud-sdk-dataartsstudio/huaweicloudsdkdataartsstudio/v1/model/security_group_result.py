# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'DiagnoseResult',
        'security_group': 'list[SecurityGroupStatus]'
    }

    attribute_map = {
        'result': 'result',
        'security_group': 'security_group'
    }

    def __init__(self, result=None, security_group=None):
        """SecurityGroupResult

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        :param security_group: kerberos信息
        :type security_group: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupStatus`]
        """
        
        

        self._result = None
        self._security_group = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if security_group is not None:
            self.security_group = security_group

    @property
    def result(self):
        """Gets the result of this SecurityGroupResult.

        :return: The result of this SecurityGroupResult.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SecurityGroupResult.

        :param result: The result of this SecurityGroupResult.
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        self._result = result

    @property
    def security_group(self):
        """Gets the security_group of this SecurityGroupResult.

        kerberos信息

        :return: The security_group of this SecurityGroupResult.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupStatus`]
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this SecurityGroupResult.

        kerberos信息

        :param security_group: The security_group of this SecurityGroupResult.
        :type security_group: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityGroupStatus`]
        """
        self._security_group = security_group

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
        if not isinstance(other, SecurityGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
