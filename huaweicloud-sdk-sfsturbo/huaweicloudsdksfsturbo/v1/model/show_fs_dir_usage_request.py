# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFsDirUsageRequest:

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
        'path': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'path': 'path'
    }

    def __init__(self, share_id=None, path=None):
        r"""ShowFsDirUsageRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统id
        :type share_id: str
        :param path: 文件系统内合法的目录全路径
        :type path: str
        """
        
        

        self._share_id = None
        self._path = None
        self.discriminator = None

        self.share_id = share_id
        self.path = path

    @property
    def share_id(self):
        r"""Gets the share_id of this ShowFsDirUsageRequest.

        文件系统id

        :return: The share_id of this ShowFsDirUsageRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ShowFsDirUsageRequest.

        文件系统id

        :param share_id: The share_id of this ShowFsDirUsageRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def path(self):
        r"""Gets the path of this ShowFsDirUsageRequest.

        文件系统内合法的目录全路径

        :return: The path of this ShowFsDirUsageRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowFsDirUsageRequest.

        文件系统内合法的目录全路径

        :param path: The path of this ShowFsDirUsageRequest.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ShowFsDirUsageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
