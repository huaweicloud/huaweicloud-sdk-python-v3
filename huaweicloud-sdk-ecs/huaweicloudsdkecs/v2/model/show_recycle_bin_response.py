# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecycleBinResponse(SdkResponse):

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
        'switch': 'str',
        'policy': 'RecycleBinPolicys'
    }

    attribute_map = {
        'project_id': 'project_id',
        'switch': 'switch',
        'policy': 'policy'
    }

    def __init__(self, project_id=None, switch=None, policy=None):
        r"""ShowRecycleBinResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param switch: 回收站配置开关
        :type switch: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkecs.v2.RecycleBinPolicys`
        """
        
        super(ShowRecycleBinResponse, self).__init__()

        self._project_id = None
        self._switch = None
        self._policy = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if switch is not None:
            self.switch = switch
        if policy is not None:
            self.policy = policy

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowRecycleBinResponse.

        项目ID

        :return: The project_id of this ShowRecycleBinResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowRecycleBinResponse.

        项目ID

        :param project_id: The project_id of this ShowRecycleBinResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def switch(self):
        r"""Gets the switch of this ShowRecycleBinResponse.

        回收站配置开关

        :return: The switch of this ShowRecycleBinResponse.
        :rtype: str
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        r"""Sets the switch of this ShowRecycleBinResponse.

        回收站配置开关

        :param switch: The switch of this ShowRecycleBinResponse.
        :type switch: str
        """
        self._switch = switch

    @property
    def policy(self):
        r"""Gets the policy of this ShowRecycleBinResponse.

        :return: The policy of this ShowRecycleBinResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.RecycleBinPolicys`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ShowRecycleBinResponse.

        :param policy: The policy of this ShowRecycleBinResponse.
        :type policy: :class:`huaweicloudsdkecs.v2.RecycleBinPolicys`
        """
        self._policy = policy

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
        if not isinstance(other, ShowRecycleBinResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
