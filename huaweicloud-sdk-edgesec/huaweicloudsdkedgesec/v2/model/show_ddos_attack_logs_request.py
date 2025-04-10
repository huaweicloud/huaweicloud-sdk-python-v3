# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdosAttackLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ShowDdosAttackLogsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        :param start_time: 起始时间(13位时间戳)
        :type start_time: int
        :param end_time: 结束时间(13位时间戳)
        :type end_time: int
        :param offset: 查询列表的偏移量
        :type offset: int
        :param limit: 查询列表每一页的条数
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDdosAttackLogsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this ShowDdosAttackLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDdosAttackLogsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this ShowDdosAttackLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDdosAttackLogsRequest.

        起始时间(13位时间戳)

        :return: The start_time of this ShowDdosAttackLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDdosAttackLogsRequest.

        起始时间(13位时间戳)

        :param start_time: The start_time of this ShowDdosAttackLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDdosAttackLogsRequest.

        结束时间(13位时间戳)

        :return: The end_time of this ShowDdosAttackLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDdosAttackLogsRequest.

        结束时间(13位时间戳)

        :param end_time: The end_time of this ShowDdosAttackLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowDdosAttackLogsRequest.

        查询列表的偏移量

        :return: The offset of this ShowDdosAttackLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDdosAttackLogsRequest.

        查询列表的偏移量

        :param offset: The offset of this ShowDdosAttackLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDdosAttackLogsRequest.

        查询列表每一页的条数

        :return: The limit of this ShowDdosAttackLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDdosAttackLogsRequest.

        查询列表每一页的条数

        :param limit: The limit of this ShowDdosAttackLogsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowDdosAttackLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
