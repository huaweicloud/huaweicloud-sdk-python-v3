# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLineGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'lines': 'list[str]',
        'status': 'str',
        'description': 'str',
        'line_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'lines': 'lines',
        'status': 'status',
        'description': 'description',
        'line_id': 'line_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, lines=None, status=None, description=None, line_id=None, created_at=None, updated_at=None):
        """UpdateLineGroupsResponse

        The model defined in huaweicloud sdk

        :param name: 线路分组名称。
        :type name: str
        :param lines: 线路分组包含的线路列表。 解析线路ID。
        :type lines: list[str]
        :param status: 资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。
        :type status: str
        :param description: 线路分组的描述信息
        :type description: str
        :param line_id: 线路分组的id。
        :type line_id: str
        :param created_at: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type created_at: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        """
        
        super(UpdateLineGroupsResponse, self).__init__()

        self._name = None
        self._lines = None
        self._status = None
        self._description = None
        self._line_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if lines is not None:
            self.lines = lines
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if line_id is not None:
            self.line_id = line_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this UpdateLineGroupsResponse.

        线路分组名称。

        :return: The name of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateLineGroupsResponse.

        线路分组名称。

        :param name: The name of this UpdateLineGroupsResponse.
        :type name: str
        """
        self._name = name

    @property
    def lines(self):
        """Gets the lines of this UpdateLineGroupsResponse.

        线路分组包含的线路列表。 解析线路ID。

        :return: The lines of this UpdateLineGroupsResponse.
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this UpdateLineGroupsResponse.

        线路分组包含的线路列表。 解析线路ID。

        :param lines: The lines of this UpdateLineGroupsResponse.
        :type lines: list[str]
        """
        self._lines = lines

    @property
    def status(self):
        """Gets the status of this UpdateLineGroupsResponse.

        资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。

        :return: The status of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateLineGroupsResponse.

        资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。

        :param status: The status of this UpdateLineGroupsResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this UpdateLineGroupsResponse.

        线路分组的描述信息

        :return: The description of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateLineGroupsResponse.

        线路分组的描述信息

        :param description: The description of this UpdateLineGroupsResponse.
        :type description: str
        """
        self._description = description

    @property
    def line_id(self):
        """Gets the line_id of this UpdateLineGroupsResponse.

        线路分组的id。

        :return: The line_id of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this UpdateLineGroupsResponse.

        线路分组的id。

        :param line_id: The line_id of this UpdateLineGroupsResponse.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def created_at(self):
        """Gets the created_at of this UpdateLineGroupsResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateLineGroupsResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this UpdateLineGroupsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateLineGroupsResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this UpdateLineGroupsResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateLineGroupsResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this UpdateLineGroupsResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, UpdateLineGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
