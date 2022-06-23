# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'total': 'int',
        'sessions': 'list[ShowBatchJobDetailResp]',
        'create_time': 'int'
    }

    attribute_map = {
        '_from': 'from',
        'total': 'total',
        'sessions': 'sessions',
        'create_time': 'create_time'
    }

    def __init__(self, _from=None, total=None, sessions=None, create_time=None):
        """ListBatchesResponse

        The model defined in huaweicloud sdk

        :param _from: 起始批处理作业的索引号。
        :type _from: int
        :param total: 返回批处理作业的总数。
        :type total: int
        :param sessions: 批处理作业信息。
        :type sessions: list[:class:`huaweicloudsdkdli.v1.ShowBatchJobDetailResp`]
        :param create_time: 批处理作业的创建时间。
        :type create_time: int
        """
        
        super(ListBatchesResponse, self).__init__()

        self.__from = None
        self._total = None
        self._sessions = None
        self._create_time = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if total is not None:
            self.total = total
        if sessions is not None:
            self.sessions = sessions
        if create_time is not None:
            self.create_time = create_time

    @property
    def _from(self):
        """Gets the _from of this ListBatchesResponse.

        起始批处理作业的索引号。

        :return: The _from of this ListBatchesResponse.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListBatchesResponse.

        起始批处理作业的索引号。

        :param _from: The _from of this ListBatchesResponse.
        :type _from: int
        """
        self.__from = _from

    @property
    def total(self):
        """Gets the total of this ListBatchesResponse.

        返回批处理作业的总数。

        :return: The total of this ListBatchesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListBatchesResponse.

        返回批处理作业的总数。

        :param total: The total of this ListBatchesResponse.
        :type total: int
        """
        self._total = total

    @property
    def sessions(self):
        """Gets the sessions of this ListBatchesResponse.

        批处理作业信息。

        :return: The sessions of this ListBatchesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ShowBatchJobDetailResp`]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this ListBatchesResponse.

        批处理作业信息。

        :param sessions: The sessions of this ListBatchesResponse.
        :type sessions: list[:class:`huaweicloudsdkdli.v1.ShowBatchJobDetailResp`]
        """
        self._sessions = sessions

    @property
    def create_time(self):
        """Gets the create_time of this ListBatchesResponse.

        批处理作业的创建时间。

        :return: The create_time of this ListBatchesResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListBatchesResponse.

        批处理作业的创建时间。

        :param create_time: The create_time of this ListBatchesResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ListBatchesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
