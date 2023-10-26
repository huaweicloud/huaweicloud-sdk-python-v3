# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackendTargetInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'target_id': 'target_id'
    }

    def __init__(self, share_id=None, target_id=None):
        """ShowBackendTargetInfoRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统id
        :type share_id: str
        :param target_id: 数据存储库 id
        :type target_id: str
        """
        
        

        self._share_id = None
        self._target_id = None
        self.discriminator = None

        self.share_id = share_id
        self.target_id = target_id

    @property
    def share_id(self):
        """Gets the share_id of this ShowBackendTargetInfoRequest.

        文件系统id

        :return: The share_id of this ShowBackendTargetInfoRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this ShowBackendTargetInfoRequest.

        文件系统id

        :param share_id: The share_id of this ShowBackendTargetInfoRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def target_id(self):
        """Gets the target_id of this ShowBackendTargetInfoRequest.

        数据存储库 id

        :return: The target_id of this ShowBackendTargetInfoRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ShowBackendTargetInfoRequest.

        数据存储库 id

        :param target_id: The target_id of this ShowBackendTargetInfoRequest.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, ShowBackendTargetInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
