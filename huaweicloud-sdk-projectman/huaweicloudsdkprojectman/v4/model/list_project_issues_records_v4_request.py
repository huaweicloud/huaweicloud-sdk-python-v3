# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectIssuesRecordsV4Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'operated_time_interval': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'operated_time_interval': 'operated_time_interval'
    }

    def __init__(self, project_id=None, offset=None, limit=None, operated_time_interval=None):
        """ListProjectIssuesRecordsV4Request

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param offset: 偏移量 从0开始,offset是limit的整数倍，limit&#x3D;10,offset&#x3D;0,10,20...
        :type offset: int
        :param limit: 每页数量 最小1,最大100
        :type limit: int
        :param operated_time_interval: 变更工作项的时间(查询的起始时间,查询的结束时间)
        :type operated_time_interval: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._operated_time_interval = None
        self.discriminator = None

        self.project_id = project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if operated_time_interval is not None:
            self.operated_time_interval = operated_time_interval

    @property
    def project_id(self):
        """Gets the project_id of this ListProjectIssuesRecordsV4Request.

        devcloud项目的32位id

        :return: The project_id of this ListProjectIssuesRecordsV4Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListProjectIssuesRecordsV4Request.

        devcloud项目的32位id

        :param project_id: The project_id of this ListProjectIssuesRecordsV4Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        """Gets the offset of this ListProjectIssuesRecordsV4Request.

        偏移量 从0开始,offset是limit的整数倍，limit=10,offset=0,10,20...

        :return: The offset of this ListProjectIssuesRecordsV4Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectIssuesRecordsV4Request.

        偏移量 从0开始,offset是limit的整数倍，limit=10,offset=0,10,20...

        :param offset: The offset of this ListProjectIssuesRecordsV4Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProjectIssuesRecordsV4Request.

        每页数量 最小1,最大100

        :return: The limit of this ListProjectIssuesRecordsV4Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectIssuesRecordsV4Request.

        每页数量 最小1,最大100

        :param limit: The limit of this ListProjectIssuesRecordsV4Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def operated_time_interval(self):
        """Gets the operated_time_interval of this ListProjectIssuesRecordsV4Request.

        变更工作项的时间(查询的起始时间,查询的结束时间)

        :return: The operated_time_interval of this ListProjectIssuesRecordsV4Request.
        :rtype: str
        """
        return self._operated_time_interval

    @operated_time_interval.setter
    def operated_time_interval(self, operated_time_interval):
        """Sets the operated_time_interval of this ListProjectIssuesRecordsV4Request.

        变更工作项的时间(查询的起始时间,查询的结束时间)

        :param operated_time_interval: The operated_time_interval of this ListProjectIssuesRecordsV4Request.
        :type operated_time_interval: str
        """
        self._operated_time_interval = operated_time_interval

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
        if not isinstance(other, ListProjectIssuesRecordsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
