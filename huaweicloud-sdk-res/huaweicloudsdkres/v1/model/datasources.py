# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datasources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datasource_id': 'str',
        'datasource_name': 'str',
        'status': 'str',
        'structure': 'str',
        'workspace_id': 'str',
        'data_config': 'DataConfig',
        'specs_config': 'SpecsConfig',
        'created_at': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'datasource_id': 'datasource_id',
        'datasource_name': 'datasource_name',
        'status': 'status',
        'structure': 'structure',
        'workspace_id': 'workspace_id',
        'data_config': 'data_config',
        'specs_config': 'specs_config',
        'created_at': 'created_at',
        'update_at': 'update_at'
    }

    def __init__(self, datasource_id=None, datasource_name=None, status=None, structure=None, workspace_id=None, data_config=None, specs_config=None, created_at=None, update_at=None):
        """Datasources

        The model defined in huaweicloud sdk

        :param datasource_id: 数据源id。
        :type datasource_id: str
        :param datasource_name: 名称。
        :type datasource_name: str
        :param status: 状态。
        :type status: str
        :param structure: 结构。
        :type structure: str
        :param workspace_id: 工作空间编号。
        :type workspace_id: str
        :param data_config: 
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        :param created_at: 创建时间。
        :type created_at: int
        :param update_at: 更新时间。
        :type update_at: int
        """
        
        

        self._datasource_id = None
        self._datasource_name = None
        self._status = None
        self._structure = None
        self._workspace_id = None
        self._data_config = None
        self._specs_config = None
        self._created_at = None
        self._update_at = None
        self.discriminator = None

        if datasource_id is not None:
            self.datasource_id = datasource_id
        if datasource_name is not None:
            self.datasource_name = datasource_name
        if status is not None:
            self.status = status
        if structure is not None:
            self.structure = structure
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if data_config is not None:
            self.data_config = data_config
        if specs_config is not None:
            self.specs_config = specs_config
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def datasource_id(self):
        """Gets the datasource_id of this Datasources.

        数据源id。

        :return: The datasource_id of this Datasources.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """Sets the datasource_id of this Datasources.

        数据源id。

        :param datasource_id: The datasource_id of this Datasources.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def datasource_name(self):
        """Gets the datasource_name of this Datasources.

        名称。

        :return: The datasource_name of this Datasources.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """Sets the datasource_name of this Datasources.

        名称。

        :param datasource_name: The datasource_name of this Datasources.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def status(self):
        """Gets the status of this Datasources.

        状态。

        :return: The status of this Datasources.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Datasources.

        状态。

        :param status: The status of this Datasources.
        :type status: str
        """
        self._status = status

    @property
    def structure(self):
        """Gets the structure of this Datasources.

        结构。

        :return: The structure of this Datasources.
        :rtype: str
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        """Sets the structure of this Datasources.

        结构。

        :param structure: The structure of this Datasources.
        :type structure: str
        """
        self._structure = structure

    @property
    def workspace_id(self):
        """Gets the workspace_id of this Datasources.

        工作空间编号。

        :return: The workspace_id of this Datasources.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this Datasources.

        工作空间编号。

        :param workspace_id: The workspace_id of this Datasources.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def data_config(self):
        """Gets the data_config of this Datasources.


        :return: The data_config of this Datasources.
        :rtype: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """Sets the data_config of this Datasources.


        :param data_config: The data_config of this Datasources.
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        self._data_config = data_config

    @property
    def specs_config(self):
        """Gets the specs_config of this Datasources.


        :return: The specs_config of this Datasources.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        """Sets the specs_config of this Datasources.


        :param specs_config: The specs_config of this Datasources.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

    @property
    def created_at(self):
        """Gets the created_at of this Datasources.

        创建时间。

        :return: The created_at of this Datasources.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datasources.

        创建时间。

        :param created_at: The created_at of this Datasources.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def update_at(self):
        """Gets the update_at of this Datasources.

        更新时间。

        :return: The update_at of this Datasources.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Datasources.

        更新时间。

        :param update_at: The update_at of this Datasources.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, Datasources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
