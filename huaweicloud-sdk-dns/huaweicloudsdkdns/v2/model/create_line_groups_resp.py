# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLineGroupsResp:

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
        r"""CreateLineGroupsResp

        The model defined in huaweicloud sdk

        :param name: 线路分组名称。
        :type name: str
        :param lines: 线路分组包含的线路列表。 解析线路ID。
        :type lines: list[str]
        :param status: 资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。
        :type status: str
        :param description: 线路分组的描述信息
        :type description: str
        :param line_id: 线路分组的ID。
        :type line_id: str
        :param created_at: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type created_at: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        """
        
        

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
        r"""Gets the name of this CreateLineGroupsResp.

        线路分组名称。

        :return: The name of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateLineGroupsResp.

        线路分组名称。

        :param name: The name of this CreateLineGroupsResp.
        :type name: str
        """
        self._name = name

    @property
    def lines(self):
        r"""Gets the lines of this CreateLineGroupsResp.

        线路分组包含的线路列表。 解析线路ID。

        :return: The lines of this CreateLineGroupsResp.
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this CreateLineGroupsResp.

        线路分组包含的线路列表。 解析线路ID。

        :param lines: The lines of this CreateLineGroupsResp.
        :type lines: list[str]
        """
        self._lines = lines

    @property
    def status(self):
        r"""Gets the status of this CreateLineGroupsResp.

        资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。

        :return: The status of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateLineGroupsResp.

        资源状态。 取值范围：PENDING_CREATE，ACTIVE，PENDING_DELETE，PENDING_UPDATE，ERROR，FREEZE，DISABLE。

        :param status: The status of this CreateLineGroupsResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this CreateLineGroupsResp.

        线路分组的描述信息

        :return: The description of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateLineGroupsResp.

        线路分组的描述信息

        :param description: The description of this CreateLineGroupsResp.
        :type description: str
        """
        self._description = description

    @property
    def line_id(self):
        r"""Gets the line_id of this CreateLineGroupsResp.

        线路分组的ID。

        :return: The line_id of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        r"""Sets the line_id of this CreateLineGroupsResp.

        线路分组的ID。

        :param line_id: The line_id of this CreateLineGroupsResp.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateLineGroupsResp.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateLineGroupsResp.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this CreateLineGroupsResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateLineGroupsResp.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this CreateLineGroupsResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateLineGroupsResp.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this CreateLineGroupsResp.
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
        if not isinstance(other, CreateLineGroupsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
