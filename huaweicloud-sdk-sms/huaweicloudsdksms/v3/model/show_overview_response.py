# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'waiting': 'int',
        'replicating': 'int',
        'syncing': 'int',
        'other': 'int'
    }

    attribute_map = {
        'waiting': 'waiting',
        'replicating': 'replicating',
        'syncing': 'syncing',
        'other': 'other'
    }

    def __init__(self, waiting=None, replicating=None, syncing=None, other=None):
        """ShowOverviewResponse

        The model defined in huaweicloud sdk

        :param waiting: 等待中
        :type waiting: int
        :param replicating: 复制中
        :type replicating: int
        :param syncing: 同步中
        :type syncing: int
        :param other: 其它
        :type other: int
        """
        
        super(ShowOverviewResponse, self).__init__()

        self._waiting = None
        self._replicating = None
        self._syncing = None
        self._other = None
        self.discriminator = None

        if waiting is not None:
            self.waiting = waiting
        if replicating is not None:
            self.replicating = replicating
        if syncing is not None:
            self.syncing = syncing
        if other is not None:
            self.other = other

    @property
    def waiting(self):
        """Gets the waiting of this ShowOverviewResponse.

        等待中

        :return: The waiting of this ShowOverviewResponse.
        :rtype: int
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this ShowOverviewResponse.

        等待中

        :param waiting: The waiting of this ShowOverviewResponse.
        :type waiting: int
        """
        self._waiting = waiting

    @property
    def replicating(self):
        """Gets the replicating of this ShowOverviewResponse.

        复制中

        :return: The replicating of this ShowOverviewResponse.
        :rtype: int
        """
        return self._replicating

    @replicating.setter
    def replicating(self, replicating):
        """Sets the replicating of this ShowOverviewResponse.

        复制中

        :param replicating: The replicating of this ShowOverviewResponse.
        :type replicating: int
        """
        self._replicating = replicating

    @property
    def syncing(self):
        """Gets the syncing of this ShowOverviewResponse.

        同步中

        :return: The syncing of this ShowOverviewResponse.
        :rtype: int
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this ShowOverviewResponse.

        同步中

        :param syncing: The syncing of this ShowOverviewResponse.
        :type syncing: int
        """
        self._syncing = syncing

    @property
    def other(self):
        """Gets the other of this ShowOverviewResponse.

        其它

        :return: The other of this ShowOverviewResponse.
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this ShowOverviewResponse.

        其它

        :param other: The other of this ShowOverviewResponse.
        :type other: int
        """
        self._other = other

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
        if not isinstance(other, ShowOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
