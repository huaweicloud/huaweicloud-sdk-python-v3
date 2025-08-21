# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisableControlOperateReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'target_identifier': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'target_identifier': 'target_identifier'
    }

    def __init__(self, identifier=None, target_identifier=None):
        r"""DisableControlOperateReqBody

        The model defined in huaweicloud sdk

        :param identifier: 控制策略ID。
        :type identifier: str
        :param target_identifier: 组织单元的ID信息。
        :type target_identifier: str
        """
        
        

        self._identifier = None
        self._target_identifier = None
        self.discriminator = None

        self.identifier = identifier
        self.target_identifier = target_identifier

    @property
    def identifier(self):
        r"""Gets the identifier of this DisableControlOperateReqBody.

        控制策略ID。

        :return: The identifier of this DisableControlOperateReqBody.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this DisableControlOperateReqBody.

        控制策略ID。

        :param identifier: The identifier of this DisableControlOperateReqBody.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def target_identifier(self):
        r"""Gets the target_identifier of this DisableControlOperateReqBody.

        组织单元的ID信息。

        :return: The target_identifier of this DisableControlOperateReqBody.
        :rtype: str
        """
        return self._target_identifier

    @target_identifier.setter
    def target_identifier(self, target_identifier):
        r"""Sets the target_identifier of this DisableControlOperateReqBody.

        组织单元的ID信息。

        :param target_identifier: The target_identifier of this DisableControlOperateReqBody.
        :type target_identifier: str
        """
        self._target_identifier = target_identifier

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
        if not isinstance(other, DisableControlOperateReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
