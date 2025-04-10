# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicePolicyBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'policy_id': 'str',
        'policy_name': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, app_id=None, policy_id=None, policy_name=None, create_time=None, update_time=None):
        r"""ListDevicePolicyBase

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。
        :type app_id: str
        :param policy_id: 策略ID。
        :type policy_id: str
        :param policy_name: 策略名称。
        :type policy_name: str
        :param create_time: 在物联网平台创建策略的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        :param update_time: 在物联网平台更新策略的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type update_time: str
        """
        
        

        self._app_id = None
        self._policy_id = None
        self._policy_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_id(self):
        r"""Gets the app_id of this ListDevicePolicyBase.

        **参数说明**：资源空间ID。

        :return: The app_id of this ListDevicePolicyBase.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListDevicePolicyBase.

        **参数说明**：资源空间ID。

        :param app_id: The app_id of this ListDevicePolicyBase.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListDevicePolicyBase.

        策略ID。

        :return: The policy_id of this ListDevicePolicyBase.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListDevicePolicyBase.

        策略ID。

        :param policy_id: The policy_id of this ListDevicePolicyBase.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListDevicePolicyBase.

        策略名称。

        :return: The policy_name of this ListDevicePolicyBase.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListDevicePolicyBase.

        策略名称。

        :param policy_name: The policy_name of this ListDevicePolicyBase.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ListDevicePolicyBase.

        在物联网平台创建策略的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this ListDevicePolicyBase.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListDevicePolicyBase.

        在物联网平台创建策略的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this ListDevicePolicyBase.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListDevicePolicyBase.

        在物联网平台更新策略的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The update_time of this ListDevicePolicyBase.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListDevicePolicyBase.

        在物联网平台更新策略的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param update_time: The update_time of this ListDevicePolicyBase.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ListDevicePolicyBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
