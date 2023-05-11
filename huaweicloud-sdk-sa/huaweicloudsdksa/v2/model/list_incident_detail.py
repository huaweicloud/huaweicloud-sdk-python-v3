# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncidentDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_object': 'Incident',
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'dataclass_id': 'str',
        'layout_id': 'str',
        'name': 'str',
        'type': 'str',
        'dataclass': 'ShowAlertDetailDataclassRef'
    }

    attribute_map = {
        'data_object': 'data_object',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_id': 'dataclass_id',
        'layout_id': 'layout_id',
        'name': 'name',
        'type': 'type',
        'dataclass': 'dataclass'
    }

    def __init__(self, data_object=None, create_time=None, update_time=None, project_id=None, workspace_id=None, dataclass_id=None, layout_id=None, name=None, type=None, dataclass=None):
        """ListIncidentDetail

        The model defined in huaweicloud sdk

        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.Incident`
        :param create_time: Create time
        :type create_time: str
        :param update_time: Update time
        :type update_time: str
        :param project_id: Id value
        :type project_id: str
        :param workspace_id: Id value
        :type workspace_id: str
        :param dataclass_id: Id value
        :type dataclass_id: str
        :param layout_id: Id value
        :type layout_id: str
        :param name: The name, display only
        :type name: str
        :param type: The name, display only
        :type type: str
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        
        

        self._data_object = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._workspace_id = None
        self._dataclass_id = None
        self._layout_id = None
        self._name = None
        self._type = None
        self._dataclass = None
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
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if layout_id is not None:
            self.layout_id = layout_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if dataclass is not None:
            self.dataclass = dataclass

    @property
    def data_object(self):
        """Gets the data_object of this ListIncidentDetail.

        :return: The data_object of this ListIncidentDetail.
        :rtype: :class:`huaweicloudsdksa.v2.Incident`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this ListIncidentDetail.

        :param data_object: The data_object of this ListIncidentDetail.
        :type data_object: :class:`huaweicloudsdksa.v2.Incident`
        """
        self._data_object = data_object

    @property
    def create_time(self):
        """Gets the create_time of this ListIncidentDetail.

        Create time

        :return: The create_time of this ListIncidentDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListIncidentDetail.

        Create time

        :param create_time: The create_time of this ListIncidentDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ListIncidentDetail.

        Update time

        :return: The update_time of this ListIncidentDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListIncidentDetail.

        Update time

        :param update_time: The update_time of this ListIncidentDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        """Gets the project_id of this ListIncidentDetail.

        Id value

        :return: The project_id of this ListIncidentDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListIncidentDetail.

        Id value

        :param project_id: The project_id of this ListIncidentDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListIncidentDetail.

        Id value

        :return: The workspace_id of this ListIncidentDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListIncidentDetail.

        Id value

        :param workspace_id: The workspace_id of this ListIncidentDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this ListIncidentDetail.

        Id value

        :return: The dataclass_id of this ListIncidentDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this ListIncidentDetail.

        Id value

        :param dataclass_id: The dataclass_id of this ListIncidentDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def layout_id(self):
        """Gets the layout_id of this ListIncidentDetail.

        Id value

        :return: The layout_id of this ListIncidentDetail.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this ListIncidentDetail.

        Id value

        :param layout_id: The layout_id of this ListIncidentDetail.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def name(self):
        """Gets the name of this ListIncidentDetail.

        The name, display only

        :return: The name of this ListIncidentDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIncidentDetail.

        The name, display only

        :param name: The name of this ListIncidentDetail.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ListIncidentDetail.

        The name, display only

        :return: The type of this ListIncidentDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListIncidentDetail.

        The name, display only

        :param type: The type of this ListIncidentDetail.
        :type type: str
        """
        self._type = type

    @property
    def dataclass(self):
        """Gets the dataclass of this ListIncidentDetail.

        :return: The dataclass of this ListIncidentDetail.
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        """Sets the dataclass of this ListIncidentDetail.

        :param dataclass: The dataclass of this ListIncidentDetail.
        :type dataclass: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        self._dataclass = dataclass

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
        if not isinstance(other, ListIncidentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
