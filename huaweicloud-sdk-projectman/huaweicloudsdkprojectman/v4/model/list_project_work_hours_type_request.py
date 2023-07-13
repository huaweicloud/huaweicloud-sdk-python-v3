# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectWorkHoursTypeRequest:

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
        'limit': 'int',
        'offset': 'int',
        'status': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, project_id=None, limit=None, offset=None, status=None):
        """ListProjectWorkHoursTypeRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param limit: 每页显示的数量，默认显示10条，最多显示100条
        :type limit: int
        :param offset: 分页索引，偏移量offset是limit的整数倍，limit&#x3D;10,offset&#x3D;0,10,20...
        :type offset: int
        :param status: 工时类型状态，支持按状态筛选查询，置空时查询所有工时类型，1表示查询启用的工时类型，2表示查询未启用的工时类型
        :type status: int
        """
        
        

        self._project_id = None
        self._limit = None
        self._offset = None
        self._status = None
        self.discriminator = None

        self.project_id = project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def project_id(self):
        """Gets the project_id of this ListProjectWorkHoursTypeRequest.

        项目id

        :return: The project_id of this ListProjectWorkHoursTypeRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListProjectWorkHoursTypeRequest.

        项目id

        :param project_id: The project_id of this ListProjectWorkHoursTypeRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def limit(self):
        """Gets the limit of this ListProjectWorkHoursTypeRequest.

        每页显示的数量，默认显示10条，最多显示100条

        :return: The limit of this ListProjectWorkHoursTypeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectWorkHoursTypeRequest.

        每页显示的数量，默认显示10条，最多显示100条

        :param limit: The limit of this ListProjectWorkHoursTypeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProjectWorkHoursTypeRequest.

        分页索引，偏移量offset是limit的整数倍，limit=10,offset=0,10,20...

        :return: The offset of this ListProjectWorkHoursTypeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectWorkHoursTypeRequest.

        分页索引，偏移量offset是limit的整数倍，limit=10,offset=0,10,20...

        :param offset: The offset of this ListProjectWorkHoursTypeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListProjectWorkHoursTypeRequest.

        工时类型状态，支持按状态筛选查询，置空时查询所有工时类型，1表示查询启用的工时类型，2表示查询未启用的工时类型

        :return: The status of this ListProjectWorkHoursTypeRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProjectWorkHoursTypeRequest.

        工时类型状态，支持按状态筛选查询，置空时查询所有工时类型，1表示查询启用的工时类型，2表示查询未启用的工时类型

        :param status: The status of this ListProjectWorkHoursTypeRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListProjectWorkHoursTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
