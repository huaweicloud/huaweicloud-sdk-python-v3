# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datasource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_name': 'str',
        'workspace_id': 'str',
        'datasource_id': 'str',
        'status': 'str',
        'created_at': 'int'
    }

    attribute_map = {
        'datasource_name': 'datasource_name',
        'workspace_id': 'workspace_id',
        'datasource_id': 'datasource_id',
        'status': 'status',
        'created_at': 'created_at'
    }

    def __init__(self, datasource_name=None, workspace_id=None, datasource_id=None, status=None, created_at=None):
        r"""Datasource

        The model defined in huaweicloud sdk

        :param datasource_name: 数据源名称。
        :type datasource_name: str
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param datasource_id: 数据源id。
        :type datasource_id: str
        :param status: 状态。
        :type status: str
        :param created_at: 创建时间。
        :type created_at: int
        """
        
        

        self._datasource_name = None
        self._workspace_id = None
        self._datasource_id = None
        self._status = None
        self._created_at = None
        self.discriminator = None

        self.datasource_name = datasource_name
        self.workspace_id = workspace_id
        if datasource_id is not None:
            self.datasource_id = datasource_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at

    @property
    def datasource_name(self):
        r"""Gets the datasource_name of this Datasource.

        数据源名称。

        :return: The datasource_name of this Datasource.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        r"""Sets the datasource_name of this Datasource.

        数据源名称。

        :param datasource_name: The datasource_name of this Datasource.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this Datasource.

        工作空间id。

        :return: The workspace_id of this Datasource.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this Datasource.

        工作空间id。

        :param workspace_id: The workspace_id of this Datasource.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def datasource_id(self):
        r"""Gets the datasource_id of this Datasource.

        数据源id。

        :return: The datasource_id of this Datasource.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        r"""Sets the datasource_id of this Datasource.

        数据源id。

        :param datasource_id: The datasource_id of this Datasource.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def status(self):
        r"""Gets the status of this Datasource.

        状态。

        :return: The status of this Datasource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Datasource.

        状态。

        :param status: The status of this Datasource.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this Datasource.

        创建时间。

        :return: The created_at of this Datasource.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Datasource.

        创建时间。

        :param created_at: The created_at of this Datasource.
        :type created_at: int
        """
        self._created_at = created_at

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
        if not isinstance(other, Datasource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
