# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateApplyHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'target_name': 'str',
        'apply_result': 'str',
        'applied_at': 'float',
        'error_code': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'target_name': 'target_name',
        'apply_result': 'apply_result',
        'applied_at': 'applied_at',
        'error_code': 'error_code'
    }

    def __init__(self, target_id=None, target_name=None, apply_result=None, applied_at=None, error_code=None):
        """TemplateApplyHistory

        The model defined in huaweicloud sdk

        :param target_id: 应用实例ID。
        :type target_id: str
        :param target_name: 应用实例名称。
        :type target_name: str
        :param apply_result: 应用结果。
        :type apply_result: str
        :param applied_at: 应用时间。
        :type applied_at: float
        :param error_code: 错误码。
        :type error_code: str
        """
        
        

        self._target_id = None
        self._target_name = None
        self._apply_result = None
        self._applied_at = None
        self._error_code = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if target_name is not None:
            self.target_name = target_name
        if apply_result is not None:
            self.apply_result = apply_result
        if applied_at is not None:
            self.applied_at = applied_at
        if error_code is not None:
            self.error_code = error_code

    @property
    def target_id(self):
        """Gets the target_id of this TemplateApplyHistory.

        应用实例ID。

        :return: The target_id of this TemplateApplyHistory.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this TemplateApplyHistory.

        应用实例ID。

        :param target_id: The target_id of this TemplateApplyHistory.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """Gets the target_name of this TemplateApplyHistory.

        应用实例名称。

        :return: The target_name of this TemplateApplyHistory.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this TemplateApplyHistory.

        应用实例名称。

        :param target_name: The target_name of this TemplateApplyHistory.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def apply_result(self):
        """Gets the apply_result of this TemplateApplyHistory.

        应用结果。

        :return: The apply_result of this TemplateApplyHistory.
        :rtype: str
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        """Sets the apply_result of this TemplateApplyHistory.

        应用结果。

        :param apply_result: The apply_result of this TemplateApplyHistory.
        :type apply_result: str
        """
        self._apply_result = apply_result

    @property
    def applied_at(self):
        """Gets the applied_at of this TemplateApplyHistory.

        应用时间。

        :return: The applied_at of this TemplateApplyHistory.
        :rtype: float
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        """Sets the applied_at of this TemplateApplyHistory.

        应用时间。

        :param applied_at: The applied_at of this TemplateApplyHistory.
        :type applied_at: float
        """
        self._applied_at = applied_at

    @property
    def error_code(self):
        """Gets the error_code of this TemplateApplyHistory.

        错误码。

        :return: The error_code of this TemplateApplyHistory.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TemplateApplyHistory.

        错误码。

        :param error_code: The error_code of this TemplateApplyHistory.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, TemplateApplyHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
