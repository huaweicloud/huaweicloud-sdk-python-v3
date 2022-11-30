# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppliedHistoriesResult:

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
        'instance_name': 'str',
        'apply_result': 'str',
        'applied_at': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'apply_result': 'apply_result',
        'applied_at': 'applied_at',
        'error_code': 'error_code'
    }

    def __init__(self, instance_id=None, instance_name=None, apply_result=None, applied_at=None, error_code=None):
        """AppliedHistoriesResult

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param apply_result: 应用状态 (SUCCESS | FAILED)。
        :type apply_result: str
        :param applied_at: 应用时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type applied_at: str
        :param error_code: 失败原因错误码，如DBS.280005。
        :type error_code: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._apply_result = None
        self._applied_at = None
        self._error_code = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.apply_result = apply_result
        self.applied_at = applied_at
        self.error_code = error_code

    @property
    def instance_id(self):
        """Gets the instance_id of this AppliedHistoriesResult.

        实例ID。

        :return: The instance_id of this AppliedHistoriesResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AppliedHistoriesResult.

        实例ID。

        :param instance_id: The instance_id of this AppliedHistoriesResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this AppliedHistoriesResult.

        实例名称。

        :return: The instance_name of this AppliedHistoriesResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this AppliedHistoriesResult.

        实例名称。

        :param instance_name: The instance_name of this AppliedHistoriesResult.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def apply_result(self):
        """Gets the apply_result of this AppliedHistoriesResult.

        应用状态 (SUCCESS | FAILED)。

        :return: The apply_result of this AppliedHistoriesResult.
        :rtype: str
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        """Sets the apply_result of this AppliedHistoriesResult.

        应用状态 (SUCCESS | FAILED)。

        :param apply_result: The apply_result of this AppliedHistoriesResult.
        :type apply_result: str
        """
        self._apply_result = apply_result

    @property
    def applied_at(self):
        """Gets the applied_at of this AppliedHistoriesResult.

        应用时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The applied_at of this AppliedHistoriesResult.
        :rtype: str
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        """Sets the applied_at of this AppliedHistoriesResult.

        应用时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param applied_at: The applied_at of this AppliedHistoriesResult.
        :type applied_at: str
        """
        self._applied_at = applied_at

    @property
    def error_code(self):
        """Gets the error_code of this AppliedHistoriesResult.

        失败原因错误码，如DBS.280005。

        :return: The error_code of this AppliedHistoriesResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AppliedHistoriesResult.

        失败原因错误码，如DBS.280005。

        :param error_code: The error_code of this AppliedHistoriesResult.
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
        if not isinstance(other, AppliedHistoriesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
