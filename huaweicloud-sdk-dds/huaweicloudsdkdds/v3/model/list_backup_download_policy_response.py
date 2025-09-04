# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupDownloadPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'id': 'id',
        'action': 'action'
    }

    def __init__(self, id=None, action=None):
        r"""ListBackupDownloadPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 备份下载策略id。
        :type id: str
        :param action: 备份下载开关。open表示打开备份下载开关，允许外网下载。close表示关闭备份下载开关，不允许外网下载。
        :type action: str
        """
        
        super(ListBackupDownloadPolicyResponse, self).__init__()

        self._id = None
        self._action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action is not None:
            self.action = action

    @property
    def id(self):
        r"""Gets the id of this ListBackupDownloadPolicyResponse.

        备份下载策略id。

        :return: The id of this ListBackupDownloadPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListBackupDownloadPolicyResponse.

        备份下载策略id。

        :param id: The id of this ListBackupDownloadPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def action(self):
        r"""Gets the action of this ListBackupDownloadPolicyResponse.

        备份下载开关。open表示打开备份下载开关，允许外网下载。close表示关闭备份下载开关，不允许外网下载。

        :return: The action of this ListBackupDownloadPolicyResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListBackupDownloadPolicyResponse.

        备份下载开关。open表示打开备份下载开关，允许外网下载。close表示关闭备份下载开关，不允许外网下载。

        :param action: The action of this ListBackupDownloadPolicyResponse.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ListBackupDownloadPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
