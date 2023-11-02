# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'data_object': 'IndicatorDataObjectDetail',
        'workspace_id': 'str',
        'project_id': 'str',
        'dataclass_ref': 'DataClassRefPojo',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'data_object': 'data_object',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'dataclass_ref': 'dataclass_ref',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, data_object=None, workspace_id=None, project_id=None, dataclass_ref=None, create_time=None, update_time=None):
        """IndicatorDetail

        The model defined in huaweicloud sdk

        :param id: 指标ID
        :type id: str
        :param name: 指标名称
        :type name: str
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetail`
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param dataclass_ref: 
        :type dataclass_ref: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._data_object = None
        self._workspace_id = None
        self._project_id = None
        self._dataclass_ref = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if data_object is not None:
            self.data_object = data_object
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if dataclass_ref is not None:
            self.dataclass_ref = dataclass_ref
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this IndicatorDetail.

        指标ID

        :return: The id of this IndicatorDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndicatorDetail.

        指标ID

        :param id: The id of this IndicatorDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this IndicatorDetail.

        指标名称

        :return: The name of this IndicatorDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndicatorDetail.

        指标名称

        :param name: The name of this IndicatorDetail.
        :type name: str
        """
        self._name = name

    @property
    def data_object(self):
        """Gets the data_object of this IndicatorDetail.

        :return: The data_object of this IndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetail`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this IndicatorDetail.

        :param data_object: The data_object of this IndicatorDetail.
        :type data_object: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetail`
        """
        self._data_object = data_object

    @property
    def workspace_id(self):
        """Gets the workspace_id of this IndicatorDetail.

        工作空间ID

        :return: The workspace_id of this IndicatorDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this IndicatorDetail.

        工作空间ID

        :param workspace_id: The workspace_id of this IndicatorDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        """Gets the project_id of this IndicatorDetail.

        项目ID

        :return: The project_id of this IndicatorDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IndicatorDetail.

        项目ID

        :param project_id: The project_id of this IndicatorDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataclass_ref(self):
        """Gets the dataclass_ref of this IndicatorDetail.

        :return: The dataclass_ref of this IndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        """
        return self._dataclass_ref

    @dataclass_ref.setter
    def dataclass_ref(self, dataclass_ref):
        """Sets the dataclass_ref of this IndicatorDetail.

        :param dataclass_ref: The dataclass_ref of this IndicatorDetail.
        :type dataclass_ref: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        """
        self._dataclass_ref = dataclass_ref

    @property
    def create_time(self):
        """Gets the create_time of this IndicatorDetail.

        创建时间

        :return: The create_time of this IndicatorDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IndicatorDetail.

        创建时间

        :param create_time: The create_time of this IndicatorDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this IndicatorDetail.

        更新时间

        :return: The update_time of this IndicatorDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this IndicatorDetail.

        更新时间

        :param update_time: The update_time of this IndicatorDetail.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, IndicatorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
