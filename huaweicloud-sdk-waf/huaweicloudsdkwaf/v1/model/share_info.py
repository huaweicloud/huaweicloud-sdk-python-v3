# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_count': 'int',
        'accept_count': 'int',
        'process_status': 'int'
    }

    attribute_map = {
        'share_count': 'share_count',
        'accept_count': 'accept_count',
        'process_status': 'process_status'
    }

    def __init__(self, share_count=None, accept_count=None, process_status=None):
        """ShareInfo

        The model defined in huaweicloud sdk

        :param share_count: 共享用户数
        :type share_count: int
        :param accept_count: 接受用户数
        :type accept_count: int
        :param process_status: 处理状态
        :type process_status: int
        """
        
        

        self._share_count = None
        self._accept_count = None
        self._process_status = None
        self.discriminator = None

        if share_count is not None:
            self.share_count = share_count
        if accept_count is not None:
            self.accept_count = accept_count
        if process_status is not None:
            self.process_status = process_status

    @property
    def share_count(self):
        """Gets the share_count of this ShareInfo.

        共享用户数

        :return: The share_count of this ShareInfo.
        :rtype: int
        """
        return self._share_count

    @share_count.setter
    def share_count(self, share_count):
        """Sets the share_count of this ShareInfo.

        共享用户数

        :param share_count: The share_count of this ShareInfo.
        :type share_count: int
        """
        self._share_count = share_count

    @property
    def accept_count(self):
        """Gets the accept_count of this ShareInfo.

        接受用户数

        :return: The accept_count of this ShareInfo.
        :rtype: int
        """
        return self._accept_count

    @accept_count.setter
    def accept_count(self, accept_count):
        """Sets the accept_count of this ShareInfo.

        接受用户数

        :param accept_count: The accept_count of this ShareInfo.
        :type accept_count: int
        """
        self._accept_count = accept_count

    @property
    def process_status(self):
        """Gets the process_status of this ShareInfo.

        处理状态

        :return: The process_status of this ShareInfo.
        :rtype: int
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this ShareInfo.

        处理状态

        :param process_status: The process_status of this ShareInfo.
        :type process_status: int
        """
        self._process_status = process_status

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
        if not isinstance(other, ShareInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
