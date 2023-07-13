# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigMapResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configmap': 'ConfigMap',
        'workspace_id': 'str'
    }

    attribute_map = {
        'configmap': 'configmap',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, configmap=None, workspace_id=None):
        """ShowConfigMapResponse

        The model defined in huaweicloud sdk

        :param configmap: 
        :type configmap: :class:`huaweicloudsdkhilens.v3.ConfigMap`
        :param workspace_id: 工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID
        :type workspace_id: str
        """
        
        super(ShowConfigMapResponse, self).__init__()

        self._configmap = None
        self._workspace_id = None
        self.discriminator = None

        if configmap is not None:
            self.configmap = configmap
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def configmap(self):
        """Gets the configmap of this ShowConfigMapResponse.

        :return: The configmap of this ShowConfigMapResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.ConfigMap`
        """
        return self._configmap

    @configmap.setter
    def configmap(self, configmap):
        """Sets the configmap of this ShowConfigMapResponse.

        :param configmap: The configmap of this ShowConfigMapResponse.
        :type configmap: :class:`huaweicloudsdkhilens.v3.ConfigMap`
        """
        self._configmap = configmap

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ShowConfigMapResponse.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :return: The workspace_id of this ShowConfigMapResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ShowConfigMapResponse.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :param workspace_id: The workspace_id of this ShowConfigMapResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ShowConfigMapResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
