# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'secret': 'CreateUpdateSecretRespSecret'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'secret': 'secret'
    }

    def __init__(self, workspace_id=None, secret=None):
        """UpdateSecretResponse

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param secret: 
        :type secret: :class:`huaweicloudsdkhilens.v3.CreateUpdateSecretRespSecret`
        """
        
        super(UpdateSecretResponse, self).__init__()

        self._workspace_id = None
        self._secret = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if secret is not None:
            self.secret = secret

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UpdateSecretResponse.

        工作空间ID

        :return: The workspace_id of this UpdateSecretResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UpdateSecretResponse.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateSecretResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def secret(self):
        """Gets the secret of this UpdateSecretResponse.

        :return: The secret of this UpdateSecretResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateUpdateSecretRespSecret`
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this UpdateSecretResponse.

        :param secret: The secret of this UpdateSecretResponse.
        :type secret: :class:`huaweicloudsdkhilens.v3.CreateUpdateSecretRespSecret`
        """
        self._secret = secret

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
        if not isinstance(other, UpdateSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
