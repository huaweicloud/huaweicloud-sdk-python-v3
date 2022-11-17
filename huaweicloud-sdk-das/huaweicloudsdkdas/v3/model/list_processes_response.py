# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProcessesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'processes': 'list[Process]',
        'count': 'int'
    }

    attribute_map = {
        'processes': 'processes',
        'count': 'count'
    }

    def __init__(self, processes=None, count=None):
        """ListProcessesResponse

        The model defined in huaweicloud sdk

        :param processes: 会话列表
        :type processes: list[:class:`huaweicloudsdkdas.v3.Process`]
        :param count: 总记录数
        :type count: int
        """
        
        super(ListProcessesResponse, self).__init__()

        self._processes = None
        self._count = None
        self.discriminator = None

        if processes is not None:
            self.processes = processes
        if count is not None:
            self.count = count

    @property
    def processes(self):
        """Gets the processes of this ListProcessesResponse.

        会话列表

        :return: The processes of this ListProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this ListProcessesResponse.

        会话列表

        :param processes: The processes of this ListProcessesResponse.
        :type processes: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        self._processes = processes

    @property
    def count(self):
        """Gets the count of this ListProcessesResponse.

        总记录数

        :return: The count of this ListProcessesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProcessesResponse.

        总记录数

        :param count: The count of this ListProcessesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListProcessesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
