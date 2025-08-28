# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleBinResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'policy': 'RecycleBinPolicy',
        'enable': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'policy': 'policy',
        'enable': 'enable'
    }

    def __init__(self, project_id=None, policy=None, enable=None):
        r"""RecycleBinResponseBody

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。
        :type project_id: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkelb.v3.RecycleBinPolicy`
        :param enable: **参数解释**：是否启用回收站。  **取值范围**： - true：启用回收站。 - false：不启用回收站。
        :type enable: bool
        """
        
        

        self._project_id = None
        self._policy = None
        self._enable = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if policy is not None:
            self.policy = policy
        if enable is not None:
            self.enable = enable

    @property
    def project_id(self):
        r"""Gets the project_id of this RecycleBinResponseBody.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :return: The project_id of this RecycleBinResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RecycleBinResponseBody.

        **参数解释**：项目ID。获取方式请参见[获取项目ID](elb_fl_0008.xml)。  **取值范围**：长度为32个字符，由小写字母和数字组成。

        :param project_id: The project_id of this RecycleBinResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def policy(self):
        r"""Gets the policy of this RecycleBinResponseBody.

        :return: The policy of this RecycleBinResponseBody.
        :rtype: :class:`huaweicloudsdkelb.v3.RecycleBinPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RecycleBinResponseBody.

        :param policy: The policy of this RecycleBinResponseBody.
        :type policy: :class:`huaweicloudsdkelb.v3.RecycleBinPolicy`
        """
        self._policy = policy

    @property
    def enable(self):
        r"""Gets the enable of this RecycleBinResponseBody.

        **参数解释**：是否启用回收站。  **取值范围**： - true：启用回收站。 - false：不启用回收站。

        :return: The enable of this RecycleBinResponseBody.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this RecycleBinResponseBody.

        **参数解释**：是否启用回收站。  **取值范围**： - true：启用回收站。 - false：不启用回收站。

        :param enable: The enable of this RecycleBinResponseBody.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, RecycleBinResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
