# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioOutputHosting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'obs': 'AudioOutputHostingObs',
        'result_json_overdue_at': 'str',
        'check_obs_after_end_state': 'bool'
    }

    attribute_map = {
        'obs': 'obs',
        'result_json_overdue_at': 'result_json_overdue_at',
        'check_obs_after_end_state': 'check_obs_after_end_state'
    }

    def __init__(self, obs=None, result_json_overdue_at=None, check_obs_after_end_state=None):
        """AudioOutputHosting

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputHostingObs`
        :param result_json_overdue_at: 托管文件result.json的过期日期，文件默认保存48小时。  result.json文件生成且未过期时，会有这个字段。 
        :type result_json_overdue_at: str
        :param check_obs_after_end_state: True表示校验obs。
        :type check_obs_after_end_state: bool
        """
        
        

        self._obs = None
        self._result_json_overdue_at = None
        self._check_obs_after_end_state = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if result_json_overdue_at is not None:
            self.result_json_overdue_at = result_json_overdue_at
        if check_obs_after_end_state is not None:
            self.check_obs_after_end_state = check_obs_after_end_state

    @property
    def obs(self):
        """Gets the obs of this AudioOutputHosting.


        :return: The obs of this AudioOutputHosting.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioOutputHostingObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this AudioOutputHosting.


        :param obs: The obs of this AudioOutputHosting.
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputHostingObs`
        """
        self._obs = obs

    @property
    def result_json_overdue_at(self):
        """Gets the result_json_overdue_at of this AudioOutputHosting.

        托管文件result.json的过期日期，文件默认保存48小时。  result.json文件生成且未过期时，会有这个字段。 

        :return: The result_json_overdue_at of this AudioOutputHosting.
        :rtype: str
        """
        return self._result_json_overdue_at

    @result_json_overdue_at.setter
    def result_json_overdue_at(self, result_json_overdue_at):
        """Sets the result_json_overdue_at of this AudioOutputHosting.

        托管文件result.json的过期日期，文件默认保存48小时。  result.json文件生成且未过期时，会有这个字段。 

        :param result_json_overdue_at: The result_json_overdue_at of this AudioOutputHosting.
        :type result_json_overdue_at: str
        """
        self._result_json_overdue_at = result_json_overdue_at

    @property
    def check_obs_after_end_state(self):
        """Gets the check_obs_after_end_state of this AudioOutputHosting.

        True表示校验obs。

        :return: The check_obs_after_end_state of this AudioOutputHosting.
        :rtype: bool
        """
        return self._check_obs_after_end_state

    @check_obs_after_end_state.setter
    def check_obs_after_end_state(self, check_obs_after_end_state):
        """Sets the check_obs_after_end_state of this AudioOutputHosting.

        True表示校验obs。

        :param check_obs_after_end_state: The check_obs_after_end_state of this AudioOutputHosting.
        :type check_obs_after_end_state: bool
        """
        self._check_obs_after_end_state = check_obs_after_end_state

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
        if not isinstance(other, AudioOutputHosting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
