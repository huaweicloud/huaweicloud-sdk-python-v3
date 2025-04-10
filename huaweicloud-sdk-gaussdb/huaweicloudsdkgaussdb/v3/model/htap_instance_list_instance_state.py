# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapInstanceListInstanceState:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_status': 'str',
        'create_fail_error_code': 'str',
        'fail_message': 'str',
        'wait_restart_for_params': 'bool'
    }

    attribute_map = {
        'instance_status': 'instance_status',
        'create_fail_error_code': 'create_fail_error_code',
        'fail_message': 'fail_message',
        'wait_restart_for_params': 'wait_restart_for_params'
    }

    def __init__(self, instance_status=None, create_fail_error_code=None, fail_message=None, wait_restart_for_params=None):
        r"""HtapInstanceListInstanceState

        The model defined in huaweicloud sdk

        :param instance_status: HTAP实例状态。
        :type instance_status: str
        :param create_fail_error_code: HTAP实例创建失败错误码。
        :type create_fail_error_code: str
        :param fail_message: HTAP实例创建失败错误信息。
        :type fail_message: str
        :param wait_restart_for_params: 是否需要重启更新参数。
        :type wait_restart_for_params: bool
        """
        
        

        self._instance_status = None
        self._create_fail_error_code = None
        self._fail_message = None
        self._wait_restart_for_params = None
        self.discriminator = None

        if instance_status is not None:
            self.instance_status = instance_status
        if create_fail_error_code is not None:
            self.create_fail_error_code = create_fail_error_code
        if fail_message is not None:
            self.fail_message = fail_message
        if wait_restart_for_params is not None:
            self.wait_restart_for_params = wait_restart_for_params

    @property
    def instance_status(self):
        r"""Gets the instance_status of this HtapInstanceListInstanceState.

        HTAP实例状态。

        :return: The instance_status of this HtapInstanceListInstanceState.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this HtapInstanceListInstanceState.

        HTAP实例状态。

        :param instance_status: The instance_status of this HtapInstanceListInstanceState.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def create_fail_error_code(self):
        r"""Gets the create_fail_error_code of this HtapInstanceListInstanceState.

        HTAP实例创建失败错误码。

        :return: The create_fail_error_code of this HtapInstanceListInstanceState.
        :rtype: str
        """
        return self._create_fail_error_code

    @create_fail_error_code.setter
    def create_fail_error_code(self, create_fail_error_code):
        r"""Sets the create_fail_error_code of this HtapInstanceListInstanceState.

        HTAP实例创建失败错误码。

        :param create_fail_error_code: The create_fail_error_code of this HtapInstanceListInstanceState.
        :type create_fail_error_code: str
        """
        self._create_fail_error_code = create_fail_error_code

    @property
    def fail_message(self):
        r"""Gets the fail_message of this HtapInstanceListInstanceState.

        HTAP实例创建失败错误信息。

        :return: The fail_message of this HtapInstanceListInstanceState.
        :rtype: str
        """
        return self._fail_message

    @fail_message.setter
    def fail_message(self, fail_message):
        r"""Sets the fail_message of this HtapInstanceListInstanceState.

        HTAP实例创建失败错误信息。

        :param fail_message: The fail_message of this HtapInstanceListInstanceState.
        :type fail_message: str
        """
        self._fail_message = fail_message

    @property
    def wait_restart_for_params(self):
        r"""Gets the wait_restart_for_params of this HtapInstanceListInstanceState.

        是否需要重启更新参数。

        :return: The wait_restart_for_params of this HtapInstanceListInstanceState.
        :rtype: bool
        """
        return self._wait_restart_for_params

    @wait_restart_for_params.setter
    def wait_restart_for_params(self, wait_restart_for_params):
        r"""Sets the wait_restart_for_params of this HtapInstanceListInstanceState.

        是否需要重启更新参数。

        :param wait_restart_for_params: The wait_restart_for_params of this HtapInstanceListInstanceState.
        :type wait_restart_for_params: bool
        """
        self._wait_restart_for_params = wait_restart_for_params

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
        if not isinstance(other, HtapInstanceListInstanceState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
