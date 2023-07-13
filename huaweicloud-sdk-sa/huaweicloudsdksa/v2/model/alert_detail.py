# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_object': 'Alert',
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'id': 'str',
        'type': 'str',
        'version': 'int',
        'format_version': 'int',
        'dataclass_ref': 'ShowAlertDetailDataclassRef'
    }

    attribute_map = {
        'data_object': 'data_object',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'id': 'id',
        'type': 'type',
        'version': 'version',
        'format_version': 'format_version',
        'dataclass_ref': 'dataclass_ref'
    }

    def __init__(self, data_object=None, create_time=None, update_time=None, project_id=None, workspace_id=None, id=None, type=None, version=None, format_version=None, dataclass_ref=None):
        """AlertDetail

        The model defined in huaweicloud sdk

        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.Alert`
        :param create_time: Create time
        :type create_time: str
        :param update_time: Update time
        :type update_time: str
        :param project_id: Id value
        :type project_id: str
        :param workspace_id: Id value
        :type workspace_id: str
        :param id: The name, display only
        :type id: str
        :param type: The name, display only
        :type type: str
        :param version: The name, display only
        :type version: int
        :param format_version: The name, display only
        :type format_version: int
        :param dataclass_ref: 
        :type dataclass_ref: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        
        

        self._data_object = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._workspace_id = None
        self._id = None
        self._type = None
        self._version = None
        self._format_version = None
        self._dataclass_ref = None
        self.discriminator = None

        if data_object is not None:
            self.data_object = data_object
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if format_version is not None:
            self.format_version = format_version
        if dataclass_ref is not None:
            self.dataclass_ref = dataclass_ref

    @property
    def data_object(self):
        """Gets the data_object of this AlertDetail.

        :return: The data_object of this AlertDetail.
        :rtype: :class:`huaweicloudsdksa.v2.Alert`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this AlertDetail.

        :param data_object: The data_object of this AlertDetail.
        :type data_object: :class:`huaweicloudsdksa.v2.Alert`
        """
        self._data_object = data_object

    @property
    def create_time(self):
        """Gets the create_time of this AlertDetail.

        Create time

        :return: The create_time of this AlertDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AlertDetail.

        Create time

        :param create_time: The create_time of this AlertDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AlertDetail.

        Update time

        :return: The update_time of this AlertDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AlertDetail.

        Update time

        :param update_time: The update_time of this AlertDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        """Gets the project_id of this AlertDetail.

        Id value

        :return: The project_id of this AlertDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AlertDetail.

        Id value

        :param project_id: The project_id of this AlertDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this AlertDetail.

        Id value

        :return: The workspace_id of this AlertDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this AlertDetail.

        Id value

        :param workspace_id: The workspace_id of this AlertDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def id(self):
        """Gets the id of this AlertDetail.

        The name, display only

        :return: The id of this AlertDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertDetail.

        The name, display only

        :param id: The id of this AlertDetail.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this AlertDetail.

        The name, display only

        :return: The type of this AlertDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertDetail.

        The name, display only

        :param type: The type of this AlertDetail.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this AlertDetail.

        The name, display only

        :return: The version of this AlertDetail.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AlertDetail.

        The name, display only

        :param version: The version of this AlertDetail.
        :type version: int
        """
        self._version = version

    @property
    def format_version(self):
        """Gets the format_version of this AlertDetail.

        The name, display only

        :return: The format_version of this AlertDetail.
        :rtype: int
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        """Sets the format_version of this AlertDetail.

        The name, display only

        :param format_version: The format_version of this AlertDetail.
        :type format_version: int
        """
        self._format_version = format_version

    @property
    def dataclass_ref(self):
        """Gets the dataclass_ref of this AlertDetail.

        :return: The dataclass_ref of this AlertDetail.
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        return self._dataclass_ref

    @dataclass_ref.setter
    def dataclass_ref(self, dataclass_ref):
        """Sets the dataclass_ref of this AlertDetail.

        :param dataclass_ref: The dataclass_ref of this AlertDetail.
        :type dataclass_ref: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        self._dataclass_ref = dataclass_ref

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
        if not isinstance(other, AlertDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
