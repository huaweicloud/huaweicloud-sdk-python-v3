# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'league_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'job_id': 'str'
    }

    attribute_map = {
        'league_id': 'league_id',
        'limit': 'limit',
        'offset': 'offset',
        'job_id': 'job_id'
    }

    def __init__(self, league_id=None, limit=None, offset=None, job_id=None):
        """ListInstanceHistoryRequest

        The model defined in huaweicloud sdk

        :param league_id: 联盟id，最大32位，字母和数字组成
        :type league_id: str
        :param limit: 每页记录数，取值0-100
        :type limit: int
        :param offset: 记录数偏移量 
        :type offset: int
        :param job_id: 任务id，最大32位，字母和数字组成
        :type job_id: str
        """
        
        

        self._league_id = None
        self._limit = None
        self._offset = None
        self._job_id = None
        self.discriminator = None

        self.league_id = league_id
        self.limit = limit
        self.offset = offset
        if job_id is not None:
            self.job_id = job_id

    @property
    def league_id(self):
        """Gets the league_id of this ListInstanceHistoryRequest.

        联盟id，最大32位，字母和数字组成

        :return: The league_id of this ListInstanceHistoryRequest.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this ListInstanceHistoryRequest.

        联盟id，最大32位，字母和数字组成

        :param league_id: The league_id of this ListInstanceHistoryRequest.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def limit(self):
        """Gets the limit of this ListInstanceHistoryRequest.

        每页记录数，取值0-100

        :return: The limit of this ListInstanceHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstanceHistoryRequest.

        每页记录数，取值0-100

        :param limit: The limit of this ListInstanceHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstanceHistoryRequest.

        记录数偏移量 

        :return: The offset of this ListInstanceHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstanceHistoryRequest.

        记录数偏移量 

        :param offset: The offset of this ListInstanceHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def job_id(self):
        """Gets the job_id of this ListInstanceHistoryRequest.

        任务id，最大32位，字母和数字组成

        :return: The job_id of this ListInstanceHistoryRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListInstanceHistoryRequest.

        任务id，最大32位，字母和数字组成

        :param job_id: The job_id of this ListInstanceHistoryRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ListInstanceHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
