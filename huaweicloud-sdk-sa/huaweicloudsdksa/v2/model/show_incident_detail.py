# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIncidentDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_object': 'ShowIncident',
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
        r"""ShowIncidentDetail

        The model defined in huaweicloud sdk

        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.ShowIncident`
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
        r"""Gets the data_object of this ShowIncidentDetail.

        :return: The data_object of this ShowIncidentDetail.
        :rtype: :class:`huaweicloudsdksa.v2.ShowIncident`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        r"""Sets the data_object of this ShowIncidentDetail.

        :param data_object: The data_object of this ShowIncidentDetail.
        :type data_object: :class:`huaweicloudsdksa.v2.ShowIncident`
        """
        self._data_object = data_object

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowIncidentDetail.

        Create time

        :return: The create_time of this ShowIncidentDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowIncidentDetail.

        Create time

        :param create_time: The create_time of this ShowIncidentDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowIncidentDetail.

        Update time

        :return: The update_time of this ShowIncidentDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowIncidentDetail.

        Update time

        :param update_time: The update_time of this ShowIncidentDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowIncidentDetail.

        Id value

        :return: The project_id of this ShowIncidentDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowIncidentDetail.

        Id value

        :param project_id: The project_id of this ShowIncidentDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowIncidentDetail.

        Id value

        :return: The workspace_id of this ShowIncidentDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowIncidentDetail.

        Id value

        :param workspace_id: The workspace_id of this ShowIncidentDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this ShowIncidentDetail.

        Id value

        :return: The dataclass_id of this ShowIncidentDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this ShowIncidentDetail.

        Id value

        :param dataclass_id: The dataclass_id of this ShowIncidentDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def layout_id(self):
        r"""Gets the layout_id of this ShowIncidentDetail.

        Id value

        :return: The layout_id of this ShowIncidentDetail.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this ShowIncidentDetail.

        Id value

        :param layout_id: The layout_id of this ShowIncidentDetail.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def name(self):
        r"""Gets the name of this ShowIncidentDetail.

        The name, display only

        :return: The name of this ShowIncidentDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowIncidentDetail.

        The name, display only

        :param name: The name of this ShowIncidentDetail.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowIncidentDetail.

        The name, display only

        :return: The type of this ShowIncidentDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowIncidentDetail.

        The name, display only

        :param type: The type of this ShowIncidentDetail.
        :type type: str
        """
        self._type = type

    @property
    def dataclass(self):
        r"""Gets the dataclass of this ShowIncidentDetail.

        :return: The dataclass of this ShowIncidentDetail.
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertDetailDataclassRef`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this ShowIncidentDetail.

        :param dataclass: The dataclass of this ShowIncidentDetail.
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
        if not isinstance(other, ShowIncidentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
